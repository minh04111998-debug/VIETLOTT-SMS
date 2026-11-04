---
description: Quy trình nhập Design System từ Figma vào dự án - Vai trò Designer
---

# Workflow: Nhập Design System Từ Figma

> **Slash command**: `/import-design-system`
> **Vai trò**: `[🟣 ROLE: DESIGNER]`
> **Đầu vào**: Thông tin Design System (text, JSON, hoặc mô tả)
> **Đầu ra**: File `artifacts/technical/design/design-system-template.md` đã điền đầy đủ

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo nhân thân:** Đầu mỗi phản hồi, BẮT BUỘC in `[🟣 ROLE: DESIGNER]`
- **Nạp Rules:** Đọc ngầm `.agents/rules/designer-rules.md`
- **Nạp Skills:** Sẵn sàng gọi `.agents/skills/designer/SKILL.md`
- **Nạp Template:** Đọc `artifacts/technical/design/design-system-template.md` làm format chuẩn
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng

---

## Các Bước Thực Hiện

### BƯỚC 1: Xác định nguồn input
- Hỏi người dùng cung cấp Design System theo một trong các cách:
  - **Cách A**: Paste trực tiếp giá trị tokens (colors, fonts, spacing...)
  - **Cách B**: Cung cấp file JSON (export từ Tokens Studio for Figma plugin)
  - **Cách C**: Mô tả bằng lời (VD: "Dùng font Inter, màu chính xanh dương #2563EB...")
  - **Cách D**: Cung cấp screenshot của DS page trong Figma → AI phân tích
- 🛑 **[DỪNG CỨNG]** — Chờ người dùng cung cấp input

### BƯỚC 2: Parse và chuyển đổi format
- Đọc template từ `artifacts/technical/design/design-system-template.md`
- Parse input của người dùng thành format chuẩn theo template
- Điền các giá trị vào đúng chỗ trong template
- Nếu thiếu thông tin → ghi `[CHƯA CÓ - CẦN BỔ SUNG]` và liệt kê danh sách thiếu
- 🛑 **[DỪNG CỨNG]** — Hiển thị bản nháp, hỏi: *"Design System spec này đã chính xác chưa? Có cần bổ sung gì không?"*

### BƯỚC 3: Validate Design System
- Kiểm tra **contrast ratio** (WCAG AA):
  - Text trên background: ≥ 4.5:1
  - Text lớn trên background: ≥ 3:1
- Kiểm tra **completeness**:
  - [ ] Có đủ color tokens (primary, semantic, neutral)?
  - [ ] Có font family và type scale?
  - [ ] Có spacing scale?
  - [ ] Có border radius?
  - [ ] Có shadow tokens?
  - [ ] Có danh sách component?
- Nếu phát hiện vấn đề → báo cáo cho người dùng
- 🛑 **[DỪNG CỨNG]** — *"Validation hoàn tất. Có [N] vấn đề cần xem xét. Tiếp tục lưu file?"*

### BƯỚC 4: Lưu file chính thức
- Lưu file tại `artifacts/technical/design/design-system-template.md`
- Nếu file đã tồn tại → hỏi có muốn ghi đè không, hoặc tạo version mới
- 🛑 **[DỪNG CỨNG]** — *"✅ [🟣 ROLE: DESIGNER] Design System đã được lưu tại `artifacts/technical/design/design-system-template.md`. Tất cả workflows thiết kế UI sẽ tự động tuân thủ spec này."*

---

## Xử Lý JSON Input (Tokens Studio)

Nếu người dùng cung cấp JSON từ Tokens Studio plugin, parse theo mapping sau:

```
JSON Path                    → Template Token
────────────────────────────────────────────
global.colors.primary        → --color-primary
global.colors.secondary      → --color-secondary
global.fontFamilies.*        → Font Family table
global.fontSize.*            → Type Scale table
global.spacing.*             → Spacing Scale table
global.borderRadius.*        → Border Radius table
global.boxShadow.*           → Shadow table
```

---

## Lưu Ý Quan Trọng

- File `artifacts/technical/design/design-system-template.md` là **Single Source of Truth** cho Design System
- Khi DS thay đổi → chạy lại `/import-design-system` để cập nhật
- Sau khi cập nhật DS → nên chạy `/change-request` nếu ảnh hưởng đến UI đã thiết kế
- Các workflow khác (`/create-ui-design`, `/code-review`) sẽ tự động đọc file này
