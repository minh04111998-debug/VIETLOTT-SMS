#!/usr/bin/env python3
"""
Generate 100 fully customized, theme-specific cover cards for "100 ngày làm BA".
- Uses authentic high-res artwork from Mr. Phú's blog for the matching days (~20 days).
- Uses bespoke editorial designs with unique thematic color palettes, SVG graphics,
  and typography for all other days.
- Output: 1200x675 (16:9) PNGs ready for Notion Gallery cards and page banners.
"""
import concurrent.futures
import glob
import html
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(r"f:\VIETLOTT-SMS\references\ba-book")
ARTICLES_JSON = BASE_DIR / "extracted" / "articles_100.json"
ORIG_DIR = BASE_DIR / "itbamentor_ref" / "original_covers"
OUT_DIR = BASE_DIR / "itba_covers" / "themed_covers"
HTML_DIR = OUT_DIR / "html"

OUT_DIR.mkdir(parents=True, exist_ok=True)
HTML_DIR.mkdir(parents=True, exist_ok=True)

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
EDGE = next(p for p in EDGE_PATHS if Path(p).exists())

with open(ARTICLES_JSON, encoding="utf-8") as f:
    articles = json.load(f)

# Map authentic original covers to book days
# Format: day -> filename in ORIG_DIR
ORIGINAL_MAPPING = {
    2: "1cdd4f15_Day 2100  BA không tư duy hệ thống  Ngườ.png",
    3: "1cdd4f15_Day 3100  3 kỹ thuật BABOK giúp BA không.png",
    4: "1cdd4f15_Day 4100  3 kỹ thuật BABOK giúp bạn xử l.png",
    5: "1ced4f15_Day 5100.png",
    7: "1e5d4f15_Day 7100 3 kỹ thuật BABOK giúp BA đo lườ.png",
    8: "1e5d4f15_Day 8100  Học gì để lên Senior BA.png",
    9: "1e5d4f15_Day 9100 3 kỹ thuật BABOK giúp bạn tránh.png",
    10: "1e5d4f15_Day 10100 PO tự vẽ UIUX rồi bảo BA check.png",
    11: "1e5d4f15_Day 11100 Khi BA gật đầu vì ngại hỏi lại.png",
    12: "1cdd4f15_BA có cần biết code không.png",
    13: "1e5d4f15_Day 12100 Data Object  Bí kíp phân tích .png",
    14: "1e5d4f15_Day 13100 3 dạng comment dễ khiến BA rơi.png",
    15: "1e5d4f15_Day 15100 BA không biết gốc  chỉ chăm ch.png",
    17: "1e5d4f15_Day 16100 Tôi từng làm ở một công ty nọ .png",
    18: "1e5d4f15_Cuối tuần rồi chắc thể nào cũng có team .png",
    19: "1e5d4f15_Day 18100 Một ngày họp 6 tiếng  còn đâu .png",
    20: "1e5d4f15_Day 19100 Không xem kỹ hệ thống hiện tại.png",
    21: "1e5d4f15_Day 20100 BA kiêm PM  tưởng được nâng tầ.png",
    22: "1e5d4f15_Day 21100 Tính năng chỉ thêm 1 dòng thôi.png",
    23: "1e5d4f15_Day 22100 Domain-Driven Design DDD là gì.png",
    24: "1e5d4f15_Day 23100.png",
    25: "1e7d4f15_Day 24100 Hidden Requirement  Khi quy tắ.png",
}

print(f"Total articles loaded: {len(articles)}")
print(f"Total mapped original covers: {len(ORIGINAL_MAPPING)}")
