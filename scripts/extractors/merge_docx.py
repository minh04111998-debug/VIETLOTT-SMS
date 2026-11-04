import os
import docx

folder_path = r"F:\VIETLOTT-SMS\04_Document\VIETLOTT_SMS\VIETLOTT_SMS\03.Business_Analysis\03.1.DangKy_QLTK"
output_md = r"f:\VIETLOTT-SMS\00_Draft\Index_TaiLieu\03.1. Đăng ký & Quản lý tài khoản (DangKy_QLTK).md"

def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            text = para.text.strip()
            if text:
                full_text.append(text)
        return '\n\n'.join(full_text)
    except Exception as e:
        return f"Error reading {file_path}: {e}"

if not os.path.exists(folder_path):
    with open(output_md, 'a', encoding='utf-8') as f:
        f.write("\n\n---\n\n## Lỗi: Không tìm thấy thư mục chứa tài liệu chi tiết.\n")
else:
    files = [f for f in os.listdir(folder_path) if f.endswith('.docx') and not f.startswith('~')]
    
    with open(output_md, 'a', encoding='utf-8') as f:
        f.write("\n\n---\n\n# TỔNG HỢP NỘI DUNG TÀI LIỆU CHI TIẾT\n\n")
        f.write("> **Cảnh báo:** Phần bên dưới là toàn bộ text được bóc tách tự động từ các file Word. Các hình ảnh, bảng biểu và format phức tạp có thể không hiển thị được.\n\n")
        
        for file in files:
            file_path = os.path.join(folder_path, file)
            f.write(f"## 📄 File: `{file}`\n\n")
            text_content = extract_text_from_docx(file_path)
            f.write(text_content)
            f.write("\n\n---\n\n")

print("Extraction and merge complete!")
