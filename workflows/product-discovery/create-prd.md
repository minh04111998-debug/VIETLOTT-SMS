---
description: Quy trình tạo Product Requirements Document (PRD) - Vai trò PO
---

# Workflow: Tạo PRD (Product Requirements Document)

> **Slash command**: `/create-prd`
> **Vai trò**: `[🔵 ROLE: PO]` (PO owns PRD, BA assists với elicitation & AC)
> **Đầu vào**: Mô tả sản phẩm/tính năng từ người dùng, Problem Statement (nếu đã qua `/product-discovery`)
> **Đầu ra**: File PRD hoàn chỉnh tại `artifacts/requirements/prd-[tên-tính-năng].md`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo nhân thân:** Đầu mỗi phản hồi, BẮT BUỘC in `[🔵 ROLE: PO]`
- **Nạp Rules:** Đọc ngầm file `.agents/rules/po-rules.md`
- **Nạp Skills:** Sẵn sàng gọi `.agents/skills/ba/SKILL.md` (Elicitation, Edge Case Analysis) + `.agents/skills/po/SKILL.md`
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng

---

## Các Bước Thực Hiện

### BƯỚC 0: Xác định Methodology
- Hỏi người dùng: *"Dự án này chạy theo **Agile/Scrum** hay **Waterfall**?"*
- Nếu **Agile** → Output PRD với **User Stories** + **Acceptance Criteria (Given/When/Then)** + Story Points
- Nếu **Waterfall** → Output PRD với **Use Cases** (Main Flow / Alt Flow / Exception Flow) + Đặc tả giao diện + Man-day estimate
- Nếu không chỉ định → Mặc định **Agile**
- *Ghi nhớ methodology đã chọn cho các bước sau*

### BƯỚC 1: Phân tích & Phản biện (Clarification)
- Đọc kỹ thông tin đầu vào từ người dùng
- Đóng vai BA khó tính, đặt **TỐI ĐA 5 CÂU HỎI** sắc bén nhất để làm rõ:
  - Mục tiêu kinh doanh (Business Goal)
  - Đối tượng người dùng (Target Users / Personas)
  - Vấn đề cần giải quyết (Pain points)
  - Ràng buộc (Timeline, ngân sách, kỹ thuật, pháp lý)
  - Logic ẩn chưa được nhắc tới (Hidden assumptions)
- 🛑 **[DỪNG CỨNG]** — Chờ người dùng trả lời các câu hỏi

### BƯỚC 2: Mô hình hóa Nghiệp vụ (Visualizing Flow)
- Tổng hợp câu trả lời ở Bước 1
- Gọi kỹ năng **Vẽ Mermaid Flow** để vẽ sơ đồ luồng nghiệp vụ tổng quan
- Gọi kỹ năng **Analyze Edge Cases** để tìm lỗ hổng/ngoại lệ
- 🛑 **[DỪNG CỨNG]** — In biểu đồ ra và hỏi: *"Sơ đồ này đã chuẩn xác chưa? Có cần bổ sung nhánh nào không?"*

### BƯỚC 3: Viết khung PRD & Lên danh sách Story (Drafting)
- Dựa trên luồng đã chốt, viết PRD theo template:

```markdown
# PRD - [Tên Sản Phẩm/Tính Năng]

## 1. Tổng Quan
### 1.1. Mục đích / 1.2. Background / 1.3. Mục tiêu & KPIs

## 2. Đối Tượng Người Dùng (Personas)
| Persona | Vai trò | Nhu cầu | Pain points |

## 3. Phạm Vi (Must/Should/Could/Won't)

## 4. Yêu Cầu Chức Năng
### Feature N: [Tên]
- User Stories: Là [...], tôi muốn [...], để [...]
- Acceptance Criteria: Given-When-Then
- Priority: Must/Should/Could

## 5. Yêu Cầu Phi Chức Năng

## 6. Luồng Nghiệp Vụ (Mermaid Diagram)

## 7. Ngoại Lệ & Edge Cases (bảng 5 nhóm)

## 8. Timeline & Milestones

## 9. Rủi Ro
```

- Bóc tách tính năng thành **danh sách User Stories** (chỉ tiêu đề)
- Tự động đề xuất thêm Stories xử lý lỗi/ngoại lệ
- 🛑 **[DỪNG CỨNG]** — Hỏi: *"Danh sách Stories có cần thêm/bớt gì không?"*

### BƯỚC 4: Chi tiết hóa User Stories
- Duyệt từng Story đã chốt, viết chi tiết:
  - **Description:** `Là [vai trò], tôi muốn [hành động], để [mục đích]`
  - **Acceptance Criteria:** `Given... When... Then...` (Happy path + Sad path)
  - Tuân thủ INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable)

### BƯỚC 5: Lưu trữ & Bàn giao
- Lưu file PRD **nháp** tại `artifacts/requirements/prd-[tên-tính-năng].md`
- 🛑 **[DỪNG CỨNG]** — In ra: *"✅ [🔵 ROLE: PO] Đã lưu PRD nháp tại `artifacts/requirements/`. Phê duyệt để tôi chuyển sang `artifacts/requirements/`?"*
- Sau khi được phê duyệt → **Chuyển file** từ `artifacts/requirements/` sang `artifacts/requirements/prd-[tên-tính-năng].md`
- Thông báo: *"PRD đã baseline. Bước tiếp theo: `/create-srs` (nếu Waterfall) hoặc `/create-ui-design` (nếu Agile)"*
