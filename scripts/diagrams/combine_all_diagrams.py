import os
import re

def combine_diagrams():
    draft_dir = r"f:\VIETLOTT-SMS\00_Draft"
    files = [
        "activity_diagram_swimlane.drawio",
        "usecase_diagram.drawio",
        "class_diagram.drawio",
        "sequence_diagram.drawio",
        "state_machine_diagram.drawio",
        "erd_diagram.drawio"
    ]
    
    diagram_blocks = []
    
    for fname in files:
        fpath = os.path.join(draft_dir, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                # Find all <diagram ...> ... </diagram> blocks
                matches = re.findall(r"(<diagram\b[^>]*>.*?</diagram>)", content, re.DOTALL)
                for m in matches:
                    diagram_blocks.append(m)
                    
    master_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-08-02T10:35:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
''' + "\n".join(diagram_blocks) + '''
</mxfile>'''

    master_path = os.path.join(draft_dir, "all_diagrams.drawio")
    with open(master_path, "w", encoding="utf-8") as f:
        f.write(master_xml)
    print(f"Master multi-tab file generated successfully at: {master_path}")

if __name__ == "__main__":
    combine_diagrams()
