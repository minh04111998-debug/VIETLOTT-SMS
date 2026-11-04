---
description: Phân tích tác động thay đổi — BA Change Management capability
---

# Workflow: Impact Analysis

> **Slash command**: `/ba impact`
> **Vai trò**: `[🟢 ROLE: BA]`
> **Khi nào dùng**: Khi cần đánh giá tác động của thay đổi TRƯỚC khi approve CR
> **Đầu ra**: Impact Analysis Report + Dependency Graph + Communication Plan

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🟢 ROLE: BA]`
- **Nạp Rules:** `.agents/rules/ba-rules.md` (đặc biệt §7 — Change Management)
- **Nạp Skills:** `.agents/skills/ba/SKILL.md` (§24 → §29)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

> [!WARNING]
> Impact Analysis PHẢI hoàn thành TRƯỚC khi approve Change Request. Không skip step này.

---

## Bước 1: Change Request Intake

Hỏi người dùng:
```
1. Thay đổi cụ thể là gì? (Before → After)
2. Tại sao cần thay đổi? (Business reason)
3. Ai request? Ai approve?
4. Có deadline cứng không?
5. Có tài liệu liên quan nào cần cung cấp? (PRD, SRS, API spec)
```

🛑 **[DỪNG]** — Thu thập thông tin Change Request

---

## Bước 2: Impact Scoring

Dùng **BA Skill §27 (Impact Scoring Matrix)**:
- Score 6 dimensions: Scope, Documents, Code, Testing, User, Risk
- Phân loại: 🟢 Minor / 🟡 Moderate / 🟠 Significant / 🔴 Major
- Quyết định mức review cần thiết

🛑 **[DỪNG]** — *"Impact score = [X]. Classification: [Level]. Đồng ý chưa?"*

---

## Bước 3: Dependency Mapping

Dùng **BA Skill §26 (Dependency Graph)**:
- Xác định điểm bắt đầu change
- Trace toàn bộ downstream dependencies
- Tạo Mermaid dependency graph
- Liệt kê Cascading Documents cần update

🛑 **[DỪNG]** — *"Dependency graph đã đủ chưa? Có document nào bị thiếu?"*

---

## Bước 4: Risk Assessment & Effort Estimation

- Liệt kê risks: probability × impact
- Mitigation plan cho mỗi risk
- Effort estimate theo role (BA, DEV, QA, Designer, SA, DevOps)
- Breaking change detection (theo `ba-rules.md` §7.3)

🛑 **[DỪNG]** — *"Risk + Effort OK? Approve Impact Analysis?"*

---

## Bước 5: Communication Plan & Lưu Trữ

Dùng **BA Skill §28 (Communication Plan)**:
- Tạo Change Notification cho affected teams
- Xác định timeline milestones
- Assign owners cho mỗi action item

Lưu trữ:
- Impact Analysis → `artifacts/requirements/impact-analysis-CR-[NNN].md`
- 🛑 **[DỪNG]** — *"✅ Impact Analysis complete. Approve để baseline?"*
- Sau approve → `artifacts/requirements/impact-analysis-CR-[NNN].md`
- Thông báo: *"Impact Analysis đã baseline. Tiếp theo: trigger cascading updates bằng `/ba change`."*
