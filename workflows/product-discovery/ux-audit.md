---
description: Thực hiện UX Audit cho sản phẩm hiện tại - Vai trò Designer
---

# Workflow: UX Audit

> **Slash command**: `/ux-audit`
> **Vai trò**: `[🟣 ROLE: Designer]`
> **Khi nào dùng**: Đánh giá UX sản phẩm hiện tại, tìm vấn đề usability
> **Đầu ra**: UX Audit Report + Prioritized Recommendations

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🟣 ROLE: Designer]`
- **Nạp Rules:** `.agents/rules/designer-rules.md` (đặc biệt §1.3 Usability)
- **Nạp Skills:** `.agents/skills/designer/SKILL.md` (Skill 4: Usability Review, Skill 7: UX Audit)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

---

## Bước 1: Audit Scope

Hỏi người dùng:
```
1. Audit toàn bộ product hay specific screens/flows?
2. Có link dev/staging để audit trực tiếp không?
3. Target users là ai? (Demographics, tech savvy level)
4. Có complaints/feedback cụ thể nào từ users không?
5. Focus areas? (Onboarding, Checkout, Navigation, Forms...)
```

🛑 **[DỪNG]** — Thu thập scope

---

## Bước 2: Heuristic Evaluation

Dùng Skill 4 (Nielsen's 10 Heuristics) + Skill 7 (UX Audit):
- Đánh giá từng heuristic cho mỗi screen/flow
- Score 1-5 cho mỗi heuristic
- Document findings: screen, issue, severity

Nếu có link dev → Dùng `browser_subagent` để screenshots + walkthrough.

🛑 **[DỪNG]** — *"Findings draft. Review trước khi recommendations?"*

---

## Bước 3: Cognitive Walkthrough

- Walk through key user flows: Registration, Login, Core feature
- Đánh giá từng step: "User có biết phải làm gì tiếp theo?"
- Xác định pain points và drop-off risks

🛑 **[DỪNG]** — *"Walkthrough OK? Có flow nào cần thêm?"*

---

## Bước 4: Recommendations

- Prioritize findings: Quick wins vs Long-term
- Estimate fix effort (Low/Medium/High)
- Tạo UX Audit Report hoàn chỉnh (Skill 7 template)
- Đề xuất A/B tests cho controversial changes
- **HEART Metrics Baseline** (`designer-rules.md` §11):
  - Đo Happiness (SUS/NPS), Engagement (DAU/MAU), Adoption, Retention, Task Success
  - Set quantitative targets: Task completion ≥ 78%, Error rate < 10%
  - Compare pre/post audit scores

🛑 **[DỪNG]** — Review final report

---

## Bước 5: Lưu Trữ

- Lưu tại `artifacts/technical/design/ux-audit-[product]-[date].md`
- Thông báo: *"✅ UX Audit complete. [N] issues found, [M] quick wins."*
