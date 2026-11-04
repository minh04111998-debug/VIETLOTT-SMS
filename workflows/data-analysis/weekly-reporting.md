# 📑 Workflow: Weekly Executive Reporting & Data Storytelling (DA)

> **Mục tiêu:** Biên soạn báo cáo phân tích hiệu suất kinh doanh định kỳ hàng tuần/tháng, chuyển hóa dữ liệu khô khan thành câu chuyện có định hướng hành động (Actionable Insights) cho buổi họp giao ban lãnh đạo.  
> **Lệnh kích hoạt:** `/da report` | **Vai trò:** Data Analyst (DA)

---

## 1. Input & Output

- **Input:** Dashboard KPIs, phân tích biến động và cây nguyên nhân 5 Whys.
- **Output:** Báo cáo Markdown chuẩn hóa lưu tại `artifacts/analysis/` theo template `templates/weekly-da-report-template.md`.

---

## 2. Các Bước Thực Hiện

### Bước 1: Tổng Hợp Số Liệu Điều Hành (Executive Summary)
1. Điền bảng tóm tắt KPI tuần theo định dạng chuẩn:
   - Tổng GTV (Doanh thu bán vé).
   - Số người mua vé thực tế (Active Users).
   - Tốc độ tăng trưởng WoW / MoM.
   - Trạng thái hoàn thành kế hoạch (🟢 Đạt / 🟡 Rủi ro / 🔴 Chậm tiến độ).

### Bước 2: Kể Chuyện Bằng Dữ Liệu (Data Storytelling)
1. **Bối cảnh:** Tuần này có sự kiện gì đặc biệt? (Jackpot chạm 100 tỷ, ra mắt kênh ngân hàng mới, nâng cấp hệ thống).
2. **Điểm nhấn (The Twist):** Chỉ ra các biến động bất thường mà bảng số tổng quan không thể hiện (ví dụ: doanh thu tăng nhưng lượng người chơi mới giảm).
3. **Phân tích so sánh:** Đối chiếu giữa các kênh (App vs Webview vs CTV).

### Bước 3: Đề Xuất Hành Động Cụ Thể (Actionable Recommendations)
1. Mọi báo cáo bắt buộc phải có ít nhất **Top 3 Insights** có thể chuyển thành hành động:
   - *Insight 1:* [Hiện tượng + Nguyên nhân] -> **Hành động đề xuất:** [Hành động cho PO/BA/Marketing].
   - *Insight 2:* [Hiện tượng + Nguyên nhân] -> **Hành động đề xuất:** [Hành động cho DEV/Vận hành].
   - *Insight 3:* [Hiện tượng + Nguyên nhân] -> **Hành động đề xuất:** [Hành động cho Kinh doanh/CSKH].

### Bước 4: 🛑 [Hard Stop] Ký Duyệt Báo Cáo
- Xuất bản báo cáo sang `artifacts/analysis/da-vietlott-sms-report-[period].md` với `status: Draft`.
- Báo cáo trải qua kiểm tra cấu trúc qua `validators/gate_runner.py --role DA --file ...`.
- Trình bày tại buổi họp giao ban và xin phê duyệt chính thức từ Lãnh đạo / Human Owner.
