import os
import re

root_dir = r"f:\VIETLOTT-SMS\04_Document\VIETLOTT_SMS\VIETLOTT_SMS"
input_file = r"f:\VIETLOTT-SMS\00_Draft\document-classification.md"
output_file = r"f:\VIETLOTT-SMS\00_Draft\document-classification.md"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

def get_files_html(subpath):
    full_path = os.path.join(root_dir, subpath)
    if not os.path.exists(full_path):
        return ""
    
    html = "\n<details>\n<summary>📁 <b>Xem danh sách tài liệu chi tiết</b></summary>\n<ul>\n"
    has_files = False
    for root, dirs, files in os.walk(full_path):
        for file in files:
            rel = os.path.relpath(os.path.join(root, file), full_path)
            html += f"  <li><code>{rel}</code></li>\n"
            has_files = True
    html += "</ul>\n</details>\n"
    
    if has_files:
        return html
    return ""

mapping = {
    "**Phiếu Yêu Cầu (PYC):**": r"02.Requirements\02.1.Phieu_Yeu_Cau",
    "**03.1. Đăng ký & Quản lý tài khoản (DangKy_QLTK):**": r"03.Business_Analysis\03.1.DangKy_QLTK",
    "**03.2. Nạp/Rút tiền & Hạn mức (NapTien_RutTien_HanMuc):**": r"03.Business_Analysis\03.2.NapTien_RutTien_HanMuc",
    "**03.3. Sản Phẩm (San_Pham):**": r"03.Business_Analysis\03.3.San_Pham",
    "**03.4. Mua Vé (Mua_Ve):**": r"03.Business_Analysis\03.4.Mua_Ve",
    "**03.5. Trả Thưởng (Tra_Thuong):**": r"03.Business_Analysis\03.5.Tra_Thuong",
    "**03.6. Đối Soát (Doi_Soat):**": r"03.Business_Analysis\03.6.Doi_Soat",
    "**03.7. Báo Cáo (Bao_Cao):**": r"03.Business_Analysis\03.7.Bao_Cao",
    "**03.8. Dịch Vụ GTGT (Dich_Vu_GTGT):**": r"03.Business_Analysis\03.8.Dich_Vu_GTGT",
    "**03.9. Tích Hợp Đối Tác (Tich_Hop_Doi_Tac):**": r"03.Business_Analysis\03.9.Tich_Hop_Doi_Tac",
    "**03.10. Cấu Hình Hệ Thống (Cau_Hinh_He_Thong):**": r"03.Business_Analysis\03.10.Cau_Hinh_He_Thong",
    "**03.11. SMS & Notification (SMS_Noti_TruyenThong):**": r"03.Business_Analysis\03.11.SMS_Noti_TruyenThong",
    "**03.12. Affiliate & Gift (Affiliate_Gift):**": r"03.Business_Analysis\03.12.Affiliate_Gift",
}

lines = content.split('\n')
new_lines = []

for line in lines:
    new_lines.append(line)
    for key, path in mapping.items():
        if key in line:
            html = get_files_html(path)
            if html:
                new_lines.append(html)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Done")
