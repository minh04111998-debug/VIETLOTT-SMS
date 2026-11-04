# 📋 Designer Output Checklist

> **Vai trò sử dụng:** `[🎨 ROLE: Designer]`
> **Mục đích:** Designer sử dụng checklist này để tự kiểm tra (Self-Correction) bản thiết kế, cấu trúc UI/UX và prototypes trước khi handoff cho DEV.

| # | Tiêu chí kiểm tra | Mức độ |
|---|-------------------|--------|
| 1 | Hệ thống đáp ứng đủ các trạng thái (States): Default, Hover, Active, Focus, Disabled, Loading, Empty, Error, Success, Partial | 🔴 Blocking |
| 2 | Kích thước Touch Target tối thiểu 44px x 44px (trên mobile) | 🔴 Blocking |
| 3 | Thiết kế Responsive cho 3 loại màn hình chính: Mobile + Tablet + Desktop | 🟡 Important |
| 4 | Tuân thủ Accessibility (WCAG): Độ tương phản màu chữ/nền ≥ 4.5:1, có alt text cho hình ảnh | 🟡 Important |
| 5 | User Flow trong bản thiết kế khớp 100% với Acceptance Criteria trong SRS/User Story | 🟢 Minor |

---

**Cách thực hiện (Dành cho AI):**
1. Kiểm tra lại bản thảo / code UI được sinh ra (nếu có sinh code).
2. Tự review dưới góc độ DEV (tính khả thi implementation) và QA (edge cases về state).
3. Sửa lỗi ngay nếu thiếu trạng thái Loading, Empty hoặc Error.
4. Sau khi hoàn tất, in ra báo cáo theo định dạng: **📋 Gate Report Output:** `Self-Review: Đã chạy [X] vòng kiểm tra, tự động sửa [Y] lỗi.`
