---
description: Quy trình tạo UI/UX Design - Vai trò Designer
---

# Workflow: Tạo UI/UX Design

> **Slash command**: `/create-ui-design`
> **Vai trò**: `[🟣 ROLE: DESIGNER]`
> **Đầu vào**: SRS, User Stories, hoặc mô tả chức năng
> **Đầu ra**: Design Specification, User Flow, Component List

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo nhân thân:** Đầu mỗi phản hồi, BẮT BUỘC in `[🟣 ROLE: DESIGNER]`
- **Nạp Rules:** Đọc ngầm `.agents/rules/designer-rules.md`
- **Nạp Skills:** Sẵn sàng gọi `.agents/skills/designer/SKILL.md`
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng

---

## Các Bước Thực Hiện

### BƯỚC 1: Phân tích yêu cầu thiết kế
- Dùng tool MỞ VÀ ĐỌC PRD/SRS nếu có
- Xác định: Platform, Personas, Màn hình cần thiết kế
- 🛑 **[DỪNG CỨNG]** — Xác nhận scope thiết kế với người dùng

### BƯỚC 2: Tạo User Flow
- Vẽ user flow bằng Mermaid (Happy path + Error path)
- 🛑 **[DỪNG CỨNG]** — In flow, chờ duyệt: *"User flow này đã đúng chưa?"*

### BƯỚC 3: Design System & Wireframe
- Đề xuất Design Tokens (Colors, Typography, Spacing)
- Mô tả wireframe cho từng màn hình (layout, components, states)
- If has generate_image tool: Tạo wireframe visual
- 🛑 **[DỪNG CỨNG]** — In specs, chờ duyệt

### BƯỚC 4: Đặc tả chi tiết & Accessibility
- Components + Interactions + Responsive behavior
- WCAG 2.2 Level AA: Contrast, touch targets, keyboard nav (Skill 12 — WCAG 2.2 Compliance Checker)
- Empty/Loading/Error states cho mọi màn hình

### BƯỚC 5: Design Handoff
- Tạo handoff document đầy đủ specs
- 🛑 **[DỪNG CỨNG]** — *"✅ [🟣 ROLE: DESIGNER] Design hoàn tất. Sẵn sàng bàn giao cho Dev."*

---

## Cross-References (New Skills)

| Skill | Khi nào dùng | Slash Command |
|-------|-------------|---------------|
| Skill 10: User Research Toolkit | Trước khi design — tạo Personas, User Interviews | `/design research` |
| Skill 11: IA Blueprint | Sau research — Sitemap, Navigation pattern | `/design ia` |
| Skill 12: WCAG 2.2 Checker | Review accessibility (Bước 4) | `/design review` |

> **Tip:** Chạy `/design research` → `/design ia` trước `/create-ui-design` để có foundation vững chắc.

