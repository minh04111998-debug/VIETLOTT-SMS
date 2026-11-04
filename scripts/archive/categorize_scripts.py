import os
import shutil
from pathlib import Path

root = Path("scripts")

categories = {
    "diagrams": [
        "combine_all_diagrams.py", "generate_all_diagrams.py", "generate_bpmn_diagram.py",
        "generate_drawio_xml.py", "generate_mapping.py", "generate_svg_b64.py",
        "generate_svg_swimlane.py", "fix_all_diagram_layouts.py", "fix_all_diagram_overlaps.py",
        "fix_svg_overlap.py"
    ],
    "converters": [
        "convert_md_to_html.py", "convert_md_to_html_full.py", "convert_standalone.py",
        "convert_word_to_md.py", "merge_markdown.py"
    ],
    "extractors": [
        "extract_all.py", "extract_docx.py", "extract_strings.py",
        "merge_docx.py", "run_recursive_extract.py"
    ]
}

for folder, files in categories.items():
    folder_path = root / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    for fname in files:
        src = root / fname
        dest = folder_path / fname
        if src.exists():
            shutil.move(str(src), str(dest))
            print(f"Moved {fname} -> {folder}/")

print("All scripts categorized successfully.")
