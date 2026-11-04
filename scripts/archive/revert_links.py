import os
import re

master_file = r"f:\VIETLOTT-SMS\00_Draft\Phân Loại & Đánh Giá Cấu Trúc Tài Liệu Vietlott SMS.md"

with open(master_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Match: optional spaces, followed by "- [Filename](file:///...)"
# Replace with: "- `Filename`"
# The regex: ^\s*- \[([^\]]+)\]\(file:\/\/\/[^\)]+\)
def clean_links(match):
    filename = match.group(1)
    return f"- `{filename}`"

new_content = re.sub(r'^[ \t]*- \[([^\]]+)\]\(file:\/\/[^\)]+\)', clean_links, content, flags=re.MULTILINE)

# Also fix any remaining <li><a href="...">filename</a></li> or <li><code>filename</code></li> just in case
def clean_html_li(match):
    filename = match.group(1)
    return f"- `{filename}`"

new_content = re.sub(r'^[ \t]*<li><a[^>]*>([^<]+)</a></li>', clean_html_li, new_content, flags=re.MULTILINE)
new_content = re.sub(r'^[ \t]*<li><code>([^<]+)</code></li>', clean_html_li, new_content, flags=re.MULTILINE)

# Ensure <details> and <summary> and <ul> have proper spacing if needed
# Actually, the user's preferred clean look inside details block is just:
# <details>
# <summary>...</summary>
# 
# - `filename`
# </details>

# Let's remove <ul> and </ul> if they still exist
new_content = re.sub(r'<ul>\n?', '', new_content)
new_content = re.sub(r'</ul>\n?', '', new_content)

with open(master_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Restored clean markdown!")
