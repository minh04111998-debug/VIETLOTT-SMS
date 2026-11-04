import os
import re
import zlib
import base64

def plantuml_to_kroki_url(plantuml_code):
    """Encodes PlantUML text into Kroki SVG image URL."""
    compressed = zlib.compress(plantuml_code.encode('utf-8'))
    encoded = base64.urlsafe_b64encode(compressed).decode('utf-8')
    return f"https://kroki.io/plantuml/svg/{encoded}"

def md_to_html(md_text, doc_title):
    lines = md_text.split('\n')
    html_out = []
    
    in_plantuml = False
    plantuml_buf = []
    
    in_mermaid = False
    mermaid_buf = []
    
    in_table = False
    table_headers = []
    table_rows = []
    
    in_alert = False
    alert_type = ""
    alert_buf = []

    for line in lines:
        raw_line = line
        strip_line = line.strip()

        # PlantUML block start/end
        if strip_line.startswith('```plantuml'):
            in_plantuml = True
            plantuml_buf = []
            continue
        elif in_plantuml and strip_line.startswith('```'):
            in_plantuml = False
            puml_code = "\n".join(plantuml_buf)
            img_url = plantuml_to_kroki_url(puml_code)
            html_out.append(f'''
<div class="diagram-wrapper">
    <div class="diagram-title">🖼️ Sơ đồ Luồng Hoạt động (PlantUML Visual Diagram)</div>
    <img class="diagram-img" src="{img_url}" alt="PlantUML Swimlane Activity Diagram" />
    <p class="diagram-caption">Sơ đồ Swimlane phân chia luồng Khách hàng, Web Admin và Realtime Rule Engine & Core Service</p>
</div>
''')
            plantuml_buf = []
            continue

        if in_plantuml:
            plantuml_buf.append(raw_line)
            continue

        # Mermaid block start/end
        if strip_line.startswith('```mermaid'):
            in_mermaid = True
            mermaid_buf = []
            continue
        elif in_mermaid and strip_line.startswith('```'):
            in_mermaid = False
            m_code = "\n".join(mermaid_buf)
            html_out.append(f'''
<div class="diagram-wrapper">
    <div class="diagram-title">📊 Sơ đồ Luồng (Mermaid Visual Diagram)</div>
    <div class="mermaid">
{m_code}
    </div>
</div>
''')
            mermaid_buf = []
            continue

        if in_mermaid:
            mermaid_buf.append(raw_line)
            continue

        # GitHub Alerts (> [!WARNING], > [!IMPORTANT], etc.)
        if strip_line.startswith('> [!'):
            in_alert = True
            alert_type = strip_line[4:].split(']')[0].lower()
            alert_buf = []
            continue
        elif in_alert and strip_line.startswith('>'):
            alert_buf.append(strip_line[1:].strip())
            continue
        elif in_alert and not strip_line.startswith('>'):
            in_alert = False
            alert_text = "<br>".join(alert_buf)
            html_out.append(f'''
<div class="alert alert-{alert_type}">
    <div class="alert-title">📌 {alert_type.upper()}</div>
    <div class="alert-body">{alert_text}</div>
</div>
''')
            alert_buf = []

        # Tables
        if strip_line.startswith('|') and '|' in strip_line[1:]:
            if '---' in strip_line:
                continue
            cols = [c.strip() for c in strip_line.split('|')[1:-1]]
            if not in_table:
                in_table = True
                table_headers = cols
                table_rows = []
            else:
                table_rows.append(cols)
            continue
        else:
            if in_table:
                in_table = False
                t_html = ['<div class="table-container"><table><thead><tr>']
                for th in table_headers:
                    t_html.append(f'<th>{th}</th>')
                t_html.append('</tr></thead><tbody>')
                for row in table_rows:
                    t_html.append('<tr>')
                    for cell in row:
                        t_html.append(f'<td>{inline_parse(cell)}</td>')
                    t_html.append('</tr>')
                t_html.append('</tbody></table></div>')
                html_out.append("".join(t_html))

        # Headings
        if strip_line.startswith('# '):
            html_out.append(f'<h1 id="{slug(strip_line[2:])}">{inline_parse(strip_line[2:])}</h1>')
        elif strip_line.startswith('## '):
            html_out.append(f'<h2 id="{slug(strip_line[3:])}">{inline_parse(strip_line[3:])}</h2>')
        elif strip_line.startswith('### '):
            html_out.append(f'<h3 id="{slug(strip_line[4:])}">{inline_parse(strip_line[4:])}</h3>')
        elif strip_line.startswith('#### '):
            html_out.append(f'<h4 id="{slug(strip_line[5:])}">{inline_parse(strip_line[5:])}</h4>')
        elif strip_line == '---':
            html_out.append('<hr>')
        elif strip_line.startswith('- ') or strip_line.startswith('* '):
            html_out.append(f'<ul><li>{inline_parse(strip_line[2:])}</li></ul>')
        elif strip_line:
            html_out.append(f'<p>{inline_parse(strip_line)}</p>')

    if in_table:
        t_html = ['<div class="table-container"><table><thead><tr>']
        for th in table_headers:
            t_html.append(f'<th>{th}</th>')
        t_html.append('</tr></thead><tbody>')
        for row in table_rows:
            t_html.append('<tr>')
            for cell in row:
                t_html.append(f'<td>{inline_parse(cell)}</td>')
            t_html.append('</tr>')
        t_html.append('</tbody></table></div>')
        html_out.append("".join(t_html))

    if in_alert:
        alert_text = "<br>".join(alert_buf)
        html_out.append(f'''
<div class="alert alert-{alert_type}">
    <div class="alert-title">📌 {alert_type.upper()}</div>
    <div class="alert-body">{alert_text}</div>
</div>
''')

    body_content = "\n".join(html_out)

    full_template = f'''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{doc_title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <style>
        :root {{
            --primary-red: #e31b23;
            --primary-dark: #0f172a;
            --secondary-dark: #1e293b;
            --accent-gold: #d97706;
            --accent-blue: #2563eb;
            --text-main: #334155;
            --text-muted: #64748b;
            --bg-body: #f1f5f9;
            --bg-card: #ffffff;
            --border-color: #cbd5e1;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background-color: var(--bg-body); color: var(--text-main); line-height: 1.6; padding: 2.5rem 1rem; }}
        .container {{ max-width: 1320px; margin: 0 auto; background: var(--bg-card); border-radius: 16px; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08); padding: 3.5rem 4.5rem; border: 1px solid var(--border-color); }}
        
        .header-banner {{ background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: white; padding: 2.5rem; border-radius: 12px; margin-bottom: 2.5rem; border-left: 8px solid var(--primary-red); }}
        .header-banner h1 {{ font-family: 'Outfit', sans-serif; font-size: 2.2rem; font-weight: 700; color: #ffffff; margin-bottom: 0.5rem; border-bottom: none; }}
        .header-banner p {{ color: #94a3b8; font-size: 1.05rem; }}
        
        h1, h2, h3, h4 {{ font-family: 'Outfit', sans-serif; color: var(--primary-dark); font-weight: 600; }}
        h1 {{ font-size: 2rem; margin-top: 2.5rem; margin-bottom: 1.25rem; padding-bottom: 0.5rem; border-bottom: 3px solid var(--primary-red); }}
        h2 {{ font-size: 1.5rem; margin-top: 2.25rem; margin-bottom: 1rem; color: #1e293b; border-left: 5px solid var(--accent-blue); padding-left: 0.85rem; }}
        h3 {{ font-size: 1.25rem; margin-top: 1.75rem; margin-bottom: 0.75rem; color: #334155; }}
        h4 {{ font-size: 1.05rem; margin-top: 1.25rem; margin-bottom: 0.5rem; color: #475569; }}

        p {{ margin-bottom: 1.1rem; font-size: 1rem; color: #334155; }}
        ul, ol {{ margin-bottom: 1.25rem; padding-left: 1.75rem; }}
        li {{ margin-bottom: 0.5rem; }}
        hr {{ border: none; border-top: 1px solid var(--border-color); margin: 2.5rem 0; }}

        /* Tables */
        .table-container {{ overflow-x: auto; margin: 1.5rem 0; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); }}
        table {{ width: 100%; border-collapse: collapse; font-size: 0.92rem; text-align: left; }}
        th {{ background-color: #f8fafc; color: #0f172a; font-weight: 700; padding: 1rem; border-bottom: 2px solid var(--border-color); font-size: 0.85rem; letter-spacing: 0.03em; }}
        td {{ padding: 0.9rem 1rem; border-bottom: 1px solid #e2e8f0; vertical-align: top; line-height: 1.5; }}
        tr:nth-child(even) td {{ background-color: #f8fafc; }}
        tr:hover td {{ background-color: #f1f5f9; }}

        /* Alerts */
        .alert {{ padding: 1.25rem 1.5rem; border-radius: 10px; margin: 1.75rem 0; border-left: 6px solid; font-size: 0.95rem; }}
        .alert-warning {{ background-color: #fffbeb; border-color: #f59e0b; color: #92400e; }}
        .alert-important {{ background-color: #eff6ff; border-color: #2563eb; color: #1e40af; }}
        .alert-note {{ background-color: #f8fafc; border-color: #64748b; color: #334155; }}
        .alert-tip {{ background-color: #f0fdf4; border-color: #16a34a; color: #166534; }}
        .alert-title {{ font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem; }}

        /* Diagrams as VISUAL IMAGES */
        .diagram-wrapper {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 2rem;
            margin: 2rem 0;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        }}

        .diagram-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 1.1rem;
            color: #0f172a;
            margin-bottom: 1.25rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}

        .diagram-img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            display: block;
            margin: 0 auto;
        }}

        .diagram-caption {{
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-top: 1rem;
            font-style: italic;
        }}

        code {{ background-color: #f1f5f9; color: #e31b23; padding: 0.2rem 0.4rem; border-radius: 4px; font-family: 'Consolas', monospace; font-size: 0.88rem; }}
        pre {{ background-color: #0f172a; color: #f8fafc; padding: 1.25rem; border-radius: 8px; overflow-x: auto; font-family: 'Consolas', monospace; font-size: 0.9rem; margin: 1.5rem 0; }}

        @media print {{
            body {{ padding: 0; background: white; }}
            .container {{ box-shadow: none; border: none; padding: 0; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header-banner">
            <h1>Vietlott SMS — System Specification Document</h1>
            <p>{doc_title}</p>
        </div>
        {body_content}
    </div>
    <script>
        mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
    </script>
</body>
</html>
'''
    return full_template

def inline_parse(t):
    t = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\*(.*?)\*', r'<em>\1</em>', t)
    t = re.sub(r'`(.*?)`', r'<code>\1</code>', t)
    t = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', t)
    return t

def slug(t):
    t = t.lower().strip()
    t = re.sub(r'[^\w\s-]', '', t)
    return re.sub(r'[\s_-]+', '-', t)

if __name__ == "__main__":
    base_dir = r"f:\VIETLOTT-SMS\00_Draft"
    
    # 1. Convert SRS md to html
    srs_md_path = os.path.join(base_dir, "srs-campaign-tang-ve-bank.md")
    srs_html_path = os.path.join(base_dir, "srs-campaign-tang-ve-bank.html")
    with open(srs_md_path, 'r', encoding='utf-8') as f:
        srs_md_text = f.read()
    srs_html = md_to_html(srs_md_text, "Đặc Tả Yêu Cầu Nghiệp Vụ SRS — Vietlott SMS")
    with open(srs_html_path, 'w', encoding='utf-8') as f:
        f.write(srs_html)
    print("SRS HTML conversion complete.")

    # 2. Convert Gap Analysis md to html
    gap_md_path = os.path.join(base_dir, "gap-analysis-campaign-tang-ve-bank.md")
    gap_html_path = os.path.join(base_dir, "gap-analysis-campaign-tang-ve-bank.html")
    with open(gap_md_path, 'r', encoding='utf-8') as f:
        gap_md_text = f.read()
    gap_html = md_to_html(gap_md_text, "Báo Cáo Phân Tích Gap Analysis — Vietlott SMS")
    with open(gap_html_path, 'w', encoding='utf-8') as f:
        f.write(gap_html)
    print("Gap Analysis HTML conversion complete.")
