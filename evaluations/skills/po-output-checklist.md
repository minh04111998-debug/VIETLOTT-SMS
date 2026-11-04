# 📋 PO Output Checklist

> **Vai trò sử dụng:** `[🔵 ROLE: PO]`
> **Mục đích:** PO sử dụng checklist này để tự kiểm tra (Self-Correction) kết quả đầu ra (PRD, Roadmap, Backlog, Product Strategy) trước khi trình User. Nếu fail bất kỳ mục 🔴 Blocking nào, AI PHẢI tự sửa và ghi log.

| # | Tiêu chí kiểm tra | Mức độ | Nguồn tham chiếu |
|---|-------------------|--------|------------------|
| 1 | PRD/Feature phải có evidence-based justification (data, user research, analytics) — không chấp nhận "tôi nghĩ user cần" | 🔴 Blocking | `po-rules.md` §1 |
| 2 | Mỗi item trong roadmap/backlog phải có RICE score hoặc prioritization framework rõ ràng | 🔴 Blocking | `po-rules.md` §2 |
| 3 | Definition of Ready (DoR) phải pass đầy đủ trước khi story vào sprint | 🔴 Blocking | `po-rules.md` §3 |
| 4 | Mỗi Experiment/MVP PHẢI có **MCS** (Minimum Criteria for Success) + tiêu chí Persist/Pivot/Kill | 🔴 Blocking | `po-rules.md` §4, `po-frameworks.md` §3 |
| 5 | OKR Key Results phải **SMART** — Specific, Measurable, Achievable, Relevant, Time-bound | 🔴 Blocking | `po-rules.md` §4 |
| 6 | Problem Statement phải validate với **≥5 users** thực tế trước khi commit vào roadmap | 🔴 Blocking | `po-rules.md` §4 |
| 7 | Có North Star Metric / OKR gắn với feature | 🟡 Important | `po-rules.md` §1 |
| 8 | Stakeholder đã align (Power/Interest matrix reviewed) | 🟡 Important | `po-rules.md` §4 |
| 9 | Product lifecycle stage đã identify, action phù hợp stage đó | 🟡 Important | `po-rules.md` §2 |
| 10 | Cross-review bằng BA + SA + PM + DEV + QA perspective | 🟢 Minor | `cross-review-protocol.md` |

---

**Cách thực hiện (Dành cho AI):**
1. Kiểm tra từng mục một, bắt đầu từ các mục 🔴 Blocking.
2. Nếu PRD/Feature thiếu evidence-based justification, yêu cầu bổ sung data hoặc user research trước khi tiếp tục.
3. Nếu backlog item chưa có RICE score, tính toán và bổ sung ngay lập tức.
4. Nếu Experiment thiếu MCS, tự động tạo template MCS rỗng + cảnh báo 🔴 cho user.
5. Nếu OKR Key Result không SMART, ghi rõ yếu tố nào thiếu + đề xuất cải thiện.
6. Nếu Problem Statement chưa validate, cảnh báo 🔴 "Assumption chưa validate — cần user research trước khi commit."
7. Ghi chú số lần tự sửa vào log trước khi xuất ra output cuối cùng.
8. Sau khi hoàn tất, in ra báo cáo theo định dạng: **📋 Gate Report Output:** `Self-Review: Đã chạy [X] vòng kiểm tra, tự động sửa [Y] lỗi.`

