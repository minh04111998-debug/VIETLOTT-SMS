#!/usr/bin/env python3
"""
AgentOps Metrics — tổng hợp tín hiệu vận hành của harness thành báo cáo theo tuần (DEC-008).

Nguồn dữ liệu:
  - observability/gate-reports/QGR-*.md        (hook tự động + gate thủ công)
  - observability/critique-conflicts/CC-*.md   (bế tắc CRITIQUE > 2 vòng)
  - evaluations/regression/results/history.jsonl (lịch sử run_evals)
  - hooks/.gate_hook_state.json                (vi phạm đang treo)

Giới hạn đã biết (ghi thẳng vào báo cáo, không che giấu):
  - Hook chỉ ghi report khi FAIL -> KHÔNG tính được tỉ lệ pass từ gate-report.
  - Report định dạng cũ (post-task.ps1, trước DEC-003) không có danh sách vi phạm chuẩn -> chỉ đếm.

Usage:
  python validators/ops_metrics.py                 # tuần hiện tại -> observability/metrics/<YYYY-Www>.md
  python validators/ops_metrics.py --week 2026-W41
  python validators/ops_metrics.py --stdout        # in ra màn hình, không ghi file
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "observability" / "gate-reports"
CONFLICT_DIR = ROOT / "observability" / "critique-conflicts"
HISTORY = ROOT / "evaluations" / "regression" / "results" / "history.jsonl"
HOOK_STATE = ROOT / "hooks" / ".gate_hook_state.json"
OUT_DIR = ROOT / "observability" / "metrics"

RE_NAME = re.compile(r"^QGR-(\d{8})-(\d{6})-([A-Za-z]+)-?(.*)$")
RE_FINDING = re.compile(r"^- L\d+ \[([^\]]+)\] (?:'([^']+)'|([^—]+?))\s*(?:—.*)?$")
RE_ARTIFACT = re.compile(r"\*\*Artifact:\*\*\s*`?([^`\s]+)`?")


def _iso_week(dt):
    y, w, _ = dt.isocalendar()
    return f"{y}-W{w:02d}"


def _artifact_key(raw):
    """Report ghi artifact theo 3 kiểu (stem / tương đối / tuyệt đối Windows) -> gom về tên file."""
    name = raw.replace("\\", "/").rstrip("/").split("/")[-1]
    return name[:-3] if name.lower().endswith(".md") else name


def load_reports():
    reports = []
    for p in sorted(REPORT_DIR.glob("QGR-*.md")):
        m = RE_NAME.match(p.stem)
        if not m:
            continue
        dt = datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M%S")
        text = p.read_text(encoding="utf-8", errors="replace")
        findings = []
        for line in text.splitlines():
            fm = RE_FINDING.match(line.strip())
            if fm:
                findings.append((fm.group(1).strip(), (fm.group(2) or fm.group(3) or "").strip()))
        am = RE_ARTIFACT.search(text)
        artifact = _artifact_key(am.group(1) if am and "$" not in am.group(1) else (m.group(4) or "(không rõ)"))
        reports.append({
            "dt": dt, "week": _iso_week(dt), "source": m.group(3).lower(),
            "artifact": artifact, "findings": findings,
            "legacy": m.group(3).lower() != "hook",
        })
    return reports


def load_history():
    rows = []
    if HISTORY.exists():
        for line in HISTORY.read_text(encoding="utf-8").splitlines():
            try:
                rows.append(json.loads(line))
            except Exception:
                continue
    return rows


def _eval_totals(row):
    s = row.get("summary", {})
    passed = sum(v.get("PASS", 0) for v in s.values())
    failed = sum(v.get("FAIL", 0) for v in s.values())
    return passed, failed


def build(week):
    reports = load_reports()
    wk = [r for r in reports if r["week"] == week]
    conflicts = [p for p in CONFLICT_DIR.glob("CC-*.md") if p.stem != "CC-template"] if CONFLICT_DIR.exists() else []
    history = load_history()
    try:
        pending = json.loads(HOOK_STATE.read_text(encoding="utf-8")).get("pending", {})
    except Exception:
        pending = {}

    cat_all, term_all = Counter(), Counter()
    per_artifact = Counter()
    by_week = Counter(r["week"] for r in reports)
    by_source = defaultdict(Counter)
    for r in reports:
        per_artifact[r["artifact"]] += 1
        by_source[r["week"]][r["source"]] += 1
        for cat, term in r["findings"]:
            cat_all[cat] += 1
            if term:
                term_all[(cat, term.lower())] += 1
    cat_wk = Counter(cat for r in wk for cat, _ in r["findings"])

    L = []
    L.append(f"# AgentOps Metrics — {week}")
    L.append("")
    L.append(f"> **Sinh bởi:** `validators/ops_metrics.py` lúc {datetime.now():%Y-%m-%d %H:%M}  ")
    L.append("> **Harness:** AgentOps (DEC-008) · **Thời gian lưu báo cáo:** `[❓ OPEN — Q-006]`")
    L.append("")
    L.append("## 1. Tóm tắt tuần")
    L.append("")
    L.append("| Chỉ số | Giá trị |")
    L.append("|---|---:|")
    L.append(f"| Gate report FAIL trong tuần | {len(wk)} |")
    L.append(f"| Vi phạm trong tuần (tổng dòng) | {sum(cat_wk.values())} |")
    L.append(f"| Artifact đang treo vi phạm (hook state) | {len(pending)} |")
    L.append(f"| Biên bản bế tắc CRITIQUE (toàn thời gian) | {len(conflicts)} |")
    L.append(f"| Gate report FAIL (toàn thời gian) | {len(reports)} |")
    L.append("")
    L.append("> [!NOTE]")
    L.append("> Hook chỉ ghi report khi FAIL nên báo cáo này **không có tỉ lệ pass**. "
             "Muốn có tỉ lệ pass cần hook ghi cả lượt PASS — chưa triển khai.")
    L.append("")

    L.append("## 2. Vi phạm theo loại")
    L.append("")
    L.append("| Loại | Tuần này | Toàn thời gian |")
    L.append("|---|---:|---:|")
    for cat, n in cat_all.most_common():
        L.append(f"| {cat} | {cat_wk.get(cat, 0)} | {n} |")
    if not cat_all:
        L.append("| (chưa có dữ liệu) | 0 | 0 |")
    L.append("")

    L.append("## 3. Top 5 từ/mẫu vi phạm lặp lại (toàn thời gian)")
    L.append("")
    L.append("| Loại | Từ / mẫu | Số lần |")
    L.append("|---|---|---:|")
    for (cat, term), n in term_all.most_common(5):
        L.append(f"| {cat} | {term} | {n} |")
    L.append("")
    L.append("> Từ lặp lại ở nhiều artifact → cân nhắc bổ sung bảng thay thế trong rule banned-words hoặc template.")
    L.append("")

    L.append("## 4. Artifact FAIL lặp lại (≥ 2 report)")
    L.append("")
    repeat = [(a, n) for a, n in per_artifact.most_common() if n >= 2]
    if repeat:
        L.append("| Artifact | Số report FAIL |")
        L.append("|---|---:|")
        for a, n in repeat:
            L.append(f"| {a} | {n} |")
    else:
        L.append("Không có artifact nào FAIL từ 2 lần trở lên.")
    L.append("")

    L.append("## 5. Xu hướng theo tuần (gate report FAIL)")
    L.append("")
    L.append("| Tuần | Hook | Gate thủ công | Tổng |")
    L.append("|---|---:|---:|---:|")
    for w in sorted(by_week):
        hook = by_source[w].get("hook", 0)
        L.append(f"| {w} | {hook} | {by_week[w] - hook} | {by_week[w]} |")
    L.append("")

    L.append("## 6. Lịch sử eval hồi quy (5 lần chạy gần nhất)")
    L.append("")
    L.append("| Thời điểm | PASS | FAIL | Biến động PASS |")
    L.append("|---|---:|---:|---:|")
    prev = None
    tail = history[-6:]
    for i, row in enumerate(tail):
        p, f = _eval_totals(row)
        if i > 0 or len(history) <= 5:
            delta = "" if prev is None else f"{p - prev:+d}"
            L.append(f"| {row.get('ts', '?')} | {p} | {f} | {delta} |")
        prev = p
    if history:
        lp, lf = _eval_totals(history[-1])
        if lf:
            L.append("")
            L.append(f"> [!WARNING]\n> Lần chạy gần nhất có {lf} FAIL — kiểm tra `python evaluations/run_evals.py`.")
    L.append("")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description="AgentOps metrics theo tuần")
    ap.add_argument("--week", default=_iso_week(datetime.now()), help="Tuần ISO, ví dụ 2026-W41")
    ap.add_argument("--stdout", action="store_true", help="In ra màn hình, không ghi file")
    args = ap.parse_args()
    if not re.fullmatch(r"\d{4}-W\d{2}", args.week):
        print("❌ --week phải có dạng YYYY-Www, ví dụ 2026-W41")
        sys.exit(1)
    body = build(args.week)
    if args.stdout:
        print(body)
        return
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{args.week}.md"
    out.write_text(body, encoding="utf-8")
    print(f"✅ Đã ghi {out.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
