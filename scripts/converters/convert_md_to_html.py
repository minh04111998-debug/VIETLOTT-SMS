import os
import re

def markdown_to_html(md_text, title="Tài Liệu Đặc Tả Nghiệp Vụ - Vietlott SMS"):
    # Convert basic markdown elements to HTML
    lines = md_text.split('\n')
    html_lines = []
    in_table = False
    table_headers = []
    table_rows = []
    in_code_block = False
    code_block_lang = ""
    code_block_content = []
    in_alert = False
    alert_type = ""
    alert_content = []

    for line in lines:
        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                in_code_block = False
                content_str = "\n".join(code_block_content)
                if code_block_lang in ['mermaid', 'flowchart']:
                    html_lines.append(f'<div class="mermaid">\n{content_str}\n</div>')
                elif code_block_lang in ['plantuml', 'uml']:
                    html_lines.append(f'<pre class="plantuml"><code>{content_str}</code></pre>')
                else:
                    html_lines.append(f'<pre class="code-block {code_block_lang}"><code>{content_str}</code></pre>')
                code_block_content = []
                code_block_lang = ""
            else:
                in_code_block = True
                code_block_lang = line.strip().replace('```', '').strip()
            continue

        if in_code_block:
            code_block_content.append(line)
            continue

        # Alerts (GitHub style)
        if line.strip().startswith('> [!'):
            in_alert = True
            alert_type = line.strip()[4:].split(']')[0].lower()
            continue
        elif in_alert and line.strip().startswith('>'):
            alert_content.append(line.strip()[1:].strip())
            continue
        elif in_alert and not line.strip().startswith('>'):
            in_alert = False
            alert_text = "<br>".join(alert_content)
            html_lines.append(f'<div class="alert alert-{alert_type}"><div class="alert-title">{alert_type.upper()}</div><div class="alert-body">{alert_text}</div></div>')
            alert_content = []

        # Tables
        if line.strip().startswith('|') and '|' in line[1:]:
            if '---' in line:
                continue
            cols = [c.strip() for c in line.strip().split('|')[1:-1]]
            if not in_table:
                in_table = True
                table_headers = cols
            else:
                table_rows.append(cols)
            continue
        else:
            if in_table:
                in_table = False
                # Build HTML table
                t_html = ['<div class="table-container"><table><thead><tr>']
                for th in table_headers:
                    t_html.append(f'<th>{th}</th>')
                t_html.append('</tr></thead><tbody>')
                for row in table_rows:
                    t_html.append('<tr>')
                    for cell in row:
                        t_html.append(f'<td>{cell}</td>')
                    t_html.append('</tr>')
                t_html.append('</tbody></table></div>')
                html_lines.append("".join(t_html))
                table_headers = []
                table_rows = []

        # Headings
        if line.startswith('# '):
            html_lines.append(f'<h1 id="{slugify(line[2:])}">{line[2:]}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2 id="{slugify(line[3:])}">{line[3:]}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3 id="{slugify(line[4:])}">{line[4:]}</h3>')
        elif line.startswith('#### '):
            html_lines.append(f'<h4 id="{slugify(line[5:])}">{line[5:]}</h4>')
        # Horizontal rule
        elif line.strip() == '---':
            html_lines.append('<hr>')
        # Unordered lists
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            html_lines.append(f'<li>{parse_inline(line.strip()[2:])}</li>')
        # Paragraphs
        elif line.strip():
            html_lines.append(f'<p>{parse_inline(line)}</p>')

    if in_table:
        t_html = ['<div class="table-container"><table><thead><tr>']
        for th in table_headers:
            t_html.append(f'<th>{th}</th>')
        t_html.append('</tr></thead><tbody>')
        for row in table_rows:
            t_html.append('<tr>')
            for cell in row:
                t_html.append(f'<td>{cell}</td>')
            t_html.append('</tr>')
        t_html.append('</tbody></table></div>')
        html_lines.append("".join(t_html))

    body_html = "\n".join(html_lines)

    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <style>
        :root {{
            --primary-red: #e31b23;
            --primary-dark: #0f172a;
            --secondary-dark: #1e293b;
            --accent-gold: #f59e0b;
            --accent-blue: #2563eb;
            --text-main: #334155;
            --text-muted: #64748b;
            --bg-body: #f8fafc;
            --bg-card: #ffffff;
            --border-color: #e2e8f0;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.6;
            padding: 2rem 1rem;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: var(--bg-card);
            border-radius: 16px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
            padding: 3rem 4rem;
            border: 1px solid var(--border-color);
        }}

        .header-banner {{
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: white;
            padding: 2.5rem;
            border-radius: 12px;
            margin-bottom: 2.5rem;
            position: relative;
            overflow: hidden;
            border-left: 6px solid var(--primary-red);
        }}

        .header-banner h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.2rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.5rem;
        }}

        .header-banner p {{
            color: #94a3b8;
            font-size: 1rem;
        }}

        h1, h2, h3, h4 {{
            font-family: 'Outfit', sans-serif;
            color: var(--primary-dark);
            font-weight: 600;
        }}

        h1 {{
            font-size: 2rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--primary-red);
        }}

        h2 {{
            font-size: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: #1e293b;
        }}

        h3 {{
            font-size: 1.2rem;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
            color: #334155;
        }}

        p {{
            margin-bottom: 1rem;
        }}

        ul, ol {{
            margin-bottom: 1.25rem;
            padding-left: 1.5rem;
        }}

        li {{
            margin-bottom: 0.4rem;
        }}

        hr {{
            border: none;
            border-top: 1px solid var(--border-color);
            margin: 2rem 0;
        }}

        /* Tables */
        .table-container {{
            overflow-x: auto;
            margin: 1.5rem 0;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
            text-align: left;
        }}

        th {{
            background-color: #f1f5f9;
            color: #1e293b;
            font-weight: 600;
            padding: 0.9rem 1rem;
            border-bottom: 2px solid var(--border-color);
        }}

        td {{
            padding: 0.85rem 1rem;
            border-bottom: 1px solid var(--border-color);
            vertical-align: top;
        }}

        tr:nth-child(even) td {{
            background-color: #f8fafc;
        }}

        tr:hover td {{
            background-color: #f1f5f9;
        }}

        /* Alert Boxes */
        .alert {{
            padding: 1.25rem 1.5rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            border-left: 4px solid;
        }}

        .alert-warning {{
            background-color: #fffbeb;
            border-color: #f59e0b;
            color: #92400e;
        }}

        .alert-important {{
            background-color: #eff6ff;
            border-color: #2563eb;
            color: #1e40af;
        }}

        .alert-note {{
            background-color: #f8fafc;
            border-color: #64748b;
            color: #334155;
        }}

        .alert-tip {{
            background-color: #f0fdf4;
            border-color: #16a34a;
            color: #166534;
        }}

        .alert-title {{
            font-weight: 700;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.4rem;
        }}

        /* Code & Diagrams */
        pre.code-block, pre.plantuml {{
            background-color: #0f172a;
            color: #f8fafc;
            padding: 1.25rem;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 0.9rem;
            margin: 1.5rem 0;
        }}

        .mermaid {{
            background: #ffffff;
            padding: 1.5rem;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            margin: 1.5rem 0;
            text-align: center;
        }}

        .badge {{
            display: inline-block;
            padding: 0.2rem 0.6rem;
            font-size: 0.75rem;
            font-weight: 600;
            border-radius: 12px;
            text-transform: uppercase;
        }}

        .badge-draft {{
            background-color: #fef3c7;
            color: #92400e;
        }}

        .badge-high {{
            background-color: #fee2e2;
            color: #991b1b;
        }}

        .badge-medium {{
            background-color: #fef3c7;
            color: #92400e;
        }}

        .badge-low {{
            background-color: #dcfce7;
            color: #166534;
        }}

        @media print {{
            body {{
                padding: 0;
                background: white;
            }}
            .container {{
                box-shadow: none;
                border: none;
                padding: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header-banner">
            <h1>Vietlott SMS — System Specification Document</h1>
            <p>Hệ thống Cấu hình & Tự động Phát tặng vé mở tài khoản từ Kênh Bank</p>
        </div>
        {body_html}
    </div>
    <script>
        mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
    </script>
</body>
</html>
"""
    return full_html

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[\s_-]+', '-', text)

def parse_inline(text):
    # Convert bold, italic, code, links
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', text)
    return text

def convert_files():
    base_dir = r"f:\VIETLOTT-SMS\00_Draft"
    files = [
        ("srs-campaign-tang-ve-bank.md", "srs-campaign-tang-ve-bank.html", "Đặc Tả Yêu Cầu Nghiệp Vụ SRS - Vietlott SMS"),
        ("gap-analysis-campaign-tang-ve-bank.md", "gap-analysis-campaign-tang-ve-bank.html", "Báo Cáo Gap Analysis - Vietlott SMS")
    ]
    for md_file, html_file, title in files:
        md_path = os.path.join(base_dir, md_file)
        html_path = os.path.join(base_dir, html_file)
        if os.path.exists(md_path):
            with open(md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            html_content = markdown_to_html(md_content, title)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"Converted {md_file} -> {html_file}")

if __name__ == "__main__":
    convert_files()
