#!/usr/bin/env python3
import os
import argparse
import re
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Dictionary of ambiguous terms
AMBIGUOUS_TERMS_VI = [
    "sẽ bổ sung sau", "tương tự như", "nhanh", "dễ dùng", "thân thiện", 
    "phù hợp", "linh hoạt", "cần thiết", "hiệu quả", "v.v.", "etc.", 
    "TBD", "TODO"
]

AMBIGUOUS_TERMS_EN = [
    "TBD", "TODO", "as needed", "if applicable", "appropriate", 
    "user-friendly", "fast", "efficient", "flexible"
]

ALL_TERMS = AMBIGUOUS_TERMS_VI + AMBIGUOUS_TERMS_EN

def scan_file(filepath):
    results = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        in_code_block = False
        for line_idx, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue

            # Strip inline code to avoid false positives in tokens or technical code snippets
            clean_line = re.sub(r'`[^`]*`', '', line).strip()
            line_lower = clean_line.lower()

            for term in ALL_TERMS:
                term_lower = term.lower()
                if term_lower == "fast":
                    pattern = r'(?<![\w\-])fast(?![\w\-])'
                elif term_lower in ("nhanh", "dễ dùng", "thân thiện", "phù hợp", "linh hoạt", "hiệu quả", "cần thiết"):
                    pattern = r'\b' + re.escape(term_lower) + r'\b'
                else:
                    pattern = r'\b' + re.escape(term_lower) + r'\b'

                if re.search(pattern, line_lower):
                    # Context exclusions for official product category
                    if term_lower in ("nhanh", "fast") and ("quay nhanh" in line_lower or "fast draw" in line_lower or "fast-play" in line_lower):
                        continue
                    results.append({
                        'line': line_idx + 1,
                        'term': term,
                        'content': line.strip()
                    })
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        
    return results

def main():
    parser = argparse.ArgumentParser(description="Scan markdown files for ambiguous terms.")
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
    print(f"🔍 AMBIGUITY SCANNER RUNNING...\n")
    
    for file_path in files_to_scan:
        issues = scan_file(file_path)
        if issues:
            print(f"⚠️  File: {file_path}")
            for issue in issues:
                print(f"   Line {issue['line']}: Found '{issue['term']}'")
                print(f"   > {issue['content']}")
                total_issues += 1
            print("-" * 50)
            
    if total_issues == 0:
        print("✅ No ambiguous terms found! Excellent specification.")
    else:
        print(f"❌ Found {total_issues} ambiguous issues across {len(files_to_scan)} file(s). Please revise to be exact and quantitative.")

if __name__ == "__main__":
    main()
