import os
import re

master_file = r"f:\VIETLOTT-SMS\00_Draft\Phân Loại & Đánh Giá Cấu Trúc Tài Liệu Vietlott SMS.md"

with open(master_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <ul> and </ul> inside <details>
# And replace <li><a href="URL">TEXT</a></li> with - [TEXT](URL)

# First, we find the blocks
def fix_details_block(match):
    block = match.group(0)
    # Remove <ul> and </ul>
    block = re.sub(r'<ul>\s*', '\n\n', block)
    block = re.sub(r'\s*</ul>', '\n\n', block)
    # Replace <li><a href="X">Y</a></li> with - [Y](X)
    # Note: some lines might be just <li><code>...</code></li> if they weren't matched before, 
    # but the previous script already changed all matched ones to <a>.
    # We will handle both <a> and <code> just in case.
    
    def replace_li_a(m_li):
        url = m_li.group(1)
        text = m_li.group(2)
        return f"- [{text}]({url})"
        
    def replace_li_code(m_li):
        text = m_li.group(1)
        return f"- `{text}`"

    block = re.sub(r'<li><a href="([^"]+)">([^<]+)</a></li>', replace_li_a, block)
    block = re.sub(r'<li><code>([^<]+)</code></li>', replace_li_code, block)
    
    return block

# The regex matches from <summary> to </details>
new_content = re.sub(r'<summary>.*?</summary>\s*<ul>.*?</ul>\s*</details>', fix_details_block, content, flags=re.DOTALL)

with open(master_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed links inside details blocks to use Markdown format!")
