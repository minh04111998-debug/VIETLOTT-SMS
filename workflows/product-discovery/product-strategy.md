---
description: Quy trình xây dựng Product Vision & Strategy - Vai trò PO
---

# Workflow: Product Strategy

> **Slash command**: `/product-strategy`
> **Vai trò**: `[🔵 ROLE: PO]`
> **Khi nào dùng**: Bắt đầu product mới, annual/quarterly planning, re-align direction
> **Đầu ra**: Product Vision + Strategic Roadmap tại `artifacts/product/strategy/`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🔵 ROLE: PO]`
- **Nạp Rules:** `po-rules.md` (§1: Foundation, §3: Lifecycle, §7: Vision)
- **Nạp Skills:** `.agents/skills/po/SKILL.md` (POA-D1: Foundational, POA-D4: Make Impact)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

---

## Bước 1: Context & Assessment

AI hỏi:
```
1. Product/Feature area cần strategic planning?
2. Product đang ở lifecycle stage nào? (Introduction/Growth/Maturity/Decline)
3. Có Product Vision hiện tại không? Nếu có, cần update hay tạo mới?
4. Target users/personas chính?
5. North Star Metric hiện tại? (nếu chưa có → cần define)
6. Competition landscape: đối thủ chính?
```

🛑 **[DỪNG]** — Thu thập context

---

## Bước 2: PO Type Assessment

AI xác định PO hat phù hợp (POA-D1.1):
- Discovery / Delivery / Growth → strategy khác nhau
- Product vs Project context

---

## Bước 3: Product Lifecycle Analysis

AI thực hiện Lifecycle Assessment (POA-D1.2):
- User growth trend
- Revenue trend
- Market competition stage
- Strategy recommendation theo stage

🛑 **[DỪNG]** — Confirm lifecycle assessment

---

## Bước 4: Product Vision Board

AI tạo Product Vision Board (POA-D4.1):
```markdown
## Product Vision Board — [Product Name]

**VISION:** [1 câu inspiring]
**TARGET GROUP:** [Persona cụ thể]
**NEEDS:** [Top 3 JTBD/Pain Points]
**PRODUCT:** [Unique solution]
**BUSINESS GOALS:** [Revenue/Market/Strategic]
**NORTH STAR METRIC:** [1 metric]
**SUPPORTING METRICS:** [3-5 metrics]
```

Nếu cần: tạo Lean Canvas (POA-D1.2)

🛑 **[DỪNG]** — Review Vision Board

---

## Bước 5: Strategic Roadmap

AI tạo 3-Horizon Roadmap (POA-D4.1):

```markdown
## NOW (Q[Current]) — Committed, High Confidence
## NEXT (Q[Current+1]) — Directional, Medium Confidence
## LATER (6+ months) — Themes only, Low Confidence
```

🛑 **[DỪNG]** — Review roadmap

---

## Bước 6: Lưu trữ

- Lưu tại `artifacts/product/product-strategy-[tên].md`
- 🛑 **[DỪNG CỨNG]** — *"Strategy nháp đã lưu. Phê duyệt để baseline?"*
- Sau khi duyệt → `artifacts/product/strategy/product-strategy-[tên].md`
