import json
import os
import subprocess
import sys
import urllib.parse
import requests

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = r"f:\VIETLOTT-SMS\references\ba-book\itbamentor_ref"
SPACE_ID = "bde9990e-dae8-4af4-8ad0-64bb91c7cbed"

samples = [
    ("cover_day24.png", "1e7d4f15-f66e-8069-ada9-e2380c21c5c3", "attachment:f2cf8b57-90fb-4284-8302-c39c6dbafda1:Thm_tiu__(28).png"),
    ("cover_day15.png", "1e5d4f15-f66e-809a-b7cb-eff2c4a36e2d", "attachment:30703239-92b8-4f29-af66-c87d88f8b5d1:Thm_tiu__(17).png"),
    ("cover_day08.png", "1e5d4f15-f66e-806f-aeb2-f457b6043bec", "attachment:69f4c864-0a67-4104-abf9-1fdfd1c14a99:Thm_tiu__(7).png"),
    ("cover_day02.png", "1cdd4f15-f66e-81d2-92e9-ec248a1d97e9", "attachment:5d31e8cd-f1af-45c5-84f9-6df7a1c54a48:ChatGPT_Image_Apr_6_2025_08_12_56_PM.png"),
]

headers = {"User-Agent": "Mozilla/5.0"}
for fname, bid, att in samples:
    enc = urllib.parse.quote(att, safe="")
    url = f"https://itbamentor.notion.site/image/{enc}?table=block&id={bid}&spaceId={SPACE_ID}&width=1600&cache=v2"
    r = requests.get(url, headers=headers, timeout=15)
    print(f"{fname}: status={r.status_code}, content-type={r.headers.get('Content-Type')}, bytes={len(r.content)}")
    if r.status_code == 200 and len(r.content) > 1000:
        with open(os.path.join(OUT_DIR, fname), "wb") as f:
            f.write(r.content)

# Also check Day 2, Article 2, Article 3 block types to see if any contain inline images or callouts
def unwrap(entry):
    if not isinstance(entry, dict):
        return entry
    v = entry.get("value")
    if isinstance(v, dict) and "value" in v and "role" in v:
        return v["value"]
    return v

for jf in ["early_1cdd4f15-f66e-81d2-92e9-ec248a1d97e9.json", "article_2_1e5d4f15-f66e-801c-8024-ddf0b7ab6df9.json", "article_3_1e5d4f15-f66e-802a-9779-fe9cff5c77c9.json"]:
    p = os.path.join(OUT_DIR, jf)
    if os.path.exists(p):
        d = json.load(open(p, encoding="utf-8"))
        btypes = {}
        for bid, b in d["recordMap"]["block"].items():
            bv = unwrap(b)
            if bv:
                t = bv.get("type")
                btypes[t] = btypes.get(t, 0) + 1
        print(f"Block counts in {jf}: {btypes}")
