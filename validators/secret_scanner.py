#!/usr/bin/env python3
"""
Secret Scanner — phát hiện token / API key / private key bị ghi lộ vào tài liệu, log, code.
Thuộc Security Harness (DEC-008). Bổ sung cho pii_scanner.py (PII của người dùng).

Nguyên tắc an toàn:
  - KHÔNG BAO GIỜ in giá trị secret ra stdout (chỉ in loại + vị trí + 4 ký tự đầu đã che).
  - Placeholder trong .env.example / tài liệu hướng dẫn (your_token, xxx, <...>, changeme...) không bị bắt.

Usage:
  python validators/secret_scanner.py --file <path>
  python validators/secret_scanner.py --dir <path>      # mặc định: thư mục gốc dự án
Exit: 0 = sạch, 1 = phát hiện secret.
"""
import argparse
import os
import re
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]

# Pattern đặc thù nhà cung cấp — độ chính xác cao.
PATTERNS = {
    "Telegram Bot Token": re.compile(r"(?<![\w])\d{8,10}:[A-Za-z0-9_-]{35}(?![\w-])"),
    "Google API Key": re.compile(r"(?<![\w])AIza[0-9A-Za-z_-]{35}(?![\w-])"),
    "Atlassian API Token": re.compile(r"(?<![\w])ATATT3[A-Za-z0-9_\-=]{40,}"),
    "GitHub Token": re.compile(r"(?<![\w])gh[pousr]_[A-Za-z0-9]{36,}"),
    "AWS Access Key ID": re.compile(r"(?<![A-Z0-9])(?:AKIA|ASIA)[0-9A-Z]{16}(?![A-Z0-9])"),
    "OpenAI / Anthropic Key": re.compile(r"(?<![\w-])sk-(?:ant-|proj-)?[A-Za-z0-9_-]{32,}"),
    "Private Key Block": re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"),
}

# Gán giá trị cho biến có tên nhạy cảm: TOKEN=..., "api_key": "...", password: ...
RE_ASSIGNMENT = re.compile(
    r"(?i)\b([A-Z0-9_]*(?:TOKEN|SECRET|PASSWORD|PASSWD|API[_-]?KEY|ACCESS[_-]?KEY|PRIVATE[_-]?KEY))\b"
    r"[\"']?\s*[:=]\s*[\"']?([^\s\"'`,;]{16,})"
)
PLACEHOLDER_HINTS = ("your", "xxx", "example", "changeme", "placeholder", "dummy", "sample",
                     "<", ">", "{", "}", "$", "***", "...", "os.getenv", "environ", "redacted")

SCAN_EXTS = (".md", ".txt", ".json", ".py", ".ps1", ".yml", ".yaml", ".env", ".html", ".csv", ".ini", ".cfg")
SKIP_DIRS = {".git", "__pycache__", "node_modules", "brain"}


def _looks_real(value):
    """Giá trị gán trông như secret thật: đủ dài, trộn chữ + số, không phải placeholder."""
    low = value.lower()
    if any(h in low for h in PLACEHOLDER_HINTS):
        return False
    return bool(re.search(r"[A-Za-z]", value)) and bool(re.search(r"\d", value))


def _mask(value):
    return value[:4] + "*" * 8


def scan_text(text):
    """Trả về list (line_no, secret_type, masked_preview). Không trả giá trị gốc."""
    issues = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        hit_spans = []
        for stype, rx in PATTERNS.items():
            for m in rx.finditer(line):
                issues.append((line_no, stype, _mask(m.group(0))))
                hit_spans.append(m.span())
        for m in RE_ASSIGNMENT.finditer(line):
            val = m.group(2)
            if any(s <= m.start(2) < e for s, e in hit_spans):
                continue  # đã bắt bởi pattern đặc thù
            if _looks_real(val):
                issues.append((line_no, f"Hardcoded secret ({m.group(1)})", _mask(val)))
    return issues


def scan_file(file_path):
    try:
        text = Path(file_path).read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        print(f"Lỗi khi đọc file {file_path}: {e}")
        return []
    return scan_text(text)


def scan_directory(dir_path):
    results = {}
    for root, dirs, files in os.walk(dir_path):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name == ".env.example" or not (name.endswith(SCAN_EXTS) or name == ".env"):
                continue
            full = os.path.join(root, name)
            issues = scan_file(full)
            if issues:
                results[full] = issues
    return results


def main():
    ap = argparse.ArgumentParser(description="Quét secret / token / API key bị ghi lộ.")
    ap.add_argument("--file", help="File cần quét")
    ap.add_argument("--dir", help="Thư mục cần quét (mặc định: gốc dự án)")
    args = ap.parse_args()

    print("🔑 SECRET SCANNER RUNNING...")
    if args.file:
        if not os.path.exists(args.file):
            print(f"File không tồn tại: {args.file}")
            sys.exit(1)
        results = {args.file: scan_file(args.file)}
        results = {k: v for k, v in results.items() if v}
    else:
        target = args.dir or str(ROOT)
        if not os.path.exists(target):
            print(f"Thư mục không tồn tại: {target}")
            sys.exit(1)
        results = scan_directory(target)

    if not results:
        print("✅ SECRET SCAN PASS: Không phát hiện token / API key / private key.")
        sys.exit(0)
    for path, issues in results.items():
        print(f"\n❌ File vi phạm: {path}")
        for line_no, stype, preview in issues:
            print(f"   Dòng {line_no} [{stype}]: {preview}")
    print("\n❌ CẢNH BÁO ĐỎ: Phát hiện secret bị ghi lộ. Thu hồi (revoke) secret, chuyển vào .env, KHÔNG chỉ xóa dòng.")
    sys.exit(1)


if __name__ == "__main__":
    main()
