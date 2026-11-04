---
description: Quy trình đánh giá giải pháp sau delivery - Vai trò BA (BABOK KA6)
---

# Workflow: Solution Evaluation

> **Slash command**: `/solution-evaluation`
> **Vai trò**: `[🟢 ROLE: BA]`
> **Khi nào dùng**: 2-4 tuần sau khi feature/release go-live
> **Đầu ra**: Solution Evaluation Report tại `artifacts/requirements/evaluations/`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🟢 ROLE: BA]`
- **Nạp Rules:** `ba-rules.md` (§7: Solution Evaluation)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

> [!IMPORTANT]
> Solution Evaluation là bước thường bị bỏ qua nhưng CỰC KỲ quan trọng.
> Nếu không evaluate, team sẽ tiếp tục build features mà không ai dùng.

---

## Bước 1: Gather Context

AI hỏi:
```
1. Feature/release cần evaluate? (tên, release date)
2. Requirements/AC gốc nằm ở file nào?
3. Tracking metrics đã define trước release?
4. Có data analytics nào available? (GA, Mixpanel, internal dashboards)
5. Có user feedback nào? (support tickets, NPS, interviews)
```

🛑 **[DỪNG]** — Thu thập context

---

## Bước 2: Requirements Fulfillment Check

AI kiểm tra từng requirement/AC đã được meet chưa:

```markdown
## Requirements Fulfillment — [Feature Name]

| Req/AC ID | Description | Expected | Actual | Status | Gap |
|-----------|-------------|----------|--------|--------|-----|
| AC-01 | Login OTP < 30s | < 30s | 15s | ✅ Met | |
| AC-02 | Error message hiển thị | Show error | Not shown for timeout | ❌ Not Met | Bug #123 |
| NFR-01 | Response < 2s | < 2s | 3.5s at peak | ⚠️ Partial | Performance issue |
```

---

## Bước 3: Value Assessment

```markdown
## Value Assessment — [Feature Name]

### Tracking Metrics (defined pre-release)
| Metric | Baseline | Target | Actual (Week 4) | Status |
|--------|----------|--------|-----------------|--------|
| [Metric 1] | [X] | [Y] | [Z] | ✅/❌ |

### Feature Adoption
- Total eligible users: [N]
- Users who tried feature: [N] ([%])
- Users who adopted (weekly active): [N] ([%])
- Users who abandoned: [N] ([%])

### User Feedback Summary
| Theme | Count | Sentiment | Example quote |
|-------|-------|-----------|---------------|

### Workarounds Still in Use
| Workaround | Why users still use it | Implication |
|-----------|----------------------|-------------|
```

🛑 **[DỪNG]** — Review assessment data

---

## Bước 3: Analyze Performance Measures (BABOK KA6 Task 8.2)

> Phân tích sâu dữ liệu performance — tìm root cause khi metric không đạt.

```markdown
## Performance Analysis — [Feature Name]

### Trend Analysis
| Metric | Week 1 | Week 2 | Week 3 | Week 4 | Trend |
|--------|--------|--------|--------|--------|-------|
| [Metric 1] | [X] | [X] | [X] | [X] | ↑/↓/→ |

### Root Cause Analysis (cho metrics chưa đạt target)
| Metric | Target | Actual | Root Cause Category | Root Cause Detail | Action |
|--------|--------|--------|--------------------|--------------------|--------|
| [Metric] | [X] | [Y] | Technical/Process/People/Data | [Chi tiết] | [Fix] |

### Correlation
| Metric A | Metric B | Correlation | Implication |
|----------|----------|-------------|-------------|
```

→ Nguồn: [BABOK® v3, KA6 Task 8.2](https://www.iiba.org/standards-and-resources/babok/)

---

## Bước 3b: Assess Enterprise Limitations (BABOK KA6 Task 8.4)

> Xác định giới hạn tổ chức ngăn solution đạt full value.

```markdown
## Enterprise Limitations — [Feature Name]

| Dimension | Limitation | Impact | Mitigation | Owner | Timeline |
|-----------|-----------|--------|-----------|-------|----------|
| Culture | [Mô tả] | 🔴/🟡/🟢 | [Giải pháp] | [Tên] | [Thời gian] |
| Process | [Mô tả] | 🔴/🟡/🟢 | [Giải pháp] | [Tên] | [Thời gian] |
| Skills | [Mô tả] | 🔴/🟡/🟢 | [Training plan] | [Tên] | [Thời gian] |
| Technology | [Mô tả] | 🔴/🟡/🟢 | [Upgrade plan] | [Tên] | [Thời gian] |
| Data | [Mô tả] | 🔴/🟡/🟢 | [Data quality plan] | [Tên] | [Thời gian] |
```

→ Nguồn: [BABOK® v3, KA6 Task 8.4](https://www.iiba.org/standards-and-resources/babok/)

---

## Bước 4: Recommendation

```markdown
## Recommendation — [Feature Name]

**Overall Assessment:** ✅ Success / ⚠️ Partial / ❌ Below Expectation

### Actions Recommended
| # | Action | Type | Priority | Owner | Next Sprint? |
|---|--------|------|----------|-------|-------------|
| 1 | [Action] | KEEP / ENHANCE / REMOVE / PIVOT | Must/Should/Could | [Name] | Yes/No |

### Lessons Learned
| What went well | What didn't | What to do differently |
|---------------|-------------|----------------------|
```

---

## Bước 4b: BA Performance Improvements (BABOK KA1 Task 1.5)

> Retrospective quy trình BA — cải thiện liên tục.

```markdown
## BA Retrospective — [Feature/Release Name]

### BA Process Metrics
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Requirements miss rate | [N] reqs missed | < 5% | ✅/❌ |
| DEV/QA clarification requests | [N] questions | < 3 per story | ✅/❌ |
| Change rate post-baseline | [N]% | < 15% | ✅/❌ |
| Elicitation → SRS cycle time | [N] days | < [target] | ✅/❌ |

### Lessons Learned
| Category | What happened | Root cause | Improvement action |
|----------|--------------|-----------|-------------------|
| Elicitation | [Mô tả] | [Nguyên nhân] | [Cải thiện] |
| Documentation | [Mô tả] | [Nguyên nhân] | [Cải thiện] |
| Stakeholder Mgmt | [Mô tả] | [Nguyên nhân] | [Cải thiện] |

### Technique Effectiveness
| Technique used | Effective? | Keep/Drop/Modify | Note |
|---------------|-----------|-------------------|------|
```

→ Nguồn: [BABOK® v3, KA1 Task 1.5](https://www.iiba.org/standards-and-resources/babok/) | [Lessons Learned — PMI](https://www.pmi.org/learning/library/lessons-learned-next-level-7991)

---

## Bước 5: Lưu trữ

- Lưu tại `artifacts/requirements/evaluations/eval-[feature]-[date].md`
- Bao gồm: Requirements Fulfillment + Value Assessment + Performance Analysis + Enterprise Limitations + Recommendation + BA Retrospective
- Link back to original requirements document
- Notify PO + PM với summary
- Input cho next sprint planning / backlog refinement
