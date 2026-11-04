#!/usr/bin/env python3
"""
Generate 100 fully bespoke, theme-tailored cover cards for "100 ngày làm BA".
- Resizes and incorporates authentic high-res artwork from Mr. Phú's blog for the ~22 matching days.
- Renders rich, topic-specific editorial graphic cards with distinctive palettes and SVGs for all other days.
"""
import concurrent.futures
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
OUT_DIR = BASE_DIR / "itba_covers" / "custom_100"
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

# Authentic covers from Mr. Phú's official blog
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

THEMES = {
    "blueprint": {
        "bg": "radial-gradient(circle at 15% 20%, #1e293b 0%, #0f172a 100%)",
        "badge_border": "#38bdf8",
        "badge_bg": "rgba(56, 189, 248, 0.15)",
        "badge_color": "#38bdf8",
        "headline_color": "#38bdf8",
        "sub_color": "#cbd5e1"
    },
    "terminal": {
        "bg": "radial-gradient(circle at 20% 25%, #27272a 0%, #18181b 100%)",
        "badge_border": "#4ade80",
        "badge_bg": "rgba(74, 222, 128, 0.15)",
        "badge_color": "#4ade80",
        "headline_color": "#4ade80",
        "sub_color": "#e4e4e7"
    },
    "amber": {
        "bg": "radial-gradient(circle at 20% 20%, #312e81 0%, #1e1b4b 100%)",
        "badge_border": "#f59e0b",
        "badge_bg": "rgba(245, 158, 11, 0.15)",
        "badge_color": "#f59e0b",
        "headline_color": "#fbbf24",
        "sub_color": "#e0e7ff"
    },
    "crimson": {
        "bg": "radial-gradient(circle at 15% 20%, #450a0a 0%, #1c1917 100%)",
        "badge_border": "#f87171",
        "badge_bg": "rgba(248, 113, 113, 0.15)",
        "badge_color": "#f87171",
        "headline_color": "#fca5a5",
        "sub_color": "#fecdd3"
    },
    "executive": {
        "bg": "radial-gradient(circle at 20% 25%, #292524 0%, #1c1917 100%)",
        "badge_border": "#eab308",
        "badge_bg": "rgba(234, 179, 8, 0.15)",
        "badge_color": "#eab308",
        "headline_color": "#fef08a",
        "sub_color": "#f5f5f4"
    },
    "creative": {
        "bg": "radial-gradient(circle at 15% 25%, #3b0764 0%, #1e1b4b 100%)",
        "badge_border": "#c084fc",
        "badge_bg": "rgba(192, 132, 252, 0.15)",
        "badge_color": "#c084fc",
        "headline_color": "#e9d5ff",
        "sub_color": "#fae8ff"
    },
    "emerald": {
        "bg": "radial-gradient(circle at 20% 20%, #064e3b 0%, #022c22 100%)",
        "badge_border": "#34d399",
        "badge_bg": "rgba(52, 211, 153, 0.15)",
        "badge_color": "#34d399",
        "headline_color": "#6ee7b7",
        "sub_color": "#ecfdf5"
    },
    "sapphire": {
        "bg": "radial-gradient(circle at 15% 25%, #1e3a8a 0%, #0f172a 100%)",
        "badge_border": "#60a5fa",
        "badge_bg": "rgba(96, 165, 250, 0.15)",
        "badge_color": "#60a5fa",
        "headline_color": "#93c5fd",
        "sub_color": "#eff6ff"
    },
    "hazard": {
        "bg": "radial-gradient(circle at 20% 20%, #431407 0%, #1c1917 100%)",
        "badge_border": "#fb923c",
        "badge_bg": "rgba(251, 146, 60, 0.15)",
        "badge_color": "#fb923c",
        "headline_color": "#fed7aa",
        "sub_color": "#ffedd5"
    }
}
