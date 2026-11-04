"""
Merge Markdown Files into One Consolidated Document
=====================================================
Reads all .md files from the converted markdown directory and merges them
into one comprehensive file with:
- Header + description
- Table of Contents (clickable anchors)
- Full content of each file, separated by horizontal rules
"""

import os
import re

# ============================================================
# Configuration
# ============================================================
INPUT_DIR = r"F:\VIETLOTT-SMS\00_Draft\03_1_markdown"
OUTPUT_FILE = r"F:\VIETLOTT-SMS\00_Draft\Index_TaiLieu\03.1. Đăng ký & Quản lý tài khoản (DangKy_QLTK) - Tổng hợp.md"

SECTION_TITLE = "03.1. Đăng ký & Quản lý tài khoản (DangKy_QLTK)"
SECTION_DESC = "Các luồng đăng ký/đăng nhập (Web/App), KYC, thay đổi thông tin cá nhân, định danh, quên mật khẩu, quản lý Role, và đóng/mở tài khoản."

WORD_SOURCE_DIR = r"F:\VIETLOTT-SMS\04_Document\VIETLOTT_SMS\VIETLOTT_SMS\03.Business_Analysis\03.1.DangKy_QLTK"


def extract_doc_title(md_content):
    """Try to extract a meaningful title from the markdown content."""
    # Look for the first heading
    match = re.search(r'^#{1,3}\s+(.+)$', md_content, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        # Clean up empty or meaningless titles
        if title and len(title) > 2:
            return title
    return None


def make_anchor(text):
    """Create a GitHub-style anchor from text."""
    anchor = text.lower()
    anchor = re.sub(r'[^\w\s\-]', '', anchor)
    anchor = re.sub(r'\s+', '-', anchor.strip())
    return anchor


def make_friendly_name(filename):
    """Convert filename to a human-friendly document name."""
    name = filename.replace('.md', '')
    # Remove common prefixes
    name = re.sub(r'^VietlottSMS?_', '', name)
    # Remove version and date suffixes like _v1.0_20251120
    name = re.sub(r'_v[\d.]+_\d{8}$', '', name)
    # Remove date-only suffixes like _20241112
    name = re.sub(r'_\d{8}$', '', name)
    # Replace underscores with spaces
    name = name.replace('_', ' ').replace('-', ' - ')
    return name


def shift_headings(md_content, shift=1):
    """Shift all headings down by `shift` levels to avoid title conflicts.
    
    e.g., # Title -> ## Title (when shift=1)
    This ensures the merged document has a clean heading hierarchy:
    - # = Document title
    - ## = Individual file sections
    - ### and below = Original file content headings
    """
    def replace_heading(match):
        hashes = match.group(1)
        rest = match.group(2)
        new_level = len(hashes) + shift
        if new_level > 6:
            new_level = 6
        return '#' * new_level + ' ' + rest
    
    return re.sub(r'^(#{1,6})\s+(.+)$', replace_heading, md_content, flags=re.MULTILINE)


def build_merged_document(input_dir, output_file):
    """Build the merged markdown document."""
    
    # Collect all .md files
    md_files = sorted([
        f for f in os.listdir(input_dir) 
        if f.endswith('.md')
    ])
    
    print(f"Found {len(md_files)} markdown files to merge.")
    
    # Read all files and prepare sections
    sections = []
    for filename in md_files:
        filepath = os.path.join(input_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        friendly_name = make_friendly_name(filename)
        doc_title = extract_doc_title(content) or friendly_name
        
        sections.append({
            'filename': filename,
            'friendly_name': friendly_name,
            'doc_title': doc_title,
            'content': content,
            'char_count': len(content),
        })
    
    # Build the document
    lines = []
    
    # --- Header ---
    lines.append(f'⬅️ **[Quay lại Trang Tổng Hợp](../Phân%20Loại%20&%20Đánh%20Giá%20Cấu%20Trúc%20Tài%20Liệu%20Vietlott%20SMS.md)**\n')
    lines.append(f'# {SECTION_TITLE}\n')
    lines.append(f'*Mô tả: {SECTION_DESC}*\n')
    lines.append(f'> **Ghi chú:** Tài liệu này được tổng hợp tự động từ {len(sections)} file Word đã chuyển đổi sang Markdown.')
    lines.append(f'> Hình ảnh không được bao gồm — vui lòng tham chiếu file Word gốc tại `03.Business_Analysis/03.1.DangKy_QLTK/` nếu cần xem hình.\n')
    
    # --- Table of Contents ---
    lines.append('---\n')
    lines.append('## 📋 Mục Lục\n')
    
    for i, section in enumerate(sections, 1):
        anchor = make_anchor(f"file-{i}-{section['friendly_name']}")
        lines.append(f'{i}. [{section["friendly_name"]}](#{anchor})')
    
    lines.append('')  # blank line after TOC
    
    # --- Statistics ---
    total_chars = sum(s['char_count'] for s in sections)
    lines.append(f'> **Thống kê:** {len(sections)} tài liệu | {total_chars:,} ký tự tổng cộng\n')
    
    # --- Content sections ---
    for i, section in enumerate(sections, 1):
        lines.append('---\n')
        
        # Section header with anchor
        anchor = make_anchor(f"file-{i}-{section['friendly_name']}")
        lines.append(f'## 📄 File {i}: {section["friendly_name"]}\n')
        
        # Metadata
        lines.append(f'> **File gốc:** `{section["filename"].replace(".md", "")}`')
        lines.append(f'> **Dung lượng nội dung:** {section["char_count"]:,} ký tự\n')
        
        # Content (with headings shifted down to avoid hierarchy conflicts)
        shifted_content = shift_headings(section['content'], shift=2)
        lines.append(shifted_content)
        lines.append('')  # blank line after content
    
    # --- Footer ---
    lines.append('---\n')
    lines.append(f'*📌 Tổng hợp từ {len(sections)} tài liệu trong thư mục `03.1.DangKy_QLTK`.*')
    lines.append(f'*Chuyển đổi tự động bằng script `convert_word_to_md.py`.*')
    
    # Write output
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    full_content = '\n'.join(lines)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"\nMerged document created:")
    print(f"  Output: {output_file}")
    print(f"  Sections: {len(sections)}")
    print(f"  Total chars: {total_chars:,}")
    print(f"  File size: {len(full_content.encode('utf-8')):,} bytes")
    print(f"\nDone!")


if __name__ == '__main__':
    build_merged_document(INPUT_DIR, OUTPUT_FILE)
