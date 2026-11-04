# 📋 QA Output Checklist

> **Vai trò sử dụng:** `[🔴 ROLE: QA]`
> **Mục đích:** QA sử dụng checklist này để tự kiểm tra (Self-Correction) kết quả đầu ra (Test Plan, Test Cases, Bug Report, Quality Gate) trước khi trình User. Nếu fail bất kỳ mục 🔴 Blocking nào, AI PHẢI tự sửa và ghi log.

| # | Tiêu chí kiểm tra | Mức độ | Nguồn tham chiếu |
|---|-------------------|--------|------------------|
| 1 | Test Plan phải risk-based — không chấp nhận chỉ có happy path | 🔴 Blocking | `qa-rules.md` §1 |
| 2 | Test cases bao gồm: Happy + Alternative + Exception + Boundary Value + Null/Empty | 🔴 Blocking | `qa-rules.md` §2 |
| 3 | Quality Gates 3 tầng (merge → staging → production) đã define rõ ràng | 🔴 Blocking | `qa-rules.md` §3 |
| 4 | Bug Report có đủ reproduction steps (DEV reproduce được trong 5 phút) | 🔴 Blocking | `qa-rules.md` §4 |
| 5 | Automation regression test coverage cho features cũ | 🟡 Important | `qa-rules.md` §3 |
| 6 | Test Oracle đã identified cho mỗi test scenario | 🟡 Important | `qa-rules.md` §5 |
| 7 | Cross-review bằng DEV perspective (testability) và BA perspective (AC coverage) | 🟢 Minor | `cross-review-protocol.md` |

---

**Cách thực hiện (Dành cho AI):**
1. Kiểm tra từng mục một, bắt đầu từ các mục 🔴 Blocking.
2. Nếu Test Plan chỉ có happy path, bổ sung ngay các negative test, boundary value và exception scenarios.
3. Nếu Bug Report thiếu reproduction steps, thêm chi tiết đủ để DEV reproduce trong 5 phút.
4. Ghi chú số lần tự sửa vào log trước khi xuất ra output cuối cùng.
5. Sau khi hoàn tất, in ra báo cáo theo định dạng: **📋 Gate Report Output:** `Self-Review: Đã chạy [X] vòng kiểm tra, tự động sửa [Y] lỗi.`
