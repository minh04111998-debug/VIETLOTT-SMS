---
description: Quy trình lập kế hoạch thu thập yêu cầu - Vai trò BA (BABOK KA1)
---

# Workflow: Elicitation Plan

> **Slash command**: `/elicitation-plan`
> **Vai trò**: `[🟢 ROLE: BA]`
> **Khi nào dùng**: Trước khi bắt đầu thu thập yêu cầu cho module/feature mới
> **Đầu ra**: Elicitation Plan tại `artifacts/requirements/elicitation-plan-[tên].md`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🟢 ROLE: BA]`
- **Nạp Rules:** Đọc ngầm `ba-rules.md` (§2: BA Planning, §3: Elicitation)
- **Nạp Skills:** `.agents/skills/ba/SKILL.md`
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng

> [!NOTE]
> "1 giờ planning tốt tiết kiệm 10 giờ elicitation lộn xộn."

---

## Bước 1: Context Assessment

AI hỏi người dùng:
```
1. Dự án/module cần thu thập yêu cầu là gì?
2. Methodology đang dùng? (Agile/Waterfall/Hybrid)
3. Có bao nhiêu stakeholder chính? Liệt kê tên + vai trò
4. Tài liệu hiện có? (SOP, Excel, Word, hệ thống cũ)
5. Timeline: Khi nào cần hoàn thành elicitation?
```

🛑 **[DỪNG]** — Thu thập input

---

## Bước 2: Stakeholder Analysis

AI tạo Stakeholder Map (Power/Interest Matrix):

```markdown
## Stakeholder Map

| Stakeholder | Vai trò | Power | Interest | Strategy | Comm Channel |
|-------------|---------|-------|----------|----------|-------------|

### Engagement Plan
| Stakeholder | Kỹ thuật elicitation | Thời lượng | Ngày dự kiến |
|-------------|---------------------|------------|-------------|
```

🛑 **[DỪNG]** — Confirm stakeholder map

---

## Bước 3: Elicitation Technique Selection

AI đề xuất kỹ thuật phù hợp dựa trên context:

```markdown
## Elicitation Plan

| # | Kỹ thuật | Với ai | Mục đích | Output dự kiến | Effort |
|---|---------|--------|----------|---------------|--------|
| 1 | Interview 1-1 | [Key user] | Deep-dive quy trình | Notes, pain points | 2h |
| 2 | Document Analysis | [SOP files] | As-Is process | Hidden business rules | 4h |
| 3 | Workshop | [Cross-dept team] | Consensus on To-Be | Agreed requirements | 3h |
| 4 | Observation | [End users] | Actual vs stated workflow | Real pain points | 4h |

### Tổng effort ước tính: [X] man-days
### Timeline: [Start] → [End]
```

🛑 **[DỪNG]** — Approve elicitation plan

---

## Bước 4: Preparation Checklist

AI tạo preparation checklist cho từng session:

```markdown
## Session Prep — [Technique] với [Stakeholder]

### Trước session
- [ ] Câu hỏi/agenda đã chuẩn bị
- [ ] Tài liệu cần đọc trước đã gửi cho stakeholder
- [ ] Meeting room/link booked
- [ ] Recording/note-taking tool ready

### Trong session
- [ ] Introduce mục đích (2 phút)
- [ ] Core questions (main time)
- [ ] Summarize key points trước khi kết thúc (5 phút)
- [ ] Confirm next steps

### Sau session (trong 24h)
- [ ] Notes cleaned up và structured
- [ ] Gửi summary cho stakeholder xác nhận
- [ ] Log open items + owners
```

---

## Bước 5: Lưu trữ

- Lưu Elicitation Plan tại `artifacts/requirements/elicitation-plan-[tên].md`
- 🛑 **[DỪNG CỨNG]** — *"Elicitation Plan nháp đã lưu. Phê duyệt để chuyển sang `artifacts/requirements/`?"*
- Sau khi duyệt → chuyển sang `artifacts/requirements/elicitation-plan-[tên].md`
