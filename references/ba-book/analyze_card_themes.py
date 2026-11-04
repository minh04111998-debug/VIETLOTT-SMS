import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open(r"f:\VIETLOTT-SMS\references\ba-book\extracted\articles_100.json", encoding="utf-8") as f:
    articles = json.load(f)

for a in articles:
    d = a["day"]
    title = a.get("notion_title", "")
    print(f"Day {d:03d}: {title}")
