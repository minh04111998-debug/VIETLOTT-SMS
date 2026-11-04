---
description: Quy trình QA end-to-end — Từ test plan đến regression + automation. Gọi `/qa` chạy full, `/qa [step]` chạy 1 step.
---

# 🔴 QA Master Workflow

> **Full flow:** `/qa` → Chạy tất cả 8 steps tuần tự
> **Từng step:** `/qa plan` hoặc `/create-test-plan` → Chạy 1 step cụ thể
> **Vai trò:** `[🔴 ROLE: QA]`

---

## CHỈ THỊ CHO AI

- **Khai báo:** `[🔴 ROLE: QA]`
- **Nạp Rules:** `.agents/rules/qa-rules.md`
- **Nạp Skills:** `.agents/skills/qa/SKILL.md` (lazy-load)
- **Dừng cứng:** 🛑 sau mỗi step

---

## Tổng Quan 8 Steps

| Step | Tên | Slash shortcut | Output |
|------|-----|----------------|--------|
| 1 | Create Test Plan | `/qa plan` hoặc `/create-test-plan` | test-plan-[tên].md |
| 2 | Write Test Cases | `/qa cases` | test-cases.md |
| 3 | Automation Test | `/qa automation` hoặc `/playwright-test` | .spec.ts files + test results |
| 4 | Bug Triage | `/qa triage` hoặc `/bug-triage` | bug-report.md |
| 5 | Regression Plan | `/qa regression` hoặc `/regression-plan` | regression-plan.md |
| 6 | Test Summary Report | `/qa summary` | test-summary.md |
| 7 | Static Testing / Requirements Review | `/qa review` | review-checklist.md |
| 8 | Test Monitoring & Reporting | `/qa report` | test-dashboard.md |

---

## STEP 1: Create Test Plan → Xem [create-test-plan.md](create-test-plan.md)
- Entry/Exit criteria → Test scope → Test strategy → Environment → Schedule
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 2: Write Test Cases
- Derive from AC (Given/When/Then) → Happy + Alternative + Exception + Edge
- Traceability: UC/US → TC mapping
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 3: Automation Test (Playwright) → Xem [playwright-test.md](playwright-test.md)
- Setup Playwright → Sinh .spec.ts từ test cases → Chạy tests → Parse results → Bug Report auto
- Ref: SKILL.md §5.3-5.5, Examples: `.agents/skills/qa-automation/SKILL.md`
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 4: Bug Triage → Xem [bug-triage.md](bug-triage.md)
- Classify severity + priority → Assign → Track → Verify fix
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 5: Regression Plan → Xem [regression-plan.md](regression-plan.md)
- Identify regression scope → Select test suite → Execute → Report
🛑 Gõ **'NEXT'** | **'STOP'**

## STEP 6: Test Summary Report
- Total cases: Passed / Failed / Blocked / Not Run
- Coverage analysis → Risk assessment → Go/No-Go recommendation
🛑 Gõ **'NEXT'** | **'STOP'**

## STEP 7: Static Testing / Requirements Review
- Shift-left review: Đánh giá requirements/SRS trước khi code
- Sử dụng Review Checklist (SKILL.md Skill 14): AC testable?, Boundary values?, Error scenarios?
- Review metrics: defects per page, review rate
- Output: review-checklist.md + danh sách defects found
- Ref: qa-rules.md §7, ISTQB CH3 Static Testing
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 8: Test Monitoring & Reporting
- Dashboard: Execution summary + Defect summary + Key metrics (DDP, Leakage, Execution Rate)
- Sử dụng template từ SKILL.md Skill 13
- Control directives nếu metrics lệch target
- GO/NO-GO recommendation cho release
- Ref: qa-rules.md §8-§9, ISTQB CH5 Managing Test Activities
🛑 **🎉 QA FLOW HOÀN TẤT.**

---

## Hướng Dẫn
| Lệnh | Hành vi |
|-------|---------|
| `/qa` | Full flow 8 steps |
| `/qa plan` | Step 1 only |
| `/qa cases` | Step 2 only |
| `/qa automation` | Step 3 only (Playwright) |
| `/qa triage` | Step 4 only |
| `/qa regression` | Step 5 only |
| `/qa summary` | Step 6 only |
| `/qa review` | Step 7 only (Static Testing) |
| `/qa report` | Step 8 only (Test Monitoring Dashboard) |
| `/playwright-test` | Alias → `/qa automation` |
| `/playwright-test setup` | Chỉ setup Playwright project |
| `/playwright-test generate` | Chỉ sinh test code |
| `/playwright-test run` | Chạy test + report |
| `/create-test-plan` | Alias → `/qa plan` |
| Điều khiển | `NEXT` / `SKIP` / `STOP` / `BACK` |
