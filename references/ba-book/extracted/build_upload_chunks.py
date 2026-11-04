#!/usr/bin/env python3
"""Generate 15 pure UTF-8 Notion upload chunks (Days 2..100) from articles_100.json."""
import json
import re
from pathlib import Path

BASE = Path(r"f:\VIETLOTT-SMS\references\ba-book\extracted")
OUT_DIR = BASE / "upload_chunks"


def polish_for_notion(md: str) -> str:
    lines = md.splitlines()
    for i in range(len(lines)):
        m = re.match(r"^(\d+)\.\s+\*\*(.+?)\*\*(.*)$", lines[i].strip())
        if m:
            num, bold_txt, rest = m.groups()
            lines[i] = f"**{num}. {bold_txt}**{rest}"

    out = []
    in_fence = False
    strip_list_indent = False
    for line in lines:
        s = line.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        # When bullets immediately follow a non-list paragraph/bold heading with leading spaces,
        # unindent the entire contiguous bullet group so all items stay sibling level-1 bullets!
        if re.match(r"^\s+(\-|\*)\s+", line):
            if strip_list_indent or (out and not re.match(r"^\s*(\-|\*|\d+\.)\s+", out[-1])):
                strip_list_indent = True
                line = line.lstrip()
                s = line.strip()
        elif s != "":
            strip_list_indent = False

        is_list = bool(re.match(r"^(\-|\*|\d+\.)\s+", s))
        is_heading = s.startswith("#")
        if out and out[-1].strip() != "":
            prev_s = out[-1].strip()
            prev_is_list = bool(re.match(r"^(\-|\*|\d+\.)\s+", prev_s))
            prev_is_heading = prev_s.startswith("#")
            if (
                (is_list and not prev_is_list)
                or (not is_list and s != "" and prev_is_list)
                or is_heading
                or prev_is_heading
            ):
                out.append("")
        out.append(line)

    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for old in OUT_DIR.glob("chunk_*.json"):
        old.unlink()

    arts = json.loads((BASE / "articles_100.json").read_text(encoding="utf-8"))
    remaining = arts[1:]  # Day 2 .. 100 (99 articles)
    chunk_size = 7
    chunks = [remaining[i : i + chunk_size] for i in range(0, len(remaining), chunk_size)]

    for idx, ch in enumerate(chunks, 1):
        pages = []
        for a in ch:
            pages.append(
                {
                    "icon": "\U0001f4d8",  # 📘
                    "properties": {
                        "Tiêu đề": a["notion_title"],
                        "Ngày": a["day"],
                        "Day": a["day_label"],
                        "Trang sách": a["page_label"],
                        "Đã đọc": "__NO__",
                    },
                    "content": polish_for_notion(a["notion_content"]),
                }
            )
        lines = ["["]
        for i, item in enumerate(pages):
            comma = "," if i < len(pages) - 1 else ""
            lines.append("  " + json.dumps(item, ensure_ascii=False) + comma)
        lines.append("]")
        txt = "\n".join(lines)
        out_p = OUT_DIR / f"chunk_{idx:02d}.json"
        out_p.write_text(txt, encoding="utf-8")
        print(
            f"{out_p.name}: {len(pages)} pages "
            f"(Day {ch[0]['day']}..{ch[-1]['day']}), {len(txt.encode('utf-8'))} bytes"
        )


if __name__ == "__main__":
    main()
