import glob
import json
import os
import sys
import urllib.parse
import requests

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = r"f:\VIETLOTT-SMS\references\ba-book\itbamentor_ref"

def unwrap(entry):
    if not isinstance(entry, dict):
        return entry
    v = entry.get("value")
    if isinstance(v, dict) and "value" in v and "role" in v:
        return v["value"]
    return v

# 1. Print full collection schema (some properties had special chars like ;UrC, vg}<)
with open(os.path.join(OUT_DIR, "page_chunk.json"), encoding="utf-8") as f:
    pchunk = json.load(f)
for cid, c in pchunk["recordMap"]["collection"].items():
    cv = unwrap(c)
    print("=== FULL SCHEMA ===")
    for k, v in (cv.get("schema") or {}).items():
        print(f"  {repr(k)} -> name={v.get('name')!r}, type={v.get('type')!r}")

# 2. List all 26 rows from collection_rows.json
with open(os.path.join(OUT_DIR, "collection_rows.json"), encoding="utf-8") as f:
    qdata = json.load(f)
block_ids = qdata["result"]["reducerResults"]["collection_group_results"]["blockIds"]
qblocks = qdata["recordMap"]["block"]
print(f"\n=== ALL {len(block_ids)} ROWS IN BLOG ===")
day1_id = None
for i, bid in enumerate(block_ids, 1):
    bv = unwrap(qblocks.get(bid, {}))
    if not bv:
        continue
    props = bv.get("properties", {})
    title = "".join(seg[0] for seg in props.get("title", []))
    tags = props.get("T\nr", [[""]])[0][0]
    pub = json.dumps(props.get("wOPZ"), ensure_ascii=False)
    other_props = {k: v for k, v in props.items() if k not in ("title", "T\nr", "wOPZ")}
    fmt = bv.get("format", {})
    print(f"  {i:2d}. {bid} | icon={fmt.get('page_icon')} | cover={fmt.get('page_cover')} | tags={tags} | title={title}")
    if other_props:
        print(f"      other_props={json.dumps(other_props, ensure_ascii=False)[:250]}")
    if "[Day 1/" in title or "[Day 2/" in title:
        day1_id = bid

# Also fetch Day 1/100 and Day 2/100 if present!
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}
for bid in block_ids:
    bv = unwrap(qblocks.get(bid, {}))
    if not bv:
        continue
    title = "".join(seg[0] for seg in bv.get("properties", {}).get("title", []))
    if any(tag in title for tag in ["[Day 1/", "[Day 2/", "[Day 3/"]):
        pr = requests.post(
            "https://itbamentor.notion.site/api/v3/loadCachedPageChunk",
            headers=headers,
            json={"page": {"id": bid}, "limit": 100, "cursor": {"stack": []}, "chunkNumber": 0, "verticalColumns": False},
            timeout=15,
        )
        if pr.status_code == 200:
            with open(os.path.join(OUT_DIR, f"early_{bid}.json"), "w", encoding="utf-8") as f:
                f.write(pr.text)
            print(f"Fetched early article {bid}: {title}")

# 3. Dump block tree of 3 articles to see exact block types, colors, callouts, images, dividers, headings!
def dump_article_tree(json_path):
    with open(json_path, encoding="utf-8") as f:
        adata = json.load(f)
    blocks = {bid: unwrap(b) for bid, b in adata["recordMap"]["block"].items()}
    # root page block is first block with type == 'page'
    root_id = None
    for bid, bv in blocks.items():
        if bv and bv.get("type") == "page":
            root_id = bid
            break
    root = blocks[root_id]
    title = "".join(seg[0] for seg in root.get("properties", {}).get("title", []))
    print(f"\n==========================================")
    print(f"ARTICLE: {title} ({root_id})")
    print(f"FORMAT: {json.dumps(root.get('format'), ensure_ascii=False)}")
    print(f"==========================================")

    def walk(bid, indent=0):
        bv = blocks.get(bid)
        if not bv:
            return
        btype = bv.get("type")
        fmt = bv.get("format", {})
        props = bv.get("properties", {})
        # keep only interesting format keys
        clean_fmt = {k: v for k, v in fmt.items() if k not in ("copied_from_pointer", "installation_imprint", "ai_property_inference_map")}
        txt = props.get("title", [])
        if btype != "page":
            print("  " * indent + f"[{btype}] fmt={json.dumps(clean_fmt, ensure_ascii=False)} | text={json.dumps(txt, ensure_ascii=False)}")
        for child_id in bv.get("content", []) or []:
            walk(child_id, indent + (0 if btype == "page" else 1))

    walk(root_id, 0)

for p in sorted(glob.glob(os.path.join(OUT_DIR, "early_*.json")))[:2] + sorted(glob.glob(os.path.join(OUT_DIR, "article_1_*.json"))):
    dump_article_tree(p)
