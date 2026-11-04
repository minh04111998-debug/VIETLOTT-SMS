---
name: po
description: Kỹ năng Product Ownership Analysis theo IIBA POA Framework — 7 Domains, 29+ Techniques. Chuẩn bị cho CPOA Certification.
---

# Kỹ Năng: Product Ownership Analysis (Core Index)

## Mô Tả
Skill gốc cho vai trò Product Owner. File này là **dispatch table** — AI đọc để biết cần nạp sub-skill nào.

> **📂 Shared resources (dùng chung cho tất cả PO sub-skills):**
> - `.agents/skills/po/templates/product-templates.md` — Mẫu tài liệu cho tất cả 7 domains
> - `references/po-frameworks.md` — Chi tiết kỹ thuật & frameworks theo 7 domains
> - `references/tech-awareness.md` — Kiến thức kỹ thuật cho PO
> - `references/cpoa-study-guide.md` — Hướng dẫn ôn thi CPOA
> - `examples/po-examples.md` — Ví dụ thực tế SaaS B2B
>
> **Nguồn:** [IIBA Guide to Product Ownership Analysis](https://www.iiba.org/business-analysis-certifications/product-ownership-analysis/)

---

## CPOA Exam Domain Weights

| Domain | Weight | Sub-skill |
|--------|:------:|-----------|
| D1: Apply Foundational Concepts | 10% | `po-discovery` |
| D2: Cultivate Customer Intimacy | 15% | `po-discovery` |
| D3: Engage the Whole Team | 15% | `po-discovery` |
| D4: Make an Impact | 15% | `po-delivery` |
| D5: Deliver Often | 15% | `po-delivery` |
| D6: Learn Fast | 15% | `po-metrics` |
| D7: Obsess About Value | 15% | `po-metrics` |

---

## Skill Dispatch Table

| Khi task liên quan đến... | Nạp skill | Domains |
|--------------------------|-----------|---------|
| Product discovery, customer research, personas, market analysis, team engagement, stakeholder management | `po-discovery` | D1 + D2 + D3 |
| Product strategy, backlog, releases, story mapping, prioritization, delivery | `po-delivery` | D4 + D5 |
| Experiments, MVP, metrics, OKR, value optimization, learning loops | `po-metrics` | D6 + D7 |
| Thẩm định chất lượng output PRD, Discovery, RICE, MVP theo chuẩn Senior IIBA POA | `po-review` | Audit & Review |

---

## Quy Tắc Sử Dụng
1. **Không nạp tất cả sub-skills cùng lúc** — chỉ nạp skill cần thiết
2. **Templates/References nằm trong `.agents/skills/po/`** — sub-skills tham chiếu: `../po/templates/...`
3. **Harness vẫn áp dụng** — mọi task tuân theo `workflows/requirement/ba-po-loop.md`
