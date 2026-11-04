# 🔄 Master Workflow: Data Analysis (DA)

> **Mục tiêu:** Chuyển đổi dữ liệu thô từ team Sale (Google Sheets) thành báo cáo Dashboard định kỳ, phát hiện biến động (WoW, MoM) và đưa ra các insight có giá trị hành động (Actionable Insights) cho buổi họp giao ban.  
> **Lệnh kích hoạt:** `/da` | **Vai trò:** Data Analyst (DA)

---

## Danh Mục Quy Trình Con (Sub-workflows)

| Bước | Quy trình chi tiết | Lệnh kích hoạt | Mục tiêu chính |
|---|---|---|---|
| Step 1 | [data-cleaning.md](data-cleaning.md) | `/da clean` | Rà soát và làm phẳng dữ liệu thô (Google Sheets/CSV) |
| Step 2 | [variance-analysis.md](variance-analysis.md) | `/da variance` | Tính biến động WoW, MoM, Run-rate, phân tích 5 Whys |
| Step 3 | [dashboard-design.md](dashboard-design.md) | `/da dashboard` | Thiết kế Wireframe Dashboard, Star Schema & DAX |
| Step 4 | [weekly-reporting.md](weekly-reporting.md) | `/da report` | Soạn thảo báo cáo giao ban & Top 3 Actionable Insights |

---

## Các Bước Thực Hiện Tuần Tự (Steps)

### Step 1: Data Preparation & Cleaning (Làm sạch dữ liệu)
- Tham chiếu quy trình chi tiết: [data-cleaning.md](data-cleaning.md).
- Nhận nguồn dữ liệu thô (thường là Google Sheets).
- Kiểm tra tính toàn vẹn của dữ liệu: Có bị thiếu ngày nào không? Có merge cells không? Format ngày tháng/tiền tệ chuẩn chưa?
- Chuyển đổi dữ liệu về cấu trúc bảng phẳng (Flat Table) để sẵn sàng load lên Dashboard.
- **[🛑 Hard Stop]** Yêu cầu xác nhận data đã sạch trước khi phân tích.

### Step 2: Metrics Calculation & Variance (Tính toán biến động)
- Tham chiếu quy trình chi tiết: [variance-analysis.md](variance-analysis.md).
- Tính toán các KPI tổng quan: Doanh thu, Lợi nhuận, Lượng user mới, Số vé bán ra.
- So sánh các KPI này với kỳ trước (Week over Week, Month over Month).
- Xác định Top Gainers (Tăng trưởng tốt nhất) và Top Losers (Giảm mạnh nhất).
- **[🛑 Hard Stop]** Hiển thị số liệu tính toán để người dùng rà soát nhanh.

### Step 3: Dashboard Layout Design (Thiết kế Dashboard)
- Tham chiếu quy trình chi tiết: [dashboard-design.md](dashboard-design.md).
- Dựa vào yêu cầu báo cáo, vẽ cấu trúc (Wireframe/Layout) cho Dashboard bằng markdown hoặc text mô tả.
- **Top:** Tổng quan KPI & % biến động.
- **Middle:** Biểu đồ xu hướng (Line chart) theo ngày, và Phân bổ (Pie/Bar chart) theo loại vé/khu vực.
- **Bottom:** Data table chi tiết.
- Cung cấp hướng dẫn setup trên công cụ BI (như Google Data Studio/Looker/PowerBI).
- **[🛑 Hard Stop]** Yêu cầu phê duyệt layout Dashboard.

### Step 4: Insight Generation & Action Plan (Phân tích nguyên nhân & Hành động)
- Tham chiếu quy trình chi tiết: [weekly-reporting.md](weekly-reporting.md).
- Đặt câu hỏi "Tại sao?" cho các chỉ số bất thường.
- Phân tách (Drill-down) dữ liệu theo khung giờ, đối tượng khách hàng, sản phẩm để tìm Insight gốc rễ.
- Tổng hợp thành "Top 3 Insights" cho buổi họp.
- Đề xuất ít nhất 1-2 hành động kinh doanh (Actionable recommendation) dựa trên Insight đó.
- **[🛑 Hoàn thành Workflow]** Bàn giao báo cáo hoàn chỉnh vào `artifacts/analysis/`.
