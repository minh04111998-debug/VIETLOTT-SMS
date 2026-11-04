---
description: Lập kế hoạch regression test trước release - Vai trò QA
---

# Workflow: Regression Plan

> **Slash command**: `/regression-plan`
> **Vai trò**: `[🔴 ROLE: QA]`
> **Khi nào dùng**: Trước mỗi release, sau major code changes
> **Đầu ra**: Regression Test Suite + GO/NO-GO decision

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🔴 ROLE: QA]`
- **Nạp Rules:** `.agents/rules/qa-rules.md`
- **Nạp Skills:** `.agents/skills/qa/SKILL.md` (Skill 12: Regression, Skill 4: Performance)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

---

## Bước 1: Release Scope Analysis

Hỏi người dùng:
```
1. Release version/name?
2. Modules/features thay đổi trong release này?
3. Có breaking changes nào không?
4. Regression scope: Full / Targeted (chỉ modules affected)?
5. Timeline: Bao nhiêu ngày dành cho regression?
6. Có automation tests nào chạy được không?
```

🛑 **[DỪNG]** — Thu thập scope

---

## Bước 2: Build Regression Suite

Dùng Skill 12 (Regression Test Management):
- Xác định core tests (P1 — always run)
- Xác định targeted tests (P2 — based on changed modules)
- Map test cases to modules changed
- Estimate effort

🛑 **[DỪNG]** — *"Regression suite OK? Có test case nào cần thêm/bỏ?"*

---

## Bước 3: Execution & Tracking

- Tạo execution checklist
- Track results: Pass / Fail / Blocked
- Nếu Fail → trigger Bug Report workflow (Skill 6)

🛑 **[DỪNG]** — *"Results ready. Review trước khi GO/NO-GO?"*

---

## Bước 4: GO/NO-GO Decision

- Tổng hợp: Total/Passed/Failed/Blocked
- Check exit criteria (qa-rules §4)
- Đề xuất GO / NO-GO với rationale
- Lưu tại `artifacts/testing/regression-release-[version].md`

🛑 **[DỪNG]** — *"Decision: [GO/NO-GO]. Approve?"*
