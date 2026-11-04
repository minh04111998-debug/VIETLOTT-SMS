# -*- coding: utf-8 -*-
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

PAT_FOOTER = re.compile(r"\s*[—–-]\s*\*\*IT\s*[-]?\s*BA\s+Mentor\*\*", re.I)
PAT_ANY_ITBA = re.compile(r"\bi\s*t\s*[-]?\s*b\s*a\b|itba", re.I)

chunk_files = sorted(glob.glob(r"f:\VIETLOTT-SMS\references\ba-book\extracted\blog_update_chunks\blog_chunk_*.json"))
cleaned_count = 0
remaining_hits = []

for cf in chunk_files:
    with open(cf, "r", encoding="utf-8") as f:
        items = json.load(f)
    modified = False
    for item in items:
        for field in ("notion_title", "summary", "blog_markdown"):
            val = item.get(field, "")
            new_val = PAT_FOOTER.sub("", val)
            # Also clean any stray ITBA Mentor or IT BA if present
            new_val = re.sub(r"IT\s*[-]?\s*BA\s+Mentor", "BA Mentor", new_val, flags=re.I)
            new_val = re.sub(r"\bIT\s*[-]?\s*BA\b", "BA", new_val, flags=re.I)
            if new_val != val:
                item[field] = new_val
                modified = True
                cleaned_count += 1
            for m in PAT_ANY_ITBA.finditer(item.get(field, "")):
                remaining_hits.append((item["day"], field, m.group(0)))
    if modified:
        with open(cf, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)

# Also check articles_100.json
art_path = r"f:\VIETLOTT-SMS\references\ba-book\extracted\articles_100.json"
with open(art_path, "r", encoding="utf-8") as f:
    arts = json.load(f)
art_mod = False
for a in arts:
    for field in ("title", "notion_title", "summary", "body_markdown", "blog_markdown"):
        if field in a and isinstance(a[field], str):
            v = a[field]
            nv = PAT_FOOTER.sub("", v)
            nv = re.sub(r"IT\s*[-]?\s*BA\s+Mentor", "BA Mentor", nv, flags=re.I)
            nv = re.sub(r"\bIT\s*[-]?\s*BA\b", "BA", nv, flags=re.I)
            if nv != v:
                a[field] = nv
                art_mod = True
if art_mod:
    with open(art_path, "w", encoding="utf-8") as f:
        json.dump(arts, f, ensure_ascii=False, indent=2)

print(f"Cleaned fields across chunks: {cleaned_count}")
print(f"Remaining IT BA / ITBA hits across all 20 chunks: {len(remaining_hits)}")
if remaining_hits:
    print("Hits:", remaining_hits[:10])
