# 🎭 Second-Agent Critic Protocol

> **Nguồn:** [SAFe — AI Toolsday: Real AI, Real Agile](https://connect.scaledagile.com/public/resources/ai-toolsday-real-ai-real-agile-real-workflows-2026-08-18),
> [DeepMind — Debate Paper](https://arxiv.org/abs/1805.00899)
>
> **Mục đích:** Sau bước Draft, AI đóng vai một "agent thứ hai" (PO hoặc Scrum Team member) để soi bản nháp từ góc nhìn khác. Tách biệt với Cross-Review Protocol (đội mũ DEV/QA/SA).

---

## Khi Nào Kích Hoạt

- Sau bước 4 (DRAFT) trong ba-po-loop, TRƯỚC bước 5 (CRITIQUE)
- Chỉ áp dụng cho output loại: **SRS, BRD, PRD, User Story batch**
- KHÔNG áp dụng cho: single-question answers, quick edits, changelog

---

## Kịch Bản Critic

### Critic 1: "Scrum Team Challenge"

AI đóng vai Dev Lead + QA Lead và hỏi:

```markdown
## 🎯 Scrum Team Challenge

1. **Story quá lớn?** Story nào có > 8 story points hoặc > 5 AC? → Đề xuất split
2. **Giả định chưa kiểm chứng?** Giả định nào trong assumptions.md chưa có nguồn xác nhận?
3. **Edge case thiếu?** Còn scenario nào chưa có AC? (empty input, concurrent, timeout, retry exhausted)
4. **Testable?** Mỗi AC có thể viết thành test case Given-When-Then không?
5. **Dependencies?** Story nào phụ thuộc story khác? Có blocking không?
```

### Critic 2: "PO Business Challenge"

AI đóng vai PO và hỏi:

```markdown
## 🔵 PO Business Challenge

1. **Value?** Feature này deliver value gì cho user? Metric nào move?
2. **Priority?** So với backlog hiện tại, feature này priority bao nhiêu? RICE score?
3. **MVP scope?** Có thể cắt gì ra khỏi MVP mà vẫn giữ được core value?
4. **User segment?** Ai là người dùng chính? Bao nhiêu % user base bị ảnh hưởng?
5. **Cannibalization?** Feature mới có conflict với feature hiện có không?
```

---

## Output Format

```markdown
## 📋 Second-Agent Critic Report

### Findings
| # | Loại | Mô tả | Mức độ | Đề xuất |
|---|------|-------|--------|---------|
| 1 | Story quá lớn | US-003 có 8 AC | 🟡 Important | Split thành 2 stories |
| 2 | Edge case thiếu | Chưa có AC cho "SIM hết hạn" | 🔴 Blocking | Bổ sung AC |

### Kết luận
- [ ] Đã sửa tất cả 🔴 Blocking → Tiếp sang CRITIQUE
- [ ] Còn 🔴 Blocking chưa sửa được → 🛑 ESCALATION
```
