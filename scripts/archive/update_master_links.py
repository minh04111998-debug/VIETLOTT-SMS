import os
import re

# 1. Build dictionary of filename -> absolute path
docs_dir = r"F:\VIETLOTT-SMS\04_Document"
file_map = {}
for root, dirs, files in os.walk(docs_dir):
    for f in files:
        # Include typical documentation extensions
        if f.endswith(('.doc', '.docx', '.pdf', '.xlsx', '.xls', '.vsdx')):
            # Store absolute path with forward slashes
            abs_path = os.path.join(root, f).replace('\\', '/')
            # URL encode spaces to ensure clickable links work reliably
            abs_path = abs_path.replace(' ', '%20')
            file_map[f] = abs_path

# 2. Read the master file
master_file = r"f:\VIETLOTT-SMS\00_Draft\Phân Loại & Đánh Giá Cấu Trúc Tài Liệu Vietlott SMS.md"
with open(master_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 3. Replace <li><code>filename</code></li>
def replacer(match):
    filename = match.group(1)
    if filename in file_map:
        return f'<li><a href="file:///{file_map[filename]}">{filename}</a></li>'
    else:
        # If the file isn't found in 04_Document, keep it as is
        return match.group(0)

new_content = re.sub(r'<li><code>(.*?)</code></li>', replacer, content)

# 4. Save the file
with open(master_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated master file with absolute links successfully!")
