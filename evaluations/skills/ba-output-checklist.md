# 📋 BA Output Checklist

> **Vai trò sử dụng:** `[🟢 ROLE: BA]`
> **Mục đích:** BA sử dụng checklist này để tự kiểm tra (Self-Correction) kết quả đầu ra (SRS, User Story, BRD) trước khi trình User. Nếu fail bất kỳ mục 🔴 Blocking nào, AI PHẢI tự sửa và ghi log.

| # | Tiêu chí kiểm tra | Mức độ | Nguồn tham chiếu |
|---|-------------------|--------|------------------|
| 1 | Mọi FR (Functional Requirement) phải trace về ít nhất 1 BR (Business Requirement) | 🔴 Blocking | `ba-rules.md` §2.1 |
| 2 | Mỗi User Story phải có ≥3 AC (Happy + Alt + Exception) | 🔴 Blocking | `ba-rules.md` §3.2 |
| 3 | Không chứa từ mơ hồ: "TBD", "sẽ bổ sung", "tương tự", "nhanh", "dễ dùng" (Có thể kiểm tra bằng `ambiguity_scanner.py`) | 🔴 Blocking | `ba-rules.md` §4 |
| 4 | Mỗi Use Case gọi external system PHẢI có **Exception Analysis Table** (bảng 8 cột) | 🔴 Blocking | `ba-rules.md` §3.5 |
| 5 | Mỗi luồng gọi external PHẢI có **Timeout & Hung State Checklist** (7 câu hỏi) | 🔴 Blocking | `ba-rules.md` §3.6 |
| 6 | Edge Case Analyzer đã quét đủ **8 nhóm** (bao gồm ⏱️ Timeout, 🔄 Retry, 🔗 Integration) | 🔴 Blocking | `analysis-frameworks.md` §2 |
| 7 | Vượt qua INVEST check | 🟡 Important | `frameworks.md` |
| 8 | Có version number (Major.Minor) + changelog table | 🟡 Important | `ba-rules.md` §2.3 |
| 9 | Các yêu cầu phi chức năng (NFR) đã được xác định (performance, security, uptime) | 🟡 Important | `ba-rules.md` §4 |
| 10 | Đã thực hiện Cross-review bằng DEV + QA perspective | 🟢 Minor | `cross-review-protocol.md` |
| 11 | **[CM]** Impact analysis trace đủ 4 layers: Requirements → Design → Technical → Testing | 🔴 Blocking | `ba-rules.md` §7 |
| 12 | **[CM]** Cascading Update Checklist (10 items) đã complete — không bỏ sót tài liệu | 🔴 Blocking | `ba-rules.md` §7.4 |
| 13 | **[CM]** Breaking change level đã classify (CRITICAL/IMPORTANT/MINOR) và notify đúng stakeholder | 🔴 Blocking | `ba-rules.md` §7.3 |
| 14 | **[CM]** CR có đầy đủ: Scope (Before → After), Lý do, Authority, Timeline | 🟡 Important | `ba-rules.md` §7.2 |
| 15 | **[CM]** Communication plan — mọi team bị ảnh hưởng đã notify | 🟡 Important | `ba-rules.md` §7.5 |
| 16 | **[CM]** `project-context.md` đã cập nhật | 🟢 Minor | `ba-rules.md` §7.6 |

> **Lưu ý:** Items 11-16 (đánh dấu `[CM]`) chỉ áp dụng khi BA thực hiện Change Management tasks (`/ba impact`, `/ba change`). Không áp dụng cho output SRS/BRD thông thường.

---

**Cách thực hiện (Dành cho AI):**
1. Kiểm tra từng mục một, bắt đầu từ các mục 🔴 Blocking.
2. Nếu phát hiện vi phạm, hãy TỰ ĐỘNG bổ sung hoặc sửa đổi bản draft.
3. Nếu mục #3 có từ mơ hồ, thay thế bằng các thông số đo lường định lượng.
4. Nếu mục #4/#5 thiếu, tự động tạo bảng Exception rỗng + cảnh báo 🔴 cho user.
5. Nếu mục #6 thiếu nhóm ⏱️/🔄/🔗, tự bổ sung phân tích + ghi log.
6. Nếu mục #11 (Impact Analysis) thiếu layer nào trong 4 layers, bổ sung trace ngay lập tức.
7. Nếu mục #12 (Cascading Update Checklist) chưa đủ 10 items, quét lại toàn bộ tài liệu dự án để tìm item còn thiếu.
8. Ghi chú số lần tự sửa vào log trước khi xuất ra output cuối cùng.


