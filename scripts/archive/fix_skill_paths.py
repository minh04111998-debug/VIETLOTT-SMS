from pathlib import Path

skills_dir = Path(".agents/skills").resolve()

replacements = {
    "`ba/SKILL.md`": "`.agents/skills/ba/SKILL.md`",
    "`dev/SKILL.md`": "`.agents/skills/dev/SKILL.md`",
    "`po/SKILL.md`": "`.agents/skills/po/SKILL.md`",
    "thư mục `ba/`": "thư mục `.agents/skills/ba/`",
    "nằm trong `po/`": "nằm trong `.agents/skills/po/`",
    "`templates/document-templates.md`": "`.agents/skills/ba/templates/document-templates.md`",
    "`templates/product-templates.md`": "`.agents/skills/po/templates/product-templates.md`",
    "`artifacts/technical/design/adr/": "`artifacts/decisions/",
}

count = 0
for f in skills_dir.rglob("*.md"):
    content = f.read_text(encoding="utf-8")
    orig = content
    for old, new in replacements.items():
        content = content.replace(old, new)
    if content != orig:
        f.write_text(content, encoding="utf-8")
        count += 1
        print(f"Updated: {f.name}")

print(f"Total files updated in skills: {count}")
