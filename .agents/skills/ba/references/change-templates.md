# 🟢 Change Management Templates — Quick Reference

> **Nguồn:** [Prosci ADKAR](https://www.prosci.com/methodology/adkar) | [ITIL Change Management](https://www.axelos.com/certifications/itil)
> **Tham chiếu từ:** `.agents/rules/ba-rules.md` §7

---

## 1. Change Request Template (CR-NNN)

```markdown
# CR-[NNN]: [Tên thay đổi ngắn gọn]

**Ngày yêu cầu:** DD/MM/YYYY
**Người yêu cầu:** [Tên / Role]
**Mức độ:** 🔴 Critical | 🟡 Important | 🟢 Minor
**Trạng thái:** Submitted | Under Review | Approved | Rejected | Implemented

## Mô Tả Thay Đổi
**Trước (AS-IS):** [Mô tả hành vi/yêu cầu hiện tại]
**Sau (TO-BE):** [Mô tả hành vi/yêu cầu mong muốn]
**Lý do thay đổi:** [Business justification]

## Phạm Vi Ảnh Hưởng
- [ ] Requirements (PRD/SRS/User Story)
- [ ] Design (UI mockup/Wireframe)
- [ ] Architecture (ADR)
- [ ] API / Interface contract
- [ ] Database schema
- [ ] Test cases
- [ ] Documentation

## Timeline
**Deadline mong muốn:** DD/MM/YYYY
**Effort ước tính:** [X] person-days

## Approval
| Role | Tên | Ngày | Quyết định |
|------|-----|------|-----------| 
| BA | | | |
| SA | | | |
| PM | | | |
| PO/Stakeholder | | | |
```

---

## 2. Impact Analysis Template

```markdown
# Impact Analysis — CR-[NNN]

## Tóm tắt Change Request
[1-2 câu mô tả thay đổi]

## Layer 1: Requirements Impact
| Document | File Path | Section bị ảnh hưởng | Hành động |
|----------|-----------|---------------------|----------|
| PRD | `artifacts/requirements/prd-xxx.md` | §3.2 Feature X | Cập nhật AC |
| SRS | `artifacts/requirements/srs-xxx.md` | FR-005 | Sửa requirement |

## Layer 2: Design Impact
| Artifact | File Path | Ảnh hưởng | Hành động |
|----------|-----------|-----------|----------|
| UI Mockup | `artifacts/technical/design/screen-xxx.md` | Thêm button | Redesign |
| ADR | `artifacts/decisions/adr-xxx.md` | Không ảnh hưởng | — |

## Layer 3: Technical Impact
| Component | Ảnh hưởng | Effort |
|-----------|-----------|--------|
| API endpoint | Thêm field mới | 0.5d |
| DB schema | ALTER TABLE | 0.5d |
| Service logic | Cập nhật validation | 1d |

## Layer 4: Testing Impact
| Test Type | Ảnh hưởng | Hành động |
|-----------|-----------|----------|
| Unit test | 3 test cases cần update | Update |
| Integration test | 1 scenario mới | Tạo mới |
| Regression | Full regression cần | Schedule |

## Tổng Kết
**Total effort:** [X] person-days
**Risk level:** 🔴/🟡/🟢
**Recommendation:** Proceed / Defer / Reject
```

---

## 3. Cascading Update Checklist Template

```markdown
# Cascading Update — CR-[NNN]

| # | Tài liệu | File | Updated? | Người thực hiện | Ghi chú |
|---|----------|------|----------|----------------|---------|
| 1 | Source requirement | | ☐ | | |
| 2 | SRS / User Story / AC | | ☐ | | |
| 3 | Wireframes / UI mockups | | ☐ | | |
| 4 | ADR (nếu architecture) | | ☐ | | |
| 5 | API spec / interface | | ☐ | | |
| 6 | DEV ticket | | ☐ | | |
| 7 | Test cases | | ☐ | | |
| 8 | QA notification | | ☐ | | |
| 9 | project-context.md | | ☐ | | |
| 10 | Stakeholder communication | | ☐ | | |

**Completed by:** [Tên]
**Date:** DD/MM/YYYY
```

---

## 4. Communication Plan Template (Major Changes)

```markdown
# Communication Plan — CR-[NNN]

| Audience | Message | Channel | Timing | Owner |
|----------|---------|---------|--------|-------|
| Dev Team | Technical details + impact | Slack/Teams | Ngay sau approval | Tech Lead |
| QA Team | Test impact + new cases | Slack + Ticket | Trong 24h | QA Lead |
| Stakeholders | Business impact summary | Email / Meeting | Trong 48h | PM |
| End Users | Release notes (nếu có) | In-app / Email | Trước release | PO/Marketing |
```
