---
description: Phân loại và xử lý bug (Bug Triage) - Vai trò QA
---

# Workflow: Bug Triage

> **Slash command**: `/bug-triage`
> **Vai trò**: `[🔴 ROLE: QA]`
> **Khi nào dùng**: Khi có danh sách bugs cần phân loại, ưu tiên, và assign
> **Đầu ra**: Bug triage report với severity, priority, và action plan

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🔴 ROLE: QA]`
- **Nạp Rules:** `.agents/rules/qa-rules.md` (đặc biệt §3.3 Bug Severity)
- **Nạp Skills:** `.agents/skills/qa/SKILL.md` (Skill 6: Bug Report)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

---

## Bước 1: Bug Collection & Duplicate Check

Hỏi người dùng:
```
1. Liệt kê các bugs cần triage (hoặc cung cấp file bug list)
2. Sprint/Release liên quan?
3. Team members available cho fix?
4. Có deadline cứng không?
```

Hoặc AI scan bugs từ test results nếu vừa chạy xong regression.

### Duplicate Detection (BẮT BUỘC)
Với mỗi bug trong danh sách:
1. Scan `artifacts/testing/bug-*.md` tìm bugs đã tồn tại
2. So sánh: cùng module? cùng endpoint? cùng steps? cùng error?
3. **Nếu trùng** → đánh dấu `DUPLICATE` + link bug gốc, không tạo mới
4. **Nếu tương tự** → tạo bug mới + thêm field `Related: BUG-XXX-NNN`
5. In kết quả: *"[N] bugs mới, [M] duplicates (đã merge vào bug gốc)"*

🛑 **[DỪNG]** — Thu thập bug list + kết quả duplicate check

---

## Bước 2: Severity & Priority Classification

AI phân loại mỗi bug:

### Severity (Technical impact)
| Level | Criteria |
|-------|----------|
| **Blocker** | System crash, data loss, security breach |
| **Critical** | Core feature broken, no workaround |
| **High** | Feature broken, workaround exists |
| **Medium** | Feature partially working, minor impact |
| **Low** | Cosmetic, typo, minor UI issue |

### Priority (Business urgency)
| Level | Action |
|-------|--------|
| **P1** | Fix now — blocks release |
| **P2** | Fix this sprint — important |
| **P3** | Fix next sprint — nice to have |
| **P4** | Backlog — fix when time allows |

🛑 **[DỪNG]** — *"Bug classification OK?"*

---

## Bước 3: Triage Decision

Cho mỗi bug, AI đề xuất:

| Bug ID | Severity | Priority | Action | Assignee | Sprint |
|--------|----------|----------|--------|----------|--------|
| BUG-001 | Critical | P1 | Fix now | [Dev] | Current |
| BUG-002 | Medium | P3 | Next sprint | [Dev] | S+1 |
| BUG-003 | Low | P4 | Backlog | - | Backlog |
| BUG-004 | High | P2 | Fix + retest | [Dev] | Current |

🛑 **[DỪNG]** — *"Triage assignments OK? Approve?"*

---

## Bước 4: Lưu Trữ

- Lưu tại `artifacts/testing/bug-triage-[sprint/release].md`
- Thông báo: *"✅ Bug triage complete. [N] bugs P1, [M] bugs P2, [K] bugs P3+."*
