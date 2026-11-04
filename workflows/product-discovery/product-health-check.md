---
description: Quy trình kiểm tra sức khỏe sản phẩm định kỳ - Vai trò PO
---

# Workflow: Product Health Check

> **Slash command**: `/product-health-check`
> **Vai trò**: `[🔵 ROLE: PO]`
> **Khi nào dùng**: Monthly/Quarterly review, khi metrics đi xuống, chuẩn bị OKR review
> **Đầu ra**: Product Health Report tại `artifacts/product/health-checks/`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🔵 ROLE: PO]`
- **Nạp Rules:** `po-rules.md` (§9: Metrics)
- **Nạp Skills:** `.agents/skills/po/SKILL.md` (POA-D1: Foundational, POA-D4: Make Impact, POA-D7: Value)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

---

## Bước 1: Gather Metrics Data

AI hỏi:
```
1. Product cần health check?
2. Period: Month [X] / Quarter [X]?
3. Cung cấp data hiện có:
   - North Star Metric: [value]
   - AARRR metrics (nếu có): Acquisition / Activation / Retention / Referral / Revenue
   - HEART metrics (nếu có): Happiness / Engagement / Adoption / Retention / Task Success
4. OKR progress (nếu có)?
5. Notable events trong period? (launches, incidents, market changes)
```

🛑 **[DỪNG]** — Thu thập data

---

## Bước 2: AARRR Funnel Analysis

```markdown
## AARRR Funnel — [Product] — [Period]

| Stage | Metric | Previous | Current | Trend | Status |
|-------|--------|----------|---------|-------|--------|
| Acquisition | New users/month | [X] | [Y] | ↑/↓/→ | 🟢/🟡/🔴 |
| Activation | Onboarding completion | [X%] | [Y%] | | |
| Retention | D30 retention | [X%] | [Y%] | | |
| Referral | NPS | [X] | [Y] | | |
| Revenue | MRR/ARR | [X] | [Y] | | |

### Funnel Leak Analysis
- Biggest drop-off: [Stage A → Stage B] ([ ]% loss)
- Root cause hypothesis: [Why users drop here?]
- Proposed experiment: [What to test?]
```

---

## Bước 3: Feature Adoption Review

```markdown
## Feature Adoption — [Period]

| Feature | Launch Date | Target Adoption | Actual | Status | Action |
|---------|-----------|----------------|--------|--------|--------|
| [Feature 1] | [Date] | [X%] | [Y%] | ✅/❌ | Keep/Enhance/Kill |

### Unused Features (< 5% adoption after 30 days)
| Feature | Adoption | Decision | Rationale |
|---------|----------|----------|-----------|
```

---

## Bước 4: OKR Progress (nếu có)

```markdown
## OKR Progress — Q[N]

| Objective | KR | Target | Current | Score (0-1.0) | On Track? |
|-----------|----|---------|---------|-----------|----|

### At-Risk KRs
| KR | Gap | Recovery Plan |
|----|-----|---------------|
```

🛑 **[DỪNG]** — Review health check data

---

## Bước 5: Health Score & Action Plan

```markdown
## Product Health Score — [Product] — [Period]

| Dimension | Score (1-5) | Trend | Key Issue |
|-----------|-----------|-------|-----------|
| Growth (Acquisition) | /5 | ↑/↓ | |
| Engagement (Activation + Retention) | /5 | | |
| Satisfaction (NPS/CSAT) | /5 | | |
| Revenue | /5 | | |
| Feature Velocity | /5 | | |
| **Overall** | **/25** | | |

### Interpretation
- ≥ 20/25: 🟢 Healthy — maintain course
- 15-19: 🟡 Needs attention — address specific issues
- < 15: 🔴 At risk — strategic review needed

### Top 3 Actions for Next Period
| # | Action | Owner | Expected Impact | Deadline |
|---|--------|-------|----------------|----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
```

- Lưu tại `artifacts/product/health-checks/health-[product]-[period].md`
