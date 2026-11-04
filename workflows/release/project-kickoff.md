---
description: Quy trình khởi động dự án (Project Kickoff) - Vai trò PM
---

# Workflow: Project Kickoff

> **Slash command**: `/project-kickoff`
> **Vai trò**: `[⚪ ROLE: PM]`
> **Khi nào dùng**: Khi bắt đầu dự án mới hoặc phase mới
> **Đầu ra**: Project Charter + WBS + Risk Register + RACI Matrix

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[⚪ ROLE: PM]`
- **Nạp Rules:** `.agents/rules/pm-rules.md`
- **Nạp Skills:** `.agents/skills/pm/SKILL.md` (Skill 1-10)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

---

## Bước 1: Thu Thập Thông Tin Dự Án

Hỏi người dùng:
```
1. Tên dự án và mô tả ngắn gọn?
2. Sponsor / Stakeholder chính?
3. Mục tiêu kinh doanh và KPIs?
4. Timeline mong muốn (deadline cứng hay linh hoạt)?
5. Team size và composition (có ai sẵn sàng chưa)?
6. Budget estimate (nếu có)?
7. Methodology: Agile (Scrum) hay Waterfall?
```

🛑 **[DỪNG]** — Thu thập input

---

## Bước 2: Tạo Project Charter

Dùng Skill 1 (Project Charter template):
- Thông tin dự án, mục tiêu, phạm vi
- Stakeholder list + kỳ vọng
- Milestones chính
- Giả định & ràng buộc

🛑 **[DỪNG]** — *"Project Charter OK? Có điều chỉnh gì?"*

---

## Bước 3: WBS + RACI

- Tạo WBS (Skill 2) — Mermaid diagram
- Tạo RACI Matrix (Skill 6) cho mỗi hoạt động chính
- Ước lượng effort: Three-point estimation (pm-rules §2.2)

🛑 **[DỪNG]** — Review WBS + RACI

---

## Bước 4: Risk Register + Capacity

- Tạo Risk Heat Map (Skill 7) — top 5 risks
- Resource Capacity Planning (Skill 8) — cho sprint/phase đầu tiên
- Phase Gate Checklist (pm-rules §5)

🛑 **[DỪNG]** — *"Risks và capacity OK?"*

---

## Bước 5: Lưu Trữ

- Lưu tại `artifacts/product/project-charter-[name].md`
- 🛑 **[DỪNG]** — *"✅ Project Charter + Plan đã lưu. Approve để baseline?"*
- Sau approve → `artifacts/requirements/`

---

## Cross-References (Phase 2 additions)

> [!NOTE]
> **Inputs bổ sung cho Kickoff:**
> - **Stakeholder Register** (SKILL.md Skill 11): Tạo Power/Interest Grid ngay trong bước 2 (Project Charter) để map stakeholder landscape sớm. Ref: `pm-rules.md` §7.
> - **Complexity Assessment** (pm-rules.md §9): Đánh giá mức độ phức tạp dự án (technical, organizational, environmental) để chọn approach phù hợp.
> - **Tailoring Decision Record** (SKILL.md Skill 15): Xác định methodology (Agile/Waterfall/Hybrid) dựa trên context assessment. Ref: `pm-rules.md` §10.
