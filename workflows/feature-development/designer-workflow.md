---
description: Quy trình Designer end-to-end — Từ UX audit đến design review. Gọi `/design` chạy full, `/design [step]` chạy 1 step.
---

# 🟣 Designer Master Workflow

> **Full flow:** `/design` → Chạy tất cả 7 steps tuần tự
> **Từng step:** `/design ui` hoặc `/create-ui-design` → Chạy 1 step cụ thể
> **Vai trò:** `[🟣 ROLE: DESIGNER]`

---

## CHỈ THỊ CHO AI

- **Khai báo:** `[🟣 ROLE: DESIGNER]`
- **Nạp Rules:** `.agents/rules/designer-rules.md`
- **Nạp Skills:** `.agents/skills/designer/SKILL.md` (lazy-load)
- **Dừng cứng:** 🛑 sau mỗi step

---

## Tổng Quan 7 Steps

| Step | Tên | Slash shortcut | Output |
|------|-----|----------------|--------|
| 1 | UX Audit | `/design audit` hoặc `/ux-audit` | ux-audit-report.md |
| 2 | User Research & Personas | `/design research` | personas.md, interview-notes.md |
| 3 | Information Architecture | `/design ia` | sitemap.md, navigation-spec.md |
| 4 | Create UI Design | `/design ui` hoặc `/create-ui-design` | ui-[tên].md |
| 5 | Design System | `/design system` hoặc `/import-design-system` | design-system.md |
| 6 | Design Review | `/design review` hoặc `/design-review` | review-report.md |
| 7 | Handoff to DEV | `/design handoff` | handoff-spec.md |

---

## STEP 1: UX Audit → Xem [ux-audit.md](ux-audit.md)
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 2: User Research & Personas
- Tạo User Personas (Skill 10 — Persona Template)
- Thực hiện User Interviews (Skill 10 — 5-question starter)
- Deliverables: Persona cards, Empathy Map, Interview synthesis
- **Ref:** `designer-rules.md` §8 (User Research Rules)
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 3: Information Architecture
- Tạo Sitemap (Skill 11 — Mermaid template)
- Xác định Navigation pattern (Skill 11 — Navigation Decision)
- Content hierarchy: F-pattern / Z-pattern
- **Ref:** `designer-rules.md` §9 (IA Rules — Rosenfeld & Morville)
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 4: Create UI Design → Xem [create-ui-design.md](create-ui-design.md)
→ User Flow (Mermaid) → Design System → Wireframe → Mockup → Interaction Spec
🛑 Gõ **'NEXT'** | **'STOP'**

## STEP 5: Design System → Xem [import-design-system.md](import-design-system.md)
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 6: Design Review → Xem [design-review.md](design-review.md)
→ Cross-Review: BA (match AC?), QA (responsive? error states?), PO (persona fit?)
🛑 Gõ **'NEXT'** | **'STOP'**

## STEP 7: Handoff to DEV
- Export design tokens, spacing, typography
- Annotate interactive states + responsive breakpoints
- Lưu → `artifacts/technical/design/ui-[tên].md`
🛑 **🎉 DESIGN FLOW HOÀN TẤT.**

---

## Hướng Dẫn
| Lệnh | Hành vi |
|-------|---------| 
| `/design` | Full flow 7 steps |
| `/design audit` | Step 1 only |
| `/design research` | Step 2 only |
| `/design ia` | Step 3 only |
| `/design ui` | Step 4 only |
| `/design system` | Step 5 only |
| `/design review` | Step 6 only |
| `/design handoff` | Step 7 only |
| `/create-ui-design` | Alias → `/design ui` |
| Điều khiển | `NEXT` / `SKIP` / `STOP` / `BACK` |
