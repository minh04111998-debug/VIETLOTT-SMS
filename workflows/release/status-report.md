---
description: Tạo báo cáo tình trạng dự án hàng tuần - Vai trò PM
---

# Workflow: Status Report

> **Slash command**: `/status-report`
> **Vai trò**: `[⚪ ROLE: PM]`
> **Khi nào dùng**: Weekly status update, steering committee meeting
> **Đầu ra**: Status Report với RAG status + risks + decisions needed

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[⚪ ROLE: PM]`
- **Nạp Rules:** `.agents/rules/pm-rules.md` (đặc biệt §3.3 Status Reporting)
- **Nạp Skills:** `.agents/skills/pm/SKILL.md` (Skill 7, 9, 10)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

> [!IMPORTANT]
> "Không bao giờ let stakeholder bị surprise bởi bad news. Escalate sớm, không đợi đến deadline." — pm-rules §3.3

---

## Bước 1: Data Collection

Hỏi người dùng:
```
1. Tuần này đã hoàn thành những gì? (Accomplishments)
2. Kế hoạch tuần tới? (Plans)
3. Có blockers/issues nào không?
4. Có risks mới phát sinh không?
5. Có decisions cần stakeholder không?
6. Sprint velocity tuần này? (nếu Agile)
```

🛑 **[DỪNG]** — Thu thập data

---

## Bước 2: Generate Status Report

AI tạo report theo format pm-rules §3.3:

```markdown
# Weekly Status Report — [Project] — Week [N] ([DD/MM])

## Overall Status: 🟢 On Track / 🟡 At Risk / 🔴 Off Track

### Accomplishments This Week
- ✅ [Item 1]
- ✅ [Item 2]

### Planned Next Week
- 📋 [Item 1]
- 📋 [Item 2]

### Risks & Issues
| # | Type | Description | Severity | Owner | Action |
|---|------|------------|----------|-------|--------|
| 1 | Risk | [Description] | 🔴/🟡/🟢 | [Name] | [Action] |
| 2 | Issue | [Description] | | | |

### Decisions Needed from Stakeholder
| # | Decision | Deadline | Impact if Delayed |
|---|----------|----------|-------------------|
| 1 | [Decision] | [Date] | [Impact] |

### Metrics Dashboard
| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| Sprint velocity | [X] SP | [Y] SP | ↑/↓/→ |
| Open bugs | [X] | [Y] | |
| Budget spent | [X]% | [Y]% | |
```

🛑 **[DỪNG]** — Review report

---

## Bước 3: Lưu Trữ

- Lưu tại `artifacts/analysis/status-report-[project]-week[N].md`
- Thông báo: *"✅ Status report đã lưu. Gửi cho stakeholders."*

---

## Cross-References (Phase 2 additions)

> [!NOTE]
> **Bổ sung cho Status Report:**
> - **Stakeholder Engagement Tracking** (pm-rules.md §7): Thêm section đánh giá mức độ engagement của từng stakeholder group (Current vs Desired). Dùng Stakeholder Register (SKILL.md Skill 11) làm baseline.
> - **Quality Metrics** (pm-rules.md §8, SKILL.md Skill 14): Bổ sung vào Metrics Dashboard các chỉ số chất lượng: test coverage, open bugs by severity, security scan status. Đối chiếu với Quality Gate criteria.
