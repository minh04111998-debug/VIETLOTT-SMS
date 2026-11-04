import os
import re

md_file = r"f:\VIETLOTT-SMS\00_Draft\Index_TaiLieu\03.1. Đăng ký & Quản lý tài khoản (DangKy_QLTK).md"
base_url = "file:///f:/VIETLOTT-SMS/04_Document/VIETLOTT_SMS/VIETLOTT_SMS/03.Business_Analysis/03.1.DangKy_QLTK/"

with open(md_file, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to find: - `filename.docx`
# Replacement: - [filename.docx](base_url/filename.docx)

def replace_link(match):
    filename = match.group(1)
    # properly encode spaces if any, though there shouldn't be
    encoded_filename = filename.replace(' ', '%20')
    return f"- [{filename}]({base_url}{encoded_filename})"

new_content = re.sub(r"- `([^`]+\.docx(?:\.doc)?)`", replace_link, content)

with open(md_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated links successfully!")
