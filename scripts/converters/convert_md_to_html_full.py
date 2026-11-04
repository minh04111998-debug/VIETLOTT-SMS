import os
import re
import zlib
import base64
import markdown

def plantuml_to_kroki_url(plantuml_code):
    """Encodes PlantUML text into a Kroki SVG URL for direct image rendering."""
    compressed = zlib.compress(plantuml_code.encode('utf-8'))
    encoded = base64.urlsafe_b64encode(compressed).decode('utf-8')
    return f"https://kroki.io/plantuml/svg/{encoded}"

def convert_md_file_to_html(md_path, html_path, title):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace PlantUML code blocks with Kroki SVG <img> tags
    def plantuml_replacer(match):
        puml_code = match.group(1).strip()
        img_url = plantuml_to_kroki_url(puml_code)
        return f'\n\n<div class="diagram-wrapper"><div class="diagram-title">Sơ đồ Luồng Hoạt động (PlantUML Visual Diagram)</div><img class="diagram-img" src="{img_url}" alt="PlantUML Swimlane Diagram" /><p class="diagram-caption">Sơ đồ Swimlane phân chia luồng Khách hàng, Web Admin và Realtime Rule Engine</p></div>\n\n'

    content = re.sub(r'```plantuml\n(.*?)```', plantuml_replacer, content, flags=re.DOTALL)

    # Replace Mermaid code blocks with mermaid div tags for client-side SVG rendering
    def mermaid_replacer(match):
        mermaid_code = match.group(1).strip()
        return f'\n\n<div class="diagram-wrapper"><div class="diagram-title">Sơ đồ Luồng (Mermaid Visual Diagram)</div><div class="mermaid">\n{mermaid_code}\n</div></div>\n\n'

    content = re.sub(r'```mermaid\n(.*?)```', mermaid_replacer, content, flags=re.DOTALL)

    # Convert GitHub Alert blockquotes
    def alert_replacer(match):
        alert_type = match.group(1).lower()
        alert_text = match.group(2).strip()
        # clean blockquote prefix '>'
        clean_lines = []
        for line in alert_text.split('\n'):
            if line.startswith('>'):
                clean_lines.append(line[1:].strip())
            else:
                clean_lines.append(line.strip())
        body = "<br>".join(clean_lines)
        return f'\n<div class="alert alert-{alert_type}"><div class="alert-title">📌 {alert_type.upper()}</div><div class="alert-body">{body}</div></div>\n'

    content = re.sub(r'> \[!(WARNING|IMPORTANT|NOTE|TIP|CAUTION)\]\n((?:>.*\n?)+)', alert_replacer, content)

    # Use Python's markdown library with tables and fenced_code extensions for 100% complete rendering
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc', 'nl2br'])
    body_html = md.convert(content)

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
        
        .header-banner {{ background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: white; padding: 2.5rem; border-radius: 12px; margin-bottom: 2.5rem; border-left: 8px solid var(--primary-red); position: relative; }}
        .header-banner h1 {{ font-family: 'Outfit', sans-serif; font-size: 2.2rem; font-weight: 700; color: #ffffff; margin-bottom: 0.5rem; border-bottom: none; }
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
        table {{ width: 100%; border-collapse: collapse; font-size: 0.92rem; text-align: left; margin: 1.5rem 0; border-radius: 8px; overflow: hidden; border: 1px solid var(--border-color); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); }}
        th {{ background-color: #f8fafc; color: #0f172a; font-weight: 700; padding: 1rem; border-bottom: 2px solid var(--border-color); text-transform: uppercase; font-size: 0.82rem; letter-spacing: 0.03em; }}
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

        .mermaid {{
            margin: 0 auto;
        }}

        code {{ background-color: #f1f5f9; color: #e31b23; padding: 0.2rem 0.4rem; border-radius: 4px; font-family: 'Consolas', monospace; font-size: 0.88rem; }}
        pre code {{ background: none; color: inherit; padding: 0; }}
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
            <h1>Vietlott SMS — System Document</h1>
            <p>{title}</p>
        </div>
        {body_html}
    </div>
    <script>
        mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
    </script>
</body>
</html>
"""
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Successfully generated {html_path}")

if __name__ == "__main__":
    base_dir = r"f:\VIETLOTT-SMS\00_Draft"
    convert_md_file_to_html(
        os.path.join(base_dir, "srs-campaign-tang-ve-bank.md"),
        os.path.join(base_dir, "srs-campaign-tang-ve-bank.html"),
        "Đặc Tả Yêu Cầu Nghiệp Vụ SRS - Vietlott SMS"
    )
    convert_md_file_to_html(
        os.path.join(base_dir, "gap-analysis-campaign-tang-ve-bank.md"),
        os.path.join(base_dir, "gap-analysis-campaign-tang-ve-bank.html"),
        "Báo Cáo Phân Tích Gap Analysis - Vietlott SMS"
    )
