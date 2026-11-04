import os

def extract_strings(filename, min_length=10):
    with open(filename, 'rb') as f:
        data = f.read()

    try:
        decoded = data.decode('utf-16le', errors='ignore')
        lines = decoded.splitlines()
        clean_lines = []
        for line in lines:
            line = line.strip()
            if len(line) > min_length:
                # Check if it has a good ratio of normal characters
                alnum_count = sum(1 for c in line if c.isalnum() or c.isspace())
                if alnum_count / len(line) > 0.7:
                    clean_lines.append(line)
        return '\n'.join(clean_lines)
    except Exception as e:
        return str(e)

test_file = r"F:\VIETLOTT-SMS\04_Document\VIETLOTT_SMS\VIETLOTT_SMS\03.Business_Analysis\03.1.DangKy_QLTK\VietlottSMS_ChucNangDangNhap-Web_v1.0_20251128.docx.doc"
out_file = r"F:\VIETLOTT-SMS\00_Draft\extracted_text.txt"

if os.path.exists(test_file):
    text = extract_strings(test_file)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Done writing to extracted_text.txt")
