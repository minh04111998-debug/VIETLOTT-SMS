#!/usr/bin/env python3
"""
Harness Eval Runner — trả lời câu hỏi "sửa rules/skills/workflows xong, harness tốt lên hay tệ đi?"

4 suite:
  harness     Toàn vẹn cấu trúc (hooks, AGENTS.md, bản đồ 7 harness...)   — tự động 100%
  validators  Golden cases cho PII / secret / từ cấm / mơ hồ             — tự động 100%
  behavior    Hành vi agent: chấm regex trên câu trả lời đã lưu           — bán tự động
              (agent không gọi được từ script -> người chạy prompt, lưu câu trả lời
               vào evaluations/regression/responses/<ID>.md, runner chấm)
  golden      Deliverable mẫu Human đã ký duyệt (evaluations/golden/, DEC-008) — manifest rỗng = NOT_RUN

Usage:
  python evaluations/run_evals.py                    # chạy cả 4 suite, ghi lịch sử
  python evaluations/run_evals.py --suite validators
  python evaluations/run_evals.py --list-prompts     # in prompt behavior để chạy tay
  python evaluations/run_evals.py --no-history       # không ghi results/history.jsonl

Exit code: 1 nếu có FAIL (kể cả harness FAIL); XFAIL/NOT_RUN không làm fail.
"""
import argparse
import json
import re
import sys
import tempfile
from collections import Counter
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
REG = Path(__file__).resolve().parent / "regression"
RESPONSES = REG / "responses"
HISTORY = REG / "results" / "history.jsonl"
GOLDEN = Path(__file__).resolve().parent / "golden" / "manifest.json"

sys.path.insert(0, str(ROOT / "validators"))
sys.path.insert(0, str(REG))


# --------------------------------------------------------------------------- harness
def suite_harness():
    import harness_integrity_checker as hic
    out = []
    for r in hic.run_checks(ROOT):
        status = {"PASS": "PASS", "WARN": "WARN", "FAIL": "FAIL"}[r["status"]]
        out.append({"id": r["check"], "status": status, "detail": r["message"]})
    return out


# --------------------------------------------------------------------------- validators
def _detect(validator, path, text):
    import ambiguity_scanner
    import banned_words_validator
    import pii_scanner
    import secret_scanner
    with redirect_stdout(StringIO()):
        if validator == "pii":
            return bool(pii_scanner.scan_file(str(path)))
        if validator == "banned":
            return bool(banned_words_validator.scan_text(text, filepath=str(path)))
        if validator == "ambiguity":
            return bool(ambiguity_scanner.scan_file(str(path)))
        if validator == "secret":
            return bool(secret_scanner.scan_file(str(path)))
    raise ValueError(f"validator không hỗ trợ: {validator}")


def suite_validators():
    from validator_cases import CASES
    ids = [c["id"] for c in CASES]
    dup = [i for i, n in Counter(ids).items() if n > 1]
    if dup:
        return [{"id": "CASES", "status": "FAIL", "detail": f"Trùng id case: {dup}"}]

    out = []
    with tempfile.TemporaryDirectory(prefix="harness-eval-") as tmp:
        for c in CASES:
            # tên file trung tính: banned_words_validator nới lỏng nếu path chứa 'rules'/'checklist'
            p = Path(tmp) / f"case-{c['id'].lower()}.md"
            p.write_text(c["text"], encoding="utf-8")
            detected = _detect(c["validator"], p, c["text"])
            ok = detected == (c["expect"] == "detect")
            if c.get("xfail"):
                status = "XPASS" if ok else "XFAIL"
                detail = (f"Lỗ hổng đã được sửa? Gỡ 'xfail' khỏi case. ({c['xfail']})" if ok
                          else f"Lỗ hổng đã biết: {c['xfail']}")
            else:
                status = "PASS" if ok else "FAIL"
                detail = "" if ok else f"{c['validator']}: kỳ vọng {c['expect']}, thực tế {'detect' if detected else 'clean'}"
            out.append({"id": c["id"], "status": status, "detail": detail})
    return out


# --------------------------------------------------------------------------- behavior
def _load_behavior():
    return json.loads((REG / "behavior-cases.json").read_text(encoding="utf-8"))["cases"]


def suite_behavior():
    out = []
    for c in _load_behavior():
        resp = RESPONSES / f"{c['id']}.md"
        if not resp.exists():
            out.append({"id": c["id"], "status": "NOT_RUN",
                        "detail": f"Chưa có câu trả lời tại responses/{c['id']}.md"})
            continue
        text = resp.read_text(encoding="utf-8", errors="ignore")
        failed = []
        for chk in c["auto_checks"]:
            hit = re.search(chk["pattern"], text) is not None
            if hit != chk["expect"]:
                failed.append(chk["desc"])
        n = len(c["auto_checks"])
        manual = c.get("manual_checks", [])
        if failed:
            out.append({"id": c["id"], "status": "FAIL",
                        "detail": f"{n - len(failed)}/{n} auto check. Trượt: {'; '.join(failed)}"})
        else:
            tail = f" · Cần người chấm: {'; '.join(manual)}" if manual else ""
            out.append({"id": c["id"], "status": "PASS", "detail": f"{n}/{n} auto check{tail}"})
    return out


# --------------------------------------------------------------------------- golden
RE_APPROVED = re.compile(r"(?im)(status|trạng thái)\s*[:|]\s*\**\s*(approved|baseline)")


def suite_golden():
    try:
        entries = json.loads(GOLDEN.read_text(encoding="utf-8")).get("entries", [])
    except Exception as e:
        return [{"id": "GOLDEN", "status": "FAIL", "detail": f"manifest.json không đọc được: {e!r}"}]
    if not entries:
        return [{"id": "GOLDEN", "status": "NOT_RUN",
                 "detail": "Chưa có mẫu golden — Human chọn deliverable đã Approved (xem evaluations/golden/README.md, Q-007)"}]
    out = []
    for e in entries:
        gid, path = e.get("id", "?"), ROOT / e.get("path", "")
        problems = []
        if not path.is_file():
            out.append({"id": gid, "status": "FAIL", "detail": f"Không tìm thấy {e.get('path')}"})
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if not RE_APPROVED.search(text):
            problems.append("không còn trạng thái Approved/Baseline")
        for v in ("pii", "secret", "banned", "ambiguity"):
            if _detect(v, path, text):
                problems.append(f"vi phạm {v}")
        score, min_score = e.get("human_score"), e.get("min_score", 8)
        if score is None:
            problems.append("thiếu human_score")
        elif score < min_score:
            problems.append(f"điểm rubric {score} < {min_score}")
        out.append({"id": gid, "status": "FAIL" if problems else "PASS",
                    "detail": "; ".join(problems) if problems else f"rubric {score}/10"})
    return out


# --------------------------------------------------------------------------- main
SUITES = {"harness": suite_harness, "validators": suite_validators, "behavior": suite_behavior,
          "golden": suite_golden}
ICON = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️ ", "XFAIL": "🟡", "XPASS": "🎉", "NOT_RUN": "⏸️ "}


def main():
    ap = argparse.ArgumentParser(description="Harness eval runner")
    ap.add_argument("--suite", choices=["all", *SUITES], default="all")
    ap.add_argument("--no-history", action="store_true")
    ap.add_argument("--list-prompts", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="Chỉ in dòng không PASS")
    args = ap.parse_args()

    if args.list_prompts:
        for c in _load_behavior():
            print(f"### {c['id']} — {c['title']}\n{c['prompt']}\n-> lưu câu trả lời vào evaluations/regression/responses/{c['id']}.md\n")
        return

    names = list(SUITES) if args.suite == "all" else [args.suite]
    summary, any_fail = {}, False
    for name in names:
        try:
            results = SUITES[name]()
        except Exception as e:
            results = [{"id": name.upper(), "status": "FAIL", "detail": f"Suite crash: {e!r}"}]
        counts = Counter(r["status"] for r in results)
        summary[name] = dict(counts)
        any_fail |= counts.get("FAIL", 0) > 0
        print(f"\n=== Suite: {name} ===")
        for r in results:
            if args.quiet and r["status"] == "PASS":
                continue
            line = f"{ICON[r['status']]} {r['status']:<7} {r['id']}"
            print(line + (f" — {r['detail']}" if r["detail"] else ""))
        print("    " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))

    print("\n=== Tổng kết ===")
    for name, counts in summary.items():
        print(f"  {name:<11} " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    b = summary.get("behavior")
    if b:
        ran = b.get("PASS", 0) + b.get("FAIL", 0)
        if ran:
            print(f"  behavior score (auto): {b.get('PASS', 0)}/{ran} case đã chạy")

    if not args.no_history:
        HISTORY.parent.mkdir(parents=True, exist_ok=True)
        with open(HISTORY, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"ts": datetime.now().isoformat(timespec="seconds"),
                                 "summary": summary}, ensure_ascii=False) + "\n")
        print(f"  Đã ghi lịch sử: {HISTORY.relative_to(ROOT).as_posix()}")
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
