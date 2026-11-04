#!/usr/bin/env python3
"""
PII Scanner - Quét và phát hiện thông tin định danh cá nhân chưa được ẩn danh (Masked)
Tuân thủ: Nghị định 13/2023/NĐ-CP và rules/security/privacy-and-pii-rules.md
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

# Regex patterns for sensitive unmasked Vietnamese PII
PATTERNS = {
    "Unmasked Phone Number (Số điện thoại thật)": re.compile(
        r"(?<!\d)(?:(?:\+84|84|0)\s*(?:3[2-9]|5[6|8|9]|7[0|6-9]|8[1-9]|9[0-9]))(?:\s*\d){7}(?!\d)"
    ),
    "Unmasked CCCD / CMND (12 chữ số)": re.compile(
        r"(?<!\d)0(?:0[1-9]|[1-8]\d|9[0-6])\d{9}(?!\d)"
    ),
    "Exposed OTP Code": re.compile(
        r"(?i)\b(?:mã\s+otp|otp\s+code|mã\s+xác\s+thực)\s*[:=]\s*\d{4,6}\b"
    ),
    "Exposed Payment Card (Số thẻ thanh toán)": re.compile(
        r"\b(?:\d{4}[ \-]){3}\d{4}\b|\b\d{16}\b"
    ),
}

def scan_file(file_path):
    issues = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            for line_no, line in enumerate(lines, start=1):
                # Bỏ qua nếu dòng là mask hoàn toàn hoặc dòng ví dụ quy chuẩn
                for pii_type, regex in PATTERNS.items():
                    matches = regex.findall(line)
                    if matches:
                        for m in matches:
                            # Đảm bảo match không nằm trong chuỗi đã mask sao
                            if isinstance(m, str) and "*" in m:
                                continue
                            issues.append((line_no, pii_type, m, line.strip()))
    except Exception as e:
        print(f"Lỗi khi đọc file {file_path}: {e}")
    return issues

def scan_directory(dir_path):
    all_issues = {}
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith((".md", ".txt", ".json", ".html")):
                full_path = os.path.join(root, file)
                issues = scan_file(full_path)
                if issues:
                    all_issues[full_path] = issues
    return all_issues

def main():
    parser = argparse.ArgumentParser(description="Scan files for unmasked PII data.")
    parser.add_argument("--file", help="Đường dẫn tới file cần quét")
    parser.add_argument("--dir", help="Đường dẫn tới thư mục cần quét")
    args = parser.parse_args()

    target_file = args.file
    target_dir = args.dir

    if not target_file and not target_dir:
        target_dir = "artifacts"

    print("🛡️ PII SCANNER RUNNING...")
    found_any = False

    if target_file:
        if not os.path.exists(target_file):
            print(f"File không tồn tại: {target_file}")
            sys.exit(1)
        issues = scan_file(target_file)
        if issues:
            found_any = True
            print(f"\n⚠️  File vi phạm: {target_file}")
            for line_no, pii_type, val, line in issues:
                print(f"   Dòng {line_no} [{pii_type}]: {val}")
                print(f"   > {line[:100]}")
    else:
        if not os.path.exists(target_dir):
            print(f"Thư mục không tồn tại: {target_dir}")
            sys.exit(1)
        results = scan_directory(target_dir)
        if results:
            found_any = True
            for fpath, issues in results.items():
                print(f"\n⚠️  File vi phạm: {fpath}")
                for line_no, pii_type, val, line in issues:
                    print(f"   Dòng {line_no} [{pii_type}]: {val}")
                    print(f"   > {line[:100]}")

    if found_any:
        print("\n❌ CẢNH BÁO ĐỎ: Phát hiện dữ liệu cá nhân (PII) chưa được ẩn danh (Masked)!")
        print("Vui lòng che số điện thoại (VD: 091****888), CCCD (VD: 001099******) theo quy định.")
        sys.exit(1)
    else:
        print("✅ PII SCAN PASS: Không phát hiện dữ liệu nhạy cảm chưa che.")
        sys.exit(0)

if __name__ == "__main__":
    main()
