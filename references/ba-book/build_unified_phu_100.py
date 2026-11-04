# -*- coding: utf-8 -*-
"""
Unified Mr. Phú Warm-Cream Concept Cover Builder for all 100 Days of '100 ngày làm BA'.
Outputs 100 clean 1200x675 PNGs in f:\\VIETLOTT-SMS\\references\\ba-book\\itba_covers\\phu_unified_100\\
- Zero 'IT BA' / 'ITBA' / 'iTBA Mentor' watermarks or QR codes anywhere.
- Exact #FAEFD3 (RGB 250, 239, 211) warm cream watercolor paper background across all 100 cards.
- Bold #054AA3 Royal Cobalt Blue Montserrat headlines + unique topic-tailored storybook illustrations.
"""
import concurrent.futures
import glob
import html
import json
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(r"f:\VIETLOTT-SMS\references\ba-book")
ORIG_DIR = BASE_DIR / "itbamentor_ref" / "original_covers"
OUT_DIR = BASE_DIR / "itba_covers" / "phu_unified_100"
HTML_DIR = OUT_DIR / "html"
SCRATCH_DIR = Path(r"C:\Users\MyLaptop\.gemini\antigravity\brain\8ea8e18e-a26f-4bc4-909c-659e5ff0e34c\scratch")

OUT_DIR.mkdir(parents=True, exist_ok=True)
HTML_DIR.mkdir(parents=True, exist_ok=True)
SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
EDGE = next(p for p in EDGE_PATHS if Path(p).exists())

sys.path.insert(0, str(BASE_DIR))
from phu_scenes_81 import BESPOKE_DAYS

# Zero original covers copied — all 100/100 days are newly illustrated in unified warm-cream style!
AUTH_CREAM = {}


def patch_paper(img: Image.Image, box: tuple, sample_origin=(25, 18)):
    x1, y1, x2, y2 = box
    bw, bh = x2 - x1, y2 - y1
    sx, sy = sample_origin
    tile = img.crop((sx, sy, sx + 180, sy + 90))
    patch = Image.new("RGB", (bw, bh))
    for py in range(0, bh, 90):
        for px in range(0, bw, 180):
            patch.paste(tile, (px, py))
    mask = Image.new("L", (bw, bh), 255)
    draw = ImageDraw.Draw(mask)
    for inset in range(6):
        alpha = int(255 * (inset + 1) / 6)
        draw.rectangle([inset, inset, bw - 1 - inset, bh - 1 - inset], outline=alpha)
    img.paste(patch, (x1, y1), mask)


def patch_shirt_text(img: Image.Image, box: tuple):
    x1, y1, x2, y2 = box
    px = img.load()
    bw, bh = x2 - x1, y2 - y1
    interp = Image.new("RGB", (bw, bh))
    ipx = interp.load()
    for dy in range(bh):
        y = min(img.height - 1, y1 + dy)
        c_left = px[max(0, x1 - 4), y]
        c_right = px[min(img.width - 1, x2 + 4), y]
        for dx in range(bw):
            t = dx / max(1, bw - 1)
            ipx[dx, dy] = (
                int(c_left[0] * (1 - t) + c_right[0] * t),
                int(c_left[1] * (1 - t) + c_right[1] * t),
                int(c_left[2] * (1 - t) + c_right[2] * t),
            )
    interp = interp.filter(ImageFilter.GaussianBlur(radius=4))
    mask = Image.new("L", (bw, bh), 0)
    ImageDraw.Draw(mask).rounded_rectangle([3, 3, bw - 4, bh - 4], radius=10, fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=3))
    img.paste(interp, (x1, y1), mask)


def reframe_to_1200x675(img: Image.Image) -> Image.Image:
    w, h = img.size
    top_trim = 18
    cropped_src = img.crop((0, top_trim, w, h))
    cw, ch = cropped_src.size
    scale = 675.0 / ch
    nw = int(round(cw * scale))
    nh = 675
    resized = cropped_src.resize((nw, nh), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (1200, 675))
    cpx = canvas.load()
    rpx = resized.load()
    left_x = (1200 - nw) // 2
    base_paper = rpx[15, 15]

    def pick_paper(samples):
        valid = [s for s in samples if s[0] > 225 and s[1] > 215 and s[2] > 185]
        if valid:
            return (
                sum(s[0] for s in valid) // len(valid),
                sum(s[1] for s in valid) // len(valid),
                sum(s[2] for s in valid) // len(valid),
            )
        return base_paper

    for y in range(nh):
        lc = pick_paper([rpx[x, y] for x in range(4, 20)])
        rc = pick_paper([rpx[nw - 1 - x, y] for x in range(4, 20)])
        for x in range(left_x + 16):
            cpx[x, y] = lc
        for x in range(left_x + nw - 16, 1200):
            cpx[x, y] = rc

    mask = Image.new("L", (nw, nh), 255)
    mp = mask.load()
    for y in range(nh):
        for dx in range(18):
            alpha = int(255 * (dx + 1) / 18)
            lp = rpx[dx, y]
            if lp[0] > 225 and lp[1] > 215:
                mp[dx, y] = alpha
            rp = rpx[nw - 1 - dx, y]
            if rp[0] > 225 and rp[1] > 215:
                mp[nw - 1 - dx, y] = alpha

    canvas.paste(resized, (left_x, 0), mask)
    return canvas


def build_bespoke_html(day: int, layout: str, lines: list, svg_markup: str) -> str:
    max_len = max(len(l) for l in lines)
    if layout == "top_center":
        if len(lines) == 1:
            fsize = "44px" if max_len <= 34 else "38px"
        elif len(lines) == 2:
            fsize = "40px" if max_len <= 32 else ("36px" if max_len <= 42 else "32px")
        else:
            fsize = "33px"
        title_html = "<br>".join(html.escape(l) for l in lines)
        body_inner = f"""
        <div class="card layout-top">
          <div class="headline-top">{title_html}</div>
          <div class="scene-bottom">{svg_markup}</div>
        </div>
        """
    elif layout == "split_left":
        fsize = "40px" if max_len <= 24 else ("36px" if max_len <= 30 else "32px")
        title_html = "<br>".join(html.escape(l) for l in lines)
        body_inner = f"""
        <div class="card layout-split">
          <div class="headline-side left">{title_html}</div>
          <div class="scene-side">{svg_markup}</div>
        </div>
        """
    else:  # split_right
        fsize = "40px" if max_len <= 24 else ("36px" if max_len <= 30 else "32px")
        title_html = "<br>".join(html.escape(l) for l in lines)
        body_inner = f"""
        <div class="card layout-split">
          <div class="scene-side">{svg_markup}</div>
          <div class="headline-side right">{title_html}</div>
        </div>
        """

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@font-face {{
  font-family: 'MontserratLocal';
  src: local('Montserrat Bold'), url('file:///C:/Windows/Fonts/Montserrat-Bold.ttf') format('truetype');
  font-weight: 800;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1200px;
  height: 675px;
  overflow: hidden;
  background: #FAEFD3;
  font-family: 'MontserratLocal', 'Montserrat', 'Segoe UI', sans-serif;
}}
.card {{
  width: 1200px;
  height: 675px;
  position: relative;
  background: radial-gradient(circle at 50% 45%, #FBF2DA 0%, #FAEFD3 70%, #F8EBD0 100%);
}}
/* Subtle warm paper grain overlay */
.card::before {{
  content: "";
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(139, 105, 60, 0.045) 1px, transparent 0);
  background-size: 18px 18px;
  pointer-events: none;
}}
.layout-top {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 46px 64px 0 64px;
}}
.headline-top {{
  text-align: center;
  color: #054AA3;
  font-size: {fsize};
  font-weight: 800;
  -webkit-text-stroke: 0.55px #054AA3;
  line-height: 1.32;
  letter-spacing: -0.2px;
  z-index: 2;
}}
.scene-bottom {{
  flex: 1;
  width: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  overflow: hidden;
  z-index: 1;
}}
.scene-bottom svg {{
  max-width: 900px;
  max-height: 468px;
  width: auto;
  height: auto;
  display: block;
}}
.layout-split {{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 32px 68px 0 68px;
  gap: 24px;
}}
.headline-side {{
  flex: 0 0 510px;
  color: #054AA3;
  font-size: {fsize};
  font-weight: 800;
  -webkit-text-stroke: 0.55px #054AA3;
  line-height: 1.36;
  padding-bottom: 36px;
  z-index: 2;
}}
.headline-side.left {{ text-align: left; }}
.headline-side.right {{ text-align: left; }}
.scene-side {{
  flex: 1;
  height: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  z-index: 1;
}}
.scene-side svg {{
  max-width: 560px;
  max-height: 545px;
  width: auto;
  height: auto;
  display: block;
}}
</style>
</head>
<body>
{body_inner}
</body>
</html>
"""


def process_single_day(day: int):
    out_png = OUT_DIR / f"day_{day:03d}_cover.png"

    if day in AUTH_CREAM:
        fname, cfg = AUTH_CREAM[day]
        im = Image.open(ORIG_DIR / fname).convert("RGB")
        # 1. Remove top-right iTBA Mentor logo cleanly
        patch_paper(im, (660, 4, 938, 120), sample_origin=(28, 16))
        # 2. Remove QR / SUBSCRIBE
        qr = cfg.get("qr")
        if qr == "bl":
            patch_paper(im, (4, 520, 348, 786), sample_origin=(28, 16))
        elif qr == "br":
            patch_paper(im, (635, 520, 938, 786), sample_origin=(28, 16))
        elif qr == "br_day5":
            patch_paper(im, (555, 535, 938, 786), sample_origin=(28, 16))
        # 3. Remove shirt watermark
        if cfg.get("shirt"):
            patch_shirt_text(im, cfg["shirt"])
        # 4. Fix Day 11 title
        if cfg.get("retitle"):
            patch_paper(im, (60, 135, 880, 355), sample_origin=(28, 16))
            font_t = ImageFont.truetype(r"C:\Windows\Fonts\Montserrat-Bold.ttf", 46)
            d = ImageDraw.Draw(im)
            l1, l2 = cfg["retitle"]
            b1 = d.textbbox((0, 0), l1, font=font_t)
            b2 = d.textbbox((0, 0), l2, font=font_t)
            d.text(((940 - (b1[2] - b1[0])) // 2, 165), l1, font=font_t, fill=(5, 74, 163), stroke_width=1, stroke_fill=(5, 74, 163))
            d.text(((940 - (b2[2] - b2[0])) // 2, 232), l2, font=font_t, fill=(5, 74, 163), stroke_width=1, stroke_fill=(5, 74, 163))

        final_im = reframe_to_1200x675(im)
        final_im.save(out_png, "PNG")
        return day, "authentic_cleaned", out_png.stat().st_size

    # Bespoke Warm-Cream Storybook Card
    layout, lines, arch_fn, scene_cfg = BESPOKE_DAYS[day]
    svg_markup = arch_fn(scene_cfg)
    html_str = build_bespoke_html(day, layout, lines, svg_markup)
    html_file = HTML_DIR / f"day_{day:03d}.html"
    html_file.write_text(html_str, encoding="utf-8")

    cmd = [
        EDGE,
        "--headless",
        "--disable-gpu",
        "--force-device-scale-factor=1",
        "--window-size=1200,675",
        f"--screenshot={out_png}",
        str(html_file),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return day, "bespoke_phu_cream", out_png.stat().st_size


def make_gallery_sheet(days_list: list, out_name: str):
    cols = 4
    rows = (len(days_list) + cols - 1) // cols
    cw, ch = 420, 275
    sheet = Image.new("RGB", (cols * cw + 20, rows * ch + 20), (245, 245, 247))
    draw = ImageDraw.Draw(sheet)
    for idx, d in enumerate(days_list):
        r, c = divmod(idx, cols)
        x0, y0 = 15 + c * cw, 15 + r * ch
        draw.rounded_rectangle([x0, y0, x0 + 402, y0 + 258], radius=12, fill=(255, 255, 255), outline=(225, 225, 228))
        p = OUT_DIR / f"day_{d:03d}_cover.png"
        thumb = Image.open(p).convert("RGB").resize((400, 225), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (x0 + 1, y0 + 1))
        tag = "AUTH" if d in AUTH_CREAM else "CUSTOM"
        draw.text((x0 + 12, y0 + 234), f"[Day {d}/100] ({tag})", fill=(40, 40, 45))
    sp = SCRATCH_DIR / out_name
    sheet.save(sp, "PNG")
    print(f"Saved preview sheet: {sp}")


if __name__ == "__main__":
    print("Rendering all 100 unified warm-cream Mr. Phú concept covers...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(process_single_day, range(1, 101)))

    auth_n = sum(1 for _, kind, _ in results if kind == "authentic_cleaned")
    besp_n = sum(1 for _, kind, _ in results if kind == "bespoke_phu_cream")
    min_sz = min(sz for _, _, sz in results)
    print(f"Done! Total={len(results)} (Authentic cleaned={auth_n}, Bespoke Phu concept={besp_n}), min_size={min_sz} bytes")

    # Update cover_png paths in all 20 chunk JSON files
    for cf in sorted(glob.glob(str(BASE_DIR / "extracted" / "blog_update_chunks" / "blog_chunk_*.json"))):
        with open(cf, "r", encoding="utf-8") as f:
            items = json.load(f)
        for it in items:
            it["cover_png"] = str(OUT_DIR / f"day_{it['day']:03d}_cover.png")
        with open(cf, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
    print("Updated cover_png paths in all 20 blog_chunk_*.json files.")

    # Generate Notion Gallery simulation preview sheets
    make_gallery_sheet([4, 5, 7, 8, 9, 11, 13, 15, 16, 21, 22, 23, 24, 25, 1, 2], "verify_auth_and_early.png")
    make_gallery_sheet(list(range(21, 37)), "verify_days_21_to_36.png")
    make_gallery_sheet([47, 49, 50, 56, 61, 64, 69, 72, 80, 82, 86, 90, 93, 98, 99, 100], "verify_highlights_47_to_100.png")
