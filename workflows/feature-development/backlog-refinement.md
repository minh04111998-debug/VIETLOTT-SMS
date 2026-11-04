---
description: Quy trình Backlog Refinement - Grooming, Scoring, Story Splitting trước Sprint Planning
---

# Workflow: Backlog Refinement

> **Slash command**: `/backlog-refinement`
> **Vai trò**: `[🔵 ROLE: PO]`
> **Khi nào dùng**: Tối thiểu 1 lần/sprint trước Sprint Planning. Khi backlog có items "thô" cần làm rõ.
> **Đầu ra**: Refined backlog items sẵn sàng cho Sprint Planning (pass Definition of Ready)

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🔵 ROLE: PO]`
- **Nạp Rules:** Đọc ngầm `po-rules.md`
- **Mục tiêu:** Sau session này, top N items trong backlog phải đủ điều kiện **Definition of Ready**
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng confirm

> [!NOTE]
> Refinement không chỉ là ước lượng story points. Đây là session để align understanding giữa PO và Dev team về "tại sao làm" trước khi "làm như thế nào".

---

## Bước 1: Thu Thập Backlog Items

AI hỏi người dùng cung cấp danh sách backlog items cần refine:

```
Yêu cầu cung cấp:
1. Danh sách các items cần refine (title + mô tả ngắn)
2. Epic/Feature mà các items thuộc về (nếu có)
3. Sprint Planning kế tiếp là khi nào? (để estimate timeline)
4. Velocity trung bình của team (story points/sprint)?
5. Có item nào đặc biệt quan trọng hoặc có dependency không?
```

🛑 **[DỪNG]** — Chờ cung cấp danh sách backlog items

---

## Bước 2: Context & Priority Check

Với mỗi item, AI kiểm tra:

### 2.1. Gắn vào Epic/Objective
```markdown
Item: [Tên story]
→ Thuộc Epic nào? [Epic title]
→ Metric nào sẽ move nếu story này done? [Cụ thể]
→ Tại sao item này quan trọng BÂY GIỜ? (thay vì để sau)
```

### 2.2. RICE Quick Score
```markdown
| Item | Reach | Impact | Confidence | Effort | RICE Score |
|------|-------|--------|-----------|--------|-----------|
| [Story 1] | [số user/quý] | [0.25-3] | [50-100%] | [person-months] | [tính] |
| [Story 2] | | | | | |

Reach × Impact × Confidence / Effort = RICE Score
→ Sort descending theo RICE Score
```

🛑 **[DỪNG]** — Trình bày priority order, hỏi: "Thứ tự này có đúng không? Item nào cần điều chỉnh priority?"

---

## Bước 3: Story Clarity Check & Writing

Với mỗi item (bắt đầu từ priority cao nhất), AI kiểm tra và chuẩn hóa:

### 3.1. User Story Completeness Check
```markdown
Checklist:
☐ Có đủ format "Là [user], tôi muốn [action], để [benefit]"?
☐ Acceptance Criteria viết theo Given/When/Then?
☐ Out of scope được liệt kê rõ?
☐ Metric gắn cụ thể?
☐ Wireframe/mockup đính kèm (nếu UI change)?
☐ Non-functional requirements (performance, security) đã xác định?
```

### 3.2. Nếu Story Cần Cải Thiện, AI Đề Xuất

**Template đề xuất rewrite:**
```markdown
## [Story Title] — Refined

**User Story:**
Là [type of user — cụ thể hơn]
Tôi muốn [action — cụ thể, có thể test được]
Để [benefit — business value rõ ràng]

**Acceptance Criteria:**
```
Given [precondition cụ thể]
When [user action cụ thể]
Then [system behavior cụ thể, measurable]

Given [precondition khác]
When [edge case action]
Then [expected behavior]
```

**Out of Scope (trong story này):**
- [Explicitly list what's NOT included]

**Metric gắn:** [Feature này ảnh hưởng metric nào? Baseline và target?]

**Dependencies:** [Story nào phải done trước? API nào cần?]
```

### 3.3. Story Too Large? → Split!

Nếu story vượt quá 1 sprint, AI đề xuất cách split theo SPIDR:

```markdown
Phát hiện: Story "[X]" ước lượng > 8 SP → Cần split

Đề xuất split theo [Path/Interface/Data/Rules]:

Story A (Sprint N): [Scope nhỏ hơn, vẫn có value]
Story B (Sprint N+1): [Phần còn lại]

Tiêu chí: Mỗi story sau split vẫn phải deliver independent value
```

🛑 **[DỪNG]** — Review các story đã refine, confirm acceptance trước khi tiếp tục

---

## Bước 4: Definition of Ready Check

Với mỗi story đã refine, kiểm tra Definition of Ready:

```markdown
## DoR Checklist — [Story Title]

□ Story viết đúng format User Story
□ Acceptance Criteria = Given/When/Then, rõ ràng, testable
□ Story đủ nhỏ (≤ 1 sprint với velocity hiện tại)
□ Dependency đã xác định + giải pháp handle
□ Wireframe/mockup đính kèm (nếu cần)
□ Non-functional requirements xác định
□ Team có thể estimate (không có unknown lớn)
□ Metric gắn rõ ràng
□ Out of scope liệt kê

**Status:**
✅ READY — Có thể vào Sprint Planning
⚠️ NEEDS WORK — [List những gì cần làm thêm trước khi ready]
❌ NOT READY — [Lý do, cần thêm Discovery]
```

---

## Bước 5: Sprint Capacity Check

Sau khi có danh sách items đã refine:

```markdown
## Sprint Capacity Planning

**Team velocity:** [X] story points/sprint
**Sprint duration:** [2 tuần]

**Proposed Sprint Backlog:**
| Story | SP estimate | Priority | Notes |
|-------|------------|---------|-------|
| [Story 1] | [SP] | Must | |
| [Story 2] | [SP] | Should | |
| [Story 3] | [SP] | Could | |
| **Tổng Must** | **[SP]** | | ≤ 80% velocity |
| **Tổng Must+Should** | **[SP]** | | ≤ velocity |

**Recommendation:**
- Must-have items: Chiếm ≤ 80% capacity (buffer cho unexpected)
- 20% còn lại: Tech debt, bugs, improvements
```

🛑 **[DỪNG]** — Confirm Sprint proposal. Hỏi: "Capacity plan này có phù hợp không? Cần swap item nào không?"

---

## Bước 6: Refinement Summary & Next Actions

```markdown
## Refinement Session Summary — Sprint [N]

**Date:** [DD/MM/YYYY]
**Items reviewed:** [Số lượng]
**Items ready:** [Số lượng] ✅
**Items need more work:** [Số lượng] ⚠️
**Items blocked/need discovery:** [Số lượng] ❌

### Items Ready for Sprint Planning
| Story | SP | Owner | Notes |
|-------|----|-------|-------|

### Action Items Before Sprint Planning
| Action | Owner | Deadline |
|--------|-------|---------|
| [Cần wireframe cho Story X] | [Designer] | [Date] |
| [Cần clarify AC với stakeholder Y] | [PO] | [Date] |

### Backlog Health
**Top 3 priorities sau session này:**
1. [Story]
2. [Story]  
3. [Story]
```

---

## Output Artifacts

| Artifact | Lưu tại |
|---------|---------|
| Refined user stories | Cập nhật trực tiếp Jira/tool | 
| Refinement notes | `artifacts/requirements/sprints/refinement-[sprint]-[date].md` |
| RICE scoring sheet | `artifacts/requirements/sprints/rice-score-[sprint].md` |
