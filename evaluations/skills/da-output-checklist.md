# 📋 DA Output Checklist

> **Vai trò sử dụng:** `[📊 ROLE: DA]` (Data Analyst)
> **Mục đích:** DA sử dụng checklist này để tự kiểm tra (Self-Correction) các báo cáo dữ liệu, Dashboard và bản phân tích Insight trước khi trình người dùng/Ban giám đốc.

| Version | Ngày | Người cập nhật | Ghi chú |
|---------|------|----------------|---------|
| 1.0.0 | 2026-09-26 | AI Architecture Review | Khởi tạo checklist cho DA |

| # | Tiêu chí kiểm tra | Mức độ |
|---|-------------------|--------|
| 1 | **Data-Driven Objectivity:** Mọi nhận định định tính ("tăng mạnh", "sụt giảm") đều đi kèm số liệu cụ thể (%, số tuyệt đối, thời gian). Không dùng từ ngữ cảm tính ("có vẻ", "nhiều", "ít"). | 🔴 Blocking |
| 2 | **Variance & Context:** Luôn có phần so sánh biến động với kỳ trước (WoW - Week over Week, MoM - Month over Month, hoặc YoY) để thấy rõ xu hướng. | 🔴 Blocking |
| 3 | **Actionable Insights:** Có tối thiểu **Top 3 Insights** chỉ ra nguyên nhân gốc rễ (Root Cause / Diagnostic) và đề xuất ít nhất 1-2 hành động cụ thể (Prescriptive), không chỉ đơn thuần liệt kê dữ liệu thô (Descriptive). | 🔴 Blocking |
| 4 | **Dashboard Layout Hierarchy:** Cấu trúc Dashboard tuân thủ phân tầng 3 lớp: Top (Tổng quan KPI thẻ số) -> Middle (Biểu đồ xu hướng Line/Bar/Pie) -> Bottom (Bảng chi tiết/Raw data). | 🟡 Important |
| 5 | **Anomaly & Red Flagging:** Bật cảnh báo đỏ (`> [!WARNING]` hoặc `> [!CAUTION]`) ngay lập tức nếu phát hiện các chỉ số kinh doanh tụt giảm bất thường hoặc có dấu hiệu rủi ro. | 🟡 Important |
| 6 | **Cross-Review:** Đã đối chiếu insight với PO (tác động chiến lược sản phẩm) hoặc BA (tác động luồng nghiệp vụ/quy tắc tính). | 🟢 Minor |

---

**Cách thực hiện (Dành cho AI):**
1. Đọc lại báo cáo số liệu, kiểm tra các con số tính toán (% tăng trưởng, chênh lệch tuyệt đối).
2. Kiểm tra xem báo cáo đã trả lời được câu hỏi *"Tại sao số liệu thay đổi và tiếp theo nên làm gì?"* chưa.
3. Sử dụng `doc_structure_validator.py` để xác nhận cấu trúc markdown nếu cần.
4. Sau khi hoàn tất, in ra báo cáo theo định dạng: **📋 Gate Report Output:** `Self-Review: Đã chạy [X] vòng kiểm tra, tự động sửa [Y] lỗi.`
