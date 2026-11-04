---
description: Quy trình review yêu cầu chính thức - Vai trò BA (BABOK KA3)
---

# Workflow: Requirements Review

> **Slash command**: `/requirements-review`
> **Vai trò**: `[🟢 ROLE: BA]`
> **Khi nào dùng**: Sau khi draft SRS/User Stories xong, cần formal review trước khi baseline
> **Đầu ra**: Review report + Updated requirements tại `artifacts/requirements/`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🟢 ROLE: BA]`
- **Nạp Rules:** `ba-rules.md` (§6: Requirements Lifecycle, §5: Analysis)
- **Nạp Cross-Review:** `evaluations/agents/cross-review-protocol.md`
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

---

## Bước 1: Identify Review Scope

AI hỏi:
```
1. File requirement cần review? (path đến SRS/PRD/User Stories)
2. Loại review: Self-review / Peer review / Formal walkthrough?
3. Perspectives cần review: DEV / QA / SA / PO? (mặc định: tất cả)
```

🛑 **[DỪNG]** — Cung cấp file cần review

---

## Bước 2a: Verify — Quality Checklist Scan (BABOK KA5 Task 6.2)

> **"Viết đúng cách?"** — BA tự kiểm tra + Cross-review.

AI đọc file requirement và kiểm tra:

```markdown
## Requirements Quality Checklist — VERIFY

### Completeness
- [ ] Tất cả actors đã xác định?
- [ ] Happy path + Alternative + Exception đều có?
- [ ] NFR (Performance, Security, Usability) đã cover?
- [ ] Business rules đã explicit?
- [ ] Transition requirements đã consider?

### Consistency
- [ ] Không có requirement mâu thuẫn nhau?
- [ ] Thuật ngữ nhất quán? (Check Business Glossary)
- [ ] Priority consistent (không phải tất cả đều Must-have)?

### Clarity
- [ ] Không có từ mập mờ? ("nhanh", "dễ dùng", "thông thường")
- [ ] Mỗi requirement đo lường được?
- [ ] AC viết đúng GWT format?

### Feasibility
- [ ] SA đã review technical feasibility? (nếu chưa → flag)
- [ ] Timeline realistic cho scope này?
- [ ] Dependencies đã identify?

### Traceability
- [ ] Mọi FR trace về BR?
- [ ] Traceability matrix updated?
```

→ Nguồn: [BABOK® v3, KA5 Task 6.2 — Verify Requirements](https://www.iiba.org/standards-and-resources/babok/)

---

## Bước 2b: Validate — Stakeholder Confirmation (BABOK KA5 Task 6.3)

> **"Viết đúng thứ?"** — Stakeholder xác nhận requirements phản ánh đúng nhu cầu thực sự.

```markdown
## Requirements Validation Checklist — VALIDATE

### Business Alignment
- [ ] Mỗi FR trace về ≥1 Business Requirement?
- [ ] Feature này match product strategy / project objective?
- [ ] KPI/metric nào sẽ move khi ship feature này?

### Stakeholder Acceptance
- [ ] Stakeholder đã walkthrough requirements chưa?
- [ ] Stakeholder confirm "đây đúng là thứ tôi cần"?
- [ ] User thật sự sẽ dùng feature này? Có data/evidence?

### Prototype/Demo (nếu có)
- [ ] Wireframe/mockup đã demo cho stakeholder?
- [ ] Feedback từ demo đã incorporate vào AC?
```

> [!IMPORTANT]
> **Verify TRƯỚC, Validate SAU.** Không cần stakeholder confirm nếu requirements còn lỗi logic cơ bản.

→ Nguồn: [BABOK® v3, KA5 Task 6.3 — Validate Requirements](https://www.iiba.org/standards-and-resources/babok/)

---

## Bước 3: Cross-Review (Multi-Perspective)

AI tự đội mũ các role để challenge:

### 🟠 DEV Perspective
```
- "API endpoint nào cần? Data type rõ chưa?"
- "Validation server-side hay client-side?"
- "Race condition khi concurrent users?"
```

### 🔴 QA Perspective
```
- "Test case nào từ AC này?"
- "Edge case: empty, null, max length, Unicode?"
- "Performance test scenario?"
```

### 🏛️ SA Perspective
```
- "Schema DB impact? Cần migration?"
- "Module nào bị ảnh hưởng?"
- "Scale ở 10x traffic?"
```

### 🔵 PO Perspective
```
- "Feature này match product strategy?"
- "Metric nào move khi ship?"
- "Priority so với backlog?"
```

---

## Bước 4a: Review Report

```markdown
## Requirements Review Report — [Document Name]

**Reviewer:** AI Agent (BA perspective + Cross-Review)
**Date:** [DD/MM/YYYY]
**Document Reviewed:** [File path]

### Summary
- Total requirements reviewed: [N]
- 🔴 Blocking findings: [N] (PHẢI fix)
- 🟡 Important findings: [N] (NÊN fix)
- 🟢 Minor findings: [N] (nice to have)

### Findings
| # | Perspective | Finding | Severity | Req ID | Recommendation |
|---|-----------|---------|----------|--------|----------------|

### Verify Status: ✅ Pass / ❌ Fail (Quality checklist)
### Validate Status: ✅ Pass / ❌ Fail (Stakeholder confirm)
```

---

## Bước 4b: Formal Approval (BABOK KA3 Task 5.5)

> Phê duyệt requirements theo RACI matrix đã define tại Scope Definition.

```markdown
### Approval Sign-off
| Role | Tên | Đã Review? | Quyết định | Ngày |
|------|-----|-----------|-----------|------|
| BA | [Tên] | ✅ | Approve | DD/MM |
| SA | [Tên] | ✅/❌ | Approve/Reject | DD/MM |
| PO/Stakeholder | [Tên] | ✅/❌ | Approve/Reject | DD/MM |
| PM | [Tên] | ✅/❌ | Approve/Reject | DD/MM |

**Không được approve nếu:**
🚩 Verify checklist chưa pass
🚩 Validate chưa có stakeholder confirm
🚩 Còn 🔴 Blocking findings chưa fix
🚩 Traceability matrix chưa cập nhật
```

🛑 **[DỪNG CỨNG]** — Trình review report + approval sign-off. Hỏi: *"Findings nào cần fix? Approve baseline?"*

→ Nguồn: [BABOK® v3, KA3 Task 5.5 — Approve Requirements](https://www.iiba.org/standards-and-resources/babok/)

---

## Bước 5: Update & Baseline

- Fix blocking findings trong requirement document
- Update traceability matrix
- Version bump: X.Y → X.(Y+1) hoặc major version
- Baseline document (freeze)
- Notify team: "Requirements baselined. Mọi thay đổi phải qua `/change-request`"
