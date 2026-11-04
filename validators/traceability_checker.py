#!/usr/bin/env python3
import os
import argparse
import re
import sys
from pathlib import Path
from collections import defaultdict

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    default_project_root = str(Path(__file__).resolve().parents[1])
    parser = argparse.ArgumentParser(description="Traceability Checker for Project Documents")
    parser.add_argument("--project-path", default=default_project_root, help="Path to the project root directory")
    args = parser.parse_args()

    project_path = Path(args.project_path)

    print("\n╔══════════════════════════════════════════════════╗")
    print("║  📋 TRACEABILITY CHECKER — BA Agent             ║")
    print("║  Quét tính nhất quán tài liệu dự án             ║")
    print("╚══════════════════════════════════════════════════╝\n")

    scan_dirs = [
        project_path / "artifacts" / "requirements",
        project_path / "artifacts" / "product",
        project_path / "artifacts" / "analysis",
        project_path / "artifacts" / "technical",
        project_path / "artifacts" / "testing"
    ]

    md_files = []
    for d in scan_dirs:
        if d.exists() and d.is_dir():
            md_files.extend(list(d.rglob("*.md")))

    if not md_files:
        print("❌ Không tìm thấy file tài liệu .md nào trong artifacts/ để kiểm tra truy vết.")
        sys.exit(1)

    print(f"📂 Đã tìm thấy {len(md_files)} file .md để quét truy vết:\n")
    for f in md_files:
        print(f"  - {f.relative_to(project_path)}")
    print()

    br_ids = defaultdict(set)
    fr_ids = defaultdict(set)
    nfr_ids = defaultdict(set)
    uc_ids = defaultdict(set)
    tc_ids = defaultdict(set)
    us_ids = defaultdict(set)

    patterns = {
        "BR": re.compile(r"\bBR-\d{1,4}\b"),
        "FR": re.compile(r"\bFR-\d{1,4}\b"),
        "NFR": re.compile(r"\bNFR-\d{1,4}\b"),
        "UC": re.compile(r"\bUC-[\w\.\-]+\b"),
        "TC": re.compile(r"\bTC-[\w\-]+\b"),
        "US": re.compile(r"\bUS-\d{1,4}\b")
    }

    # Extract IDs from all files
    for filepath in md_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for m in patterns["BR"].finditer(content):
                br_ids[m.group(0)].add(filepath.name)
            for m in patterns["FR"].finditer(content):
                fr_ids[m.group(0)].add(filepath.name)
            for m in patterns["NFR"].finditer(content):
                nfr_ids[m.group(0)].add(filepath.name)
            for m in patterns["UC"].finditer(content):
                uc_ids[m.group(0)].add(filepath.name)
            for m in patterns["TC"].finditer(content):
                tc_ids[m.group(0)].add(filepath.name)
            for m in patterns["US"].finditer(content):
                us_ids[m.group(0)].add(filepath.name)
        except Exception:
            pass

    total_found = len(br_ids) + len(fr_ids) + len(nfr_ids) + len(uc_ids) + len(us_ids) + len(tc_ids)

    print("═══════════════════════════════════════")
    print("📊 TỔNG QUAN IDs TÌM THẤY")
    print("═══════════════════════════════════════")
    print(f"  BR (Business Requirements)     : {len(br_ids)}")
    print(f"  FR (Functional Requirements)   : {len(fr_ids)}")
    print(f"  NFR (Non-Functional Reqs)      : {len(nfr_ids)}")
    print(f"  UC (Use Cases)                 : {len(uc_ids)}")
    print(f"  US (User Stories)              : {len(us_ids)}")
    print(f"  TC (Test Cases)                : {len(tc_ids)}")
    print(f"  Tổng số IDs tìm thấy           : {total_found}\n")

    def show_table(label, id_map):
        if id_map:
            print(f"📝 {label}")
            print("  " + "-" * 50)
            for k in sorted(id_map.keys()):
                print(f"  {k} → {', '.join(sorted(id_map[k]))}")
            print()

    show_table("Business Requirements (BR)", br_ids)
    show_table("Functional Requirements (FR)", fr_ids)
    show_table("Non-Functional Requirements (NFR)", nfr_ids)
    show_table("Use Cases (UC)", uc_ids)
    show_table("User Stories (US)", us_ids)
    show_table("Test Cases (TC)", tc_ids)

    print("═══════════════════════════════════════")
    print("🔍 KIỂM TRA MỒ CÔI (ORPHAN DETECTION)")
    print("═══════════════════════════════════════")

    orphans = []
    warnings = []

    if total_found == 0:
        warnings.append("⚠️ Không tìm thấy bất kỳ ID yêu cầu nào (BR/FR/NFR/UC/US/TC). Vui lòng gắn tag ID vào tài liệu.")

    for br, files in br_ids.items():
        if len(files) == 1:
            warnings.append(f"⚠️  {br} chỉ xuất hiện trong 1 file ({list(files)[0]}). Có thể chưa được trace sang SRS/Test.")

    for fr, files in fr_ids.items():
        if len(files) == 1:
            warnings.append(f"⚠️  {fr} chỉ xuất hiện trong 1 file ({list(files)[0]}). Chưa được phân bổ sang Test Plan/Test Case.")

    for nfr, files in nfr_ids.items():
        if len(files) == 1:
            warnings.append(f"⚠️  {nfr} chỉ xuất hiện trong 1 file ({list(files)[0]}). Chưa được phân bổ sang Test Plan/Security Spec.")

    tc_files = set()
    for files in tc_ids.values():
        tc_files.update(files)
        
    for uc, files in uc_ids.items():
        has_tc_ref = any(f in tc_files for f in files)
        if not has_tc_ref and tc_ids:
            orphans.append(f"❌ {uc} không có Test Case nào tham chiếu (orphaned UC)")

    if not orphans and not warnings:
        print("\n  ✅ Không phát hiện mục mồ côi nào. Tài liệu đồng bộ tốt!")
    else:
        if warnings:
            print(f"\n  CẢNH BÁO ({len(warnings)}):")
            for w in warnings:
                print(f"  {w}")
        if orphans:
            print(f"\n  LỖI TRUY VẾT ({len(orphans)}):")
            for o in orphans:
                print(f"  {o}")
            print("\n❌ TRACEABILITY CHECK FAILED: Có yêu cầu/UC bị mồ côi.")
            sys.exit(1)

    print("\n═══════════════════════════════════════")
    import datetime
    print(f"✅ Quét hoàn tất — {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("═══════════════════════════════════════\n")
    sys.exit(0)

if __name__ == "__main__":
    main()
