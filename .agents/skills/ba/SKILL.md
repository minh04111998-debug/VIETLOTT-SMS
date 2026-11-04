---
name: ba
description: Kỹ năng phân tích yêu cầu, tạo tài liệu nghiệp vụ, vẽ luồng Mermaid, và phân tích ngoại lệ
---

# Kỹ Năng: BA Requirements (Core Index)

## Mô Tả
Skill gốc cho vai trò Business Analyst. File này là **dispatch table** — AI đọc để biết cần nạp sub-skill nào cho task cụ thể.

> **📂 Shared resources (dùng chung cho tất cả BA sub-skills):**
> - `templates/email-templates.md` — Mẫu email giao tiếp Stakeholder
> - `.agents/skills/ba/templates/document-templates.md` — Mẫu SRS, Gap Analysis, NFR, Interface, Glossary...
> - `templates/diagram-templates.md` — Mẫu Mermaid: Activity, Decision, State, BPMN, Context
> - `references/analysis-frameworks.md` — Framework phân tích: Edge Case, 5 Whys, Impact Analysis
> - `references/babok-knowledge-areas.md` — BABOK® v3: 6 KAs, 50 Techniques
> - `examples/ba-examples.md` — Ví dụ thực tế

---

## Skill Dispatch Table

| Khi task liên quan đến... | Nạp skill | Mô tả |
|--------------------------|-----------|-------|
| Thu thập yêu cầu, viết SRS/BRD, Use Case, NFR, Scope, Glossary, Traceability | `ba-requirements` | Kỹ thuật elicitation & tài liệu hóa yêu cầu |
| Vẽ luồng Mermaid: Activity, State, BPMN, Context, Decision, Dependency | `ba-diagrams` | Visual modeling bằng Mermaid |
| Phân tích: Gap, Edge Cases, 5 Whys, SWOT, BABOK techniques nâng cao | `ba-analysis` | Phân tích nghiệp vụ nâng cao + BABOK KA5 |
| Change Request, Impact Analysis, Cascading Update, Version Control | `ba-change` | Change Management (CM) |
| Thẩm định chất lượng output SRS/Use Case/NFR theo chuẩn Senior BABOK v3 | `ba-review` | Thẩm định & kiểm soát chất lượng đầu ra BA |

---

## Quy Tắc Sử Dụng

1. **Không nạp tất cả sub-skills cùng lúc** — chỉ nạp skill cần thiết cho task
2. **Templates/References nằm trong thư mục `.agents/skills/ba/`** — các sub-skills tham chiếu ngược: `../ba/templates/...`
3. **Harness vẫn áp dụng** — mọi task vẫn tuân theo `workflows/requirement/ba-po-loop.md`
