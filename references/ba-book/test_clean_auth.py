# -*- coding: utf-8 -*-
"""
Clean and reframe the 19 warm-cream authentic Mr. Phú covers to 1200x675:
- Remove top-right 'iTBA Mentor' logo using clean paper texture sampled from the same image
- Remove bottom-left / bottom-right QR & SUBSCRIBE blocks using clean paper texture
- Remove tiny 'ITBA MENTOR' shirt text on Days 4, 5, 22, 23 using local shirt color median/patch
- Fix Day 11 title ("Khi BA gật đầu vì ngại hỏi lại") so it matches Day 11's book article
- Reframe 940x788 onto 1200x675 warm cream canvas seamlessly so ZERO character faces are cropped off!
"""
import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.stdout.reconfigure(encoding="utf-8")

ORIG_DIR = Path(r"f:\VIETLOTT-SMS\references\ba-book\itbamentor_ref\original_covers")
TEST_OUT = Path(r"C:\Users\MyLaptop\.gemini\antigravity\brain\8ea8e18e-a26f-4bc4-909c-659e5ff0e34c\scratch\auth_cleaned")
TEST_OUT.mkdir(parents=True, exist_ok=True)

AUTH_CREAM = {
    4: ("1cdd4f15_Day 4100  3 kỹ thuật BABOK giúp bạn xử l.png", {"qr": None, "shirt": (690, 680, 845, 760)}),
    5: ("1ced4f15_Day 5100.png", {"qr": "br_large", "shirt": (115, 625, 255, 695)}),
    7: ("1e5d4f15_Day 7100 3 kỹ thuật BABOK giúp BA đo lườ.png", {"qr": "br"}),
    8: ("1e5d4f15_Day 8100  Học gì để lên Senior BA.png", {"qr": "br"}),
    9: ("1e5d4f15_Day 9100 3 kỹ thuật BABOK giúp bạn tránh.png", {"qr": "bl"}),
    10: ("1e5d4f15_Day 10100 PO tự vẽ UIUX rồi bảo BA check.png", {"qr": None}),
    11: ("1e5d4f15_Day 11100 Khi BA gật đầu vì ngại hỏi lại.png", {"qr": None, "retitle": ("Khi BA gật đầu", "vì ngại hỏi lại")}),
    13: ("1e5d4f15_Day 12100 Data Object  Bí kíp phân tích .png", {"qr": "bl"}),
    14: ("1e5d4f15_Day 13100 3 dạng comment dễ khiến BA rơi.png", {"qr": "bl"}),
    15: ("1e5d4f15_Day 14100 BA không biết gốc  chỉ chăm ch.png", {"qr": "bl"}),
    16: ("1e5d4f15_Day 15100 BA không biết gốc  chỉ chăm ch.png", {"qr": "bl"}),
    18: ("1e5d4f15_Cuối tuần rồi chắc thể nào cũng có team .png", {"qr": None}),
    19: ("1e5d4f15_Day 18100 Một ngày họp 6 tiếng  còn đâu .png", {"qr": None}),
    20: ("1e5d4f15_Day 19100 Không xem kỹ hệ thống hiện tại.png", {"qr": None}),
    21: ("1e5d4f15_Day 20100 BA kiêm PM  tưởng được nâng tầ.png", {"qr": None}),
    22: ("1e5d4f15_Day 21100 Tính năng chỉ thêm 1 dòng thôi.png", {"qr": None, "shirt": (500, 620, 615, 705)}),
    23: ("1e5d4f15_Day 22100 Domain-Driven Design DDD là gì.png", {"qr": None, "shirt": (735, 625, 845, 705)}),
    24: ("1e5d4f15_Day 23100.png", {"qr": None}),
    25: ("1e7d4f15_Day 24100 Hidden Requirement  Khi quy tắ.png", {"qr": None}),
}


def patch_paper(img: Image.Image, box: tuple, sample_origin=(25, 20)):
    """Fill `box` (x1, y1, x2, y2) with tiled clean paper texture from `sample_origin` with feathered border."""
    x1, y1, x2, y2 = box
    bw, bh = x2 - x1, y2 - y1
    sx, sy = sample_origin
    tile = img.crop((sx, sy, sx + 180, sy + 90))
    patch = Image.new("RGB", (bw, bh))
    for py in range(0, bh, 90):
        for px in range(0, bw, 180):
            patch.paste(tile, (px, py))
    mask = Image.new("L", (bw, bh), 255)
    # Feather 6px border
    draw = ImageDraw.Draw(mask)
    for inset in range(6):
        alpha = int(255 * (inset + 1) / 6)
        draw.rectangle([inset, inset, bw - 1 - inset, bh - 1 - inset], outline=alpha)
    img.paste(patch, (x1, y1), mask)


def patch_shirt_text(img: Image.Image, box: tuple):
    """Smoothly inpaint text on shirt by row-wise interpolation between clean left/right/top shirt fabric."""
    x1, y1, x2, y2 = box
    px = img.load()
    # Create smooth horizontal + vertical blend from border pixels of box
    bw, bh = x2 - x1, y2 - y1
    sub = img.crop((x1 - 12, y1 - 12, x2 + 12, y2 + 12)).filter(ImageFilter.MedianFilter(size=9)).filter(ImageFilter.GaussianBlur(radius=6))
    # Also blend left-to-right clean fabric samples
    interp = Image.new("RGB", (bw, bh))
    ipx = interp.load()
    for dy in range(bh):
        y = y1 + dy
        c_left = px[max(0, x1 - 4), y]
        c_right = px[min(img.width - 1, x2 + 4), y]
        for dx in range(bw):
            t = dx / max(1, bw - 1)
            r = int(c_left[0] * (1 - t) + c_right[0] * t)
            g = int(c_left[1] * (1 - t) + c_right[1] * t)
            b = int(c_left[2] * (1 - t) + c_right[2] * t)
            ipx[dx, dy] = (r, g, b)
    interp = interp.filter(ImageFilter.GaussianBlur(radius=4))
    mask = Image.new("L", (bw, bh), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle([4, 4, bw - 5, bh - 5], radius=12, fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=4))
    img.paste(interp, (x1, y1), mask)


def reframe_to_1200x675(img: Image.Image) -> Image.Image:
    """Place cleaned 940x788 card seamlessly onto 1200x675 warm cream canvas without cutting off characters."""
    w, h = img.size
    # Trim excess top cream margin (e.g., 28px) so character + title sit at optimal large scale
    top_trim = 24
    cropped_src = img.crop((0, top_trim, w, h))
    cw, ch = cropped_src.size  # 940 x 764
    scale = 675.0 / ch  # ~0.8835
    nw = int(round(cw * scale))  # ~830
    nh = 675
    resized = cropped_src.resize((nw, nh), Image.Resampling.LANCZOS)

    # Build 1200x675 background matching exact row-by-row edge paper colors of resized image!
    canvas = Image.new("RGB", (1200, 675))
    cpx = canvas.load()
    rpx = resized.load()
    left_x = (1200 - nw) // 2

    # Sample clean edge strips (12px inside left and right edges, avoiding any bottom corner artifacts)
    for y in range(nh):
        # Average 8 pixels near left edge and right edge (if near paper color)
        l_samples = [rpx[x, y] for x in range(4, 20)]
        r_samples = [rpx[nw - 1 - x, y] for x in range(4, 20)]
        # Use top-left paper color if bottom edge has character shoulder touching edge
        def pick_paper(samples, fallback):
            valid = [s for s in samples if s[0] > 225 and s[1] > 215 and s[2] > 185]
            if valid:
                return (
                    sum(s[0] for s in valid) // len(valid),
                    sum(s[1] for s in valid) // len(valid),
                    sum(s[2] for s in valid) // len(valid),
                )
            return fallback

        base_paper = rpx[15, 15]
        lc = pick_paper(l_samples, base_paper)
        rc = pick_paper(r_samples, base_paper)
        for x in range(left_x + 16):
            cpx[x, y] = lc
        for x in range(left_x + nw - 16, 1200):
            cpx[x, y] = rc

    # Paste resized in center with soft 18px horizontal edge feather only where edge is paper-colored
    mask = Image.new("L", (nw, nh), 255)
    mp = mask.load()
    for y in range(nh):
        for dx in range(18):
            alpha = int(255 * (dx + 1) / 18)
            # Only feather if pixel is paper-like so character shoulders touching right edge stay crisp!
            lp = rpx[dx, y]
            if lp[0] > 225 and lp[1] > 215:
                mp[dx, y] = alpha
            rp = rpx[nw - 1 - dx, y]
            if rp[0] > 225 and rp[1] > 215:
                mp[nw - 1 - dx, y] = alpha

    canvas.paste(resized, (left_x, 0), mask)
    return canvas


font_title = ImageFont.truetype(r"C:\Windows\Fonts\Montserrat-Bold.ttf", 40)

rendered = []
for day, (fname, cfg) in sorted(AUTH_CREAM.items()):
    im = Image.open(ORIG_DIR / fname).convert("RGB")
    # 1. Always remove top-right iTBA Mentor logo (x: 700..936, y: 12..95)
    patch_paper(im, (700, 12, 936, 95), sample_origin=(30, 18))

    # 2. Remove QR / SUBSCRIBE if present
    qr = cfg.get("qr")
    if qr == "bl":
        patch_paper(im, (8, 520, 295, 785), sample_origin=(30, 18))
    elif qr == "br":
        patch_paper(im, (640, 520, 936, 785), sample_origin=(30, 18))
    elif qr == "br_large":
        patch_paper(im, (560, 495, 936, 785), sample_origin=(30, 18))

    # 3. Remove shirt text if present
    if cfg.get("shirt"):
        patch_shirt_text(im, cfg["shirt"])

    # 4. Retitle Day 11 if configured
    if cfg.get("retitle"):
        patch_paper(im, (80, 140, 860, 325), sample_origin=(30, 18))
        d = ImageDraw.Draw(im)
        l1, l2 = cfg["retitle"]
        b1 = d.textbbox((0, 0), l1, font=font_title)
        b2 = d.textbbox((0, 0), l2, font=font_title)
        d.text(((940 - (b1[2] - b1[0])) // 2, 165), l1, font=font_title, fill=(6, 78, 168))
        d.text(((940 - (b2[2] - b2[0])) // 2, 225), l2, font=font_title, fill=(6, 78, 168))

    out_im = reframe_to_1200x675(im)
    out_p = TEST_OUT / f"day_{day:03d}_cover.png"
    out_im.save(out_p, "PNG")
    rendered.append((day, out_im))

# Build contact sheet of all 19 cleaned authentic covers
cols = 4
rows = (len(rendered) + cols - 1) // cols
cw, ch = 420, 265
sheet = Image.new("RGB", (cols * cw, rows * ch), (50, 50, 50))
sdraw = ImageDraw.Draw(sheet)
for idx, (day, im) in enumerate(rendered):
    r, c = divmod(idx, cols)
    thumb = im.resize((400, 225), Image.Resampling.LANCZOS)
    sheet.paste(thumb, (c * cw + 10, r * ch + 30))
    sdraw.text((c * cw + 12, r * ch + 8), f"Day {day:02d} (Cleaned 1200x675)", fill=(255, 255, 255))

sheet_path = TEST_OUT / "cleaned_auth_sheet.png"
sheet.save(sheet_path, "PNG")
print(f"Saved {len(rendered)} cleaned authentic covers + {sheet_path}")
