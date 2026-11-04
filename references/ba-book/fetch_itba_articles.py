import json
import os
import sys
import requests

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = r"f:\VIETLOTT-SMS\references\ba-book\itbamentor_ref"
COLL_ID = "1cdd4f15-f66e-816e-87e3-000b5b2519dd"
VIEW_ID = "1cdd4f15-f66e-81a0-940e-000c585d6507"
SPACE_ID = "bde9990e-dae8-4af4-8ad0-64bb91c7cbed"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}

q_payload = {
    "source": {"type": "collection", "id": COLL_ID, "spaceId": SPACE_ID},
    "collectionView": {"id": VIEW_ID, "spaceId": SPACE_ID},
    "loader": {
        "type": "reducer",
        "reducers": {
            "collection_group_results": {
                "type": "results",
                "limit": 50,
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
print("queryCollection status:", r.status_code, "len:", len(r.text))
if r.status_code != 200:
    print("Error text:", r.text)
else:
    with open(os.path.join(OUT_DIR, "collection_rows.json"), "w", encoding="utf-8") as f:
        f.write(r.text)
    qdata = r.json()
    def unwrap(entry):
        if not isinstance(entry, dict):
            return entry
        v = entry.get("value")
        if isinstance(v, dict) and "value" in v and "role" in v:
            return v["value"]
        return v

    block_ids = (
        qdata.get("result", {})
        .get("reducerResults", {})
        .get("collection_group_results", {})
        .get("blockIds", [])
    )
    print("Total blockIds returned:", len(block_ids))
    qblocks = qdata.get("recordMap", {}).get("block", {})
    for i, bid in enumerate(block_ids[:20], 1):
        bv = unwrap(qblocks.get(bid, {}))
        if bv:
            print(f"{i}. {bid} | props={json.dumps(bv.get('properties'), ensure_ascii=False)} | format={json.dumps(bv.get('format'), ensure_ascii=False)}")

    # Fetch top 6 articles (especially BA100 articles!)
    ba100_ids = []
    other_ids = []
    for bid in block_ids:
        bv = unwrap(qblocks.get(bid, {}))
        if not bv:
            continue
        pstr = json.dumps(bv.get("properties", {}), ensure_ascii=False)
        if "BA100" in pstr or "BABOK" in pstr:
            ba100_ids.append(bid)
        else:
            other_ids.append(bid)

    chosen = (ba100_ids[:5] + other_ids[:3])[:6]
    print("Fetching full chunks for chosen articles:", chosen)
    for idx, pid in enumerate(chosen, 1):
        pr = requests.post(
            "https://itbamentor.notion.site/api/v3/loadCachedPageChunk",
            headers=headers,
            json={"page": {"id": pid}, "limit": 100, "cursor": {"stack": []}, "chunkNumber": 0, "verticalColumns": False},
            timeout=15,
        )
        print(f"  Article {idx} ({pid}): status={pr.status_code}, len={len(pr.text)}")
        if pr.status_code == 200:
            with open(os.path.join(OUT_DIR, f"article_{idx}_{pid}.json"), "w", encoding="utf-8") as f:
                f.write(pr.text)
