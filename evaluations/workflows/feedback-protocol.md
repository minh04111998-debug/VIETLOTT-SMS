# 🔁 Feedback Protocol — Vòng Học Từ Sửa Lỗi

> **Nguồn:** [StoriesOnBoard — AI Agent Harness: Feedback Component](https://storiesonboard.com/blog/?p=6342)
> **Mục đích:** Khi người dùng sửa bản nháp của AI, ghi lại lý do và cập nhật vào file quy tắc để AI không lặp lại lỗi.

---

## Quy Trình Closed-Loop

```
AI soạn draft → Human review → Human sửa/reject
                                     │
                                     ▼
                        AI hỏi: "Bạn sửa vì lý do gì?"
                                     │
                                     ▼
                        Ghi nhận vào feedback-log.md
                                     │
                                     ▼
                        Cùng loại sửa lặp ≥ 2 lần?
                           │              │
                          YES            NO
                           │              │
                           ▼              ▼
                   AI ĐỀ XUẤT cập nhật   Ghi log,
                   knowledge/business-rules/business-rules.md   tiếp tục
                           │
                           ▼
                   Human đồng ý? → Cập nhật file
```

---

## Feedback Log

**File:** `artifacts/requirements/[feature]/feedback-log.md`

```markdown
# Feedback Log — [Tên Feature]

| Ngày | File bị sửa | Nội dung AI viết | Nội dung Human sửa | Lý do | Rule cần cập nhật |
|------|------------|-----------------|-------------------|-------|------------------|
| YYYY-MM-DD | srs-v1.md, §3.2 | "Timeout = 30s" | "Timeout = 60s" | SLA Telco yêu cầu 60s | business-rules.md BR-0XX |
```

---

## Quy Tắc Cập Nhật Rules

1. **Ngưỡng kích hoạt:** Cùng 1 loại sửa lặp lại ≥ 2 lần trong cùng dự án
2. **AI trình đề xuất:** *"Tôi nhận thấy bạn đã sửa [X] 2 lần. Nên thêm quy tắc: [Y] vào [file Z] không?"*
3. **Chỉ cập nhật sau khi Human đồng ý** — AI KHÔNG tự sửa rules
4. **File có thể cập nhật:**
   - `knowledge/business-rules/business-rules.md` — quy tắc nghiệp vụ mới
   - `knowledge/glossary/glossary.md` — thuật ngữ mới
   - `.agents/rules/banned-words.md` — từ cấm mới
   - `.agents/rules/ba-rules.md` hoặc `.agents/rules/po-rules.md` — quy tắc vai trò
