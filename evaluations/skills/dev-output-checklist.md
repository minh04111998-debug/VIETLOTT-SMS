# 📋 DEV Output Checklist

> **Vai trò sử dụng:** `[💻 ROLE: DEV]`
> **Mục đích:** DEV sử dụng checklist này để tự kiểm tra chất lượng code (Self-Correction) trước khi trình User hoặc chuyển sang QA. Nếu fail bất kỳ mục 🔴 Blocking nào, AI PHẢI tự sửa và ghi log. Tham chiếu 8-Gate từ `dev-rules.md`.

| # | Tiêu chí kiểm tra | Mức độ |
|---|-------------------|--------|
| 1 | **Functional:** AC đúng, bao gồm happy + error + edge cases | 🔴 Blocking |
| 2 | **Code Quality:** Không có duplicate code, ≤30 dòng/function, ≤3 mức nesting | 🔴 Blocking |
| 3 | **Error Handling:** Đã try-catch cho các external calls, xử lý timeout, hỗ trợ retry idempotent | 🔴 Blocking |
| 4 | **Security:** Có input validation, không SQL/Command injection, có kiểm tra auth/authz | 🔴 Blocking |
| 5 | **Observability:** Có structured log (JSON), correlation ID, health check | 🔴 Blocking |
| 6 | **Testing:** Unit test bao phủ logic cốt lõi ≥80%, có integration test cho API | 🔴 Blocking |
| 7 | **Performance:** Không N+1 query, đã phân trang, dùng index, không chặn I/O | 🔴 Blocking |
| 8 | **Deployability:** Có migration (kèm rollback), cấu hình externalized (env), file lock (package-lock.json) | 🔴 Blocking |
| 9 | Kiến trúc code không vi phạm nguyên tắc trong ADR đã chốt | 🔴 Blocking |
| 10 | Không còn TODO/FIXME/HACK nào trong code chưa được giải thích hợp lý | 🟡 Important |
| 11 | Commit message tuân thủ Conventional Commits | 🟢 Minor |

---

**Cách thực hiện (Dành cho AI):**
1. Quét code bạn vừa viết qua tất cả 11 tiêu chí trên.
2. Với các mục có vi phạm, hãy tiến hành Refactor/Cập nhật code ngay lập tức (không đợi review).
3. Sau khi pass hết các mục Blocking, in ra `Gate Report Output` theo template ở `dev-rules.md`.
