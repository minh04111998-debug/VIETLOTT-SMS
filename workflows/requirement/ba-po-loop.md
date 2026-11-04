# 🔄 BA/PO Loop — Vòng Lặp 6 Bước

> **Nguồn:** [StoriesOnBoard — AI Agent Playbook](https://storiesonboard.com/blog/?p=6342),
> [TechCanvass — AI Agents for BA](https://www.techcanvass.com/studygroup/event/AI-Agents-for-Business-Analysts),
> [SAFe — AI Toolsday: Real AI, Real Agile](https://connect.scaledagile.com/public/resources/ai-toolsday-real-ai-real-agile-real-workflows-2026-08-18)
>
> **Nguyên tắc:** Tách riêng bước ANALYZE và bước CRITIQUE → kết quả đáng tin hơn.

---

## Sơ Đồ Vòng Lặp

```
  [1] FRAME ──→ [2] RESEARCH ──→ [3] ANALYZE
                                      │
                                      ▼
                [5] CRITIQUE ◄── [4] DRAFT
                     │
                Pass? ──YES──→ [6] FINALIZE
                     │              │
                    NO              ▼
                     │         🛑 HARD STOP
                     └──→ Quay lại [3] hoặc [4]
                          (Max 2 vòng critique)
```

---

## Chi Tiết Từng Bước

### Bước 1: FRAME (Đóng Khung Vấn Đề)

**Input:** Yêu cầu từ người dùng hoặc stakeholder
**Hành động:**
1. Xác định: mục tiêu, phạm vi, đối tượng, ràng buộc
2. Đọc source từ `knowledge/standards/source-registry.md` — xác định nguồn liên quan
3. Đối chiếu thuật ngữ ban đầu với `knowledge/glossary/glossary.md`
4. Tạo danh sách câu hỏi mở `[❓ OPEN]`

**Output:** Scope statement sơ bộ + danh sách câu hỏi mở
**Stopping condition:** 🛑 DỪNG nếu có > 3 câu hỏi blocking chưa được trả lời

---

### Bước 2: RESEARCH (Thu Thập & Khảo Cứu)

**Input:** Scope statement từ bước 1
**Hành động:**
1. Đọc tài liệu gốc từ source registry (SRC-01 → SRC-10)
2. Đối chiếu quy tắc nghiệp vụ với `knowledge/business-rules/business-rules.md`
3. Trích dẫn mọi thông tin với provenance: `[Nguồn: SRC-XX, mục Y.Z]`
4. Ghi nhận thông tin thiếu → `[⚠️ KHÔNG CÓ NGUỒN]`

**Output:** Ghi chú nghiên cứu có trích dẫn nguồn
**Stopping condition:** DỪNG nếu không tìm thấy nguồn trong registry → hỏi người dùng

---

### Bước 3: ANALYZE (Phân Tích — TÁCH RIÊNG Khỏi Draft)

**Input:** Ghi chú nghiên cứu từ bước 2
**Hành động:**
1. Phân nhóm requirements (affinity clustering)
2. Phân tích exception & edge cases (8 nhóm theo `ba-rules.md` §3.5)
3. Xây dựng luồng nghiệp vụ bằng Mermaid (Sequence/Flowchart)
4. Phát hiện xung đột, gaps, dependencies
5. Kiểm tra ranh giới Human ↔ AI (xem `.agents/rules/boundaries.md`)

**Output:** Phân tích có cấu trúc (CHƯA phải tài liệu hoàn chỉnh)

---

### Bước 4: DRAFT (Soạn Thảo Nháp)

**Input:** Phân tích từ bước 3
**Hành động:**
1. Soạn thảo tài liệu theo template `templates/`
2. Lưu vào `artifacts/requirements/[feature-name]/[tên-file].md`
3. Gắn nhãn đúng tag: `[⚠️ GIẢ ĐỊNH]`, `[❓ OPEN]`, `[📌 CẦN HUMAN QUYẾT ĐỊNH]`
4. Tạo file observation kèm theo: `assumptions.md`, `open-questions.md`

**Output:** File nháp vật lý + observation files

---

### Bước 5: CRITIQUE (Rà Soát — TÁCH RIÊNG Khỏi Draft)

**Input:** Draft từ bước 4
**Hành động:**
1. Chạy checklist nghiệm thu: `evaluations/skills/ba-output-checklist.md` hoặc `po-output-checklist.md`
2. Đối chiếu `.agents/rules/banned-words.md` — thay thế từ mơ hồ
3. Cross-review: AI đội mũ role khác (DEV, QA, PO) để challenge (xem `evaluations/agents/cross-review-protocol.md`)
4. Second-agent critic (xem `evaluations/agents/second-agent-critic.md`)
5. Ghi nhận lỗi phát hiện và cách sửa

**Quyết định:**
- Nếu **PASS** tất cả 🔴 Blocking items → tiếp bước 6
- Nếu **FAIL** → quay lại bước 3 hoặc 4 (max 2 vòng)
- Nếu **vượt 2 vòng** → 🛑 HARD STOP + Escalation (xem `.agents/rules/self-correction-rules.md`)

**Output:** Báo cáo critique + danh sách lỗi đã sửa

---

### Bước 6: FINALIZE (Hoàn Thiện & Giao)

**Input:** Draft đã pass critique
**Hành động:**
1. Trình người dùng với báo cáo tổng hợp:
   ```
   📋 Self-Review: X vòng kiểm tra, Y lỗi tự sửa
   📝 Giả định chờ xác nhận: [danh sách]
   ❓ Câu hỏi mở còn lại: [danh sách]
   📊 Nguồn trích dẫn: [danh sách SRC-XX]
   ```
2. 🛑 **HARD STOP** — Chờ Human approve

**Sau khi approve:**
- Di chuyển từ `artifacts/requirements/[feature]/` sang `artifacts/requirements/`
- Cập nhật `decisions.md` với quyết định phê duyệt
- Thông báo: *"Tài liệu đã baseline. Bước tiếp theo: [gợi ý]"*

---

## Stopping Conditions Tổng Hợp

| Bước | Điều kiện dừng | Hành động |
|------|---------------|-----------|
| Frame | > 3 câu hỏi blocking chưa trả lời | 🛑 DỪNG, hỏi người dùng |
| Research | Không tìm thấy nguồn trong registry | 🛑 DỪNG, hỏi nguồn mới |
| Critique | Fail sau 2 vòng | 🛑 HARD STOP + Escalation report |
| Finalize | Luôn luôn | 🛑 HARD STOP, chờ Human approve |
