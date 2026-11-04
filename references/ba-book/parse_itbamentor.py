import json
import os
import sys
import requests

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = r"f:\VIETLOTT-SMS\references\ba-book\itbamentor_ref"
with open(os.path.join(OUT_DIR, "page_chunk.json"), encoding="utf-8") as f:
    data = json.load(f)

rm = data["recordMap"]

def unwrap(entry):
    if not isinstance(entry, dict):
        return entry
    v = entry.get("value")
    if isinstance(v, dict) and "value" in v and "role" in v:
        return v["value"]
    return v

print("=== COLLECTIONS ===")
coll_id = None
for cid, c in rm.get("collection", {}).items():
    cv = unwrap(c)
    coll_id = cid
    print("Collection ID:", cid)
    print("Name:", cv.get("name"))
    print("Icon:", cv.get("icon"), "Cover:", cv.get("cover"))
    print("Description:", cv.get("description"))
    print("Schema:")
    for pid, prop in (cv.get("schema") or {}).items():
        print(f"  {pid}: {json.dumps(prop, ensure_ascii=False)}")

print("\n=== VIEWS ===")
view_ids = []
for vid, v in rm.get("collection_view", {}).items():
    vv = unwrap(v)
    view_ids.append(vid)
    print("View ID:", vid)
    print("  Name:", vv.get("name"), "| Type:", vv.get("type"))
    print("  Format:", json.dumps(vv.get("format"), ensure_ascii=False))
    print("  Query2:", json.dumps(vv.get("query2"), ensure_ascii=False))

print("\n=== PAGE BLOCKS ===")
for bid, b in rm.get("block", {}).items():
    bv = unwrap(b)
    if not bv:
        continue
    print(f"Block {bid} | type={bv.get('type')} | parent={bv.get('parent_id')}")
    if bv.get("format"):
        print("  format:", json.dumps(bv.get("format"), ensure_ascii=False))
    if bv.get("properties"):
        print("  properties:", json.dumps(bv.get("properties"), ensure_ascii=False)[:400])
    if bv.get("view_ids"):
        print("  view_ids:", bv.get("view_ids"))

# Now query the collection to get the list of articles!
if coll_id and view_ids:
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }
    q_payload = {
        "source": {"type": "collection", "id": coll_id},
        "collectionView": {"id": view_ids[0]},
        "loader": {
            "reducers": {
                "collection_group_results": {
                    "type": "results",
                    "limit": 30,
                }
            },
            "searchQuery": "",
            "userTimeZone": "Asia/Saigon",
        },
    }
    r = requests.post(
        "https://itbamentor.notion.site/api/v3/queryCollection",
        headers=headers,
        json=q_payload,
        timeout=15,
    )
    print(f"\nqueryCollection status: {r.status_code}, len={len(r.text)}")
    if r.status_code == 200:
        with open(os.path.join(OUT_DIR, "collection_rows.json"), "w", encoding="utf-8") as f:
            f.write(r.text)
        qdata = r.json()
        qblocks = qdata.get("recordMap", {}).get("block", {})
        print(f"Returned blocks in collection query: {len(qblocks)}")
        sample_page_ids = []
        for bid, b in qblocks.items():
            bv = unwrap(b)
            if bv and bv.get("type") == "page" and bv.get("parent_id") == coll_id:
                sample_page_ids.append(bid)
                print(
                    f"  Article Page {bid}: props={json.dumps(bv.get('properties'), ensure_ascii=False)[:300]} | format={json.dumps(bv.get('format'), ensure_ascii=False)}"
                )
        # Fetch full content of top 5 articles!
        for idx, pid in enumerate(sample_page_ids[:5], 1):
            pr = requests.post(
                "https://itbamentor.notion.site/api/v3/loadCachedPageChunk",
                headers=headers,
                json={"page": {"id": pid}, "limit": 100, "cursor": {"stack": []}, "chunkNumber": 0, "verticalColumns": False},
                timeout=15,
            )
            if pr.status_code == 200:
                with open(os.path.join(OUT_DIR, f"sample_article_{idx}.json"), "w", encoding="utf-8") as f:
                    f.write(pr.text)
                print(f"Saved sample_article_{idx}.json ({pid}), len={len(pr.text)}")
