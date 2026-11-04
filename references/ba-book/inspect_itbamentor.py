import json
import subprocess
import sys
import os
import requests

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = r"f:\VIETLOTT-SMS\references\ba-book\itbamentor_ref"
os.makedirs(OUT_DIR, exist_ok=True)

PAGE_ID = "1cdd4f15-f66e-8094-b665-eb1fca016d5f"
PUBLIC_URL = "https://itbamentor.notion.site/Blog-ITBA-Mentor-1cdd4f15f66e8094b665eb1fca016d5f"

# 1. Try Notion's standard public page chunk endpoint for *.notion.site
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

payload = {
    "page": {"id": PAGE_ID},
    "limit": 100,
    "cursor": {"stack": []},
    "chunkNumber": 0,
    "verticalColumns": False,
}

for endpoint in [
    "https://itbamentor.notion.site/api/v3/loadCachedPageChunk",
    "https://www.notion.so/api/v3/loadCachedPageChunk",
]:
    try:
        r = requests.post(endpoint, headers=headers, json=payload, timeout=15)
        print(f"POST {endpoint} -> status {r.status_code}, len={len(r.text)}")
        if r.status_code == 200:
            out_json = os.path.join(OUT_DIR, "page_chunk.json")
            with open(out_json, "w", encoding="utf-8") as f:
                f.write(r.text)
            data = r.json()
            rm = data.get("recordMap", {})
            print("recordMap keys:", list(rm.keys()))
            blocks = rm.get("block", {})
            collections = rm.get("collection", {})
            views = rm.get("collection_view", {})
            print(f"blocks={len(blocks)}, collections={len(collections)}, views={len(views)}")
            break
        else:
            print("Response snippet:", r.text[:300])
    except Exception as e:
        print(f"Error calling {endpoint}: {e}")
