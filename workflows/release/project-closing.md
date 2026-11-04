---
name: project-closing
description: Project Closing workflow — Lessons Learned, Acceptance, Archive
---

# 🛑 Project Closing Workflow

> **CHỈ THỊ CHO AI:** Đọc file này khi user gõ `/pm close`. In `[⚪ ROLE: PM]` đầu mỗi phản hồi.

## Bước 1: Deliverable Acceptance
- Thu thập formal sign-off cho tất cả deliverables
- Nếu có outstanding items → tạo punch list với deadline
- Lưu: `artifacts/decisions/acceptance-sign-off-[project].md`

🛑 **Hard Stop** — Chờ user xác nhận deliverables đã accepted

## Bước 2: Lessons Learned Workshop
- Facilitate workshop: What went well? What went wrong? What surprised us?
- Document sử dụng SKILL.md Skill 7 template
- Lưu: `artifacts/analysis/lessons-learned-[project].md`

🛑 **Hard Stop** — Chờ user review lessons learned

## Bước 3: Knowledge Transfer
- Identify successor / maintenance team
- Tạo knowledge transfer checklist: docs, access, contacts, known issues
- Lưu: `artifacts/analysis/knowledge-transfer-[project].md`

🛑 **Hard Stop** — Chờ user confirm KT completed

## Bước 4: Financial & Contract Closure
- Budget vs Actual summary
- Vendor contract closure (if applicable)
- Lưu: `artifacts/analysis/closure-report-[project].md`

🛑 **Hard Stop** — Chờ user approve closure report

## Bước 5: Archive & Celebrate
- Archive all project artifacts
- Team recognition
- Close project in tracking tools

## Hướng Dẫn
| Lệnh | Mô tả |
|------|--------|
| `/pm close` | Chạy full closing flow |
| `NEXT` | Qua bước tiếp |
| `STOP` | Dừng flow |
