import re
import os

filepath = r"f:\VIETLOTT-SMS\00_Draft\Phân Loại & Đánh Giá Cấu Trúc Tài Liệu Vietlott SMS.md"
out_dir = r"f:\VIETLOTT-SMS\00_Draft\Index_TaiLieu"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the <details> tags and replace them with a link.
# But we also need the title which is just above the <details> block.

# Pattern to find: 
# 1. Title line: - **Title:** description
# 2. <details> block
pattern = r"(?:-\s*\*\*(.*?)\*\*(?:.*?)\n+)(?:<details>(?:.*?)<\/details>)"

# Actually, it's better to iterate over the document line by line to maintain state.
lines = content.split('\n')
new_lines = []

i = 0
while i < len(lines):
    line = lines[i]
    if line.strip().startswith('- **') and (':**' in line or ')**' in line):
        # We found a potential title. Let's look ahead to see if there's a <details> block soon.
        j = i + 1
        found_details = False
        while j < i + 5 and j < len(lines):
            if '<details>' in lines[j]:
                found_details = True
                break
            j += 1
        
        if found_details:
            # Extract title
            title_match = re.search(r'-\s*\*\*(.*?)\*\*', line)
            title = title_match.group(1).strip().strip(':')
            
            # Clean title for filename
            filename = title.replace('/', '_').replace('\\', '_').replace(':', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
            filename += '.md'
            out_path = os.path.join(out_dir, filename)
            
            # Extract the details block
            details_start = j
            details_end = j
            while details_end < len(lines):
                if '</details>' in lines[details_end]:
                    break
                details_end += 1
            
            details_content = '\n'.join(lines[details_start:details_end+1])
            
            # Create the standalone markdown file
            with open(out_path, 'w', encoding='utf-8') as out_f:
                out_f.write(f"# {title}\n\n")
                out_f.write(f"*(Trích xuất từ [Phân Loại & Đánh Giá Cấu Trúc Tài Liệu Vietlott SMS.md](../Phân%20Loại%20&%20Đánh%20Giá%20Cấu%20Trúc%20Tài%20Liệu%20Vietlott%20SMS.md))*\n\n")
                # Remove the outer <details> and <summary> to just show the content
                # The content is usually a <ul> list. Let's just strip <details>, </details> and <summary>...</summary>
                clean_details = re.sub(r'<details>', '', details_content)
                clean_details = re.sub(r'</details>', '', clean_details)
                clean_details = re.sub(r'<summary>.*?</summary>', '', clean_details, flags=re.DOTALL)
                out_f.write(clean_details.strip() + "\n")
            
            # Append the original title line
            new_lines.append(line)
            # Add a link instead of the details block
            rel_link = f"./Index_TaiLieu/{filename.replace(' ', '%20')}"
            new_lines.append(f"  👉 **[Xem danh sách chi tiết tài liệu tại đây]({rel_link})**")
            new_lines.append("") # blank line for spacing
            
            i = details_end + 1
            continue

    new_lines.append(line)
    i += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Extraction completed successfully!")
