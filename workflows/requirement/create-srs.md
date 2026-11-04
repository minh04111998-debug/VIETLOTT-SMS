---
description: Quy trình tạo Software Requirements Specification (SRS) - Vai trò BA
---

# Workflow: Tạo SRS (Software Requirements Specification)

> **Slash command**: `/create-srs`
> **Vai trò**: `[🟢 ROLE: BA]`
> **Đầu vào**: PRD, thông tin yêu cầu, wireframe/mockup (nếu có)
> **Đầu ra**: File SRS hoàn chỉnh tại `artifacts/requirements/srs-[tên-module].md`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo nhân thân:** Đầu mỗi phản hồi, BẮT BUỘC in `[🟢 ROLE: BA]`
- **Nạp Rules:** Đọc ngầm `.agents/rules/ba-rules.md` (Mindset: Tech-Agnostic, No Hallucination, BDD)
- **Nạp Skills:** Sẵn sàng gọi `.agents/skills/ba/SKILL.md`
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng

---

## Các Bước Thực Hiện

### BƯỚC 1: Thu thập và phân tích yêu cầu
- Nếu đã có PRD: Dùng tool MỞ VÀ ĐỌC LẠI file PRD. TUYỆT ĐỐI tuân thủ file này.
- Nếu chưa có PRD: Hỏi người dùng về hệ thống, chức năng, actors, quy trình
- Gọi kỹ năng **Analyze Edge Cases** để rà soát 5 nhóm ngoại lệ
- 🛑 **[DỪNG CỨNG]** — Xác nhận phạm vi và danh sách Use Cases với người dùng

### BƯỚC 2: Vẽ Diagrams
- Gọi kỹ năng **Vẽ Mermaid Flow** để tạo:
  - **Use Case Diagram**: Tổng quan hệ thống
  - **Activity Diagram**: Cho mỗi Use Case phức tạp
  - **ERD**: Mô hình dữ liệu (nếu cần)
- 🛑 **[DỪNG CỨNG]** — In diagrams và hỏi: *"Các sơ đồ này đã chuẩn chưa?"*

### BƯỚC 3: Viết SRS chi tiết
- Cho mỗi Use Case, viết đầy đủ:
  - **Phần A**: Mô tả chức năng (Main Flow, Alternative, Exception, Business Rules)
  - **Phần B**: Wireframe/Mockup reference
  - **Phần C**: Đặc tả giao diện (Interface Specification table)
- Acceptance Criteria: BẮT BUỘC format Gherkin (Given/When/Then)
- **[BẮT BUỘC]** Nếu Use Case có gọi external system:
  - Phải kèm **Exception Analysis Table** → template tại `.agents/skills/ba/templates/document-templates.md` §6b
  - Phải kèm **Timeout & Hung State Checklist** → template tại `.agents/skills/ba/templates/document-templates.md` §6c
  - Phải trả lời 7 câu hỏi Timeout (ba-rules §3.6) cho mỗi bước gọi external
- Gọi kỹ năng **Analyze Edge Cases** (8 nhóm bao gồm Timeout/Retry/Integration Failure)
- 🛑 **[DỪNG CỨNG]** — Trình bày SRS draft để review. **Kiểm tra:** Exception Table + Timeout Checklist đã đầy đủ chưa?

### BƯỚC 4: Tạo Traceability Matrix
- Liên kết: BR → FR → UC → US → TC
- Đảm bảo mọi yêu cầu đều được trace

### BƯỚC 5: Lưu trữ & Baseline
- Lưu file SRS **nháp** tại `artifacts/requirements/srs-[tên-module].md` (sau khi duyệt → chuyển sang `artifacts/requirements/`)
- Ghi nhận lịch sử thay đổi
- 🛑 **[DỪNG CỨNG]** — In ra: *"✅ [🟢 ROLE: BA] SRS nháp đã lưu tại `artifacts/requirements/`. Phê duyệt để tôi chuyển sang `artifacts/requirements/` và baseline?"*
- Sau khi được phê duyệt → **Chuyển file** từ `artifacts/requirements/` sang `artifacts/requirements/srs-[tên-module].md`
- Thông báo: *"SRS đã baseline. Bước tiếp theo: `/create-ui-design` hoặc `/architecture-review`"*
