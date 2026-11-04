---
description: Quy trình PO end-to-end theo POA Framework — Từ discovery đến release. Gọi `/po` chạy full flow, `/po [step]` chạy 1 step.
---

# 🔵 PO Master Workflow — POA Framework

> **Full flow:** `/po` → Chạy tất cả 10 steps tuần tự
> **Từng step:** `/po discovery` hoặc `/product-discovery` → Chạy 1 step cụ thể
> **Vai trò:** `[🔵 ROLE: PO]`
> **Framework:** IIBA POA 7 Domains

---

## CHỈ THỊ CHO AI

- **Khai báo:** Đầu mỗi phản hồi, BẮT BUỘC in `[🔵 ROLE: PO]`
- **Nạp Rules:** Đọc ngầm `.agents/rules/po-rules.md`
- **Nạp Skills:** Sẵn sàng gọi `.agents/skills/po/SKILL.md` (lazy-load khi step cần)
- **Dừng cứng:** 🛑 sau mỗi step, chờ user gõ lệnh điều khiển

---

## Tổng Quan 10 Steps

| Step | Tên | Slash shortcut | POA Domain | Output |
|------|-----|----------------|------------|--------|
| 1 | Product Strategy | `/po strategy` hoặc `/product-strategy` | D1 + D4 | product-strategy.md |
| 2 | Product Discovery | `/po discovery` hoặc `/product-discovery` | D2 + D6 | discovery-report.md |
| 3 | User Journey Mapping | `/po journey` hoặc `/user-journey-mapping` | D2 | user-journey.md |
| 4 | Stakeholder Alignment | `/po stakeholder` hoặc `/stakeholder-alignment` | D3 | stakeholder-map.md |
| 5 | Create PRD | `/po prd` hoặc `/create-prd` | D5 | prd-[tên].md |
| 6 | Backlog Refinement | `/po backlog` hoặc `/backlog-refinement` | D5 + D7 | refined-backlog.md |
| 7 | Product Health Check | `/po health` hoặc `/product-health-check` | D1 + D4 | health-report.md |
| 8 | Release Planning | `/po release` hoặc `/release-planning` | D5 | release-plan.md |
| 9 | Production Readiness | `/po ready` hoặc `/production-readiness` | Cross-domain | readiness-checklist.md |
| 10 | Post-Release Review | `/po review` | D6 + D7 | post-release-report.md |

---

## STEP 1: Product Strategy
> Xác định vision, target group, North Star Metric, lifecycle stage.
→ Chi tiết: Xem [product-strategy.md](product-strategy.md)
→ Gọi Skills: POA-D1 (Foundational), POA-D4 (Make Impact — Vision, OKR)
🛑 **Xong Step 1.** Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 2: Product Discovery
> Market scan → User interview → Empathy Map → VPC → Problem validation → GO/NO-GO.
→ Chi tiết: Xem [product-discovery.md](product-discovery.md)
→ Gọi Skills: POA-D2 (Customer Intimacy — Market, Journey, Empathy, VPC, PMF), POA-D6 (Learn Fast — Experiment/MVP)
🛑 **Xong Step 2.** Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 3: User Journey Mapping
> Vẽ journey, empathy maps, pain points, moments of truth.
→ Chi tiết: Xem [user-journey-mapping.md](user-journey-mapping.md)
→ Gọi Skills: POA-D2 (Customer Intimacy — Journey, Empathy Map, HCD)
🛑 **Xong Step 3.** Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 4: Stakeholder Alignment
> Map stakeholders, align expectations, resolve conflicts, collaborative games.
→ Chi tiết: Xem [stakeholder-alignment.md](stakeholder-alignment.md)
→ Gọi Skills: POA-D3 (Engage Whole Team — Stakeholder, Cross-functional, Games)
🛑 **Xong Step 4.** Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 5: Create PRD
> Viết Product Requirements Document + User Stories / Job Stories + AC.
→ Chi tiết: Xem [create-prd.md](create-prd.md)
→ Gọi Skills: POA-D5 (Deliver Often — Backlog, Story Map, Job Stories), BA skills (Elicitation, Mermaid Flow, Edge Cases)
🛑 **Xong Step 5.** PRD nháp đã lưu. Gõ **'NEXT'** | **'STOP'**

## STEP 6: Backlog Refinement
> Grooming, RICE scoring, story mapping, story splitting, Sprint Planning input.
→ Chi tiết: Xem [backlog-refinement.md](backlog-refinement.md)
→ Gọi Skills: POA-D5 (Backlog, Story Map), POA-D7 (Prioritization — RICE/WSJF/Kano, Value Modelling)
🛑 **Xong Step 6.** Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 7: Product Health Check
> Đánh giá product health — metrics, lifecycle, value stream, adoption.
→ Chi tiết: Xem [product-health-check.md](product-health-check.md)
→ Gọi Skills: POA-D1 (Lifecycle), POA-D4 (Metrics, OKR), POA-D7 (Value Stream)
🛑 **Xong Step 7.** Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 8: Release Planning
> Plan release approach, timeline, communication, DoR/DoV/DoD check.
→ Chi tiết: Xem [release-planning.md](release-planning.md)
→ Gọi Skills: POA-D5 (Release Management, Definition Concepts)
🛑 **Xong Step 8.** Gõ **'NEXT'** | **'SKIP'** | **'STOP'**

## STEP 9: Production Readiness
> Checklist 5 giai đoạn trước khi release. **PM lead** — PO participate.
→ Chi tiết: Xem [production-readiness.md](../pm/production-readiness.md)
🛑 **Xong Step 9.** Gõ **'NEXT'** | **'STOP'**

## STEP 10: Post-Release Review
> Đánh giá sau release: metrics vs baseline, user feedback, learning loops.
- Measure against MCS/OKR
- Feature adoption tracking
- User feedback synthesis
- Learning Loop: "We assumed → We tested → We learned → Next action"
- Decide: Keep / Enhance / Pivot / Kill
→ Gọi Skills: POA-D6 (Learning Loops), POA-D7 (Continuous Value Optimization)
🛑 **Xong Step 10.** **🎉 PO FLOW HOÀN TẤT.**

---

## Hướng Dẫn Sử Dụng

| Lệnh | Hành vi |
|-------|---------|
| `/po` | Chạy full flow 10 steps |
| `/po discovery` | Chạy chỉ Step 2 |
| `/po prd` | Chạy chỉ Step 5 |
| `/po step-6` | Chạy từ Step 6 trở đi |
| `/product-discovery` | Alias → `/po discovery` |
| `/create-prd` | Alias → `/po prd` |

### Lệnh điều khiển
| Lệnh | Hành vi |
|-------|---------|
| `NEXT` | Tiếp step tiếp theo |
| `SKIP` | Bỏ qua step hiện tại |
| `STOP` | Kết thúc flow |
| `BACK` | Quay lại step trước |
