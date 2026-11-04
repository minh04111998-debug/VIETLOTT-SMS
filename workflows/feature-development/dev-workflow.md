---
description: Quy trình DEV end-to-end — Từ architecture review đến production gate. Gọi `/dev` chạy full, `/dev [step]` chạy 1 step.
---

# 💻 DEV Master Workflow

> **Full flow:** `/dev` → Chạy tất cả 7 steps tuần tự
> **Từng step:** `/dev review` hoặc `/code-review` → Chạy 1 step cụ thể
> **Vai trò:** `[💻 ROLE: DEV]`

---

## CHỈ THỊ CHO AI

- **Khai báo:** Đầu mỗi phản hồi, BẮT BUỘC in `[💻 ROLE: DEV]`
- **Nạp Rules:** Đọc ngầm `.agents/rules/dev-rules.md`
- **Nạp Skills:** Sẵn sàng gọi `.agents/skills/dev/SKILL.md` (lazy-load khi step cần)
- **Dừng cứng:** 🛑 sau mỗi step

---

## Tổng Quan 7 Steps

| Step | Tên | Slash shortcut | Output |
|------|-----|----------------|--------|
| 1 | Architecture Review | `/dev arch` hoặc `/architecture-review` | ADR + diagrams |
| 2 | Tech Design | `/dev design` | tech-design.md |
| 3 | Implementation | `/dev code` | Source code + unit tests |
| 4 | Code Review | `/dev review` hoặc `/code-review` | Review report |
| 5 | Refactoring | `/dev refactor` hoặc `/refactoring-plan` | Refactoring plan |
| 6 | Technical Debt Management | `/dev debt` | Tech debt inventory |
| 7 | Maintenance & Bug Fix | `/dev maintain` | Maintenance report |

---

## STEP 1: Architecture Review (Gate bắt buộc)
> Chốt kiến trúc + tạo ADR TRƯỚC KHI code.
→ Chi tiết: Xem [../sa/architecture-review.md](../sa/architecture-review.md)
→ Gọi Skills: Tech Design Plan
- Context Gathering → So sánh phương án → Đề xuất + ADR → Diagram → Tech Design
🛑 **PHẢI có ADR approved trước khi tiếp.**

## STEP 2: Tech Design Plan
> Database changes, API contracts, file list, dependencies.
→ Gọi Skills: §6 Tech Design Plan trong SKILL.md
- DB Schema → API Endpoints → File structure → Dependencies audit
🛑 **Xong Step 2.** Gõ **'NEXT'** | **'STOP'**

## STEP 3: Implementation
> Code theo AC + viết Unit Test.
- Đọc PRD/SRS + Design Spec → Code → Unit Test → Structured logging
- Rules kiểm soát: Production-Ready Gate (8 gates)
🛑 **Xong Step 3.** Gõ **'NEXT'** | **'STOP'**

## STEP 4: Code Review
> Self-review + cross-review.
→ Chi tiết: Xem [code-review.md](code-review.md)
- Code quality scan → Security scan → Performance review → Gate Report
🛑 **Xong Step 4.** Gõ **'NEXT'** | **'STOP'**

## STEP 5: Refactoring Plan
> Lập kế hoạch refactor — khi cần.
→ Chi tiết: Xem [refactoring-plan.md](refactoring-plan.md)
🛑 **Xong Step 5.** Gõ **'NEXT'** | **'STOP'**

## STEP 6: Technical Debt Management
> `/dev debt`
> Đọc: `SKILL.md` Skill 11 (Tech Debt Tracker)

1. Scan codebase cho tech debt (functions >30 lines, cyclomatic complexity >10, deprecated deps)
2. Classify theo Maintenance Types + Tech Debt Quadrant (dev-rules.md §8)
3. Tạo Tech Debt Inventory (SKILL.md Skill 11 template)
4. Prioritize: Impact/Effort ratio, allocate ≥ 15% sprint capacity
5. Lưu: `plans/tech-debt/tech-debt-register.md`

🛑 **Hard Stop** — Chờ user review debt inventory

## STEP 7: Maintenance & Bug Fix
> `/dev maintain`
> Đọc: `dev-rules.md` §8 (Software Maintenance Rules)

1. Classify maintenance type: Corrective / Adaptive / Perfective / Preventive
2. Nếu legacy code: assess với Strangler Fig vs Boy Scout strategy
3. Write characterization tests TRƯỚC khi touch legacy code
4. Apply fix/improvement
5. Verify: existing tests still pass, new tests cover change

🛑 **Hard Stop** — Chờ user review maintenance output. **🎉 DEV FLOW HOÀN TẤT.**

---

## Hướng Dẫn Sử Dụng

| Lệnh | Hành vi |
|-------|---------|
| `/dev` | Chạy full flow 7 steps |
| `/dev arch` | Chạy chỉ Step 1 |
| `/dev code` | Chạy chỉ Step 3 |
| `/dev debt` | Chạy chỉ Step 6 |
| `/dev maintain` | Chạy chỉ Step 7 |
| `/architecture-review` | Alias → `/dev arch` |
| `/code-review` | Alias → `/dev review` |

### Lệnh điều khiển
`NEXT` | `SKIP` | `STOP` | `BACK`
