---
description: Quy trình vẽ User Journey Map có cấu trúc - Vai trò PO
---

# Workflow: User Journey Mapping

> **Slash command**: `/user-journey-mapping`
> **Vai trò**: `[🔵 ROLE: PO]`
> **Khi nào dùng**: Hiểu trải nghiệm user end-to-end, tìm pain points và cơ hội cải thiện
> **Đầu ra**: User Journey Map tại `artifacts/product/research/`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🔵 ROLE: PO]`
- **Nạp Rules:** `po-rules.md` (§4.2: User Journey Mapping)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

> [!NOTE]
> Journey ≠ Flow. Journey = trải nghiệm cảm xúc theo thời gian (ngày/tuần).
> Flow = luồng màn hình trong app (phút). Workflow này tập trung vào Journey.

---

## Bước 1: Define Scope

AI hỏi:
```
1. Persona cần vẽ journey? (cụ thể: vai trò, bối cảnh)
2. Goal/Job-to-be-Done của persona này?
3. Journey scope: End-to-end hay focus vào giai đoạn cụ thể?
4. Có data user research sẵn không? (interviews, surveys, analytics)
5. Journey hiện tại (As-Is) hay mong muốn (To-Be)?
```

🛑 **[DỪNG]** — Confirm scope

---

## Bước 2: Map Journey Stages

AI tạo User Journey Map:

```markdown
## User Journey Map

**Persona:** [Tên] — [Mô tả ngắn]
**Goal:** [Job-to-be-Done]
**Journey Type:** As-Is / To-Be

| Giai đoạn | Hành động | Suy nghĩ | Cảm xúc | Touchpoint | Pain Point | Cơ hội |
|-----------|-----------|----------|---------|------------|------------|--------|
| Awareness | [User biết đến sản phẩm/vấn đề] | "Tôi cần..." | 😐 0 | [Channel] | [Pain] | [Opportunity] |
| Research | [User tìm hiểu options] | "Cái nào phù hợp?" | 🤔 -1 | [Channel] | [Pain] | [Opportunity] |
| Decision | [User quyết định chọn] | "Tôi sẽ thử..." | 😊 +1 | [Channel] | [Pain] | [Opportunity] |
| Onboarding | [User bắt đầu sử dụng] | "Dễ không?" | 😐/😠 | [Feature] | [Pain] | [Opportunity] |
| Core Usage | [User dùng tính năng chính] | "Có giải quyết được không?" | 😊/😠 | [Feature] | [Pain] | [Opportunity] |
| Retention | [User quay lại] | "Tôi quay lại vì..." | 😊 +2 | [Feature] | [Pain] | [Opportunity] |
```

---

## Bước 3: Emotion Curve

AI vẽ Emotion Curve dạng text hoặc Mermaid:

```
Cảm xúc
+2  😊😊                                    ████
+1  😊       ██████                    ████
 0  😐  ████           ████
-1  😠                       ██████
-2  😠😠
    ────────────────────────────────────────
    Awareness → Research → Decision → Onboarding → Core → Retention
```

**Moment of Truth:** Giai đoạn nào nếu trải nghiệm tốt → user trung thành?
**Critical Friction:** Giai đoạn nào nếu trải nghiệm xấu → user churn?

🛑 **[DỪNG]** — Review Journey Map + Emotion Curve

---

## Bước 4: Opportunity Prioritization

```markdown
## Opportunities Identified

| # | Giai đoạn | Pain Point | Opportunity | Impact (H/M/L) | Effort (H/M/L) | Priority |
|---|----------|-----------|-------------|----------------|----------------|----------|
| 1 | Onboarding | Setup quá phức tạp | Wizard step-by-step | High | Medium | 🔴 Do First |
| 2 | Core Usage | Search chậm | AI suggestion | High | High | 🟡 Plan |
```

---

## Bước 5: Lưu trữ

- Lưu tại `artifacts/product/research/journey-[persona]-[goal].md`
- Link to related: Problem Statement, PRD, User Stories
- Input cho: `/product-discovery`, `/backlog-refinement`
