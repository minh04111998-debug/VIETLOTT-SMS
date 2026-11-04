---
description: Quy trình BA end-to-end — Từ scope đến evaluation + change management. Gọi `/ba` chạy full flow, `/ba [step]` chạy 1 step.
---

# 🟢 BA Master Workflow

> **Full flow:** `/ba` → Chạy tất cả 11 steps tuần tự
> **Từng step:** `/ba scope` hoặc `/scope-definition` → Chạy 1 step cụ thể
> **Vai trò:** `[🟢 ROLE: BA]`
> **Benchmark:** BABOK® v3 — 30/30 Tasks covered (6 Knowledge Areas)

---

## CHỈ THỊ CHO AI

- **Khai báo:** Đầu mỗi phản hồi, BẮT BUỘC in `[🟢 ROLE: BA]`
- **Nạp Rules:** Đọc ngầm `.agents/rules/ba-rules.md`
- **Nạp Skills:** Sẵn sàng gọi `.agents/skills/ba/SKILL.md` (lazy-load khi step cần)
- **Dừng cứng:** 🛑 sau mỗi step, chờ user gõ lệnh điều khiển

---

## Tổng Quan 11 Steps

| Step | Tên | Slash shortcut | Output |
|------|-----|----------------|--------|
| 1 | Scope Definition | `/ba scope` hoặc `/scope-definition` | `scope-[tên].md` |
| 2 | Elicitation Plan | `/ba elicit` hoặc `/elicitation-plan` | `elicitation-plan-[tên].md` |
| 3 | Thu thập & Phân tích | `/ba analyze` | requirements-summary.md |
| 4 | Create BRD (Waterfall) | `/ba brd` hoặc `/create-brd` | `brd-[tên].md` |
| 5 | Create SRS | `/ba srs` hoặc `/create-srs` | `srs-[tên].md` |
| 6 | Requirements Review | `/ba review` hoặc `/requirements-review` | review-report.md |
| 7 | Create Jira Tasks | `/ba jira` hoặc `/create-jira-task` | Jira tickets |
| 8 | Solution Evaluation | `/ba eval` hoặc `/solution-evaluation` | eval-report.md |
| 9 | Impact Analysis | `/ba impact` | impact-analysis-CR-[NNN].md |
| 10 | Change Request | `/ba change` | CR + cascading updates |
| 11 | Change Log | `/ba changelog` | change-log.md |

---

## STEP 1: Scope Definition

> Xác định ranh giới hệ thống — TRƯỚC khi phân tích chi tiết.
> **BABOK Tasks:** KA4 (Analyze Current State, Define Future State, Assess Risks, Define Change Strategy) + KA1 (Plan BA Governance, Plan BA Info Mgmt) + KA5 (Analyze Potential Value)

→ Chi tiết: Xem [scope-definition.md](scope-definition.md)
- Understand Context → Context Diagram → Scope Statement → Gap Analysis (As-Is vs To-Be) → **BA Governance (RACI)** → **BA Info Management** → **Value Assessment** → Lưu trữ
- Gọi Skills: §21 (Scope Modeling), §4 (Gap Analysis), §31 (Value Analysis)

🛑 **Xong Step 1.** Gõ **'NEXT'** → Step 2 | **'SKIP'** → bỏ qua | **'STOP'** → kết thúc flow.

---

## STEP 2: Elicitation Plan

> Lập kế hoạch thu thập yêu cầu — ai, kỹ thuật nào, bao lâu.

→ Chi tiết: Xem [elicitation-plan.md](elicitation-plan.md)
- Context Assessment → Stakeholder Analysis → Technique Selection → Preparation Checklist → Lưu trữ
- Gọi Skills: BABOK KA2 (Elicitation Techniques)

🛑 **Xong Step 2.** Gõ **'NEXT'** → Step 3 | **'SKIP'** | **'STOP'**

---

## STEP 3: Thu Thập & Phân Tích Requirements

> Thực hiện elicitation + phân tích ngoại lệ + xác nhận kết quả.
> **BABOK Tasks:** KA2 (Conduct Elicitation, Confirm Elicitation Results, Manage Stakeholder Collaboration)

- Áp dụng kỹ thuật đã chọn ở Step 2 (Interview, Workshop, Document Analysis...)
- Gọi Skills: **Brainstorm Ngược** (5W1H + What-If Challenge)
- Gọi Skills: **Analyze Edge Cases** (8 nhóm: Empty, Error, Limits, Permissions, Concurrency, Timeout/Latency, Retry/Recovery, Integration Failure)
- Output: Requirements raw list + Edge Cases identified

🛑 **[DẪNGA]** — **Confirm Elicitation Results (BABOK KA2 Task 3.3):**
AI tổng hợp kết quả thu thập thành **Elicitation Summary** và yêu cầu user xác nhận:
```
"Tôi đã thu thập được [N] requirements, [M] business rules, [K] edge cases.
Dưới đây là tóm tắt. Vui lòng xác nhận đúng/sai TRƯỚC khi tôi viết SRS/BRD:
- [Summary các requirements chính]
- [Business rules phát hiện]
- [Open questions còn lại]"
```
Chỉ tiếp khi user confirm. Nếu sai → quay lại elicitation.

🛑 **Xong Step 3.** Gõ **'NEXT'** → Step 4 (BRD) hoặc Step 5 (SRS) | **'SKIP'** | **'STOP'**

---

## STEP 4: Create BRD (Waterfall)

> Tạo Business Requirements Document — nếu methodology là Waterfall.

→ Chi tiết: Xem [create-brd.md](create-brd.md)
- Thu thập thông tin nghiệp vụ → Gap Analysis → Viết BRD template → Traceability Matrix → Lưu trữ
- Gọi Skills: Gap Analysis, Vẽ Mermaid Flow, Analyze Edge Cases

> **Lưu ý:** Nếu Agile → bỏ qua Step 4, nhảy sang Step 5 tạo PRD/SRS.

🛑 **Xong Step 4.** BRD nháp đã lưu tại `artifacts/requirements/`. Gõ **'NEXT'** → Step 5 | **'STOP'**

---

## STEP 5: Create SRS

> Tạo Software Requirements Specification — chi tiết hóa yêu cầu.

→ Chi tiết: Xem [create-srs.md](create-srs.md)
- Thu thập reqs → Vẽ Diagrams → Viết SRS chi tiết → Traceability Matrix → Lưu trữ
- Gọi Skills: Vẽ Mermaid Flow, Analyze Edge Cases, Write SRS
- Rules kiểm soát: BDD format bắt buộc, Traceability non-negotiable

🛑 **Xong Step 5.** SRS nháp đã lưu tại `artifacts/requirements/`. Gõ **'NEXT'** → Step 6 | **'STOP'**

---

## STEP 6: Requirements Review

> Formal review chất lượng yêu cầu — Verify + Validate + Approve.
> **BABOK Tasks:** KA5 (Verify Requirements, Validate Requirements) + KA3 (Approve Requirements)

→ Chi tiết: Xem [requirements-review.md](requirements-review.md)
- **Verify:** Quality Checklist Scan (completeness, consistency, clarity, traceability)
- **Validate:** Stakeholder xác nhận "đúng thứ họ cần" (business alignment, user acceptance)
- **Cross-Review:** DEV + QA + SA + PO perspective
- **Approve:** Formal sign-off theo RACI matrix
- Gọi Protocol: `evaluations/agents/cross-review-protocol.md`

🛑 **Xong Step 6.** Review report đã lưu. Gõ **'NEXT'** → Step 7 | **'STOP'**

---

## STEP 7: Create Jira Tasks

> Đẩy User Stories/Requirements lên Jira.

→ Chi tiết: Xem [create-jira-task.md](create-jira-task.md)
- Parse requirements → Map sang Jira structure → Tạo Epics/Stories/Tasks → Link traceability

🛑 **Xong Step 7.** Tasks đã tạo. Gõ **'NEXT'** → Step 8 | **'STOP'**

---

## STEP 8: Solution Evaluation (Post-Delivery)

> Đánh giá giải pháp sau 2-4 tuần go-live + BA Retrospective.
> **BABOK Tasks:** KA6 (Measure Performance, Analyze Performance Measures, Assess Solution Limitations, Assess Enterprise Limitations, Recommend Actions) + KA1 (BA Performance Improvements)

→ Chi tiết: Xem [solution-evaluation.md](solution-evaluation.md)
- Gather Context → Requirements Fulfillment Check → Value Assessment → **Performance Analysis (root cause)** → **Enterprise Limitations** → Recommendation → **BA Retrospective / Lessons Learned**
- Gọi Skills: BABOK KA6 (Solution Evaluation) + KA1 (Performance Improvements)

🛑 **Xong Step 8.** Evaluation report đã lưu. Gõ **'NEXT'** → Step 9 | **'STOP'**

---

## STEP 9: Impact Analysis (Change Management)

> Đánh giá tác động khi có thay đổi requirement — gộp từ Change Manager role.

→ Chi tiết: Xem [impact-analysis.md](impact-analysis.md)
- Change Request Intake → Impact Scoring (6 dimensions) → Dependency Mapping → Risk Assessment → Communication Plan
- Gọi Skills: §24 (Impact Analysis), §26 (Dependency Graph), §27 (Impact Scoring)

🛑 **Xong Step 9.** Impact Analysis đã lưu. Gõ **'NEXT'** → Step 10 | **'STOP'**

---

## STEP 10: Change Request & Cascading Update

> Thực hiện cập nhật lan truyền tài liệu sau khi CR được approve.

→ Chi tiết: Xem [change-request.md](change-request.md)
- Tiếp nhận & phân loại CR → Document Scan → Impact Analysis → Cascading Update → Traceability → Tổng kết
- Gọi Skills: §25 (Cascading Process), §28 (Communication Plan), §29 (Version Control)

🛑 **Xong Step 10.** CR đã hoàn tất. Gõ **'NEXT'** → Step 11 | **'STOP'**

---

## STEP 11: Change Log

> Tổng hợp tất cả CR → Update change-log.md → Notify team.

- Tổng hợp tất cả CRs đã thực hiện
- Cập nhật `artifacts/requirements/change-log.md`
- Notify affected teams

🛑 **Xong Step 11.** **🎉 BA FLOW HOÀN TẤT.**

---

## Hướng Dẫn Sử Dụng

| Lệnh | Hành vi |
|-------|---------|
| `/ba` | Chạy full flow 11 steps, 🛑 sau mỗi step |
| `/ba scope` | Chạy chỉ Step 1: Scope Definition |
| `/ba srs` | Chạy chỉ Step 5: Create SRS |
| `/ba impact` | Chạy chỉ Step 9: Impact Analysis |
| `/ba change` | Chạy chỉ Step 10: Change Request |
| `/ba changelog` | Chạy chỉ Step 11: Change Log |
| `/ba step-3` | Chạy từ Step 3 trở đi |
| `/scope-definition` | Alias → tương đương `/ba scope` |
| `/create-srs` | Alias → tương đương `/ba srs` |
| `/create-brd` | Alias → tương đương `/ba brd` |

### Lệnh điều khiển giữa các steps

| Lệnh | Hành vi |
|-------|---------|
| `NEXT` | Tiếp tục step tiếp theo |
| `SKIP` | Bỏ qua step hiện tại, nhảy sang step tiếp |
| `STOP` | Kết thúc flow tại đây |
| `BACK` | Quay lại step trước |

---

## Waterfall vs Agile

### Waterfall: Chạy tuần tự 1 lần
- Step 1-2: Chạy 1 lần đầu dự án (Phase 0: Khởi động)
- Step 3-7: Chạy 1 lần theo waterfall phases (Phase 1-3)
- Step 8: Chạy sau go-live (Phase 4)
- Step 9-11: Chạy khi có CR (event-driven)

### Agile: Lặp lại Step 3-7 mỗi Sprint
- Step 1-2: **Sprint 0** — 1 lần (refine mỗi PI/quarter)
- Step 4 (BRD): **Skip** trong Agile — PO viết PRD thay BA viết BRD
- Step 3→5→6→7: **Lặp lại mỗi Sprint** — BA refine stories, review, push Jira
- Step 8: **Mỗi Sprint Review** (mini) + **Post-Release** (full)
- Step 9-11: **Bất kỳ lúc nào** có backlog change

> **Lưu ý Agile:** KA3 (Lifecycle Management) không phải phase riêng — nó ngấm vào mọi Sprint. Traceability, Prioritization, Maintain Requirements diễn ra liên tục.

---

## BABOK® v3 Coverage — 30/30 Tasks

| KA | Task | Step |
|----|------|------|
| KA1 | Plan BA Approach | Step 2 |
| KA1 | Plan Stakeholder Engagement | Step 2 |
| KA1 | Plan BA Governance | Step 1 |
| KA1 | Plan BA Information Management | Step 1 |
| KA1 | Identify BA Performance Improvements | Step 8 |
| KA2 | Prepare for Elicitation | Step 2 |
| KA2 | Conduct Elicitation | Step 3 |
| KA2 | Confirm Elicitation Results | Step 3 |
| KA2 | Communicate BA Information | Step 9-11 |
| KA2 | Manage Stakeholder Collaboration | Ongoing |
| KA3 | Trace Requirements | Step 4-5 |
| KA3 | Maintain Requirements | Step 7, 10 |
| KA3 | Prioritize Requirements | Step 4-5 |
| KA3 | Assess Requirements Changes | Step 9 |
| KA3 | Approve Requirements | Step 6 |
| KA4 | Analyze Current State | Step 1 |
| KA4 | Define Future State | Step 1 |
| KA4 | Assess Risks | Step 1 |
| KA4 | Define Change Strategy | Step 1 |
| KA5 | Specify & Model Requirements | Step 4-5 |
| KA5 | Verify Requirements | Step 6 |
| KA5 | Validate Requirements | Step 6 |
| KA5 | Define Requirements Architecture | Step 4-5 |
| KA5 | Define Design Options | Step 4-5 |
| KA5 | Analyze Potential Value | Step 1 |
| KA6 | Measure Solution Performance | Step 8 |
| KA6 | Analyze Performance Measures | Step 8 |
| KA6 | Assess Solution Limitations | Step 8 |
| KA6 | Assess Enterprise Limitations | Step 8 |
| KA6 | Recommend Actions | Step 8 |
