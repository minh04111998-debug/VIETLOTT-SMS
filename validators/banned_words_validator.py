#!/usr/bin/env python3
"""
Banned Words Validator - Quét các từ ngữ mơ hồ, lười biếng, cấm đoán theo rules/global/banned-words.md
"""

import os
import re
import sys
import argparse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BANNED_WORDS = [
    # Mơ hồ về hiệu năng / tính năng
    "nhanh", "dễ dùng", "thân thiện", "mượt mà", "tối ưu", "linh hoạt", "hiệu quả",
    "đơn giản", "tiện lợi", "ổn định", "mạnh mẽ", "thông minh",
    # Mơ hồ về tiến độ / trạng thái
    "tbd", "todo", "sắp có", "tính sau", "cập nhật sau", "chưa rõ", "tuỳ ý",
    # Mơ hồ về bảo mật
    "an toàn", "bảo mật cao", "chuẩn ngân hàng",
    # Mơ hồ về số lượng
    "vài", "nhiều", "một số", "ít", "khoảng", "khoảng chừng"
]

def scan_text(content, filepath=""):
    findings = []
    lines = content.splitlines()
    in_code_block = False
    is_rule_def = "rules" in filepath.lower() or "banned-words" in filepath.lower() or "checklist" in filepath.lower()

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        # Bỏ qua dòng trích dẫn văn bản quy phạm pháp luật / trích dẫn gốc
        stripped_lower = stripped.lower()
        if "văn bản gốc:" in stripped_lower or "*văn bản gốc:*" in stripped_lower:
            continue
        if stripped_lower.startswith('*"trong trường hợp') or stripped_lower.startswith('> *"trong trường hợp'):
            continue

        # Bỏ qua mã inline `...`
        clean_line = re.sub(r'`[^`]*`', '', line)
        line_lower = clean_line.lower()

        # Bỏ qua header "An Toàn & Bảo Mật"
        is_security_header = stripped.startswith('#') and any(term in line_lower for term in ("an toàn & bảo mật", "an toàn và bảo mật", "an toàn, bảo mật"))

        for bw in BANNED_WORDS:
            if bw == "ít":
                pattern = r'\bít(?!\s+nhất\s+\d+)\b'
            elif bw == "khoảng":
                pattern = r'\bkhoảng(?!\s+cách)\b'
            elif bw == "an toàn" and is_security_header:
                continue
            elif bw == "nhanh":
                pattern = r'(?<!quay\s)\bnhanh\b'
            else:
                pattern = r'\b' + re.escape(bw) + r'\b'
            if re.search(pattern, line_lower):
                findings.append((idx, bw, stripped))
    return findings

def main():
    parser = argparse.ArgumentParser(description="Scan for banned ambiguous terms.")
    parser.add_argument("--file", help="Path to markdown/text file to scan")
    parser.add_argument("--dir", help="Path to directory to scan recursively")
    args = parser.parse_args()

    if not args.file and not args.dir:
        args.dir = "artifacts"

    print("🔎 BANNED WORDS VALIDATOR RUNNING...")
    violations = 0

    if args.file:
        if not os.path.exists(args.file):
            print(f"File not found: {args.file}")
            sys.exit(1)
        with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        issues = scan_text(content, filepath=args.file)
        if issues:
            violations += len(issues)
            print(f"\n⚠️  {args.file}:")
            for line_no, word, text in issues:
                preview = text[:80] + "..." if len(text) > 80 else text
                print(f"   Line {line_no} [{word}]: {preview}")
    else:
        for root, _, files in os.walk(args.dir):
            for file in files:
                if file.endswith((".md", ".txt")):
                    fp = os.path.join(root, file)
                    with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    issues = scan_text(content, filepath=fp)
                    if issues:
                        violations += len(issues)
                        print(f"\n⚠️  {fp}:")
                        for line_no, word, text in issues:
                            preview = text[:80] + "..." if len(text) > 80 else text
                            print(f"   Line {line_no} [{word}]: {preview}")

    print("-" * 50)
    if violations > 0:
        print(f"❌ FAILED: Found {violations} instances of banned/ambiguous words.")
        print("Please replace with quantitative, concrete specifications.")
        sys.exit(1)
    else:
        print("✅ BANNED WORDS SCAN PASS: Không phát hiện từ ngữ mơ hồ vi phạm.")
        sys.exit(0)

if __name__ == "__main__":
    main()
