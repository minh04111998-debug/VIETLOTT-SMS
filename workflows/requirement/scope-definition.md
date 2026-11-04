---
description: Quy trình xác định phạm vi hệ thống - Vai trò BA (BABOK KA4)
---

# Workflow: Scope Definition

> **Slash command**: `/scope-definition`
> **Vai trò**: `[🟢 ROLE: BA]`
> **Khi nào dùng**: Bắt đầu phân tích hệ thống/module mới — TRƯỚC `/create-srs`
> **Đầu ra**: Scope Document + Context Diagram tại `artifacts/requirements/`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🟢 ROLE: BA]`
- **Nạp Rules:** `ba-rules.md` (§4: Strategy Analysis)
- **Nạp Skills:** `.agents/skills/ba/SKILL.md` (§21: Scope Modeling)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

> [!CAUTION]
> Bỏ qua Scope Definition = mời scope creep vào dự án.
> "Nếu bạn không define boundary, stakeholder sẽ define nó cho bạn."

---

## Bước 1: Understand Context

AI hỏi:
```
1. Hệ thống/module cần phân tích phạm vi?
2. Mục tiêu business chính là gì? (BR level)
3. Có hệ thống hiện tại (As-Is) không? Nếu có, mô tả ngắn
4. External systems cần tích hợp? (APIs, databases, 3rd-party)
5. Users/actors chính?
6. Known constraints? (budget, timeline, technology, regulation)
```

🛑 **[DỪNG]** — Thu thập context

---

## Bước 2: Context Diagram

AI vẽ Context Diagram (system boundary):
- Hệ thống chính ở giữa
- External actors (users, systems) xung quanh
- Data flows giữa system và actors

Sử dụng Mermaid flowchart (ref: skills/ba §21)

🛑 **[DỪNG]** — Confirm Context Diagram

---

## Bước 3: Scope Statement

```markdown
## Scope Definition — [Tên Hệ Thống/Module]

### In Scope (Hệ thống SẼ làm)
| # | Chức năng / Capability | Priority (MoSCoW) | Notes |
|---|----------------------|-------------------|-------|
| 1 | [Chức năng 1] | Must | |
| 2 | [Chức năng 2] | Should | |

### Out of Scope (Hệ thống KHÔNG làm)
| # | Chức năng | Lý do loại trừ | Có thể xem xét khi |
|---|----------|---------------|-------------------|
| 1 | [Chức năng X] | Phase 2 / Hệ thống khác | Q3/2026 |

### External Systems (Tích hợp)
| System | Direction | Data exchanged | Protocol |
|--------|-----------|---------------|----------|

### Assumptions (Giả định)
1. [Giả định 1 — cần validate]
2. [Giả định 2]

### Constraints (Ràng buộc)
1. [Ràng buộc business]
2. [Ràng buộc kỹ thuật]
3. [Ràng buộc pháp lý]

### Risk Register (Sơ bộ)
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
```

🛑 **[DỪNG]** — Review Scope Statement

---

## Bước 4: As-Is vs To-Be (nếu có hệ thống hiện tại)

Gọi skill Gap Analysis (skills/ba §4):
- Vẽ As-Is process flow
- Vẽ To-Be process flow
- Tạo Gap Matrix

🛑 **[DỪNG]** — Confirm Gap Analysis

---

## Bước 4b: BA Governance (BABOK KA1)

> Xác định ai có quyền gì đối với requirements — TRƯỚC khi bắt đầu thu thập.

AI tạo RACI Matrix cho dự án/module:

```markdown
## Requirements Governance — [Tên Module]

### RACI Matrix
| Hoạt động                    | BA | PO | SA | PM | DEV | QA |
|------------------------------|----|----|----|----|-----|-----|
| Viết requirement             | R  | C  | C  | I  | I   | I  |
| Review requirement           | A  | C  | R  | I  | R   | R  |
| Approve requirement          | C  | A  | C  | R  | I   | I  |
| Thay đổi baselined req       | R  | A  | C  | A  | I   | I  |

### Escalation Path
BA → PM → PO → Sponsor

### Approval Authority
- BR: [Tên PO/Sponsor]
- FR/NFR: [Tên PO + SA]
- CR: [Tên PM + PO]
```

→ Ref: `ba-rules.md` §2.5 | Template: `.agents/skills/ba/templates/document-templates.md` §10
→ Nguồn: [BABOK® v3, KA1 Task 1.3](https://www.iiba.org/standards-and-resources/babok/)

---

## Bước 4c: BA Information Management (BABOK KA1)

> Xác định cách lưu trữ và quản lý requirement artifacts.

AI xác nhận với user:
```
1. Repository: Lưu tại file system (artifacts/requirements/ → artifacts/requirements/) hay tool khác?
2. Naming: Tuân thủ convention tại ba-rules.md §2.6?
3. Version Control: Major.Minor + change log header?
4. Access: Ai cần quyền đọc/sửa?
```

→ Ref: `ba-rules.md` §2.6
→ Nguồn: [BABOK® v3, KA1 Task 1.4](https://www.iiba.org/standards-and-resources/babok/)

---

## Bước 4d: Value Assessment Sơ Bộ (BABOK KA5)

> Đánh giá giá trị tiềm năng — TRƯỚC khi tốn effort phân tích chi tiết.

AI tạo Value Proposition Canvas (lightweight):

```markdown
## Value Assessment — [Tên Module]

| Mục                | Nội dung                          |
|--------------------|-----------------------------------|
| Problem            | [Vấn đề nghiệp vụ cần giải quyết] |
| Proposed Solution  | [Giải pháp high-level]            |
| Target Users       | [Ai? Số lượng?]                   |
| Expected Benefit   | [Lợi ích cụ thể]                  |
| Success KPI        | [Metric đo lường]                 |
| Cost Estimate      | [Effort ước tính]                 |
| Risk if NOT done   | [Rủi ro nếu không làm]           |
| Alternative        | [Workaround nào có thể?]         |

**Decision:** GO / NO-GO / NEED MORE DATA
```

🛑 **[DỪNG]** — Review Value Assessment. Hỏi: *"Giá trị tiềm năng đủ justify effort? GO hay NO-GO?"*

→ Ref: `.agents/skills/ba/references/babok-knowledge-areas.md` KA5 — Analyze Potential Value
→ Nguồn: [BABOK® v3, KA5 Task 6.6](https://www.iiba.org/standards-and-resources/babok/)

---

## Bước 5: Lưu trữ

- Lưu tại `artifacts/requirements/scope-[tên-module].md`
- Bao gồm: Context Diagram + Scope Statement + Gap Analysis + RACI + Value Assessment
- 🛑 **[DỪNG CỨNG]** — *"Scope Definition nháp đã lưu. Phê duyệt để baseline?"*
- Sau khi duyệt → `artifacts/requirements/scope-[tên-module].md`
- Thông báo: *"Scope đã baseline. Bước tiếp: `/create-srs` hoặc `/create-brd`"*
