"""
Word → Markdown Batch Converter
================================
Converts Word documents (.docx and MHTML-based .doc) to structured Markdown.

Supports two file formats:
1. ZIP-based .docx → uses `mammoth` library for high-quality conversion
2. MHTML-based .doc → uses custom HTML parser for structured conversion

Output preserves: headings, tables, bold/italic, lists.
Images are skipped (text-only mode).

Usage:
    python convert_word_to_md.py [--input-dir DIR] [--output-dir DIR] [--dry-run]
"""

import mammoth
import os
import sys
import email
import re
import argparse
import time

sys.stdout.reconfigure(encoding='utf-8')


# ============================================================
# Configuration
# ============================================================
DEFAULT_INPUT_DIR = r"F:\VIETLOTT-SMS\04_Document\VIETLOTT_SMS\VIETLOTT_SMS\03.Business_Analysis\03.1.DangKy_QLTK"
DEFAULT_OUTPUT_DIR = r"F:\VIETLOTT-SMS\00_Draft\03_1_markdown"


# ============================================================
# Utility Functions
# ============================================================
def is_zip_docx(filepath):
    """Check if file is a ZIP-based .docx (vs MHTML-based .doc)"""
    with open(filepath, 'rb') as f:
        return f.read(4) == b'PK\x03\x04'


def clean_filename_for_md(filename):
    """Convert a Word filename to a clean .md filename"""
    name = filename
    # Remove multiple extensions like .docx.doc
    for ext in ['.docx.doc', '.docx', '.doc']:
        if name.lower().endswith(ext):
            name = name[:-len(ext)]
            break
    return name + ".md"


# ============================================================
# Mammoth-based Converter (for real .docx files)
# ============================================================
def convert_docx_with_mammoth(filepath):
    """Convert a real .docx (ZIP-based) file to Markdown using mammoth."""
    with open(filepath, 'rb') as f:
        result = mammoth.convert_to_markdown(f)
    
    md_content = result.value
    messages = result.messages
    
    # Post-processing for mammoth output
    md_content = postprocess_mammoth_md(md_content)
    
    return md_content, messages


def postprocess_mammoth_md(md):
    """Clean up mammoth's markdown output."""
    # 1. Remove inline base64 images (they are huge and useless as text)
    #    mammoth outputs: ![](data:image/png;base64,...)
    md = re.sub(r'!\[.*?\]\(data:image/[^)]+\)', '\n*(Hình ảnh - xem file Word gốc)*\n', md)
    
    # 2. Remove empty anchor tags: <a id="..."></a>
    md = re.sub(r'<a\s+id="[^"]*">\s*</a>', '', md)
    
    # 3. Remove unnecessary escaping that mammoth adds
    #    e.g., \. \- \( \) etc.
    md = re.sub(r'\\([.\-\(\)\[\]])', r'\1', md)
    
    # 4. Clean up excessive blank lines (more than 2 consecutive)
    md = re.sub(r'\n{4,}', '\n\n\n', md)
    
    # 5. Trim leading/trailing whitespace
    md = md.strip()
    
    return md


# ============================================================
# MHTML-based Converter (for .doc files saved as MHTML)
# ============================================================
def convert_mhtml_to_md(filepath):
    """Convert an MHTML-based .doc file to Markdown via HTML parsing."""
    with open(filepath, 'rb') as f:
        msg = email.message_from_binary_file(f)
    
    html_content = ""
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            payload = part.get_payload(decode=True)
            if payload:
                html_content = payload.decode('utf-8', errors='ignore')
                break
    
    if not html_content:
        return "ERROR: No text/html part found in MHTML file", []
    
    md = html_to_markdown(html_content)
    return md, []


def html_to_markdown(html):
    """Convert HTML to structured Markdown."""
    text = html
    
    # Remove style and script tags completely
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Remove comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    
    # Convert headings (h1-h6)
    for i in range(6, 0, -1):
        def heading_replacer(m, level=i):
            content = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            if content:
                return f"\n{'#' * level} {content}\n"
            return ''
        text = re.sub(
            rf'<h{i}[^>]*>(.*?)</h{i}>',
            heading_replacer,
            text, flags=re.IGNORECASE | re.DOTALL
        )
    
    # Convert bold
    text = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Convert italic
    text = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Convert tables
    text = re.sub(
        r'<table[^>]*>.*?</table>',
        convert_table_to_md,
        text, flags=re.IGNORECASE | re.DOTALL
    )
    
    # Convert list items
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'\n- \1', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'</?[ou]l[^>]*>', '', text, flags=re.IGNORECASE)
    
    # Convert line breaks and paragraphs
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<div[^>]*>(.*?)</div>', r'\n\1\n', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Remove image tags (text-only mode)
    text = re.sub(r'<img[^>]*>', '\n*(Hình ảnh - xem file Word gốc)*\n', text, flags=re.IGNORECASE)
    
    # Remove all remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Decode HTML entities
    text = decode_html_entities(text)
    
    # Clean up whitespace
    text = re.sub(r'[ \t]+\n', '\n', text)  # trailing spaces
    text = re.sub(r'\n{3,}', '\n\n', text)  # excessive blank lines
    text = re.sub(r'^\s+', '', text)  # leading whitespace
    text = re.sub(r'\s+$', '', text)  # trailing whitespace
    
    return text


def convert_table_to_md(match):
    """Convert an HTML table to Markdown table format."""
    table_html = match.group(0)
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.IGNORECASE | re.DOTALL)
    
    if not rows:
        return ""
    
    md_rows = []
    max_cols = 0
    
    for i, row in enumerate(rows):
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.IGNORECASE | re.DOTALL)
        
        clean_cells = []
        for cell in cells:
            # Remove HTML tags from cell content
            c = re.sub(r'<br\s*/?>', ' ', cell, flags=re.IGNORECASE)
            c = re.sub(r'<[^>]+>', '', c)
            c = decode_html_entities(c)
            c = re.sub(r'\s+', ' ', c).strip()
            # Escape pipe characters in cell content
            c = c.replace('|', '\\|')
            clean_cells.append(c)
        
        if clean_cells:
            max_cols = max(max_cols, len(clean_cells))
            md_rows.append(clean_cells)
    
    if not md_rows:
        return ""
    
    # Normalize column count
    for row in md_rows:
        while len(row) < max_cols:
            row.append("")
    
    # Build markdown table
    result_lines = []
    for i, row in enumerate(md_rows):
        result_lines.append("| " + " | ".join(row) + " |")
        if i == 0:
            result_lines.append("| " + " | ".join(["---"] * len(row)) + " |")
    
    return "\n" + "\n".join(result_lines) + "\n"


def decode_html_entities(text):
    """Decode common HTML entities."""
    entities = {
        '&nbsp;': ' ',
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&#39;': "'",
        '&laquo;': '«',
        '&raquo;': '»',
        '&ndash;': '–',
        '&mdash;': '—',
        '&bull;': '•',
        '&hellip;': '…',
        '&trade;': '™',
        '&copy;': '©',
        '&reg;': '®',
    }
    for entity, char in entities.items():
        text = text.replace(entity, char)
    
    # Handle numeric entities like &#123;
    text = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), text)
    # Handle hex entities like &#x1F4;
    text = re.sub(r'&#x([0-9a-fA-F]+);', lambda m: chr(int(m.group(1), 16)), text)
    
    return text


# ============================================================
# Main Batch Converter
# ============================================================
def convert_file(filepath, output_dir):
    """Convert a single Word file to Markdown."""
    filename = os.path.basename(filepath)
    
    # Skip temp files
    if filename.startswith('~'):
        return None, "SKIPPED (temp file)"
    
    is_zip = is_zip_docx(filepath)
    file_format = "ZIP/DOCX" if is_zip else "MHTML/DOC"
    
    try:
        if is_zip:
            md_content, messages = convert_docx_with_mammoth(filepath)
        else:
            md_content, messages = convert_mhtml_to_md(filepath)
        
        # Generate output filename
        out_name = clean_filename_for_md(filename)
        out_path = os.path.join(output_dir, out_name)
        
        # Write output
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        return {
            'input': filename,
            'output': out_name,
            'format': file_format,
            'input_size': os.path.getsize(filepath),
            'output_chars': len(md_content),
            'warnings': len(messages) if messages else 0,
        }, None
        
    except Exception as e:
        return None, f"ERROR ({file_format}): {str(e)}"


def batch_convert(input_dir, output_dir, dry_run=False):
    """Convert all Word files in input_dir to Markdown in output_dir."""
    
    print(f"{'=' * 70}")
    print(f"Word → Markdown Batch Converter")
    print(f"{'=' * 70}")
    print(f"Input:  {input_dir}")
    print(f"Output: {output_dir}")
    print(f"Mode:   {'DRY RUN' if dry_run else 'CONVERT'}")
    print(f"{'=' * 70}")
    
    if not os.path.exists(input_dir):
        print(f"ERROR: Input directory not found: {input_dir}")
        return
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Collect Word files
    word_files = []
    for filename in sorted(os.listdir(input_dir)):
        if filename.startswith('~'):
            continue
        if filename.lower().endswith(('.docx', '.doc')):
            word_files.append(os.path.join(input_dir, filename))
    
    print(f"\nFound {len(word_files)} Word files to convert.\n")
    
    if dry_run:
        for fp in word_files:
            fn = os.path.basename(fp)
            is_zip = is_zip_docx(fp)
            fmt = "ZIP/DOCX" if is_zip else "MHTML/DOC"
            size = os.path.getsize(fp)
            out_name = clean_filename_for_md(fn)
            print(f"  [{fmt:10s}] {size:>12,} bytes → {out_name}")
        print(f"\nDry run complete. Use without --dry-run to convert.")
        return
    
    # Convert files
    success_count = 0
    error_count = 0
    skip_count = 0
    total_input_bytes = 0
    total_output_chars = 0
    start_time = time.time()
    
    for i, filepath in enumerate(word_files, 1):
        filename = os.path.basename(filepath)
        print(f"[{i:3d}/{len(word_files)}] Converting: {filename}...", end=" ", flush=True)
        
        result, error = convert_file(filepath, output_dir)
        
        if error:
            if "SKIPPED" in error:
                skip_count += 1
                print(error)
            else:
                error_count += 1
                print(f"FAILED - {error}")
        else:
            success_count += 1
            total_input_bytes += result['input_size']
            total_output_chars += result['output_chars']
            warn_str = f" ({result['warnings']} warnings)" if result['warnings'] else ""
            print(f"OK → {result['output']} ({result['output_chars']:,} chars){warn_str}")
    
    elapsed = time.time() - start_time
    
    print(f"\n{'=' * 70}")
    print(f"CONVERSION COMPLETE")
    print(f"{'=' * 70}")
    print(f"  Success: {success_count}")
    print(f"  Failed:  {error_count}")
    print(f"  Skipped: {skip_count}")
    print(f"  Total input:  {total_input_bytes:>12,} bytes")
    print(f"  Total output: {total_output_chars:>12,} chars")
    print(f"  Time:    {elapsed:.1f}s")
    print(f"  Output:  {output_dir}")
    print(f"{'=' * 70}")


# ============================================================
# Entry Point
# ============================================================
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Word → Markdown Batch Converter')
    parser.add_argument('--input-dir', default=DEFAULT_INPUT_DIR, 
                        help='Input directory containing Word files')
    parser.add_argument('--output-dir', default=DEFAULT_OUTPUT_DIR,
                        help='Output directory for Markdown files')
    parser.add_argument('--dry-run', action='store_true',
                        help='List files without converting')
    
    args = parser.parse_args()
    batch_convert(args.input_dir, args.output_dir, args.dry_run)
