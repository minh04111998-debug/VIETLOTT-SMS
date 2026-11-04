---
description: Quy trình PM end-to-end — Từ kickoff đến sprint ceremony. Gọi `/pm` chạy full, `/pm [step]` chạy 1 step.
---

# ⚪ PM Master Workflow

> **Full flow:** `/pm` → Chạy tất cả 4 steps tuần tự
> **Từng step:** `/pm kickoff` hoặc `/project-kickoff` → Chạy 1 step cụ thể
> **Vai trò:** `[⚪ ROLE: PM]`

---

## CHỈ THỊ CHO AI

- **Khai báo:** `[⚪ ROLE: PM]`
- **Nạp Rules:** `.agents/rules/pm-rules.md`
- **Nạp Skills:** `.agents/skills/pm/SKILL.md` (lazy-load)
- **Dừng cứng:** 🛑 sau mỗi step

---

## Tổng Quan 8 Steps

| Step | Tên | Slash shortcut | Output |
|------|-----|----------------|--------|
| 1 | Project Kickoff | `/pm kickoff` hoặc `/project-kickoff` | project-brief.md |
| 2 | Sprint Ceremony | `/pm sprint` hoặc `/sprint-ceremony` | sprint-plan.md |
| 3 | Status Report | `/pm status` hoặc `/status-report` | status-report.md |
| 4 | E2E Pipeline | `/pm e2e` | Chạy full pipeline DA→PO→PM→BA→Designer→DEV→QA |
| 5 | Stakeholder Management | `/pm stakeholder` | stakeholder-register.md |
| 6 | Quality Gate | `/pm quality` | quality-gate-assessment.md |
| 7 | Change Control | `/pm change` | change-request.md |
| 8 | Project Closing | `/pm close` | closure-report.md |

---

## STEP 1: Project Kickoff → Xem [project-kickoff.md](project-kickoff.md)
- Define objectives → Stakeholders → Timeline → Risk register → Kick-off meeting
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 2: Sprint Ceremony → Xem [sprint-ceremony.md](../feature-development/sprint-ceremony.md)
- Sprint Planning → Daily Standup → Sprint Review → Retro → E2E Auto-Agent Pipeline
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 3: Status Report → Xem [status-report.md](status-report.md)
- Progress update → Risk/Issue log → Milestone tracking → Communication
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 4: E2E Pipeline
- Kích hoạt full pipeline: DA → PO → PM → BA → Designer → DEV → QA
- Mỗi phase có 🛑 Hard Stop chờ user trigger phase tiếp
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 5: Stakeholder Management → Xem SKILL.md (Skill 11)
- Tạo Stakeholder Register (Power/Interest Grid)
- Xây dựng Communication Plan cho từng stakeholder group
- Ref: `pm-rules.md` §7 (Stakeholder Engagement)
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 6: Quality Gate → Xem SKILL.md (Skill 14)
- Đánh giá Quality Gate cho phase/sprint hiện tại
- Criteria: test coverage, bugs, security, performance, code review, docs
- Decision: 🟢 PASS / 🟡 CONDITIONAL / 🔴 FAIL
- Ref: `pm-rules.md` §8 (Quality Management)
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 7: Change Control
- Tiếp nhận Change Request → Impact Analysis → Approve/Reject
- Cập nhật cascading tài liệu nếu approved
- Ref: `pm-rules.md` §11 (Change Management), liên kết `/ba change`
🛑 Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 8: Project Closing → Xem [project-closing.md](project-closing.md)
- Deliverable Acceptance → Lessons Learned → Knowledge Transfer → Financial Closure → Archive
- Ref: `pm-rules.md` §9 (Closing), SKILL.md Skill 12-13
🛑 **🎉 PM FLOW HOÀN TẤT.**

---

## Hướng Dẫn
| Lệnh | Hành vi |
|-------|---------|
| `/pm` | Full flow 8 steps |
| `/pm kickoff` | Step 1 only |
| `/pm stakeholder` | Step 5 only |
| `/pm quality` | Step 6 only |
| `/pm change` | Step 7 only |
| `/pm close` | Step 8 only |
| `/sprint-ceremony` | Alias → `/pm sprint` |
| Điều khiển | `NEXT` / `SKIP` / `STOP` / `BACK` |
