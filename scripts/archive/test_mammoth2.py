import mammoth
import os
import zipfile
import email
import re

output_dir = r"f:\VIETLOTT-SMS\00_Draft\test_output"
os.makedirs(output_dir, exist_ok=True)

def is_zip_docx(filepath):
    with open(filepath, 'rb') as f:
        return f.read(4) == b'PK\x03\x04'

def convert_docx_mammoth(filepath):
    """Convert real .docx (ZIP-based) to markdown using mammoth"""
    with open(filepath, 'rb') as f:
        result = mammoth.convert_to_markdown(f)
    return result.value, result.messages

def convert_mhtml_to_md(filepath):
    """Convert MHTML-based .doc file to markdown via HTML parsing"""
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
        return "ERROR: No text/html part found in MHTML", []
    
    # Convert HTML to structured markdown
    md = html_to_markdown(html_content)
    return md, []

def html_to_markdown(html):
    """Basic HTML to Markdown converter preserving structure"""
    # Remove style and script tags
    text = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.IGNORECASE|re.DOTALL)
    text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.IGNORECASE|re.DOTALL)
    
    # Convert headings
    for i in range(6, 0, -1):
        text = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', lambda m: f"\n{'#' * i} {m.group(1).strip()}\n", text, flags=re.IGNORECASE|re.DOTALL)
    
    # Convert bold
    text = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', text, flags=re.IGNORECASE|re.DOTALL)
    text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', text, flags=re.IGNORECASE|re.DOTALL)
    
    # Convert italic
    text = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', text, flags=re.IGNORECASE|re.DOTALL)
    text = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', text, flags=re.IGNORECASE|re.DOTALL)
    
    # Convert table rows/cells
    # Simple approach: convert <tr> to lines, <td>/<th> to | separated
    def convert_table(match):
        table_html = match.group(0)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.IGNORECASE|re.DOTALL)
        if not rows:
            return ""
        
        md_rows = []
        for i, row in enumerate(rows):
            cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.IGNORECASE|re.DOTALL)
            # Clean HTML from cells
            clean_cells = []
            for cell in cells:
                c = re.sub(r'<[^>]+>', ' ', cell)
                c = re.sub(r'\s+', ' ', c).strip()
                clean_cells.append(c)
            
            if clean_cells:
                md_rows.append("| " + " | ".join(clean_cells) + " |")
                if i == 0:
                    md_rows.append("| " + " | ".join(["---"] * len(clean_cells)) + " |")
        
        return "\n" + "\n".join(md_rows) + "\n"
    
    text = re.sub(r'<table[^>]*>.*?</table>', convert_table, text, flags=re.IGNORECASE|re.DOTALL)
    
    # Convert list items
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'\n- \1', text, flags=re.IGNORECASE|re.DOTALL)
    
    # Convert line breaks and paragraphs
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', text, flags=re.IGNORECASE|re.DOTALL)
    text = re.sub(r'<div[^>]*>(.*?)</div>', r'\n\1\n', text, flags=re.IGNORECASE|re.DOTALL)
    
    # Remove remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Decode HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&amp;', '&')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&quot;', '"')
    text = text.replace('&#39;', "'")
    
    # Clean up excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()


# ===== TEST with files from 03.1 =====
src_dir = r"F:\VIETLOTT-SMS\04_Document\VIETLOTT_SMS\VIETLOTT_SMS\03.Business_Analysis\03.1.DangKy_QLTK"

# Pick 3 test files: 1 real docx, 2 MHTML-based
test_files = [
    "VietlottSMS_BRD_DieuChinhLuongDangNhap_20241112.docx",  # real docx
    "VietlottSMS_ChucNangDangNhap-Web_v1.0_20251128.docx.doc",  # MHTML small
    "VietlottSMS_DangNhap-App_v1.1_20251120.docx.doc",  # MHTML large
]

for fname in test_files:
    fpath = os.path.join(src_dir, fname)
    if not os.path.exists(fpath):
        print(f"SKIP: {fname} not found")
        continue
    
    is_zip = is_zip_docx(fpath)
    print(f"\n{'='*60}")
    print(f"File: {fname}")
    print(f"Size: {os.path.getsize(fpath)} bytes")
    print(f"Format: {'ZIP/DOCX' if is_zip else 'MHTML/DOC'}")
    
    try:
        if is_zip:
            md_content, messages = convert_docx_mammoth(fpath)
        else:
            md_content, messages = convert_mhtml_to_md(fpath)
        
        # Save output
        out_name = os.path.splitext(fname)[0]
        if out_name.endswith('.docx'):
            out_name = out_name[:-5]
        out_path = os.path.join(output_dir, out_name + ".md")
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"Output: {out_name}.md ({len(md_content)} chars)")
        if messages:
            print(f"Warnings: {len(messages)}")
        print("SUCCESS")
    except Exception as e:
        print(f"ERROR: {e}")

print(f"\n\nDone! Check output in: {output_dir}")
