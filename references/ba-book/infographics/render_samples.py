#!/usr/bin/env python3
"""Render high-resolution @2x Retina BA Infographics for Day 1 and Day 2 using Headless Edge + Pillow trim."""
import subprocess
from pathlib import Path
from PIL import Image, ImageChops

OUT_DIR = Path(r"f:\VIETLOTT-SMS\references\ba-book\infographics")
OUT_DIR.mkdir(parents=True, exist_ok=True)

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
EDGE = next(p for p in EDGE_PATHS if Path(p).exists())

COMMON_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: #EEF2F6;
  font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
  color: #0F172A;
  width: 1200px;
  padding: 0;
  margin: 0;
  -webkit-font-smoothing: antialiased;
}
.canvas {
  width: 1200px;
  background: linear-gradient(145deg, #FFFFFF 0%, #F8FAFC 100%);
  padding: 38px 44px 34px 44px;
  position: relative;
  overflow: hidden;
  border-bottom: 6px solid #1E40AF;
}
.bg-orb-1 {
  position: absolute; top: -120px; right: -100px;
  width: 380px; height: 380px; border-radius: 50%;
  background: radial-gradient(circle, rgba(59,130,246,0.10) 0%, rgba(59,130,246,0) 70%);
  pointer-events: none;
}
.bg-orb-2 {
  position: absolute; bottom: -140px; left: -100px;
  width: 420px; height: 420px; border-radius: 50%;
  background: radial-gradient(circle, rgba(16,185,129,0.08) 0%, rgba(16,185,129,0) 70%);
  pointer-events: none;
}
.topbar {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 14px;
}
.badge {
  display: inline-flex; align-items: center; gap: 8px;
  background: #EFF6FF; color: #1D4ED8; border: 1px solid #BFDBFE;
  padding: 6px 14px; border-radius: 999px;
  font-size: 13px; font-weight: 700; letter-spacing: 0.6px; text-transform: uppercase;
}
.brand {
  font-size: 13px; font-weight: 600; color: #64748B; letter-spacing: 0.4px;
}
h1.title {
  font-size: 29px; font-weight: 800; line-height: 1.25; color: #0F172A;
  margin-bottom: 18px; letter-spacing: -0.3px;
}
h1.title span.accent { color: #1D4ED8; }
.footer-bar {
  margin-top: 22px;
  background: linear-gradient(90deg, #0F172A 0%, #1E293B 100%);
  color: #F8FAFC;
  border-radius: 14px;
  padding: 15px 22px;
  display: flex; align-items: center; justify-content: space-between; gap: 18px;
}
.footer-left {
  display: flex; align-items: center; gap: 12px;
  font-size: 15px; font-weight: 600; line-height: 1.4;
}
.footer-pill {
  background: rgba(56, 189, 248, 0.16);
  border: 1px solid rgba(56, 189, 248, 0.35);
  color: #7DD3FC;
  padding: 6px 14px; border-radius: 999px;
  font-size: 13px; font-weight: 700; white-space: nowrap;
}
"""

DAY1_HTML = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
{COMMON_CSS}
.mindset-strip {{
  display: grid; grid-template-columns: 1fr 1fr; gap: 16px;
  margin-bottom: 24px;
}}
.mind-card {{
  border-radius: 14px; padding: 14px 18px;
  display: flex; align-items: flex-start; gap: 12px;
}}
.mind-wrong {{
  background: #FEF2F2; border: 1px solid #FECACA;
}}
.mind-right {{
  background: #ECFDF5; border: 1px solid #A7F3D0;
}}
.mind-icon {{
  width: 30px; height: 30px; border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  font-weight: 800; font-size: 15px; flex-shrink: 0; margin-top: 2px;
}}
.mind-wrong .mind-icon {{ background: #FEE2E2; color: #DC2626; }}
.mind-right .mind-icon {{ background: #D1FAE5; color: #059669; }}
.mind-label {{ font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 3px; }}
.mind-wrong .mind-label {{ color: #B91C1C; }}
.mind-right .mind-label {{ color: #047857; }}
.mind-text {{ font-size: 14.5px; color: #1E293B; line-height: 1.4; font-weight: 500; }}

.steps-grid {{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 14px;
}}
.step-card {{
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 18px 15px 16px 15px;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
  display: flex; flex-direction: column;
  position: relative;
  border-top: 4px solid var(--c);
}}
.step-head {{
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 12px;
}}
.step-num {{
  font-size: 12px; font-weight: 800; color: var(--c);
  background: var(--bg); padding: 4px 9px; border-radius: 8px;
  letter-spacing: 0.5px;
}}
.step-svg {{
  width: 34px; height: 34px; border-radius: 10px;
  background: var(--bg); color: var(--c);
  display: flex; align-items: center; justify-content: center;
}}
.step-title {{
  font-size: 15.5px; font-weight: 800; color: #0F172A;
  line-height: 1.3; margin-bottom: 10px; min-height: 40px;
}}
.step-list {{
  list-style: none; display: flex; flex-direction: column; gap: 7px;
  flex-grow: 1;
}}
.step-list li {{
  font-size: 13px; line-height: 1.42; color: #475569;
  padding-left: 13px; position: relative;
}}
.step-list li::before {{
  content: ""; position: absolute; left: 0; top: 7px;
  width: 5px; height: 5px; border-radius: 50%; background: var(--c);
}}
.step-note {{
  margin-top: 12px; padding-top: 9px;
  border-top: 1px dashed #E2E8F0;
  font-size: 12px; font-weight: 700; color: var(--c); line-height: 1.35;
}}
</style>
</head>
<body>
<div class="canvas" id="card">
  <div class="bg-orb-1"></div>
  <div class="bg-orb-2"></div>

  <div class="topbar">
    <div class="badge">📘 DAY 01 / 100 · POST-RELEASE PLAYBOOK</div>
    <div class="brand">100 NGÀY LÀM BA · ITBA MENTOR (TRANG 4)</div>
  </div>

  <h1 class="title">BA Nên Làm Gì Sau Khi Tính Năng Được <span class="accent">Release?</span></h1>

  <div class="mindset-strip">
    <div class="mind-card mind-wrong">
      <div class="mind-icon">✕</div>
      <div>
        <div class="mind-label">Lầm tưởng phổ biến</div>
        <div class="mind-text">Xong tài liệu → Dev code xong → Test pass → <b>Release = Hết việc!</b> (Ngủ quên sau release, đợi sếp gọi hỏi bug).</div>
      </div>
    </div>
    <div class="mind-card mind-right">
      <div class="mind-icon">✓</div>
      <div>
        <div class="mind-label">Tư duy BA thực chiến</div>
        <div class="mind-text"><b>Release không phải điểm kết thúc</b> — đó là lúc BA chứng minh giá trị qua quan sát, phản hồi &amp; cải tiến thực tế.</div>
      </div>
    </div>
  </div>

  <div class="steps-grid">
    <div class="step-card" style="--c:#2563EB; --bg:#EFF6FF;">
      <div class="step-head">
        <span class="step-num">BƯỚC 01</span>
        <div class="step-svg">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        </div>
      </div>
      <div class="step-title">Kiểm tra thực tế trên Production</div>
      <ul class="step-list">
        <li>Đăng nhập như user thật, tự thao tác từng bước.</li>
        <li>Soi kỹ từng nút bấm, luồng xử lý, dữ liệu hiển thị.</li>
      </ul>
      <div class="step-note">⚡ Đừng tin QA 100% — hãy tự trải nghiệm thật!</div>
    </div>

    <div class="step-card" style="--c:#7C3AED; --bg:#F5F3FF;">
      <div class="step-head">
        <span class="step-num">BƯỚC 02</span>
        <div class="step-svg">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M8 10h.01M12 10h.01M16 10h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
        </div>
      </div>
      <div class="step-title">Ghi nhận phản hồi người dùng</div>
      <ul class="step-list">
        <li>Hỏi stakeholder &amp; user nội bộ: <i>"Dùng thấy sao?", "Có gì khó hiểu?"</i></li>
        <li>Đối chiếu với kỳ vọng lúc họp bàn ban đầu.</li>
      </ul>
      <div class="step-note">💬 Feedback đời thực luôn khác xa phòng họp.</div>
    </div>

    <div class="step-card" style="--c:#0891B2; --bg:#ECFEFF;">
      <div class="step-head">
        <span class="step-num">BƯỚC 03</span>
        <div class="step-svg">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M16 8v8m-4-5v5m-4-2v2m-2 4h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
        </div>
      </div>
      <div class="step-title">Theo dõi chỉ số sử dụng</div>
      <ul class="step-list">
        <li>Tính năng có được dùng không? Bao nhiêu user?</li>
        <li>Người dùng bị rớt (drop-off) ở bước nào?</li>
      </ul>
      <div class="step-note">📊 Data nói thật thay cho lời khen xã giao.</div>
    </div>

    <div class="step-card" style="--c:#D97706; --bg:#FFFBEB;">
      <div class="step-head">
        <span class="step-num">BƯỚC 04</span>
        <div class="step-svg">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
        </div>
      </div>
      <div class="step-title">Hỗ trợ Team sau Release</div>
      <ul class="step-list">
        <li><b>Tester</b> báo bug → Hỗ trợ xác minh.</li>
        <li><b>DEV</b> hỏi flow → Cung cấp tài liệu.</li>
        <li><b>CSKH</b> cần HD → Soạn Quick Guide.</li>
      </ul>
      <div class="step-note">🤝 BA chủ động = BA được yêu thương.</div>
    </div>

    <div class="step-card" style="--c:#059669; --bg:#ECFDF5;">
      <div class="step-head">
        <span class="step-num">BƯỚC 05</span>
        <div class="step-svg">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
        </div>
      </div>
      <div class="step-title">Tổng kết &amp; Cải tiến</div>
      <ul class="step-list">
        <li>Ghi lại bài học: viết thiếu gì, flow nào lủng, user vướng đâu.</li>
        <li>Tự hỏi: <i>"Nếu làm lại, mình sẽ làm gì khác?"</i></li>
      </ul>
      <div class="step-note">🚀 Mỗi lần tổng kết = 1 lần nâng cấp!</div>
    </div>
  </div>

  <div class="footer-bar">
    <div class="footer-left">
      <span>💡</span>
      <span><b>Đúc kết:</b> BA giỏi không dừng lại ở lúc bàn giao SRS, mà đồng hành tới khi tính năng tạo ra giá trị thật trên Production.</span>
    </div>
    <div class="footer-pill">Quan sát → Phản hồi → Cải tiến</div>
  </div>
</div>
</body>
</html>
"""

DAY2_HTML = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
{COMMON_CSS}
.canvas {{ border-bottom-color: #0F766E; }}
.badge {{ background: #F0FDFA; color: #0F766E; border-color: #99F6E4; }}
h1.title span.accent {{ color: #0F766E; }}

.split-top {{
  display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 18px;
  margin-bottom: 20px;
}}
.panel-warn {{
  background: #FFF1F2; border: 1px solid #FECDD3; border-radius: 16px;
  padding: 16px 18px;
}}
.panel-arch {{
  background: #F0F9FF; border: 1px solid #BAE6FD; border-radius: 16px;
  padding: 16px 18px;
}}
.panel-tag {{
  font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px;
  margin-bottom: 10px; display: flex; align-items: center; gap: 6px;
}}
.panel-warn .panel-tag {{ color: #BE123C; }}
.panel-arch .panel-tag {{ color: #0369A1; }}

.chain {{
  display: flex; align-items: center; gap: 6px; margin-bottom: 11px; flex-wrap: wrap;
}}
.chain-box {{
  background: #FFFFFF; border: 1px solid #FDA4AF; border-radius: 8px;
  padding: 6px 10px; font-size: 12.5px; font-weight: 600; color: #881337;
}}
.chain-break {{ color: #E11D48; font-weight: 800; font-size: 14px; }}

.pitfalls {{
  display: flex; flex-direction: column; gap: 6px;
}}
.pitfall-item {{
  font-size: 13px; color: #4C0519; line-height: 1.38;
  background: rgba(255,255,255,0.65); padding: 6px 10px; border-radius: 8px;
}}
.arch-compare {{
  display: flex; flex-direction: column; gap: 9px;
}}
.arch-quote {{
  background: #FFFFFF; border-left: 4px solid #0284C7; border-radius: 8px;
  padding: 10px 12px; font-size: 13.5px; line-height: 1.45; color: #0F172A;
}}
.arch-sub {{ font-size: 13px; color: #334155; line-height: 1.45; }}

.section-header {{
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 12px;
}}
.section-title {{
  font-size: 15px; font-weight: 800; color: #0F172A; text-transform: uppercase;
  letter-spacing: 0.5px; display: flex; align-items: center; gap: 8px;
}}
.checklist-grid {{
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 13px;
}}
.chk-card {{
  background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px;
  padding: 14px 16px;
  box-shadow: 0 3px 10px rgba(15, 23, 42, 0.03);
  border-left: 4px solid var(--c);
}}
.chk-top {{
  display: flex; align-items: center; gap: 9px; margin-bottom: 6px;
}}
.chk-idx {{
  width: 24px; height: 24px; border-radius: 7px;
  background: var(--bg); color: var(--c);
  font-size: 12px; font-weight: 800;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}}
.chk-name {{ font-size: 14.5px; font-weight: 800; color: #0F172A; line-height: 1.25; }}
.chk-desc {{ font-size: 12.8px; color: #475569; line-height: 1.42; }}
</style>
</head>
<body>
<div class="canvas" id="card">
  <div class="bg-orb-1"></div>
  <div class="bg-orb-2"></div>

  <div class="topbar">
    <div class="badge">🏗️ DAY 02 / 100 · SYSTEM THINKING &amp; SCALABILITY</div>
    <div class="brand">100 NGÀY LÀM BA · ITBA MENTOR (TRANG 5–7)</div>
  </div>

  <h1 class="title">BA Không Tư Duy Hệ Thống = <span class="accent">Xây Nhà Không Có Bản Vẽ</span></h1>

  <div class="split-top">
    <div class="panel-warn">
      <div class="panel-tag">⚠️ Hệ quả khi chỉ làm từng mảnh rời rạc</div>
      <div class="chain">
        <div class="chain-box">GĐ1: Đơn hàng (Sales)</div>
        <span class="chain-break">⚡</span>
        <div class="chain-box">GĐ2: Kế toán (Thiếu thuế/CK)</div>
        <span class="chain-break">⚡</span>
        <div class="chain-box">GĐ3: Kho (Lệch tồn kho)</div>
      </div>
      <div class="pitfalls">
        <div class="pitfall-item"><b>1. Không kết nối:</b> Làm đúng yêu cầu lẻ nhưng cả hệ thống đứt đoạn, không dùng được.</div>
        <div class="pitfall-item"><b>2. Lệ thuộc ngược vào DEV:</b> Không nắm ảnh hưởng chéo → chỉ biết "giao nộp và chạy".</div>
        <div class="pitfall-item"><b>3. Thiếu nhất quán:</b> Duyệt đơn chỗ 2 cấp chỗ làm tay; cập nhật chỗ gọi API chỗ tải Excel.</div>
      </div>
    </div>

    <div class="panel-arch">
      <div class="panel-tag">📐 Tư duy Kiến trúc sư Hệ thống</div>
      <div class="arch-compare">
        <div class="arch-quote">
          Người xây nhà giỏi không chỉ hỏi: <i>"Phòng khách to bao nhiêu?"</i><br/>
          Mà luôn hỏi trước: <b>"Sau có lên tầng không? Mặt bằng chịu lực ổn không? Đường điện – nước chạy ra sao?"</b>
        </div>
        <div class="arch-sub">
          👉 <b>BA không cần biết viết code, nhưng bắt buộc phải biết tư duy cấu trúc:</b> nhìn tổng thể luồng dữ liệu, điểm tích hợp và khả năng mở rộng ngay từ ngày đầu đặt bút viết SRS.
        </div>
      </div>
    </div>
  </div>

  <div class="section-header">
    <div class="section-title">✅ Checklist 6 Trụ Cột Đánh Giá Luồng Nghiệp Vụ Có Khả Năng Mở Rộng</div>
  </div>

  <div class="checklist-grid">
    <div class="chk-card" style="--c:#0284C7; --bg:#E0F2FE;">
      <div class="chk-top"><span class="chk-idx">01</span><span class="chk-name">Dữ liệu liên thông bước sau</span></div>
      <div class="chk-desc">Đầu vào đủ cho nghiệp vụ kế tiếp; không lặp dữ liệu hệ thống khác; thống nhất thuật ngữ giữa các phòng ban.</div>
    </div>
    <div class="chk-card" style="--c:#0D9488; --bg:#CCFBF1;">
      <div class="chk-top"><span class="chk-idx">02</span><span class="chk-name">Sẵn sàng điểm nối tích hợp</span></div>
      <div class="chk-desc">Nhận diện rõ phụ thuộc hệ thống ngoài; tách bạch xử lý nghiệp vụ với kỹ thuật; chừa sẵn điểm nối API.</div>
    </div>
    <div class="chk-card" style="--c:#4F46E5; --bg:#EEF2FF;">
      <div class="chk-top"><span class="chk-idx">03</span><span class="chk-name">Tách bạch Logic &amp; Giao diện</span></div>
      <div class="chk-desc">Không "chôn" cứng điều kiện nghiệp vụ vào màn hình UI — khi thay đổi UI/UX không phải đập sửa lại core logic.</div>
    </div>
    <div class="chk-card" style="--c:#D97706; --bg:#FEF3C7;">
      <div class="chk-top"><span class="chk-idx">04</span><span class="chk-name">Dự phòng ngoại lệ &amp; mở rộng</span></div>
      <div class="chk-desc">Không chỉ vẽ Happy Case — chừa sẵn đường xử lý cho Exception, kịch bản biên và thay đổi quy trình tương lai.</div>
    </div>
    <div class="chk-card" style="--c:#7C3AED; --bg:#F3E8FF;">
      <div class="chk-top"><span class="chk-idx">05</span><span class="chk-name">Tái sử dụng liên Module</span></div>
      <div class="chk-desc">Chuẩn hóa luồng dùng chung (duyệt đơn, trạng thái, phân quyền) để áp dụng lại, tránh viết trùng lặp nhiều nơi.</div>
    </div>
    <div class="chk-card" style="--c:#059669; --bg:#D1FAE5;">
      <div class="chk-top"><span class="chk-idx">06</span><span class="chk-name">Phép thử chịu tải gấp đôi (x2)</span></div>
      <div class="chk-desc">Nếu user / giao dịch / dữ liệu x2: API có nghẽn không? Cấu trúc bảng đủ định danh mở rộng mà không phải refactor?</div>
    </div>
  </div>

  <div class="footer-bar">
    <div class="footer-left">
      <span>🏛️</span>
      <span><b>Nguyên tắc cốt lõi:</b> Đừng chỉ hoàn thành từng tính năng đúng hạn — <b>Hãy thiết kế một hệ thống sống lâu dài.</b></span>
    </div>
    <div class="footer-pill">System Thinking First</div>
  </div>
</div>
</body>
</html>
"""


def trim_bottom_bg(png_path: Path):
    with Image.open(png_path) as im:
        im = im.convert("RGB")
        # Background color outside .canvas is #EEF2F6 -> (238, 242, 246)
        bg = Image.new("RGB", im.size, im.getpixel((im.width - 1, im.height - 1)))
        diff = ImageChops.difference(im, bg)
        bbox = diff.getbbox()
        if bbox:
            cropped = im.crop((0, 0, im.width, bbox[3]))
            cropped.save(png_path, "PNG", optimize=True)


def render(name: str, html_str: str) -> Path:
    html_p = OUT_DIR / f"{name}.html"
    png_p = OUT_DIR / f"{name}.png"
    html_p.write_text(html_str, encoding="utf-8")
    cmd = [
        EDGE,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1200,1100",
        "--force-device-scale-factor=2",
        f"--screenshot={png_p}",
        html_p.as_uri(),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    trim_bottom_bg(png_p)
    with Image.open(png_p) as im:
        print(f"Rendered {png_p.name}: {im.size} ({png_p.stat().st_size // 1024} KB)")
    return png_p


if __name__ == "__main__":
    render("day_001_infographic", DAY1_HTML)
    render("day_002_infographic", DAY2_HTML)
