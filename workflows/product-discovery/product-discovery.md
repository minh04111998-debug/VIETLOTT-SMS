---
description: Quy trình Product Discovery - Từ Idea đến Validated Solution trước khi code
---

# Workflow: Product Discovery

> **Slash command**: `/product-discovery`
> **Vai trò**: `[🔵 ROLE: PO]`
> **Khi nào dùng**: Khi có idea mới / tính năng mới / cần quyết định "có nên build không?"
> **Đầu ra**: Problem Statement validated + Experiment Design + GO/NO-GO decision

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🔵 ROLE: PO]`
- **Nạp Rules:** Đọc ngầm `po-rules.md`
- **Nguyên tắc bất di bất dịch:** Discovery luôn đi TRƯỚC Delivery. Không viết User Story khi chưa qua bước 3.
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng confirm

> [!CAUTION]
> Bỏ qua Discovery và code thẳng là cách nhanh nhất để tạo ra một sản phẩm không ai dùng.
> Jeff Bezos: "We are not building features, we are solving problems."

---

## Bước 1: Input Collection & Idea Framing

AI hỏi người dùng **tối đa 5 câu**:

```
1. Idea/tính năng muốn explore là gì? Mô tả ngắn gọn.
2. Idea này đến từ đâu? (User phản ánh / Data / Stakeholder yêu cầu / Cạnh tranh)
3. Bạn nghĩ vấn đề nào của user mà idea này giải quyết?
4. Sản phẩm/feature này target segment nào?
5. Có timeline hoặc deadline nào không?
```

🛑 **[DỪNG]** — Thu thập input trước khi bước vào Discovery

---

## Bước 2: Market Intelligence Gate (POA-D2.1)

Dựa trên idea được mô tả, AI thực hiện phân tích thị trường:

### 2.1. Competitive Mapping
Phân tích và đề xuất:
- Ai đang giải bài toán này? (Tên thực tế)
- Họ đang ở giai đoạn nào? (Early/Growth/Mature)
- User reviews của họ nói gì? (Pain points chưa được giải)

### 2.2. Feature Comparison
Tạo bảng so sánh dựa trên thông tin có sẵn:
```markdown
| Tính năng/Approach | Chúng ta | Đối thủ A | Đối thủ B |
|-------------------|---------|----------|----------|
| [Approach 1] | | | |
```

### 2.3. White Space Analysis
Xác định: Khoảng trắng nào chưa ai làm tốt?

**Output bước này:**
```markdown
## Market Scan Summary
**Thị trường:** [Mô tả ngắn]
**Đối thủ chính:** [Danh sách]
**White Space phát hiện:** [Cơ hội cụ thể]
**Preliminary view:** GO / NO-GO / CẦN THÊM DATA
```

🛑 **[DỪNG]** — Trình bày Market Scan, hỏi: "Insight nào bạn đồng ý/không đồng ý? Có thêm thông tin về thị trường không?"

---

## Bước 3: Problem Validation (POA-D2.2)

### 3.1. User Segment Definition
Xác định:
- Ai là target user cụ thể? (Không phải "tất cả mọi người")
- User vs Customer — ai dùng, ai trả tiền? Có khác nhau không?

### 3.2. Interview Planning
AI tạo **Interview Guide** sẵn sàng để dùng:

```markdown
## Interview Guide: [Tên Feature Area]
**Target:** [Mô tả người cần phỏng vấn]
**Số lượng:** Tối thiểu 5 người
**Thời gian:** 30-45 phút / người

### Câu hỏi mở đầu (Warm-up — 5 phút)
- "Bạn đang làm ở vị trí gì? Role của bạn liên quan đến [domain] như thế nào?"
- "Ngày làm việc điển hình của bạn trông như thế nào?"

### Câu hỏi khám phá vấn đề (Core — 20 phút)
- "Lần gần nhất bạn phải [task liên quan]... kể tôi nghe?"
- "Khó khăn lớn nhất trong quy trình đó là gì?"
- "Hiện tại bạn giải quyết điều đó như thế nào? Bắt đầu từ bước nào?"
- "Điều gì trong cách làm hiện tại khiến bạn bực nhất?"
- "Nếu vấn đề này biến mất ngày mai, điều gì thay đổi?"

### Câu hỏi về giá trị (Value — 10 phút)
- "Bạn đã thử giải pháp/tool nào khác chưa? Kết quả thế nào?"
- "Điều gì khiến bạn tiếp tục dùng / bỏ [tool cũ]?"

### Câu hỏi kết thúc
- "Nếu tôi có thể xây một thứ giúp bạn trong lĩnh vực này, điều đầu tiên bạn muốn là gì?"
- "Bạn có muốn được thông báo khi chúng tôi có prototype để test không?"
```

### 3.3. Problem Statement Formulation
Sau khi có interview data, AI giúp tổng hợp thành Problem Statement:

```markdown
## Problem Statement: [Tên]

**Validated với:** [X] users phỏng vấn

**Persona:** [Tên] — [Mô tả 1-2 câu từ data thật]

**Job-to-be-Done:**
"Khi [situation], tôi muốn [motivation] để [outcome]"

**Pain Points (Đã confirm ≥ 3/5 users đề cập):**
1. [Pain] — Severity: High/Med/Low | Frequency: Daily/Weekly/Monthly
2. [Pain]
3. [Pain]

**Current Workaround:** [Họ đang làm gì? Đây là indirect competitor]

**Insight quan trọng nhất:** [1 câu — "điều chúng ta không biết trước khi interview"]
```

🛑 **[DỪNG]** — Xác nhận Problem Statement. Hỏi: "Problem Statement này có đúng không? Missing insight nào không?"

---

## Bước 4: Hypothesis Formation & Experiment Design (POA-D6.1)

### 4.1. Từ Problem → Hypothesis
```markdown
## Hypothesis

**Assumption cần kiểm chứng:**
"Chúng ta giả định rằng [X là thật về user behavior/market]"

**Hypothesis:**
"Chúng ta tin rằng [làm A] sẽ giúp [persona] [đạt outcome B]
vì [lý do từ interview insight]
Chúng ta sẽ biết điều này đúng khi [metric C đạt D trong E ngày]"

**Minimum Criteria for Success (MCS):**
- Experiment PASS nếu: [metric X ≥ Y%] trong [Z ngày]
- Nếu KHÔNG đạt → [Kill / Pivot sang approach gì]
```

### 4.2. Chọn Loại MVP Phù Hợp
AI đề xuất loại MVP phù hợp dựa trên:
- Uncertainty level (Problem uncertainty vs Solution uncertainty)
- Timeline
- Available resources

| Nếu... | Dùng MVP type... |
|--------|-----------------|
| Chưa biết có demand không | Fake Door / Smoke Test |
| Biết có demand, chưa biết solution đúng không | Concierge / Wizard of Oz |
| Biết solution, chưa biết user dùng được không | Prototype (Figma) |
| Cần validate tech feasibility | Tracer Bullet / Spike |

### 4.3. Experiment Plan
```markdown
## Experiment Plan

**MVP Type:** [Loại]
**Duration:** [X ngày/tuần]
**Target participants:** [Số lượng + profile]
**Success metric:** [Cụ thể, measurable]
**Failure criteria:** [Khi nào thì kill?]
**Resources needed:** [Effort estimate — người + thời gian]
**Risk:** [Điều gì có thể làm experiment không chính xác?]
```

🛑 **[DỪNG]** — Xem xét Experiment Plan. Hỏi: "Plan này có khả thi không? Resource có sẵn không?"

---

## Bước 5: Go/No-Go Decision & Next Steps

### 5.1. Decision Matrix

```markdown
## GO / NO-GO Decision: [Tên Feature/Product]

| Chiều đánh giá | Score (1-5) | Ghi chú |
|---------------|------------|---------|
| Problem real & frequent? | /5 | |
| Market opportunity clear? | /5 | |
| We have unfair advantage? | /5 | |
| Team can execute? | /5 | |
| Timeline viable? | /5 | |
| **Tổng** | **/25** | |

**Threshold:** ≥18/25 → GO | 12-17 → Conditional GO (giải quyết blockers trước) | <12 → NO-GO
```

### 5.2. Nếu GO:
→ Tạo Product Brief → Conceptualize Solution (POA-D5.6) → Backlog (POA-D5.1)
→ Lưu tại: `artifacts/product/product-brief-[tên].md`

### 5.3. Nếu NO-GO:
→ Document lý do trong `artifacts/decisions/no-go-[tên]-[date].md`
→ "No-go ngày hôm nay, không phải mãi mãi" — ghi rõ điều kiện review lại

### 5.4. Nếu PIVOT:
→ Document: "Chúng ta học được gì? Approach mới là gì?"
→ Quay lại Bước 2 với angle mới

---

## Output Artifacts

| Artifact | Lưu tại | Status |
|---------|---------|--------|
| Market Scan Report | `artifacts/product/market/market-scan-[tên].md` | Sau Bước 2 |
| Interview Guide | `artifacts/product/research/interview-guide-[tên].md` | Bước 3 |
| Problem Statement | `artifacts/product/research/problem-statement-[tên].md` | Sau Bước 3 |
| Experiment Plan | `artifacts/product/experiments/exp-plan-[tên].md` | Bước 4 |
| GO/NO-GO Decision | `artifacts/decisions/` | Bước 5 |
