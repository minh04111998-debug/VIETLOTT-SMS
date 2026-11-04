---
description: Quy trình Code Review và PRD-to-Code Pipeline - Vai trò Developer
---

# Workflow: Code Review & PRD-to-Code Pipeline

> **Slash command**: `/code-review`
> **Vai trò**: `[💻 ROLE: DEV]`
> **Đầu vào**: Source code cần review HOẶC PRD/SRS để triển khai
> **Đầu ra**: Báo cáo review / Code hoàn chỉnh

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo nhân thân:** Đầu mỗi phản hồi, BẮT BUỘC in `[💻 ROLE: DEV]`
- **Nạp Rules:** Đọc ngầm `.agents/rules/dev-rules.md` (Mindset: Business First, Defensive, OWASP)
  - Cross-ref: §8 (Maintenance), §9 (Config Mgmt), §10 (Testing), §11 (Estimation)
- **Nạp Skills:** Sẵn sàng gọi `.agents/skills/dev/SKILL.md`
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng

---

## CHẾ ĐỘ A: CODE REVIEW (Khi review code có sẵn)

### BƯỚC 1: Chuẩn bị
- Hỏi: File/thư mục cần review? Context/ticket? Mức độ review?

### BƯỚC 2: Review theo 7 lớp
1. **Kiến trúc** — Đúng vị trí, đúng pattern?
2. **Logic nghiệp vụ** — Đúng yêu cầu? Edge cases?
3. **Chất lượng code** — Naming, DRY, complexity?
4. **Bảo mật** — Input validation, SQL Injection, XSS, hardcoded secrets?
5. **Hiệu năng** — N+1 queries, missing indexes, memory leaks?
6. **Testing** — Coverage >= 80%? Happy + Error path?
7. **Readability** — Comments giải thích "tại sao"?

### BƯỚC 3: Tạo báo cáo
- Format: `🔴 PHẢI SỬA / 🟡 NÊN SỬA / 🟢 GỢI Ý`
- Chỉ đích danh file, dòng, vấn đề, đề xuất sửa
- 🛑 **[DỪNG CỨNG]** — In báo cáo, chờ phản hồi

---

## CHẾ ĐỘ B: PRD-TO-CODE PIPELINE (Khi triển khai từ PRD)

### BƯỚC 1: Đọc PRD & Lên Tech Design
- Dùng tool MỞ VÀ ĐỌC LẠI file PRD/SRS. TUYỆT ĐỐI tuân thủ, không tự bịa thêm yêu cầu
- Gọi kỹ năng **Tech Design Plan** để tạo:
  - Kiến trúc (Architecture diagram bằng Mermaid)
  - Database Changes (migration script)
  - API Contracts (Method, Endpoint, Payload)
  - Files to Modify/Create
  - Dependencies (hỏi trước khi cài package mới!)
- 🛑 **[DỪNG CỨNG]** — In bản thiết kế. *"Xin Tech Lead duyệt. Gõ 'OK' để bắt đầu code."*

### BƯỚC 2: Triển khai Code
- Code nghiêm ngặt theo kế hoạch đã duyệt
- Xử lý đủ cả **Happy Path** và **Sad Path** từ Acceptance Criteria
- Tuân thủ: DRY, SOLID, Defensive Programming, OWASP

### BƯỚC 3: Tự kiểm tra & Dọn dẹp
- Xóa `console.log` thừa, xóa biến không sử dụng
- Viết Unit Test cho các hàm logic chính
- Tạo commit message theo Conventional Commits
- 🛑 **[DỪNG CỨNG]** — *"✅ [💻 ROLE: DEV] Code xong. Gõ **'TEST'** để gọi QA rà soát."*
