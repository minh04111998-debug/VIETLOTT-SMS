---
description: Quy trình quản lý stakeholder và giải quyết xung đột ưu tiên - Vai trò PO
---

# Workflow: Stakeholder Alignment

> **Slash command**: `/stakeholder-alignment`
> **Vai trò**: `[🔵 ROLE: PO]`
> **Khi nào dùng**: Conflict ưu tiên, HiPPO override, cần defend product decision
> **Đầu ra**: Stakeholder Map + Decision Record tại `artifacts/product/stakeholders/`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🔵 ROLE: PO]`
- **Nạp Rules:** `po-rules.md` (§6: Stakeholder Management)
- **Nạp Skills:** `.agents/skills/po/SKILL.md` (POA-D3: Engage the Whole Team)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

---

## Bước 1: Situation Assessment

AI hỏi:
```
1. Tình huống cần alignment là gì? (conflict / new stakeholder / decision defense)
2. Stakeholders liên quan? (tên, vai trò, vị trí)
3. Quyết định cần bảo vệ / đàm phán là gì?
4. Data/evidence hiện có? (RICE scores, user data, analytics)
5. Có pressure/deadline nào không?
```

🛑 **[DỪNG]** — Thu thập context

---

## Bước 2: Stakeholder Mapping

AI tạo Stakeholder Map (POA-D3.1):

```markdown
## Stakeholder Map — [Situation]

| Stakeholder | Role | Power | Interest | Current Position | Strategy |
|-------------|------|-------|----------|-----------------|----------|
```

Xác định:
- Ai ủng hộ? Ai phản đối? Ai trung lập?
- Key influencer là ai?

---

## Bước 3: Prepare Defense / Negotiation

Tùy tình huống:

### Nếu Conflict Ưu Tiên:
AI chuẩn bị RICE comparison và trade-off analysis

### Nếu HiPPO Override:
AI chuẩn bị "Experiment Proposal" (ref: po-rules.md §6.2)

### Nếu Defend Decision:
AI chuẩn bị defense template (ref: po-rules.md §6.3)

🛑 **[DỪNG]** — Review preparation

---

## Bước 4: Communication Plan

```markdown
## Communication Plan — [Situation]

| Stakeholder | Message Key Point | Channel | When | Owner |
|-------------|------------------|---------|------|-------|

### Meeting Agenda (nếu cần meeting)
| # | Topic | Duration | Goal (Inform/Discuss/Decide) |
|---|-------|----------|------------------------------|
```

---

## Bước 5: Document Decision

```markdown
## Decision Record — [Date]

**Context:** [Mô tả tình huống]
**Stakeholders:** [Danh sách]
**Options Considered:**
- Option A: [Mô tả] — Pros/Cons
- Option B: [Mô tả] — Pros/Cons

**Decision:** [Option được chọn]
**Rationale:** [Lý do, data support]
**Decided By:** [Tên + vai trò]
**Trade-offs Accepted:** [Rủi ro/hạn chế chấp nhận]
**Review Date:** [Khi nào review lại quyết định này?]
```

- Lưu tại `artifacts/product/stakeholders/decision-[date]-[topic].md`
