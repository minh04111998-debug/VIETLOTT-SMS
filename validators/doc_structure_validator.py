#!/usr/bin/env python3
import os
import argparse
import re
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def validate_adr(content):
    errors = []
    required_checks = [
        ("Bối cảnh / Context", r"(#+\s*.*(bối cảnh|ngữ cảnh|context)|\*\*Bối cảnh|\*\*Context)"),
        ("Quyết định / Decision", r"(#+\s*.*(quyết định|decision|solution|giải pháp)|\*\*Quyết định|\*\*Decision)"),
        ("Phương án / Options / Trade-off", r"(#+\s*.*(phương án|options|analysis|lý do|trade-off|cân nhắc|xem xét)|\*\*Phương án|\*\*Trade-offs)"),
        ("Hệ quả / Consequences / Tác động", r"(#+\s*.*(hệ quả|hậu quả|consequences|tác động|impact)|\*\*Hệ quả|\*\*Consequences)"),
        ("Review / Xem lại / Verification", r"(#+\s*.*(review|xem lại|verification|kiểm tra)|\*\*Review|\*\*Verification)")
    ]
    
    for section_name, pattern in required_checks:
        if not re.search(pattern, content, re.IGNORECASE):
            errors.append(f"Missing required ADR section: {section_name}")
            
    return errors

def validate_srs(content):
    errors = []
    has_fr = bool(re.search(r"(FR-|Functional Requirement|Yêu cầu chức năng|Chức năng)", content, re.IGNORECASE))
    has_nfr = bool(re.search(r"(NFR|Non-Functional|Phi chức năng)", content, re.IGNORECASE))
    if not has_fr:
        errors.append("SRS missing Functional Requirements")
    if not has_nfr:
        errors.append("SRS missing Non-Functional Requirements (NFR)")
    return errors

def validate_general(content, filepath=None):
    errors = []
    
    # Skip non-spec files (README, assets, mockups, data, templates)
    if filepath:
        fp_str = str(filepath).lower().replace('\\', '/')
        if filepath.name.lower() in ["readme.md", ".gitkeep"] or "-template" in filepath.name.lower():
            return errors
        if any(skip_dir in fp_str for skip_dir in ["/presentation", "/mockup", "/tokens", "/data/", "/templates/"]):
            return errors

    # Check for versioning table or header metadata
    has_version = bool(re.search(r"(\|\s*(Version|Phiên bản|Ver)\b|Version Control|Lịch sử phiên bản|\bVersion:\s*|\bPhiên bản:\s*|\bMã tài liệu:)", content, re.IGNORECASE))
    if not has_version:
        errors.append("Missing Version Control table or metadata header")
        
    # Check heading hierarchy jump (ignoring code blocks)
    lines = content.split('\n')
    last_level = 0
    in_code_block = False
    for idx, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        match = re.match(r'^(#+)\s+', line)
        if match:
            level = len(match.group(1))
            if last_level > 0 and level > last_level + 1:
                errors.append(f"Heading hierarchy jump at line {idx+1}: H{last_level} -> H{level}")
            last_level = level
            
    return errors

def scan_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        filename = filepath.name.lower()
        errors = validate_general(content, filepath)
        
        if "adr-" in filename:
            errors.extend(validate_adr(content))
        elif "srs-" in filename:
            errors.extend(validate_srs(content))
            
        return errors
    except Exception as e:
        return [f"Error reading file: {e}"]

def main():
    parser = argparse.ArgumentParser(description="Validate markdown document structure.")
    parser.add_argument("--file", help="Path to a specific markdown file")
    parser.add_argument("--dir", help="Path to a directory to scan all markdown files")
    
    args = parser.parse_args()
    
    if not args.file and not args.dir:
        parser.print_help()
        return

    files_to_scan = []
    if args.file:
        files_to_scan.append(Path(args.file))
    if args.dir:
        dir_path = Path(args.dir)
        if dir_path.exists() and dir_path.is_dir():
            files_to_scan.extend(list(dir_path.rglob("*.md")))
        else:
            print(f"Directory not found: {args.dir}")
            return

    total_issues = 0
    print(f"📐 DOCUMENT STRUCTURE VALIDATOR RUNNING...\n")
    
    for file_path in files_to_scan:
        issues = scan_file(file_path)
        if issues:
            print(f"⚠️  File: {file_path}")
            for issue in issues:
                print(f"   - {issue}")
                total_issues += 1
            print("-" * 50)
            
    if total_issues == 0:
        print("✅ All documents have valid structures!")
    else:
        print(f"❌ Found {total_issues} structural issues. Please fix them according to conventions.md.")

if __name__ == "__main__":
    main()
