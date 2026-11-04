# 📝 Observation Protocol — Nhật Ký Quá Trình Phân Tích

> **Nguồn:** [StoriesOnBoard — AI Agent Harness Components](https://storiesonboard.com/blog/?p=6342)
> **Mục đích:** Lưu trữ metadata quá trình phân tích — giả định, câu hỏi mở, quyết định đã chốt, nguồn của từng yêu cầu, phiên bản tài liệu.
> **Áp dụng:** Mỗi khi AI tạo/cập nhật tài liệu BA/PO, PHẢI duy trì các nhật ký trong cùng thư mục `artifacts/requirements/[feature-name]/`

---

## 1. Assumption Log (Nhật Ký Giả Định)

**File:** `artifacts/requirements/[feature]/assumptions.md`

```markdown
# Assumption Log — [Tên Feature]

| ID | Giả định | Nguồn (SRC-XX) | Trạng thái | Ngày tạo | Xác nhận bởi |
|----|----------|----------------|-----------|----------|-------------|
| A-001 | ... | SRC-XX, §Y.Z | [⚠️ CHƯA XÁC NHẬN] | YYYY-MM-DD | — |
| A-002 | ... | Không có nguồn | [⚠️ CHƯA XÁC NHẬN] | YYYY-MM-DD | — |
```

**Quy tắc:**
- Mỗi giả định AI đưa ra PHẢI được log vào đây
- Khi Human xác nhận → cập nhật trạng thái `[✅ ĐÃ XÁC NHẬN bởi: Tên]`
- Khi Human bác bỏ → cập nhật `[❌ BÁC BỎ — Lý do: ...]` + cập nhật draft

---

## 2. Open Questions (Câu Hỏi Mở)

**File:** `artifacts/requirements/[feature]/open-questions.md`

```markdown
# Open Questions — [Tên Feature]

| ID | Câu hỏi | Gửi cho (Role) | Trạng thái | Ngày hỏi | Trả lời |
|----|---------|----------------|-----------|----------|---------|
| Q-001 | ... | PO | [❓ OPEN] | YYYY-MM-DD | — |
| Q-002 | ... | Stakeholder X | [✅ ĐÃ TRẢ LỜI] | YYYY-MM-DD | "..." |
```

**Quy tắc:**
- Câu hỏi phải **cụ thể và có mục đích** (không hỏi "Bạn muốn gì?")
- Phân loại priority: Blocking (chặn tiếp tục) vs. Nice-to-have

---

## 3. Decision Log (Quyết Định Đã Chốt)

**File:** `artifacts/requirements/[feature]/decisions.md`

```markdown
# Decision Log — [Tên Feature]

| ID | Quyết định | Người quyết định | Ngày | Lý do | Ảnh hưởng |
|----|-----------|-----------------|------|-------|----------|
| D-001 | ... | PO (Human) | YYYY-MM-DD | ... | SRS mục X.Y cần cập nhật |
```

**Quy tắc:**
- AI KHÔNG tự ghi decision — chỉ ghi sau khi Human tuyên bố quyết định
- Mỗi decision phải có "Ảnh hưởng" — trace sang tài liệu nào cần cập nhật

---

## 4. Source Tracking (Nguồn Của Từng Yêu Cầu)

- Mỗi requirement trong SRS/BRD/PRD PHẢI có trường `Source:` trỏ về ID trong `source-registry.md`
- Format: `Source: SRC-XX, Chương Y mục Z.W`
- Nếu requirement không có nguồn → gắn `[⚠️ KHÔNG CÓ NGUỒN — cần stakeholder xác nhận]`

---

## 5. Version Tracking

- Mỗi file nháp phải có version header:
  ```
  Version: 0.1 (Draft)
  Created: YYYY-MM-DD
  Last Modified: YYYY-MM-DD
  Self-Review Rounds: X
  ```
- Trước mỗi vòng self-correction → lưu backup: `draft-v1.md`, `draft-v2.md`
