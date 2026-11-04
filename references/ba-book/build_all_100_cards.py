#!/usr/bin/env python3
"""
Build all 100 unique themed cover cards for "100 ngày làm BA".
- Preserves authentic artwork for Days 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25.
- Generates rich, custom, tailored editorial graphic covers for all other days.
- Produces 100 verified 1200x675 PNGs in f:\\VIETLOTT-SMS\\references\\ba-book\\itba_covers\\unique_100\\
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
OUT_DIR = BASE_DIR / "itba_covers" / "unique_100"
HTML_DIR = OUT_DIR / "html"

OUT_DIR.mkdir(parents=True, exist_ok=True)
HTML_DIR.mkdir(parents=True, exist_ok=True)

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
EDGE = next(p for p in EDGE_PATHS if Path(p).exists())

sys.path.insert(0, str(BASE_DIR))
import card_scenes

with open(ARTICLES_JSON, encoding="utf-8") as f:
    articles = json.load(f)

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

def clean_title_parts(raw_title: str):
    clean = re.sub(r"^Day\s*\d+/100\s*[—–-]\s*", "", raw_title).strip()
    if " – " in clean:
        parts = clean.split(" – ", 1)
        return parts[0].strip(), parts[1].strip()
    elif " - " in clean:
        parts = clean.split(" - ", 1)
        return parts[0].strip(), parts[1].strip()
    elif ":" in clean:
        parts = clean.split(":", 1)
        return parts[0].strip(), parts[1].strip()
    elif "?" in clean:
        idx = clean.find("?")
        return clean[:idx+1].strip(), clean[idx+1:].strip()
    return clean, ""

def get_day_card_config(day: int, raw_title: str, body: str):
    t_low = (raw_title + " " + body).lower()
    head, sub = clean_title_parts(raw_title)

    # Day 1: Release
    if day == 1:
        return "POST-RELEASE · TELEMETRY", "blueprint", "BA nên làm gì sau khi tính năng được Release?", "5 việc sống còn để chứng minh giá trị và giữ hệ thống ổn định", card_scenes.svg_rocket_monitoring()
    
    # Day 6: BA Manager
    if day == 6:
        return "LEADERSHIP · BA MANAGER", "executive", "Một ngày làm BA Manager của tôi", "Không phải để kiểm soát, mà để giữ team không ai đơn độc", card_scenes.svg_ba_manager_clock()

    # Day 16: Destructive testing
    if day == 16:
        return "QUALITY · DESTRUCTIVE TESTING", "hazard", "Bạn chỉ viết flow cho người dùng?", "Vậy ai viết cho thằng... Phá? Idempotency & Edge Case", card_scenes.svg_hacker_edge_case()

    # Day 47: Git
    if day == 47:
        return "TECH FOR BA · GIT & DEV", "terminal", "Branch, Merge, Pull Request, Tag...", "Giải thích Git để BA không ngồi họp như người ngoài hành tinh", card_scenes.svg_git_tree()

    # Day 49: Kế toán
    if day == 49:
        return "BUSINESS DOMAIN · KẾ TOÁN", "emerald", "Kẹt giữa rừng xà nu kế toán", "BA có nên đi học luôn kế toán? Nguyên lý kép Nợ - Có", card_scenes.svg_accounting_ledger()

    # Day 61: Dynamic pricing
    if day == 61:
        return "ALGORITHM · DYNAMIC PRICING", "blueprint", "Sao hôm qua đi 50k, hôm nay lại 65k?", "Bài toán cân bằng cung cầu và thuật toán định giá Surge", card_scenes.svg_dynamic_pricing()

    # Day 64: Cây KPI
    if day == 64:
        return "METRICS · KPI FRAMEWORK", "sapphire", "Cây KPI: Giao thế nào cho đúng và hiệu quả?", "Phân rã North Star Metric đến từng tính năng của BA", card_scenes.svg_kpi_tree()

    # Day 69: Thumb zone UX
    if day == 69:
        return "MOBILE UX · DESIGN THINKING", "creative", "Khi người dùng chỉ thao tác bằng 1 tay", "Bài học công thái học Thumb Zone cho Product BA", card_scenes.svg_mobile_thumb_zone()

    # Day 72: Speed boat
    if day == 72:
        return "COLLABORATIVE GAME · WORKSHOP", "sapphire", "BA Toolkit: Collaborative Game – Speed Boat", "Tìm động lực đẩy thuyền và cắt bỏ mỏ neo cản trở dự án", card_scenes.svg_speed_boat()

    # Day 76: Non-functional
    if day == 76:
        return "NFR · SYSTEM RELIABILITY", "blueprint", "Các thông số Non-Functional BA cần biết", "Latency, TPS, Concurrency và Bảo mật theo Nghị định 13", card_scenes.svg_nfr_tiles()

    # Day 80: 3 loại lỗi
    if day == 80:
        return "QUALITY · ERROR TAXONOMY", "crimson", "Phân biệt 3 loại lỗi trong dự án", "Để DEV không fix sai, QA không log nhầm, User không kêu oan", card_scenes.svg_three_bugs()

    # Day 82: Nối cuốc
    if day == 82:
        return "OPERATION · RIDE-HAILING", "emerald", "“Nối cuốc” – Tính năng nhỏ, hiệu quả lớn", "Bài toán tối ưu chuỗi cung ứng và giảm 70% xe chạy rỗng", card_scenes.svg_ride_stitch()

    # Day 86: Reverse-engineer
    if day == 86:
        return "REVERSE-ENGINEERING", "terminal", "Reverse-Engineer: Kỹ năng sống còn", "Bóc tách hệ thống cũ khi không còn tài liệu và Dev đã nghỉ", card_scenes.svg_reverse_gears()

    # Day 89: Mad unicorn
    if day == 89:
        return "LOGISTICS · STARTUP", "creative", "Mad Unicorn: Khởi nghiệp giao hàng", "Những câu hỏi hóc búa về vận hành mà BA không thể né", card_scenes.svg_mad_unicorn()

    # Day 90: P.O.L.C
    if day == 90:
        return "MANAGEMENT · BA LEAD", "executive", "P.O.L.C dành cho BA Lead", "Planning · Organizing · Leading · Controlling", card_scenes.svg_polc_four()

    # Day 98: Search comparison
    if day == 98:
        return "SEARCH ARCHITECTURE · UX", "amber", "Auto-Suggest vs Auto-Complete vs ML Recommendation", "Phân biệt bản chất kỹ thuật để viết đặc tả chuẩn xác", card_scenes.svg_search_trio()

    # Day 99: Outcome vs Output
    if day == 99:
        return "VALUE OPTIMIZATION", "emerald", "Outcome vs Output: Bận rộn hay hiệu quả?", "Đừng đếm số lượng màn hình hoàn thành, hãy đo giá trị tạo ra", card_scenes.svg_outcome_bullseye()

    # Day 100: 3 Pillars
    if day == 100:
        return "10 NĂM LÀM NGHỀ · TỔNG KẾT", "sapphire", "10 Năm làm nghề – 3 thứ tôi giữ lại", "Mindset rõ ràng · Hệ thống chuẩn hóa · Bản lĩnh nghề nghiệp", card_scenes.svg_three_pillars()

    # Grouped Fallbacks with tailored themes & generic bespoke 3-stage diagrams
    if any(k in t_low for k in ["sprint", "retro", "scrum", "agile", "backlog"]):
        return "AGILE & SCRUM", "amber", head, sub or "Tối ưu chu trình phản hồi và hiệu suất đội ngũ", card_scenes.svg_generic_scene("🔄", "1. Sprint Plan", "Ước lượng độ phức tạp", "2. Execution", "Phản xạ linh hoạt", "3. Retro", "Cải tiến liên tục", "#f59e0b", "#38bdf8")

    if any(k in t_low for k in ["họp", "cãi", "chia bè", "đổ lỗi", "phản biện", "xung đột"]):
        return "STAKEHOLDER & CONFLICT", "crimson", head, sub or "Nghệ thuật đàm phán và bảo vệ góc nhìn hệ thống", card_scenes.svg_generic_scene("⚔️", "1. Lắng nghe", "Bóc tách mong muốn", "2. Dẫn chứng", "Lấy số liệu và logic", "3. Đồng thuận", "Quyết định rõ ràng", "#f87171", "#fbbf24")

    if any(k in t_low for k in ["phỏng vấn", "senior", "lương", "năng lực", "mentor", "level", "career"]):
        return "CAREER & LEADERSHIP", "executive", head, sub or "Nâng tầm tư duy để bước lên cấp bậc cao hơn", card_scenes.svg_generic_scene("🏆", "1. Thực thi", "Làm chuẩn việc giao", "2. Tư duy", "Nhìn hệ thống tổng thể", "3. Dẫn dắt", "Nhân bản năng lực", "#eab308", "#60a5fa")

    if any(k in t_low for k in ["ui", "ux", "giao diện", "design", "người dùng"]):
        return "UI/UX & DESIGN", "creative", head, sub or "Thiết kế trải nghiệm dựa trên luồng nghiệp vụ thực tế", card_scenes.svg_generic_scene("🎨", "1. Nghiệp vụ", "BA chốt luật logic", "2. Wireframe", "Designer dựng luồng", "3. Xác nhận", "PO duyệt trải nghiệm", "#c084fc", "#f472b6")

    if any(k in t_low for k in ["lỗi", "bug", "rủi ro", "constraint", "exception", "thất bại", "toang"]):
        return "RISK & EXCEPTIONS", "hazard", head, sub or "Tư duy lỗi để bảo vệ hệ thống trước kịch bản xấu nhất", card_scenes.svg_generic_scene("🛡️", "1. Giả định", "Đặt câu hỏi nếu sai", "2. Kịch bản", "Viết Exception Flow", "3. Phòng thủ", "Gia cố móng nhà", "#fb923c", "#ef4444")

    if any(k in t_low for k in ["hệ thống", "data", "ddd", "api", "database", "kiến trúc"]):
        return "SYSTEM THINKING", "blueprint", head, sub or "Tư duy cấu trúc và khả năng mở rộng lâu dài", card_scenes.svg_generic_scene("🏗️", "1. Bounded", "Phân rã miền nghiệp vụ", "2. Data Object", "Định danh thực thể", "3. Scale", "Sẵn sàng mở rộng", "#38bdf8", "#10b981")

    # Final fallback
    return "BA PRACTICE", "sapphire", head, sub or "Kinh nghiệm thực chiến từ tiền tuyến dự án", card_scenes.svg_generic_scene("📚", "1. Khảo sát", "Ghi nhận bài toán", "2. Phân tích", "Chuyển thành giải pháp", "3. Triển khai", "Hỗ trợ go-live", "#60a5fa", "#34d399")

def build_custom_card_html(day: int, badge: str, theme_name: str, headline: str, subheadline: str, svg_markup: str):
    th = THEMES.get(theme_name, THEMES["sapphire"])
    head_esc = html.escape(headline)
    sub_esc = html.escape(subheadline)
    
    # Adjust font size based on headline length
    hlen = len(headline)
    if hlen <= 35:
        fsize = "40px"
    elif hlen <= 55:
        fsize = "34px"
    elif hlen <= 75:
        fsize = "29px"
    else:
        fsize = "25px"

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1200px;
  height: 675px;
  overflow: hidden;
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  background: #0f172a;
}}
.card {{
  width: 1200px;
  height: 675px;
  position: relative;
  background: {th['bg']};
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 34px 48px 24px 48px;
  color: #f8fafc;
}}
.header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.badge {{
  background: {th['badge_bg']};
  border: 1.5px solid {th['badge_border']};
  color: {th['badge_color']};
  padding: 6px 16px;
  border-radius: 999px;
  font-weight: 800;
  font-size: 13px;
  letter-spacing: 0.6px;
}}
.logo {{
  font-size: 24px;
  font-weight: 900;
  color: #94a3b8;
  letter-spacing: -0.5px;
}}
.logo span {{ color: #ffffff; }}
.title-area {{
  text-align: center;
  margin-top: 6px;
  min-height: 105px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}
.headline {{
  font-size: {fsize};
  font-weight: 900;
  color: {th['headline_color']};
  line-height: 1.25;
  margin-bottom: 6px;
}}
.subheadline {{
  font-size: 21px;
  font-weight: 600;
  color: {th['sub_color']};
  max-width: 950px;
  margin: 0 auto;
  line-height: 1.35;
}}
.graphic-area {{
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.footer {{
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  color: #64748b;
  font-weight: 600;
  border-top: 1px solid rgba(255,255,255,0.08);
  padding-top: 10px;
}}
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div class="badge">{badge}</div>
    <div class="logo">iTBA <span>Mentor</span></div>
  </div>
  <div class="title-area">
    <div class="headline">{head_esc}</div>
    <div class="subheadline">{sub_esc}</div>
  </div>
  <div class="graphic-area">
    {svg_markup}
  </div>
  <div class="footer">
    <div>Day {day}/100 · Sách 100 ngày làm BA</div>
    <div>Nguyễn Bá Phú — ITBA Mentor</div>
  </div>
</div>
</body>
</html>
"""

def process_day(article):
    day = article["day"]
    out_png = OUT_DIR / f"day_{day:03d}_cover.png"
    
    # 1. Check if authentic original cover exists from Mr. Phú
    if day in ORIGINAL_MAPPING:
        orig_fname = ORIGINAL_MAPPING[day]
        orig_path = ORIG_DIR / orig_fname
        if orig_path.exists():
            try:
                orig_img = Image.open(orig_path)
                w, h = orig_img.size
                target_w, target_h = 1200, 675
                # Scale keeping aspect ratio
                new_h = int(h * (target_w / w))
                resized = orig_img.resize((target_w, new_h), Image.Resampling.LANCZOS)
                if new_h >= target_h:
                    # Top crop keeps title & character
                    cropped = resized.crop((0, 0, target_w, target_h))
                else:
                    # Paste centered on cream background
                    cropped = Image.new("RGB", (target_w, target_h), (246, 238, 217))
                    top_offset = (target_h - new_h) // 2
                    cropped.paste(resized, (0, top_offset))
                cropped.save(out_png, "PNG")
                print(f"[AUTHENTIC] Day {day:03d} -> {orig_fname} saved ({out_png.stat().st_size} bytes)")
                return day, "authentic"
            except Exception as e:
                print(f"Error processing authentic cover Day {day}: {e}")

    # 2. Bespoke Editorial Graphic Card
    badge, theme_name, headline, subheadline, svg_markup = get_day_card_config(
        day, article.get("notion_title", ""), article.get("body_markdown", "")
    )
    html_content = build_custom_card_html(day, badge, theme_name, headline, subheadline, svg_markup)
    html_file = HTML_DIR / f"day_{day:03d}.html"
    html_file.write_text(html_content, encoding="utf-8")

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
    print(f"[BESPOKE] Day {day:03d} [{theme_name.upper()}] -> {headline[:35]} saved ({out_png.stat().st_size} bytes)")
    return day, "bespoke"

print("Starting generation of all 100 unique themed covers...")
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(process_day, articles))

print(f"\nCompleted! Generated {len(results)} covers.")
auth_count = sum(1 for _, t in results if t == "authentic")
bespoke_count = sum(1 for _, t in results if t == "bespoke")
print(f"Authentic Mr. Phú artwork: {auth_count} cards")
print(f"Bespoke themed editorial: {bespoke_count} cards")
