#!/usr/bin/env python3
"""
Agent Gate Hook — vòng phản hồi tự động cho Quality Gate (Antigravity lifecycle hooks).

Vì sao cần file này (thay cho việc gọi post-task.ps1 trực tiếp từ hooks.json):
  1. Payload PostToolUse KHÔNG chứa toolCall/TargetFile (chỉ có stepIdx, error, metadata)
     -> post-task.ps1 không biết file nào vừa sửa -> luôn "Bỏ qua" (hook vô hiệu).
  2. PostToolUse chỉ được trả "{}" -> không thể báo lỗi lại cho agent.
  3. Write-Host của PowerShell làm bẩn stdout (hook yêu cầu stdout là JSON thuần).

Cơ chế:
  post-tool       (PostToolUse, matcher = các tool ghi file)
      Quét artifacts/**/*.md, phát hiện file mới/đổi theo mtime, chạy 4 validator
      (ambiguity, PII, banned words, secret — DEC-008). FAIL -> ghi Gate Report + đưa vào hàng chờ phản hồi.
  pre-invocation  (PreInvocation)
      Nếu hàng chờ có vi phạm CHƯA báo -> inject ephemeralMessage để agent tự sửa.

Nguyên tắc an toàn: mọi lỗi nội bộ đều bị nuốt, stdout LUÔN là JSON hợp lệ,
hook không bao giờ làm treo / sập vòng lặp agent.

Chạy tay để debug:
  python hooks/agent_gate_hook.py post-tool < NUL
  python hooks/agent_gate_hook.py pre-invocation < NUL
  python hooks/agent_gate_hook.py status
"""
import io
import json
import sys
import time
from contextlib import redirect_stdout
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WATCH_DIR = ROOT / "artifacts"
STATE_FILE = Path(__file__).resolve().parent / ".gate_hook_state.json"
REPORT_DIR = ROOT / "observability" / "gate-reports"
FRESH_WINDOW_SEC = 300      # lần chạy đầu: chỉ kiểm tra file sửa trong 5 phút gần nhất
MAX_FINDINGS_PER_FILE = 8   # giới hạn để không làm phình context của agent

sys.path.insert(0, str(ROOT / "validators"))


def _load_state():
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_state(state):
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def _validate(path):
    """Trả về list chuỗi vi phạm (rỗng = PASS). Import validator in-process để chạy < 1s."""
    findings = []
    # Import TRƯỚC khi redirect: ambiguity_scanner gọi sys.stdout.reconfigure() lúc import.
    import ambiguity_scanner
    import banned_words_validator
    import pii_scanner
    import secret_scanner

    with redirect_stdout(io.StringIO()):  # validator có thể in ra stdout -> chặn lại
        content = path.read_text(encoding="utf-8", errors="ignore")
        for line_no, pii_type, _val, _ in pii_scanner.scan_file(str(path)):
            # KHÔNG đưa giá trị PII vào message (tránh chính hook làm lộ PII)
            findings.append((line_no, pii_type, f"L{line_no} [PII] {pii_type} — phải mask theo NĐ 13/2023"))
        for line_no, stype, _preview in secret_scanner.scan_text(content):
            # KHÔNG đưa giá trị secret vào message
            findings.append((line_no, stype, f"L{line_no} [Secret] {stype} — thu hồi secret, chuyển vào .env"))
        for line_no, word, _ in banned_words_validator.scan_text(content, filepath=str(path)):
            findings.append((line_no, word, f"L{line_no} [Từ cấm] '{word}' — thay bằng chỉ số đo lường được"))
        for item in ambiguity_scanner.scan_file(str(path)):
            findings.append((item["line"], item["term"], f"L{item['line']} [Mơ hồ] '{item['term']}'"))
    # khử trùng lặp theo (dòng, từ): banned-words & ambiguity chồng lấn nhau
    seen, uniq = set(), []
    for line_no, term, msg in sorted(findings, key=lambda x: x[0]):
        key = (line_no, str(term).lower())
        if key not in seen:
            seen.add(key)
            uniq.append(msg)
    return uniq


def _write_report(rel, findings):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now()
    name = f"QGR-{ts:%Y%m%d-%H%M%S}-hook-{Path(rel).stem}.md"
    body = [
        f"# Quality Gate Report — {Path(rel).name}",
        "",
        f"> **Nguồn:** `hooks/agent_gate_hook.py` (PostToolUse, tự động)  ",
        f"> **Thời gian:** {ts:%Y-%m-%d %H:%M:%S}  ",
        f"> **Artifact:** `{rel}`  ",
        "> **Kết quả:** **[FAIL]**",
        "",
        f"## Vi phạm ({len(findings)})",
        "",
        *[f"- {f}" for f in findings],
        "",
        "## Bước tiếp theo",
        "- [ ] BLOCKING: sửa các vi phạm trên trước khi bàn giao hoặc trình Human baseline.",
        "",
    ]
    (REPORT_DIR / name).write_text("\n".join(body), encoding="utf-8")
    return f"observability/gate-reports/{name}"


def post_tool():
    state = _load_state()
    first_run = "mtimes" not in state
    mtimes = state.setdefault("mtimes", {})
    pending = state.setdefault("pending", {})
    now = time.time()

    for p in WATCH_DIR.rglob("*.md"):
        rel = p.relative_to(ROOT).as_posix()
        mt = p.stat().st_mtime
        if mtimes.get(rel) == mt:
            continue
        mtimes[rel] = mt
        if first_run and now - mt > FRESH_WINDOW_SEC:
            continue  # baseline: không quét lại toàn bộ lịch sử ở lần chạy đầu
        findings = _validate(p)
        if findings:
            report = _write_report(rel, findings)
            pending[rel] = {"findings": findings, "report": report, "delivered": False}
        else:
            pending.pop(rel, None)

    # file đã bị xóa -> dọn state
    for rel in [r for r in mtimes if not (ROOT / r).exists()]:
        mtimes.pop(rel, None)
        pending.pop(rel, None)
    _save_state(state)
    return {}


def pre_invocation():
    state = _load_state()
    pending = state.get("pending", {})
    fresh = {r: v for r, v in pending.items() if not v.get("delivered")}
    if not fresh:
        return {}
    lines = ["[QUALITY GATE — hooks/agent_gate_hook.py] Artifact vừa ghi KHÔNG đạt gate tự động:"]
    for rel, v in fresh.items():
        shown = v["findings"][:MAX_FINDINGS_PER_FILE]
        more = len(v["findings"]) - len(shown)
        lines.append(f"- {rel} (report: {v['report']})")
        lines += [f"    {f}" for f in shown]
        if more > 0:
            lines.append(f"    ... và {more} vi phạm khác (xem report)")
        v["delivered"] = True
    lines.append("Hãy sửa trước khi bàn giao. Nếu là false positive, nêu rõ lý do cho Human thay vì im lặng bỏ qua.")
    _save_state(state)
    return {"injectSteps": [{"ephemeralMessage": "\n".join(lines)}]}


def status():
    return _load_state().get("pending", {})


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    # Không đọc stdin: payload không cần dùng (PostToolUse không có TargetFile),
    # và read() có thể treo nếu process cha không đóng stdin.
    result = {}
    try:
        if mode == "post-tool":
            result = post_tool()
        elif mode == "pre-invocation":
            result = pre_invocation()
        elif mode == "status":
            result = status()
    except Exception as e:  # không bao giờ làm sập vòng lặp agent
        try:
            sys.stderr.write(f"agent_gate_hook error: {e!r}\n")
        except Exception:
            pass
        result = {}
    sys.stdout.write(json.dumps(result, ensure_ascii=True))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
