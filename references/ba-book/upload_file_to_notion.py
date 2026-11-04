#!/usr/bin/env python3
"""
Helper to POST one or more local files to Notion File Upload URLs returned by `notion-create-file-upload`.
Usage:
  python upload_file_to_notion.py <manifest_json_path>
Where manifest_json_path contains a JSON list of:
  [{"file_path": "...", "upload_url": "...", "upload_headers": {...}}, ...]
"""
import concurrent.futures
import json
import os
import sys
import requests

sys.stdout.reconfigure(encoding="utf-8")


def post_one(item):
    fpath = item["file_path"]
    url = item["upload_url"]
    headers = dict(item.get("upload_headers") or {})
    # Never manually set Content-Type for multipart/form-data; requests adds boundary!
    headers.pop("Content-Type", None)
    headers.pop("content-type", None)
    fname = os.path.basename(fpath)
    with open(fpath, "rb") as f:
        r = requests.post(url, headers=headers, files={"file": (fname, f, "image/png")}, timeout=30)
    return fname, r.status_code, r.text[:300]


if __name__ == "__main__":
    manifest_path = sys.argv[1]
    items = json.loads(open(manifest_path, encoding="utf-8").read())
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        for fname, code, body in ex.map(post_one, items):
            print(f"{fname} -> HTTP {code} | {body}")
            if code >= 300:
                sys.exit(1)
