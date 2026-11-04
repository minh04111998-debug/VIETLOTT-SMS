# 📈 Workflow: Variance & Trend Analysis (DA)

> **Mục tiêu:** Tính toán độ lệch biến động (DoD, WoW, MoM), tốc độ chạy số (Run-rate), bóc tách nguyên nhân gốc rễ (5 Whys) và phân khúc đóng góp doanh thu theo sản phẩm/nhà mạng.  
> **Lệnh kích hoạt:** `/da variance` | **Vai trò:** Data Analyst (DA)

---

## 1. Input & Output

- **Input:** Bảng dữ liệu phẳng đã làm sạch từ bước `/da clean`.
- **Output:** Bảng phân tích biến động, Run-rate dự báo và cây nguyên nhân 5 Whys.

---

## 2. Các Bước Thực Hiện

### Bước 1: Tính Toán Các Chỉ Số Biến Động Chuẩn (Variance Calculation)
1. **Week over Week (WoW):** `((Doanh thu tuần này - Doanh thu tuần trước) / Doanh thu tuần trước) * 100%`.
2. **Month over Month (MoM):** So sánh cùng kỳ tháng trước hoặc cùng số ngày MTD (Month-to-Date).
3. **Tốc độ chạy số (Run-rate):** 
   - `Doanh thu TB ngày = Doanh thu MTD / Số ngày đã qua`.
   - `Doanh thu dự báo tháng = Doanh thu TB ngày * Tổng số ngày trong tháng`.
4. **Tỷ lệ hoàn thành KPI:** Đo lường so với KPI Cam kết và KPI Phấn đấu.

### Bước 2: Phân Tích Đóng Góp & Top Gainers / Losers
1. Bóc tách theo dòng sản phẩm xổ số: Mega 6/45, Power 6/55, Max 3D, Keno, Bingo18.
2. Bóc tách theo kênh đối tác: Viettel, MobiFone, VinaPhone, Kênh Bank (VPBank, VietinBank...).
3. Xác định **Top Gainer** (Đóng góp tăng trưởng lớn nhất) và **Top Loser** (Kéo tụt doanh thu mạnh nhất).

### Bước 3: Đào Sâu Nguyên Nhân Gốc Rễ (5 Whys Root Cause Analysis)
1. Không dừng lại ở việc mô tả số liệu (ví dụ: "Doanh thu giảm 8%").
2. Đặt liên tiếp 5 câu hỏi "Tại sao?" để tìm nguyên nhân nội tại:
   - *Tại sao giảm?* -> Do lượng vé Bingo18 giảm.
   - *Tại sao Bingo18 giảm?* -> Do giờ cao điểm buổi tối người chơi gặp lỗi mạng.
   - *Tại sao gặp lỗi mạng?* -> Do cổng thanh toán bị timeout quá 30 giây.
   - *Tại sao timeout?* -> Do thiếu cơ chế hàng đợi xử lý bất đồng bộ.

### Bước 4: 🛑 [Hard Stop] Thẩm Định Kết Quả Biến Động
- Trình bày bảng so sánh và cây nguyên nhân cho PO / PM rà soát trước khi đưa vào Dashboard.
