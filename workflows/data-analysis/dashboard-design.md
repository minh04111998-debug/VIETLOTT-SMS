# 📊 Workflow: BI Dashboard Layout & Data Modeling (DA)

> **Mục tiêu:** Thiết kế cấu trúc trực quan hóa dữ liệu (Wireframe/Layout Dashboard), định nghĩa mô hình ngữ nghĩa (Semantic Model) và chỉ số tính toán (DAX Measures) trên PowerBI / Looker Studio.  
> **Lệnh kích hoạt:** `/da dashboard` | **Vai trò:** Data Analyst (DA)

---

## 1. Input & Output

- **Input:** Kết quả phân tích biến động, yêu cầu hiển thị từ các bên liên quan.
- **Output:** Wireframe Layout Dashboard (Markdown/ASCII), file cấu hình TMDL / PBIX hoặc bản đặc tả Visuals.

---

## 2. Các Bước Thực Hiện

### Bước 1: Thiết Kế Bố Cục Trực Quan Hóa (Dashboard Hierarchy)
Áp dụng cấu trúc 3 tầng chuẩn:
1. **Tầng đỉnh (Top - KPI Cards):**
   - Tổng doanh thu (GTV), % tăng trưởng WoW/MoM, Số tài khoản mở mới, Tỷ lệ hoàn thành KPI.
2. **Tầng giữa (Middle - Trend & Composition):**
   - Biểu đồ đường (Line Chart): Xu hướng doanh thu theo ngày và so sánh với cùng kỳ.
   - Biểu đồ cột chồng (Stacked Bar Chart): Cơ cấu doanh thu theo loại vé và nhà mạng.
3. **Tầng đáy (Bottom - Drill-down Data Table):**
   - Bảng kê chi tiết theo từng ngày/kỳ quay, có bộ lọc linh hoạt (Slicers) theo Kênh, Sản phẩm, Tỉnh/Thành.

### Bước 2: Xây Dựng Semantic Data Model & DAX Measures
1. **Thiết lập mô hình hình sao (Star Schema):**
   - `Fact_Sales`: Chứa các giao dịch bán vé và số tiền.
   - `Dim_Date`: Chiều thời gian (Ngày, Tuần, Tháng, Quý, Năm).
   - `Dim_Product`: Chiều sản phẩm xổ số.
   - `Dim_Partner`: Chiều đối tác viễn thông và ngân hàng.
2. **Định nghĩa các chỉ số đo lường (Measures):**
   - `Total_Revenue = SUM(Fact_Sales[Amount])`
   - `WoW_Growth = DIVIDE([Total_Revenue] - [Revenue_Last_Week], [Revenue_Last_Week])`
   - `Target_Completion_Rate = DIVIDE([Total_Revenue], [Monthly_KPI_Target])`

### Bước 3: Kiểm Thử Hiệu Năng Visuals
1. Đảm bảo thời gian load trang Dashboard dưới 3 giây.
2. Kiểm tra tính tương tác của các Slicers khi lọc đa chiều.

### Bước 4: 🛑 [Hard Stop] Nghiệm Thu Giao Diện Dashboard
- Bàn giao mockup layout hoặc bản Dashboard tương tác cho PO/PM ký duyệt.
