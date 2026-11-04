# Mẫu Tài Liệu Product — POA Framework

> Tham chiếu từ: `.agents/skills/po/SKILL.md` — Tất cả 7 POA Domains
> **Cấu trúc:** Giữ nguyên templates gốc + bổ sung templates mới từ POA

---

## 0. PRD Template (Product Requirements Document)

> **Khi nào dùng:** Khi PO cần tài liệu hóa requirements cho 1 feature/product mới. Đây là template chuẩn — `create-prd.md` workflow sẽ generate file theo template này.

```markdown
# PRD — [Tên Sản Phẩm/Tính Năng]

**Version:** 1.0 | **Ngày:** [DD/MM/YYYY] | **PO:** [Tên] | **Status:** Draft / Approved

## 1. Tổng Quan
### 1.1. Mục đích
[Tại sao build? Problem gì đang giải quyết?]

### 1.2. Background & Context
[Bối cảnh dẫn đến nhu cầu này. Discovery evidence, user research findings.]

### 1.3. Mục tiêu & KPIs
| Mục tiêu | Metric | Baseline | Target | Timeline |
|----------|--------|----------|--------|----------|
| [Goal 1] | [Metric] | [Current] | [Target] | [By when] |

### 1.4. Evidence
| Nguồn | Key Insight | Confidence |
|-------|-------------|-----------|
| [User interview / Analytics / Market research] | [Phát hiện] | [High/Med/Low] |

## 2. Đối Tượng Người Dùng (Personas)
| Persona | Vai trò | Nhu cầu chính | Pain points | Frequency |
|---------|---------|--------------|-------------|-----------|
| [Tên] | [Role] | [JTBD] | [Đau gì?] | [Hàng ngày/tuần] |

## 3. Phạm Vi (MoSCoW)
| Must Have | Should Have | Could Have | Won't Have |
|-----------|------------|------------|------------|
| [Items] | [Items] | [Items] | [Items] |

## 4. Yêu Cầu Chức Năng
### Feature 1: [Tên]
**User Stories:**
- Là [vai trò], tôi muốn [hành động], để [outcome]

**Acceptance Criteria:**
- Given [context] When [action] Then [result]

**Priority:** Must/Should/Could

### Feature N: [Tên]
...

## 5. Yêu Cầu Phi Chức Năng (FURPS+)
| Khía cạnh | Yêu cầu | Đo bằng |
|-----------|---------|---------|
| Performance | [Response time < Xs] | [Load test] |
| Reliability | [Uptime ≥ X%] | [Monitoring] |
| Security | [Auth, encryption] | [Pentest] |

## 6. Luồng Nghiệp Vụ
[Mermaid diagram]

## 7. Ngoại Lệ & Edge Cases
[Bảng 8 nhóm — xem ba/templates/document-templates.md §6b]

## 8. Timeline & Milestones
| Phase | Scope | Duration | Dependencies |
|-------|-------|----------|-------------|

## 9. Rủi Ro
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|

## 10. Changelog
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [PO] | Initial draft |
```

---

## 1. Epic Template (POA-D5)

```markdown
## Epic: [Tên Epic]
**Objective:** [Mục tiêu business cụ thể]
**Metric gắn:** [Metric nào sẽ move nếu Epic này thành công?]
**Timeline:** [Q?/Sprint ?-?]
**Features included:** [Danh sách Feature]
```

---

## 2. User Story Template — INVEST Criteria (POA-D5)

```markdown
**Là** [type of user]
**Tôi muốn** [goal/action]
**Để** [benefit/outcome]

**Acceptance Criteria:**
Given [tiền điều kiện]
When [hành động của user]
Then [kết quả hệ thống phải làm]

And [additional AC nếu cần]

**Metric gắn:** [Feature này đóng góp vào metric nào?]
**Out of scope:** [Liệt kê rõ những gì KHÔNG làm trong story này]
```

**INVEST Check:**
- **I**ndependent: Story không phụ thuộc story khác
- **N**egotiable: Scope có thể thương lượng
- **V**aluable: Tạo giá trị cho user hoặc business
- **E**stimable: Team có thể estimate được
- **S**mall: Xong trong 1 sprint
- **T**estable: Có AC rõ ràng để test

### Story Splitting Techniques (SPIDR)
- **S**pike: Tách research/spike thành story riêng
- **P**ath: Tách theo user path (happy path trước, edge case sau)
- **I**nterface: Tách theo platform (web trước, mobile sau)
- **D**ata: Tách theo loại data (loại A trước, loại B sau)
- **R**ules: Tách theo business rule (rule đơn giản trước)

---

## 3. Job Story Template ⭐ NEW (POA-D5)

```markdown
**When** [situation/context cụ thể]
**I want to** [motivation/action]
**So I can** [expected outcome]

**Acceptance Criteria:**
Given [context đã đủ]
When [trigger event]
Then [system response]

**Context Notes:** [Tại sao situation này trigger nhu cầu?]
**Metric gắn:** [Feature này đóng góp vào metric nào?]
```

---

## 4. OKR Template (POA-D4)

```markdown
## OKR — [Team/Product] Q[N] [Year]

**Objective:** [Tham vọng, định tính, inspiring]

**Key Results:**
- KR1: [Metric] tăng từ [baseline] lên [target] vào [deadline]
  → Current: [X] | Target: [Y] | Owner: [Tên]
- KR2: [Metric] đạt [target] vào [deadline]
  → Current: [X] | Target: [Y] | Owner: [Tên]
- KR3: [Metric] giảm từ [baseline] xuống [target] vào [deadline]
  → Current: [X] | Target: [Y] | Owner: [Tên]

**Initiatives (hành động dự kiến):**
- [ ] [Feature/Project 1] → Ảnh hưởng KR[?]
- [ ] [Feature/Project 2] → Ảnh hưởng KR[?]

**Scoring cuối kỳ:** 0.0 - 1.0
(0.7 là tốt. 1.0 = goal quá dễ. 0.3 = goal quá khó hoặc execution kém)
```

---

## 5. Lean Canvas (POA-D1)

```markdown
## Lean Canvas — [Product/Feature Name]

| Problem | Solution | Unique Value Proposition |
|---------|----------|-------------------------|
| Top 3 problems: | Top 3 features: | Single clear message: |
| 1. | 1. | "Chúng tôi giúp [X] |
| 2. | 2. | đạt được [Y] |
| 3. | 3. | bằng cách [Z]" |

| Key Metrics | Unfair Advantage |
|-------------|-----------------|
| - Metric 1 | - Cái gì không thể |
| - Metric 2 | copy/buy dễ dàng? |

| Channels | Customer Segments | Cost Structure | Revenue Streams |
|----------|-------------------|----------------|-----------------|
| How to | Who specifically | Fixed costs: | Pricing model: |
| reach? | are we serving? | Variable costs: | Revenue sources: |

**Riskiest Assumption:** [Assumption cần validate TRƯỚC tiên]
```

---

## 6. Product Lifecycle Assessment (POA-D1)

```markdown
## Product Lifecycle Assessment — [Product Name]

**Current Stage:** [Introduction / Growth / Maturity / Decline]

**Evidence (data points):**
- User growth trend: [Accelerating / Stable / Decelerating / Declining]
- Revenue trend: [Same]
- Market competition: [Few / Growing / Saturated / Consolidating]
- Feature innovation pace: [High / Medium / Low]
- Churn rate trend: [Stable / Increasing]

**Strategy Recommendation:**
| Stage | Strategy | PO Actions |
|-------|----------|------------|
| Introduction | Find PMF | Experiment, interview, iterate fast, kill bad ideas |
| Growth | Scale | Feature expansion, platform play, team scaling |
| Maturity | Optimize | Retention focus, cost efficiency, adjacent innovation |
| Decline | Decide | Sunset plan, pivot assessment, reinvention investment |

**Decision:** [Continue investing / Optimize & harvest / Plan sunset / Reinvent as v2]
**Next Review Date:** [Quarterly review]
```

---

## 7. Release Plan Template (POA-D5)

```markdown
## Release Plan — [Feature/Product v.X]

**Release Date:** [DD/MM/YYYY]
**Release Type:** Big Bang / Incremental / Feature Toggle / Canary
**Target Audience:** All users / Segment [X] / Beta users

### Pre-Launch Checklist
- [ ] All stories in release: Done (DoD met)
- [ ] UAT completed and signed off
- [ ] Rollback plan documented and tested
- [ ] Monitoring & alerting configured
- [ ] Docs / Help center updated
- [ ] Stakeholders notified (release notes sent)
- [ ] Customer support team briefed
- [ ] Tracking/telemetry events verified

### Post-Launch Monitoring (Week 1)
| Metric | Baseline | Target | Actual | Status |
|--------|----------|--------|--------|--------|
| Error rate | [X%] | < [Y%] | | |
| Feature adoption | 0% | ≥ [X%] | | |
| Support tickets | [X/day] | ≤ [Y/day] | | |

### Post-Launch Review (Week 4)
| Question | Answer |
|----------|--------|
| Did we hit MCS? | |
| What surprised us? | |
| User feedback themes | |
| Decision: Keep/Enhance/Pivot/Kill | |
```

---

## 8. Product Vision Board (POA-D4)

```markdown
## Product Vision Board — [Product Name]

**VISION (3-5 năm):**
[1 câu inspiring — "We exist to [X]"]

**TARGET GROUP:** [Specific persona, not "everyone"]
**NEEDS:** [Top 3 Jobs-to-be-Done / Pain Points]
**PRODUCT:** [How we uniquely solve these needs]
**BUSINESS GOALS:** [Revenue / Market share / Strategic objectives]

**NORTH STAR METRIC:** [1 metric that captures core value]
**SUPPORTING METRICS:** [3-5 metrics that support North Star]
```

---

## 9. Strategic Roadmap (POA-D4)

```markdown
## Product Roadmap — [Product Name]

### NOW (Q[Current] — Committed)
| Theme | Key Deliverables | Success Metric | Confidence |
|-------|-----------------|----------------|------------|
| [Theme 1] | [Features] | [Metric target] | 🟢 High |

### NEXT (Q[Current+1] — Directional)
| Theme | Key Deliverables | Success Metric | Confidence |
|-------|-----------------|----------------|------------|
| [Theme 1] | [Features] | [Metric target] | 🟡 Medium |

### LATER (6+ months — Themes only)
| Theme | Opportunity | Confidence |
|-------|------------|------------|
| [Theme 1] | [Why this matters] | 🔴 Low |
```

---

## 10. A/B Test Log (POA-D6)

```markdown
## Experiment Log — [Product Name]

| # | Hypothesis | Variant A | Variant B | MCS | Duration | Result | Decision |
|---|-----------|-----------|-----------|-----|----------|--------|----------|
| 1 | [Hypothesis] | [Control] | [Treatment] | [Metric ≥ X] | [Days] | [Data] | Persist/Pivot/Kill |
```

---

## 11. Stakeholder Map & Conflict Resolution (POA-D3)

```markdown
## Stakeholder Map — [Product/Project Name]

| Stakeholder | Role | Power (H/M/L) | Interest (H/M/L) | Strategy | Comm Freq |
|-------------|------|---------------|------------------|----------|-----------|
| [Name] | Sponsor | High | Medium | Keep Satisfied | Monthly |
| [Name] | Key User | Low | High | Keep Informed | Weekly |

### Communication Plan
| Stakeholder | Channel | Frequency | Content | Owner |
|-------------|---------|-----------|---------|-------|
```

### Conflict Resolution Protocol
```
Khi 2 stakeholders muốn ngược nhau:
1. DOCUMENT both perspectives
2. DATA check: "User data/analytics support A hay B?"
3. PROPOSE compromise: "Option C giải quyết 80% cả 2 concern"
4. ESCALATE if needed: Lên PM/Sponsor với options + recommendation
5. DOCUMENT decision: "Decision: [X], by: [Name], date: [Date], trade-off accepted: [Y]"
```

### Defend Decision Template
```
"Feature [X] scored [RICE = N].
Current top priorities: [list with scores].
Position: [rank].

If we do [X] now, we trade-off [Y] — delayed by [Z sprints].
Impact: [metric A] won't improve on schedule.

Recommendation: Schedule [X] for Q[N], when [condition].
Meanwhile, [alternative W] addresses 70% of the need at lower cost."
```

---

## 12. Empathy Map Template ⭐ NEW (POA-D2)

```markdown
## Empathy Map — [Persona Name]

**Data Source:** [X interviews, Y observations, Z analytics reports]

### Think & Feel
- [What are they worried about?]
- [What matters most to them?]
- [What are their aspirations?]

### See
- [What does their environment look like?]
- [What do competitors offer them?]
- [What are their peers doing?]

### Hear
- [What do their friends/colleagues say?]
- [What does their boss tell them?]
- [What influencers affect them?]

### Say & Do
- [What do they tell others?]
- [What is their observable behavior?]
- [Any conflict between say and do?]

### Pains
- [Frustrations?]
- [Obstacles?]
- [Fears?]
- [Risks they face?]

### Gains
- [What do they want to achieve?]
- [How do they measure success?]
- [What would delight them?]

**Key Insight:** [1 sentence — the most important thing we learned]
```

---

## 13. Value Proposition Canvas Template ⭐ NEW (POA-D2)

```markdown
## Value Proposition Canvas — [Product/Feature Name]

### Customer Profile
**Customer Jobs:**
1. [Functional job: what task are they trying to complete?]
2. [Social job: how do they want to be perceived?]
3. [Emotional job: how do they want to feel?]

**Pains (ranked by severity):**
1. [Pain 1 — Severity: High] — [Evidence from interview]
2. [Pain 2 — Severity: Medium]
3. [Pain 3 — Severity: Low]

**Gains (ranked by importance):**
1. [Required gain — must have]
2. [Expected gain — standard expectation]
3. [Desired gain — would love to have]
4. [Unexpected gain — delight opportunity]

### Value Map
**Products & Services:**
- [Product/Feature we offer]

**Pain Relievers:**
- [How we address Pain 1]
- [How we address Pain 2]

**Gain Creators:**
- [How we create Gain 1]
- [How we create Gain 2]

### FIT Assessment
| Pain/Gain | Addressed? | How? | Confidence |
|-----------|:----------:|------|:----------:|
| Pain 1 | ✅/❌ | [Feature X] | High/Med/Low |
| Pain 2 | ✅/❌ | [Feature Y] | |
| Gain 1 | ✅/❌ | [Feature Z] | |

**FIT Score:** [X/Y pains addressed, X/Y gains created]
**Decision:** Strong Fit / Partial Fit / No Fit → [Action]
```

---

## 14. Product-Market Fit Assessment ⭐ NEW (POA-D2)

```markdown
## Product-Market Fit Assessment — [Product Name]

### Sean Ellis Survey Results
**Question:** "Bạn sẽ cảm thấy thế nào nếu không còn dùng sản phẩm này?"
| Response | Count | % |
|----------|:-----:|:-:|
| Rất thất vọng | | |
| Hơi thất vọng | | |
| Không thất vọng | | |
| N/A (không dùng nữa) | | |

**PMF Score:** [X%] "Rất thất vọng"
**Verdict:** ≥ 40% = PMF achieved | < 40% = Need more discovery

### Supporting Indicators
| Indicator | Current | Target | Status |
|-----------|---------|--------|--------|
| Retention curve flattening? | | | ✅/❌ |
| Organic growth > 0? | | | ✅/❌ |
| NPS > 40? | | | ✅/❌ |
| Users complain when down? | | | ✅/❌ |

**Next Steps:** [Based on PMF score]
```

---

## 15. Story Map Template ⭐ NEW (POA-D5)

```markdown
## Story Map — [Feature/Product Name]

### Backbone (User Activities & Tasks)
| Activity 1: [Name] | Activity 2: [Name] | Activity 3: [Name] |
|---|---|---|
| Task 1.1: [Name] | Task 2.1: [Name] | Task 3.1: [Name] |
| Task 1.2: [Name] | Task 2.2: [Name] | Task 3.2: [Name] |

### Release Slices
**Release 1 (Walking Skeleton / MVP):**
| Activity 1 | Activity 2 | Activity 3 |
|---|---|---|
| [Story A — minimal] | [Story D — minimal] | [Story G — minimal] |

**Release 2 (Enhancement):**
| Activity 1 | Activity 2 | Activity 3 |
|---|---|---|
| [Story B] | [Story E] | [Story H] |

**Release 3 (Full Feature):**
| Activity 1 | Activity 2 | Activity 3 |
|---|---|---|
| [Story C] | [Story F] | [Story I] |

### Validation
- [ ] Release 1 covers full user journey (thin slice)?
- [ ] User can complete primary goal with Release 1 alone?
- [ ] Stories are INVEST compliant?
```

---

## 16. Impact Map Template ⭐ NEW (POA-D4)

```markdown
## Impact Map — [Business Goal]

**WHY (Goal):** [Measurable business goal]

### Actor 1: [Persona/Role]
**HOW (Impact):** [Behavior change 1]
- **WHAT:** [Deliverable A]
- **WHAT:** [Deliverable B]

**HOW (Impact):** [Behavior change 2]
- **WHAT:** [Deliverable C]

### Actor 2: [Persona/Role]
**HOW (Impact):** [Behavior change 3]
- **WHAT:** [Deliverable D]
- **WHAT:** [Deliverable E]

### Traceability Check
| Deliverable | → Impact | → Goal | Validated? |
|------------|----------|--------|:----------:|
| [A] | [Impact 1] | [Goal] | ✅/❌ |
| [B] | [Impact 1] | [Goal] | ✅/❌ |
```

---

## 17. Business Case Template ⭐ NEW (POA-D4)

```markdown
## Business Case: [Feature Name]

**Problem:** [What problem does this solve?]
**Proposed Solution:** [High-level description]
**Requestor:** [Who asked for this?]

### Cost Estimate
| Item | Effort | Cost | Notes |
|------|--------|------|-------|
| Development | [X person-days] | | |
| Design | [X person-days] | | |
| QA | [X person-days] | | |
| Infrastructure | [Monthly] | | |
| **Total** | | **[Sum]** | |

### Expected Benefits
| Benefit | Metric | Current | Target | Timeline |
|---------|--------|---------|--------|----------|
| [Revenue increase] | MRR | $X | $Y | 3 months |
| [Cost reduction] | Support tickets | X/mo | Y/mo | 1 month |

### ROI Analysis
**ROI:** [Expected benefit / Cost] = [X]%
**Payback Period:** [X months]

### Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| [Risk 1] | [H/M/L] | [H/M/L] | [How] |

### Decision
**Decision:** ✅ Approved / ❌ Rejected / 🔄 Needs more data
**Decision Maker:** [Name]
**Date:** [DD/MM/YYYY]
```

---

## 18. Value Stream Map Template ⭐ NEW (POA-D7)

```markdown
## Value Stream Map — [Process Name]

### Current State
| Step | Process Time | Wait Time | Value-Add? | Owner |
|------|:-----------:|:---------:|:----------:|-------|
| [Step 1] | [X days] | [Y days] | ✅/❌ | [Team] |
| [Step 2] | [X days] | [Y days] | ✅/❌ | [Team] |
| [Step 3] | [X days] | [Y days] | ✅/❌ | [Team] |

**Total Process Time:** [Sum of process times]
**Total Wait Time:** [Sum of wait times]
**Total Lead Time:** [Process + Wait]
**Efficiency:** [Process Time / Lead Time] = [X%]

### Waste Identified
| Waste Type | Where | Impact | Improvement |
|-----------|-------|--------|-------------|
| Waiting | [Step X → Y] | [X days] | [How to reduce] |
| Handoff | [Step Y → Z] | [Knowledge loss] | [How to reduce] |
| Rework | [Step Z] | [X% rework rate] | [Root cause fix] |

### Future State Target
**Target Lead Time:** [X days] (current: [Y days])
**Target Efficiency:** [X%] (current: [Y%])
```

---

## 19. Collaborative Game Facilitation Card ⭐ NEW (POA-D3)

```markdown
## Collaborative Game: [Game Name]

**Purpose:** [What decision/outcome does this game help with?]
**Participants:** [Who should participate? Min/Max count]
**Duration:** [X minutes]
**Materials Needed:** [Sticky notes, virtual board, play money, etc.]

### Setup
1. [Preparation step 1]
2. [Preparation step 2]

### Rules
1. [Rule 1]
2. [Rule 2]

### Process
1. [Step 1 — X minutes]
2. [Step 2 — X minutes]
3. [Step 3 — X minutes]

### Debrief Questions
1. "What surprised you?"
2. "What patterns emerged?"
3. "How does this change our priority?"

### Output
[What artifact/decision comes out of this game?]
```

---

## 20. Learning Log Template ⭐ NEW (POA-D6)

```markdown
## Learning Log — [Product/Sprint/Release]

| # | Date | We assumed... | We tested by... | We learned... | Next action | Domain |
|---|------|--------------|-----------------|---------------|-------------|--------|
| 1 | [Date] | [Assumption] | [Experiment] | [Insight] | [Action] | D[X] |
| 2 | | | | | | |

### Quarterly Review
**Top 3 learnings this quarter:**
1. [Learning + impact on strategy]
2. [Learning + impact on strategy]
3. [Learning + impact on strategy]

**Patterns:** [Are we repeating mistakes? What themes emerge?]
```
