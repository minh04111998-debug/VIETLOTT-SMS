#!/usr/bin/env python3
"""
Merge & Verify 234 extracted book pages into 100 BA articles (Day 1/100 .. Day 100/100),
generate local Markdown files, and prepare Notion-flavored Markdown batches.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(r"f:\VIETLOTT-SMS\references\ba-book")
PAGES_DIR = BASE_DIR / "extracted" / "pages"
DAYS_DIR = BASE_DIR / "days"
BATCHES_DIR = BASE_DIR / "extracted" / "notion_batches"


def parse_page_file(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8").strip()
    # Strip accidental outer markdown fences if any subagent wrapped output
    if raw.startswith("```"):
        lines = raw.splitlines()
        if lines[0].startswith("```") and lines[-1].strip() == "```":
            raw = "\n".join(lines[1:-1]).strip()

    if "\n---\n" in raw:
        header_part, body = raw.split("\n---\n", 1)
    elif "\r\n---\r\n" in raw:
        header_part, body = raw.split("\r\n---\r\n", 1)
    else:
        # Fallback regex split on standalone ---
        m = re.search(r"^---\s*$", raw, flags=re.MULTILINE)
        if not m:
            raise ValueError(f"Missing '---' separator in {path.name}")
        header_part = raw[: m.start()]
        body = raw[m.end() :]

    meta = {}
    for line in header_part.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().upper()] = v.strip()

    idx_from_name = int(re.search(r"(\d+)", path.stem).group(1))
    image_index = int(meta.get("IMAGE_INDEX", idx_from_name))
    book_page = int(re.search(r"\d+", meta.get("BOOK_PAGE", str(image_index + 3))).group(0))
    day_match = re.search(r"\d+", meta.get("DAY", "0"))
    day = int(day_match.group(0)) if day_match else 0
    is_start = meta.get("IS_START_PAGE", "").lower() in ("true", "yes", "1")
    title = meta.get("TITLE", "").strip()

    return {
        "file": path.name,
        "image_index": image_index,
        "book_page": book_page,
        "day": day,
        "is_start": is_start,
        "title": title,
        "body": body.strip(),
    }


def join_continuation_pages(bodies: list[str]) -> str:
    """Join multi-page bodies cleanly, merging mid-sentence page wraps when appropriate."""
    if not bodies:
        return ""
    merged = bodies[0].strip()
    for nxt in bodies[1:]:
        nxt = nxt.strip()
        if not nxt:
            continue
        if not merged:
            merged = nxt
            continue
        last_line = merged.splitlines()[-1].strip()
        first_line = nxt.splitlines()[0].strip()
        # Check if last_line ended mid-sentence (not ending with sentence punctuation or colon)
        # and first_line is plain continuation text (not a list item, heading, or icon bullet)
        ends_open = bool(last_line) and last_line[-1] not in ".!?:;\"”’)"
        starts_block = bool(
            re.match(
                r"^(#|\-|\*|\+|\d+[\.\)]|>|→|[■▲●◆✦💡📌✖🎯❓❗✓✔☑️])",
                first_line,
            )
        )
        if ends_open and not starts_block and first_line and first_line[0].islower():
            merged = merged + " " + nxt
        else:
            merged = merged + "\n\n" + nxt
    return merged


def escape_notion_markdown(md: str) -> str:
    """
    Ensure plain-text angle brackets like <id> or <field> outside inline code / code blocks
    are escaped as \\<...>, per notion-flavored-markdown-spec.
    """
    out_lines = []
    in_fence = False
    for line in md.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        # Split by inline backticks `...` so code spans stay untouched
        parts = re.split(r"(`+[^`]*`+)", line)
        for i in range(0, len(parts), 2):
            # Escape <something> in non-code segments
            parts[i] = re.sub(r"<([A-Za-zÀ-ỹ0-9_/\-\s]+)>", r"\\<\1>", parts[i])
        out_lines.append("".join(parts))
    return "\n".join(out_lines)


def main():
    files = sorted(PAGES_DIR.glob("img_*.md"))
    print(f"Found {len(files)}/234 page files.")
    missing_indices = set(range(1, 235)) - {
        int(re.search(r"(\d+)", f.stem).group(1)) for f in files
    }
    if missing_indices:
        print(f"MISSING IMAGE INDICES ({len(missing_indices)}): {sorted(missing_indices)}")
        sys.exit(1)

    pages = [parse_page_file(f) for f in files]
    pages.sort(key=lambda x: x["image_index"])

    # Audit book_page sequence (4..237)
    bad_pages = [
        (p["image_index"], p["book_page"])
        for p in pages
        if p["book_page"] != p["image_index"] + 3
    ]
    if bad_pages:
        print(f"WARNING - Book page drift detected: {bad_pages}")

    # Group sequentially in book page order so publisher header typos on continuation pages
    # (e.g., Page 219 printing 'DAY 89/100' while continuing Day 90 from Page 218)
    # never attach a continuation page to the wrong Day!
    by_day = defaultdict(list)
    active_day = None
    header_typos = []
    for p in pages:
        if p["is_start"] or active_day is None:
            active_day = p["day"]
        else:
            if p["day"] != active_day:
                header_typos.append(
                    f"Book Page {p['book_page']} ({p['file']}): continuation page printed 'DAY {p['day']}/100' "
                    f"after DAY {active_day}/100 -> kept in DAY {active_day}/100"
                )
        by_day[active_day].append(p)
    if header_typos:
        print("Detected & auto-corrected book header typos on continuation pages:")
        for ht in header_typos:
            print("  *", ht)

    missing_days = sorted(set(range(1, 101)) - set(by_day.keys()))
    extra_days = sorted(set(by_day.keys()) - set(range(1, 101)))
    if missing_days or extra_days:
        print(f"DAY ANOMALY! Missing days: {missing_days} | Extra days: {extra_days}")
        sys.exit(2)

    DAYS_DIR.mkdir(parents=True, exist_ok=True)
    BATCHES_DIR.mkdir(parents=True, exist_ok=True)

    articles = []
    warnings = []
    for day_num in range(1, 101):
        day_pages = sorted(by_day[day_num], key=lambda x: x["image_index"])
        titles = [p["title"] for p in day_pages if p["title"]]
        title = titles[0] if titles else ""
        if not title:
            # Try extracting first bold/heading line if subagent forgot TITLE field
            first_lines = day_pages[0]["body"].splitlines()
            if first_lines:
                cand = first_lines[0].strip("#* ").strip()
                warnings.append(f"Day {day_num} (img_{day_pages[0]['image_index']:03d}) had empty TITLE, candidate: {cand}")
                title = cand
            else:
                warnings.append(f"Day {day_num} has NO title and empty body!")

        p_start = day_pages[0]["book_page"]
        p_end = day_pages[-1]["book_page"]
        page_label = f"Trang {p_start}" if p_start == p_end else f"Trang {p_start}–{p_end}"
        day_label = f"DAY {day_num}/100"

        page_bodies = []
        for idx_in_day, p in enumerate(day_pages):
            b = p["body"]
            # If a continuation page within the same DAY has its own bonus centered section title
            # (e.g., Day 2 Page 7: CHECKLIST...), preserve it as an H2 heading!
            if idx_in_day > 0 and p["title"] and p["title"].upper() != title.upper():
                b = f"## {p['title']}\n\n{b}"
            page_bodies.append(b)

        merged_body = join_continuation_pages(page_bodies)
        notion_body = escape_notion_markdown(merged_body)

        # Save standalone Markdown file
        md_doc = (
            f"# {day_label} — {title}\n\n"
            f"> **Nguồn:** 100 ngày làm BA (ITBA Mentor) · **{page_label}**\n\n"
            f"{merged_body}\n"
        )
        (DAYS_DIR / f"day-{day_num:03d}.md").write_text(md_doc, encoding="utf-8")

        # Notion page title: clean, readable, searchable
        notion_title = f"Day {day_num}/100 — {title}" if title else f"Day {day_num}/100"
        articles.append(
            {
                "day": day_num,
                "day_label": day_label,
                "page_label": page_label,
                "raw_title": title,
                "notion_title": notion_title,
                "body_markdown": merged_body,
                "notion_content": notion_body,
                "image_indices": [p["image_index"] for p in day_pages],
            }
        )

    # Write full combined Markdown book
    full_md = [
        "# 100 Ngày Làm BA — ITBA Mentor (Bản Số Hóa Đầy Đủ)\n",
        "> Tổng hợp 100 bài viết thực chiến Business Analyst (Trang 4–237).\n",
    ]
    for a in articles:
        full_md.append(
            f"\n---\n\n## {a['day_label']} — {a['raw_title']}\n\n"
            f"*{a['page_label']}*\n\n{a['body_markdown']}\n"
        )
    (BASE_DIR / "100-ngay-lam-ba-full.md").write_text("\n".join(full_md), encoding="utf-8")
    (BASE_DIR / "extracted" / "articles_100.json").write_text(
        json.dumps(articles, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Write Notion batches (20 pages per batch -> 5 batches total)
    batch_size = 20
    for b_idx in range(0, len(articles), batch_size):
        chunk = articles[b_idx : b_idx + batch_size]
        notion_pages = []
        for a in chunk:
            notion_pages.append(
                {
                    "icon": "📘",
                    "properties": {
                        "Tiêu đề": a["notion_title"],
                        "Ngày": a["day"],
                        "Day": a["day_label"],
                        "Trang sách": a["page_label"],
                        "Đã đọc": "__NO__",
                    },
                    "content": a["notion_content"],
                }
            )
        b_num = (b_idx // batch_size) + 1
        (BATCHES_DIR / f"notion_batch_{b_num:02d}.json").write_text(
            json.dumps(notion_pages, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    print(f"SUCCESS! Built all {len(articles)} articles and 5 Notion batches.")
    if warnings:
        print("Warnings:")
        for w in warnings:
            print(" -", w)


if __name__ == "__main__":
    main()
