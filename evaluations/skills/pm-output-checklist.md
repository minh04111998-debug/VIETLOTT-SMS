# 📋 PM Output Checklist

> **Vai trò sử dụng:** `[⚪ ROLE: PM]`
> **Mục đích:** PM sử dụng checklist này để tự kiểm tra (Self-Correction) kết quả đầu ra (Timeline, Risk Register, Status Report, Phase Gate) trước khi trình User. Nếu fail bất kỳ mục 🔴 Blocking nào, AI PHẢI tự sửa và ghi log.

| # | Tiêu chí kiểm tra | Mức độ | Nguồn tham chiếu |
|---|-------------------|--------|------------------|
| 1 | Timeline phải dựa trên velocity data thực tế, không dựa trên áp lực stakeholder | 🔴 Blocking | `pm-rules.md` §1 |
| 2 | Risk Register đã cập nhật (< 2 tuần) với Probability × Impact scoring | 🔴 Blocking | `pm-rules.md` §3 |
| 3 | Phase Gate checklist pass — deliverables sign-off, dependencies identified | 🔴 Blocking | `pm-rules.md` §4 |
| 4 | Iron Triangle trade-off đã thương lượng rõ ràng với stakeholder | 🟡 Important | `pm-rules.md` §2 |
| 5 | Resource cho phase tiếp theo đã confirmed | 🟡 Important | `pm-rules.md` §5 |
| 6 | Status report có velocity data, burn-down/up chart | 🟢 Minor | `pm-rules.md` §2 |

---

**Cách thực hiện (Dành cho AI):**
1. Kiểm tra từng mục một, bắt đầu từ các mục 🔴 Blocking.
2. Nếu timeline không dựa trên velocity data, yêu cầu cung cấp dữ liệu thực tế hoặc tính toán lại.
3. Nếu Risk Register thiếu hoặc quá hạn, bổ sung ngay với Probability × Impact scoring.
4. Ghi chú số lần tự sửa vào log trước khi xuất ra output cuối cùng.
5. Sau khi hoàn tất, in ra báo cáo theo định dạng: **📋 Gate Report Output:** `Self-Review: Đã chạy [X] vòng kiểm tra, tự động sửa [Y] lỗi.`
