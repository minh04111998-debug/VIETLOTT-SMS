---
description: Review thiết kế trước khi handoff cho DEV - Vai trò Designer
---

# Workflow: Design Review

> **Slash command**: `/design-review`
> **Vai trò**: `[🟣 ROLE: Designer]`
> **Khi nào dùng**: Review design trước khi handoff cho DEV implementation
> **Đầu ra**: Review report + Approved design + Handoff package

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🟣 ROLE: Designer]`
- **Nạp Rules:** `.agents/rules/designer-rules.md`
- **Nạp Skills:** `.agents/skills/designer/SKILL.md` (Skill 9: Design Handoff, Skill 8: Design Tokens)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

---

## Bước 1: Design Input

Hỏi người dùng:
```
1. Thiết kế cần review (Figma link, screenshot, hoặc file)?
2. User Story / SRS liên quan?
3. Design đã có responsive versions chưa?
4. Có design system / tokens nào đang dùng?
```

🛑 **[DỪNG]** — Thu thập design files

---

## Bước 2: Review Checklist

AI đánh giá design theo:
- **Consistency:** Có follow design system không? (Skill 3, 8)
- **Usability:** Nielsen's heuristics check (Skill 4)
- **Responsive:** Đủ breakpoints? (Skill 5)
- **Accessibility:** Contrast, touch targets, labels + WCAG 2.2 Compliance (Skill 12)
- **States:** Tất cả states có documented? (Default, Hover, Error, Loading, Empty)
- **Edge cases:** Long text, empty data, offline
- **Ethics:** Dark Patterns Blacklist + Anti-Manipulation Checklist (`designer-rules.md` §10)
  - 🚫 Confirmshaming, Roach Motel, Misdirection, Hidden Costs, Bait & Switch
  - □ User có thể undo mọi action? Pricing rõ ràng? Unsubscribe dễ?

🛑 **[DỪNG]** — *"Review findings. Có issues cần fix trước handoff?"*

---

## Bước 3: Design Handoff Package

Nếu design approved, tạo handoff package (Skill 9):
- Specifications document
- Design tokens export (Skill 8)
- Asset list
- Interaction notes

🛑 **[DỪNG]** — *"Handoff package ready. Approve để gửi DEV?"*

---

## Bước 4: Lưu Trữ

- Lưu review tại `artifacts/technical/design/review-[feature]-[date].md`
- Handoff tại `artifacts/technical/design/handoff-[feature].md`
- Thông báo: *"✅ Design approved + handoff ready for DEV."*
