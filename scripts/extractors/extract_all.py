import os
import email
import zipfile
import xml.etree.ElementTree as ET
import re

input_dir = r"F:\VIETLOTT-SMS\04_Document\VIETLOTT_SMS\VIETLOTT_SMS\03.Business_Analysis\03.1.DangKy_QLTK"
output_dir = r"F:\VIETLOTT-SMS\00_Draft\03_1_extracted"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def extract_from_docx_zip(filepath):
    try:
        with zipfile.ZipFile(filepath) as docx:
            xml_content = docx.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        paragraphs = []
        for paragraph in tree.iterfind('.//w:p', namespaces):
            texts = [node.text for node in paragraph.iterfind('.//w:t', namespaces) if node.text]
            if texts:
                paragraphs.append(''.join(texts))
        return '\n'.join(paragraphs)
    except Exception as e:
        return f"ZIP_ERROR: {str(e)}"

def extract_from_mhtml(filepath):
    try:
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
            return "MHTML_ERROR: No text/html part found"
            
        # Strip HTML tags
        text = re.sub(r'<style.*?>.*?</style>', '', html_content, flags=re.IGNORECASE|re.DOTALL)
        text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.IGNORECASE|re.DOTALL)
        text = re.sub(r'<[^>]+>', '\n', text)
        
        # Clean up excessive newlines
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return '\n'.join(lines)
    except Exception as e:
        return f"MHTML_ERROR: {str(e)}"

count_zip = 0
count_mhtml = 0
count_err = 0

for filename in os.listdir(input_dir):
    if not filename.startswith('~') and (filename.endswith('.docx') or filename.endswith('.doc')):
        filepath = os.path.join(input_dir, filename)
        
        # Check signature
        with open(filepath, 'rb') as f:
            header = f.read(4)
            
        text = ""
        if header == b'PK\x03\x04':
            text = extract_from_docx_zip(filepath)
            count_zip += 1
        else:
            text = extract_from_mhtml(filepath)
            count_mhtml += 1
            
        if "ERROR:" in text[:20]:
            print(f"Failed extracting {filename}: {text[:50]}")
            count_err += 1
            
        out_name = filename + ".txt"
        out_path = os.path.join(output_dir, out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(text)

print(f"\nExtraction complete: {count_zip} ZIP files, {count_mhtml} MHTML files processed. {count_err} errors.")
