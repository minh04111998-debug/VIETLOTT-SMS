# 🧹 Workflow: Data Cleaning & Preprocessing (DA)

> **Mục tiêu:** Chuẩn hóa dữ liệu thô từ các nguồn phân tán (Google Sheets, CSV đối soát, log giao dịch) thành bảng phẳng (Flat Table) chuẩn mực, đảm bảo tính toàn vẹn và sẵn sàng nạp vào Data Model.  
> **Lệnh kích hoạt:** `/da clean` | **Vai trò:** Data Analyst (DA)

---

## 1. Input & Output

- **Input:** File dữ liệu thô (Google Sheets, CSV, Excel) hoặc dữ liệu xuất từ Core Ticketing.
- **Output:** Bảng dữ liệu phẳng chuẩn hóa (`.csv` hoặc bảng Markdown) kèm biên bản kiểm tra dữ liệu sạch.

---

## 2. Các Bước Thực Hiện

### Bước 1: Kiểm Tra Tính Toàn Vẹn Cấu Trúc (Structural Integrity)
1. Kiểm tra cấu trúc dòng/cột: Loại bỏ các ô bị gộp (Merged Cells), tiêu đề nhiều tầng (Multi-level Headers).
2. Kiểm tra chuỗi thời gian: Đảm bảo không bị khuyết ngày (Missing Dates) hoặc khoảng trống chu kỳ quay số.
3. Chuẩn hóa tên cột theo định dạng snake_case: `transaction_id`, `order_date`, `lottery_product`, `gross_revenue`, `telco_partner`.

### Bước 2: Chuẩn Hóa Kiểu Dữ Liệu & Định Dạng (Type Casting)
1. **Ngày tháng:** Chuyển đổi toàn bộ về chuẩn ISO-8601 (`YYYY-MM-DD` hoặc `YYYY-MM-DD HH:mm:ss`).
2. **Tiền tệ & Số liệu:** Loại bỏ ký tự phân cách nghìn thừa (`.`, `,`, `VNĐ`), ép kiểu `numeric / decimal` chính xác.
3. **Mã định danh:** Giữ nguyên số 0 ở đầu (Leading zeros) đối với số điện thoại (`091...`), số CCCD hoặc mã đại lý.

### Bước 3: Rà Soát Dữ Liệu Bất Thường (Outliers & Missing Values)
1. Xử lý giá trị rỗng (`NULL / N/A`): Phân loại rỗng do không phát sinh giao dịch (điền `0`) hay do mất dữ liệu kỹ thuật (cần ghi log).
2. Phát hiện số liệu âm bất thường đối với doanh thu vé bán.
3. Khử trùng giao dịch lặp (Deduplication) dựa trên khóa chính `transaction_id`.

### Bước 4: 🛑 [Hard Stop] Xác Nhận Dữ Liệu Sạch
- Trình bày tóm tắt: Tổng số dòng, số dòng lỗi đã làm sạch, khoảng thời gian dữ liệu.
- Xin xác nhận của Human / Lead trước khi nạp vào phân tích biến động hoặc Dashboard.
