# Ví Dụ Thực Tế: Product Ownership Analysis — SaaS B2B

> Ngữ cảnh: SaaS B2B Platform (CRM / Project Management / HR Tech)
> Tổ chức theo 7 POA Domains — mỗi domain ít nhất 1 ví dụ
> **Nguồn:** IIBA Guide to Product Ownership Analysis

---

## Ví dụ 1: Organizational Readiness (POA-D1)

**Bối cảnh:** Startup SaaS CRM chuyển từ project-based sang product-based approach.

```markdown
## Organizational Readiness — TechCRM Inc.

| Dimension | Level (1-5) | Evidence | Gap |
|-----------|:-----------:|----------|-----|
| Culture | 2 | Team chờ chỉ đạo, chưa có fail-fast mindset | Training cần |
| Structure | 3 | Cross-functional teams nhưng còn silo | Cần Dual-Track |
| Skills | 2 | Không có BA/PO chuyên nghiệp | Hire hoặc upskill |
| Processes | 4 | Scrum đã adopt, sprint 2 tuần | OK |
| Leadership | 3 | CEO ủng hộ nhưng CTO skeptical | Cần alignment |
| Data | 2 | Analytics chưa setup, decisions = gut feeling | Setup Mixpanel |

**Average Score:** 2.7/5 — Partially Ready
**Top Priority:** Setup analytics (Data) → upskill PO (Skills)
```

---

## Ví dụ 2: Empathy Map + Value Proposition Canvas (POA-D2)

**Bối cảnh:** SaaS Project Management tool đang build "Resource Planning" feature.

```markdown
## Empathy Map — Sarah, Project Manager (Mid-size Agency)

**Data Source:** 8 interviews, 15 survey responses, 3 session recordings

### Think & Feel
- "Tôi sợ promise deadline rồi không đủ người làm"
- "Mỗi sáng thứ Hai tôi dành 2 tiếng check ai rảnh tuần này"
- "Tôi muốn được tin tưởng là PM giỏi, không phải PM hay miss deadline"

### See
- Đồng nghiệp dùng Excel để track resource → ai cũng khác format
- Competitor (Monday.com) có resource view nhưng quá phức tạp
- Client complain về delivery delay

### Hear
- Boss: "Tại sao project X delay? Tôi tưởng chúng ta có đủ người?"
- Team: "Tôi đang bị assign 3 projects cùng lúc, không đủ thời gian"

### Say & Do
- Nói: "Resource planning tool sẽ rất hữu ích"
- Làm: Vẫn dùng Excel vì "tool mới learning curve cao"
- ⚠️ Conflict: nói muốn tool mới nhưng resist change

### Pains
1. Mất 2-3 giờ/tuần check resource availability thủ công
2. Over-allocation: assign người đã full → burnout + chất lượng giảm
3. Không thấy conflict cho đến khi quá muộn

### Gains
1. Thấy ai rảnh, ai full trong 1 dashboard (required)
2. Alert tự động khi over-allocate (expected)
3. Forecast resource needs cho 3 tháng tới (desired)

**Key Insight:** "Sarah không cần tool phức tạp — cần 1 view đơn giản cho thứ Hai sáng."
```

```markdown
## Value Proposition Canvas — Resource Planning Feature

### Customer Profile
**Customer Jobs:**
1. [Functional] Assign đúng người cho đúng project đúng thời điểm
2. [Social] Được team trust là PM phân bổ công bằng
3. [Emotional] Giảm stress về deadline miss

**Top Pains:** Over-allocation (Severity: High) | Manual tracking (Severity: High)
**Top Gains:** Single dashboard view (Required) | Auto-alert (Expected)

### Value Map
**Pain Relievers:**
- Real-time utilization bar per team member → instantly see over-allocation
- Conflict detection: alert khi assign > 100% capacity

**Gain Creators:**
- Weekly resource dashboard (the "Monday Morning View")
- 3-month forecast based on planned project timelines

### FIT Assessment
| Pain/Gain | Addressed? | How? | Confidence |
|-----------|:----------:|------|:----------:|
| Over-allocation | ✅ | Utilization bar + alert | High |
| Manual tracking | ✅ | Auto-sync from project | High |
| Dashboard view | ✅ | Monday Morning View | High |
| 3-month forecast | 🟡 | Needs more data | Medium |

**FIT Score:** 3/4 addressed with high confidence
**Decision:** Strong Fit → Proceed to MVP
```

---

## Ví dụ 3: Collaborative Game — Buy a Feature (POA-D3)

**Bối cảnh:** SaaS HR platform có 8 feature requests, team cần prioritize cho Q3.

```markdown
## Buy a Feature — Q3 Planning Workshop

**Participants:** 2 PMs, 3 HR Directors (customers), 1 Dev Lead, 1 Designer
**Budget per person:** 100 points (total pool: 700 points)
**Feature prices set by effort:**

| Feature | Price | Points Received | Buyers | Rank |
|---------|:-----:|:---------------:|:------:|:----:|
| Performance Review Templates | 80 | 320 | 5/7 | ⭐ 1 |
| Payroll Integration | 120 | 280 | 4/7 | 2 |
| Employee Self-Service Portal | 60 | 210 | 4/7 | 3 |
| Advanced Reporting | 100 | 180 | 3/7 | 4 |
| AI Resume Screening | 150 | 150 | 2/7 | 5 |
| Mobile App | 90 | 90 | 2/7 | 6 |
| Dark Mode | 30 | 40 | 2/7 | 7 |
| Slack Integration | 40 | 30 | 1/7 | 8 |

**Key Insight:**
- Performance Review Templates (#1) surprised us — 5/7 people pooled budget cho feature này
- AI Resume Screening (#5) — chỉ 2 people invest, dù team expected nó sẽ #1
- Mobile App — HR Directors nói "Nice to have nhưng desktop là primary"

**Decision:** Q3 = Performance Review Templates + Employee Self-Service Portal
```

---

## Ví dụ 4: Impact Map + Business Case (POA-D4)

**Bối cảnh:** SaaS CRM cần justify "AI Email Drafting" feature.

```markdown
## Impact Map — Increase Sales Conversion Rate

WHY: "Tăng conversion rate từ 12% lên 18% trong Q3"

### Actor 1: Sales Rep
HOW: Respond to leads faster (< 30 min instead of 4 hours)
- WHAT: AI Email Draft suggestion
- WHAT: One-click send from CRM

HOW: Personalize outreach at scale
- WHAT: AI template with dynamic fields from lead profile
- WHAT: A/B test subject lines

### Actor 2: Sales Manager
HOW: Identify underperforming reps
- WHAT: Response time dashboard
- WHAT: Email open rate tracking per rep

### Traceability
| Deliverable | → Impact | → Goal | Validated? |
|------------|----------|--------|:----------:|
| AI Email Draft | Faster response | +6% conversion | ✅ (interview) |
| One-click send | Faster response | +6% conversion | ✅ (time study) |
| A/B subject lines | Better personalization | +6% conversion | 🟡 (hypothesis) |
```

```markdown
## Business Case: AI Email Drafting

**Problem:** Sales reps spend 45 min/day drafting emails → slow response → lost deals
**Proposed Solution:** AI draft email from lead context + CRM data

### Cost Estimate
| Item | Effort | Notes |
|------|--------|-------|
| Development | 20 person-days | Backend AI + Frontend UI |
| Design | 5 person-days | Email composer UX |
| QA | 5 person-days | |
| OpenAI API | $500/month | GPT-4 API costs |
| **Total** | **30 person-days + $500/mo** | |

### Expected Benefits
| Benefit | Metric | Current | Target | Timeline |
|---------|--------|---------|--------|----------|
| Revenue increase | Conversion rate | 12% | 18% | 3 months |
| Time saved | Draft time/day | 45 min | 10 min | 1 month |

### ROI
Cost: ~$30,000 (dev) + $6,000/year (API)
Benefit: +6% conversion × $50K avg deal × 100 deals/quarter = $300K/quarter
**ROI: 833%** | **Payback: < 1 month**

**Decision:** ✅ Approved — Sprint 1-2 Q3
```

---

## Ví dụ 5: Story Map + Job Stories (POA-D5)

**Bối cảnh:** SaaS Project Management tool — "Client Portal" feature.

```markdown
## Story Map — Client Portal

### Backbone
| Activity 1: View Project | Activity 2: Give Feedback | Activity 3: Approve Deliverable |
|---|---|---|
| Task: Login to portal | Task: Comment on task | Task: Review milestone |
| Task: See project status | Task: Upload reference | Task: Sign-off deliverable |
| Task: View timeline | Task: Tag team member | Task: Download invoice |

### Release 1 (Walking Skeleton)
| View Project | Give Feedback | Approve |
|---|---|---|
| Login (email magic link) | Comment on task (text only) | Review milestone (view only) |
| Project status (3 states) | | Simple approve/reject button |

### Release 2
| View Project | Give Feedback | Approve |
|---|---|---|
| Timeline view (Gantt) | Upload files | Digital signature |
| | Tag team member | Download invoice |

### Release 3
| View Project | Give Feedback | Approve |
|---|---|---|
| Real-time notifications | Video comments | Batch approve |
| Multi-project dashboard | | Payment integration |
```

```markdown
## Job Stories — Client Portal

**Job Story 1:**
When I receive an email that a project milestone is ready for review,
I want to click one link and see the deliverable immediately,
so I can approve it without needing to create an account or learn a new tool.

**AC:**
Given client receives milestone notification email
When client clicks "Review" link
Then client lands directly on deliverable page (no login required first time, magic link)
And client sees deliverable + approve/reject buttons within 3 seconds

**Job Story 2:**
When I'm reviewing a design mockup from my agency and spot an issue,
I want to leave a comment directly on the specific area of the design,
so the designer knows exactly what I'm referring to without a separate email thread.

**AC:**
Given client is viewing a design deliverable
When client clicks on specific area of the image
Then a comment box appears anchored to that location
And designer receives notification with pinpoint location
```

---

## Ví dụ 6: Real Options + Learning Loop (POA-D6)

**Bối cảnh:** SaaS CRM đang chọn AI provider cho email drafting feature.

```markdown
## Real Options — AI Provider Decision

| Decision | Options | Last Responsible Moment | Data Needed | Current Lean |
|----------|---------|------------------------|-------------|-------------|
| AI Provider | OpenAI GPT-4, Anthropic Claude, Self-hosted Llama | Sprint 2 start (2 weeks) | Latency test, cost/1K requests, quality score | OpenAI (familiar) |

**Option Analysis:**
| Criteria | OpenAI GPT-4 | Claude | Self-hosted Llama |
|----------|:---:|:---:|:---:|
| Quality | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Cost/1K req | $0.06 | $0.08 | $0.01 (infra only) |
| Latency (p95) | 1.2s | 1.5s | 0.8s |
| Vendor lock-in | High | Medium | None |
| Setup effort | 1 day | 1 day | 5 days |

**Decision:** Start with OpenAI (fastest), abstract with adapter pattern → switch later if needed.
**Real Option kept:** Adapter interface allows swapping provider in < 1 day.
```

```markdown
## Learning Log — AI Email Feature (Sprint 1-3)

| # | Date | We assumed... | We tested by... | We learned... | Next action |
|---|------|--------------|-----------------|---------------|-------------|
| 1 | W1 | Reps want full email draft | Concierge MVP (manual AI draft) | 7/10 reps edited < 20% → draft quality OK | Proceed to auto-generate |
| 2 | W2 | Subject line matters most | A/B test: AI subject vs manual | AI subject: +23% open rate | Double down on AI subject lines |
| 3 | W4 | All reps will adopt | Tracked adoption D7 | Only 45% adopted (target 60%) | Interview non-adopters → found: onboarding gap |
| 4 | W5 | Onboarding video enough | Added interactive tutorial | Adoption jumped to 68% | Keep tutorial, remove video |
```

---

## Ví dụ 7: Value Stream Map + RICE Scoring (POA-D7)

**Bối cảnh:** SaaS platform muốn optimize feature delivery pipeline.

```markdown
## Value Stream Map — Feature Delivery Pipeline

### Current State
| Step | Process Time | Wait Time | Value-Add? | Owner |
|------|:-----------:|:---------:|:----------:|-------|
| Discovery & Research | 3 days | 2 days (wait for interview slots) | ✅ | PO |
| Write PRD | 2 days | 3 days (wait for PO availability) | ✅ | PO |
| Design | 3 days | 1 day | ✅ | Designer |
| Dev Review PRD | 0.5 day | 2 days (wait for sprint slot) | ✅ | Dev |
| Development | 8 days | 0 days | ✅ | Dev |
| Code Review | 0.5 day | 1.5 days (wait for reviewer) | ✅ | Dev |
| QA | 2 days | 1 day (wait for deploy to staging) | ✅ | QA |
| Deploy | 0.5 day | 0 days | ✅ | DevOps |

**Process Time:** 19.5 days
**Wait Time:** 10.5 days
**Lead Time:** 30 days
**Efficiency:** 65%

### Waste Identified
| Waste | Where | Impact | Fix |
|-------|-------|--------|-----|
| Waiting | PRD → Design (3 days) | Longest wait | Dual-track: overlap discovery+design |
| Waiting | Code Review (1.5 days) | Blocks deploy | Same-day review policy |
| Waiting | Sprint slot (2 days) | Delays start | Kanban pull instead of sprint push |

### Future State Target
- Lead Time: 30 → 21 days (-30%)
- Efficiency: 65% → 80%
```

```markdown
## RICE Scoring — Q3 Backlog

| Item | Reach/quý | Impact | Conf. | Effort (PM) | RICE | Rank |
|------|-----------|--------|-------|-------------|------|------|
| AI Email Draft | 500 reps | 3 | 80% | 2 | **600** | 1 |
| Client Portal | 200 clients | 2 | 70% | 3 | **93** | 2 |
| Advanced Reports | 50 managers | 2 | 90% | 1 | **90** | 3 |
| API v2 | 30 devs | 1 | 100% | 2 | **15** | 4 |
| Mobile App | 100 reps | 0.5 | 50% | 5 | **5** | Last |

**Decision:**
- Sprint 1-2: AI Email Draft (RICE 600)
- Sprint 3-4: Client Portal MVP (RICE 93)
- Q4: Advanced Reports (RICE 90) — can wait, stable demand
- Kill: Mobile App (RICE 5 — ROI too low)
```
