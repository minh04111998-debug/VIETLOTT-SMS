# POA Frameworks & Techniques Reference

> **Cấu trúc:** Theo 7 Domains của IIBA POA Framework
> **Tham chiếu từ:** `.agents/skills/po/SKILL.md` — Tất cả POA-D1 ~ POA-D7
> **Nguồn:** [IIBA Guide to Product Ownership Analysis](https://www.iiba.org/business-analysis-certifications/product-ownership-analysis/)

---

## Domain 1: Apply Foundational Concepts (10%)

### D1.1: PO Type Assessment

```markdown
## PO Type Assessment — [Product/Project Name]

**Product Stage hiện tại:**
- [ ] Pre-PMF (chưa có Product-Market Fit) → Discovery PO
- [ ] Post-PMF, đang scale → Delivery PO
- [ ] Growth/Mature, tối ưu → Growth PO

**Context:**
- [ ] Product-based (continuous) vs Project-based (fixed scope)
- [ ] Internal product vs External/Customer-facing
- [ ] Greenfield (mới) vs Brownfield (legacy)

**PO Hat cần đội chính:** [Discovery / Delivery / Growth]
```

### D1.2: Product vs Project Check
```
1. "Dự án có end date cố định không?" → Yes = Project
2. "Budget cố định hay flexible?" → Fixed = Project, Flexible = Product
3. "Scope đã chốt hay còn thay đổi?" → Fixed = Project, Evolving = Product
4. "Ai own requirement?" → Client = Project, PO = Product
5. "Success đo bằng gì?" → Deliverables = Project, Outcomes = Product

⚠️ Nếu Project context: PO vẫn inject product thinking bằng cách
   validate assumptions, đề xuất scope negotiation, track outcome metrics.
```

### D1.3: Organizational Readiness Assessment ⭐ NEW

```markdown
## Organizational Readiness — [Organization Name]

| Dimension | Level (1-5) | Evidence | Gap |
|-----------|:-----------:|----------|-----|
| **Culture** — Fail-fast mindset? | | | |
| **Structure** — Cross-functional teams? | | | |
| **Skills** — BA/PO analysis capability? | | | |
| **Processes** — Agile/Lean adopted? | | | |
| **Leadership** — Executive sponsor? | | | |
| **Data** — Data-driven decisions? | | | |

**Average Score:** [X/5]
**Readiness Level:**
- 1-2: Not Ready — Need foundational transformation
- 3: Partially Ready — Specific gaps to address
- 4-5: Ready — Can adopt POA practices

**Transformation Actions:**
1. [Action for lowest-scoring dimension]
2. [Action for second lowest]
```

> **Nguồn:** [IIBA Guide to POA, Chapter 2](https://www.iiba.org/) — Evolving Product Ownership to POA

### D1.4: Product Lifecycle Stages

```
Introduction → Growth → Maturity → Decline

Introduction: Discovery PO → Validate problem, find PMF, iterate fast
Growth:       Delivery + Growth PO → Scale features, optimize funnel
Maturity:     Growth PO → Retention, efficiency, defend position
Decline:      Discovery PO (reinvent) → Sunset or pivot

Lean Build-Measure-Learn Loop:
1. BUILD: Smallest thing to test hypothesis
2. MEASURE: Collect data against pre-defined MCS
3. LEARN: Decide Persist / Pivot / Kill
```

---

## Domain 2: Cultivate Customer Intimacy (15%)

### D2.1: Market Intelligence & Competitive Analysis

#### Bước 1: Market Sizing
```
TAM (Total Addressable Market): Toàn bộ thị trường nếu we take 100%
SAM (Serviceable Addressable Market): Phần chúng ta có thể reach được
SOM (Serviceable Obtainable Market): Phần thực tế chúng ta có thể chiếm trong 1-2 năm

→ Câu hỏi: Thị trường này có đủ lớn để justify effort không?
→ Blue Ocean (ít cạnh tranh) hay Red Ocean (cạnh tranh khốc liệt)?
```

#### Bước 2: Competitive Mapping
```
Đối thủ trực tiếp: Cùng giải pháp, cùng khách hàng mục tiêu
Đối thủ gián tiếp: Giải pháp khác nhưng cùng giải vấn đề
Đối thủ thay thế: Không phải phần mềm (Excel, quy trình tay, không làm gì)
Potential disruptors: Ai có thể vào thị trường trong 12-24 tháng?

Theo dõi đúng cách:
- App Store reviews của đối thủ → Pain points của user hiện tại
- G2/Capterra/Trustpilot reviews → Strength & Weakness thực tế
- Job postings của đối thủ → Họ đang invest vào đâu?
- Changelog/Release notes → Họ đang ưu tiên gì?
```

#### Bước 3: Feature Parity vs Differentiation
```markdown
| Feature | Chúng ta | Đối thủ A | Đối thủ B | Đối thủ C |
|---------|---------|----------|----------|----------|
| [Feature 1] | ✅ | ✅ | ❌ | ✅ |
| [Feature 2] | ❌ | ✅ | ✅ | ❌ |

⚠️ Ghi chú:
- ✅ Có  |  ❌ Không  |  🔄 Đang làm  |  ⭐ Tốt hơn  |  💩 Kém hơn
- Đối thủ có feature X VÀ users đang chê → cơ hội làm tốt hơn
- Đối thủ có feature X VÀ users hài lòng → cần unfair advantage để cạnh tranh
```

#### Bước 4: Go/No-Go Decision
```markdown
## Kết Luận Market Analysis: [Tên Feature/Product]

**Unfair Advantage của chúng ta:** [Cụ thể, không phải "chúng ta làm tốt hơn"]
**White Space (Cơ hội chưa ai khai thác tốt):** [Pain point cụ thể]

**Rủi ro nếu vào:**
1. [Rủi ro chính] → Giảm thiểu bằng [cách gì]

**Quyết định:** ✅ GO / ❌ NO-GO / 🔄 PIVOT sang [hướng nào]
**Lý do:** [Cụ thể, data-backed]
**Điều kiện thành công (Measurable):** [Metric X đạt Y trong Z ngày]
```

### D2.2: User Journey & Customer Development

#### 3 Loại Journey
```
1. Goal-based Journey: Người dùng muốn đạt GÌ?
2. Pain Point & Friction Map: Đau ở đâu? Emotion curve: Vui/Bực ở từng bước
3. Moment of Truth: Điểm nếu tốt → trung thành, nếu xấu → churn

⚠️ Journey = Trải nghiệm cảm xúc theo thời gian (ngày/tuần/tháng)
   Flow = Luồng màn hình trong app (minutes)
```

#### Customer Development Interview
```
❌ SAI: "Bạn có thích tính năng X không?" → Leading question
❌ SAI: "Nếu có tính năng Y, bạn có dùng không?" → Hypothetical
✅ ĐÚNG: "Lần cuối bạn gặp vấn đề [X] là khi nào? Kể tôi nghe câu chuyện đó?"
✅ ĐÚNG: "Hiện tại bạn giải quyết vấn đề này như thế nào?"
✅ ĐÚNG: "Điều gì khó chịu nhất trong cách bạn đang làm hiện tại?"
✅ ĐÚNG: "Bạn đã thử những gì? Kết quả ra sao?"
✅ ĐÚNG: "Nếu vấn đề này biến mất ngày mai, cuộc sống bạn thay đổi thế nào?"
```

#### Phân tích Insight
```
Frequency: Vấn đề xảy ra bao thường xuyên?
Severity: User đau đớn đến mức nào? Có trả tiền để giải không?
Current Solution: Đang giải bằng cách gì? (indirect competitor)
Willingness to Switch: Điều gì khiến họ chuyển sang giải pháp mới?
```

#### Problem Statement Output
```markdown
## Problem Statement: [Tên]

**Persona:** [Tên persona] — [mô tả ngắn, từ data thật]
**Job-to-be-Done:** Khi [situation], tôi muốn [motivation], để [expected outcome]
**Pain Points (Đã validate với ≥5 users):**
1. [Pain 1] — Frequency: [Hàng ngày/tuần/tháng] | Severity: [Low/Med/High]
**Current Solutions:** [Họ đang giải như thế nào?]
**Hypothesis:** Chúng ta tin rằng [solution] sẽ giúp [persona] [outcome]
vì [lý do cụ thể từ interview]
```

### D2.3: Empathy Map ⭐ NEW

```
┌─────────────────────────────────────────────────┐
│                    [Persona Name]                │
├────────────────────┬────────────────────────────┤
│   THINK & FEEL     │         SEE                │
│ Điều gì quan trọng?│ Môi trường xung quanh?     │
│ Lo lắng gì?        │ Đối thủ cung cấp gì?      │
│ Mơ ước gì?         │ Đồng nghiệp làm gì?       │
├────────────────────┼────────────────────────────┤
│   HEAR             │       SAY & DO             │
│ Bạn bè nói gì?    │ Thái độ với người khác?     │
│ Boss nói gì?       │ Hành vi observable?         │
│ Influencers?       │ Có mâu thuẫn say vs do?    │
├────────────────────┴────────────────────────────┤
│ PAINS                  │ GAINS                   │
│ Nỗi sợ? Rào cản?      │ Muốn đạt gì? Đo bằng   │
│ Frustrations?          │ gì là thành công?       │
└────────────────────────┴─────────────────────────┘

Quy trình tạo Empathy Map:
1. Chọn 1 persona cụ thể (từ interview data, không tưởng tượng)
2. Điền 4 quadrants dựa trên quotes từ interviews
3. Tổng hợp Pains & Gains → input cho Value Proposition Canvas
4. Review với team → shared understanding

⚠️ Empathy Map ≠ Persona. Persona = ai họ là. Empathy Map = họ trải nghiệm gì.
```

> **Nguồn:** [Gamestorming — Dave Gray](https://gamestorming.com/empathy-mapping/), [IIBA Guide to POA, Chapter 6](https://www.iiba.org/)

### D2.4: Value Proposition Canvas ⭐ NEW

```
┌─────────────────────────┐    ┌─────────────────────────┐
│    CUSTOMER PROFILE      │    │      VALUE MAP           │
│                          │    │                          │
│  ┌──────────────────┐   │    │   ┌──────────────────┐  │
│  │ Customer Jobs     │   │    │   │ Products/Services │  │
│  │ - Functional jobs │   │←──→│   │ - Features        │  │
│  │ - Social jobs     │   │    │   │ - Services        │  │
│  │ - Emotional jobs  │   │    │   │ - Digital/Physical│  │
│  └──────────────────┘   │    │   └──────────────────┘  │
│                          │    │                          │
│  ┌──────────────────┐   │    │   ┌──────────────────┐  │
│  │ Pains             │   │←──→│   │ Pain Relievers    │  │
│  │ - Undesired costs │   │    │   │ - How we reduce   │  │
│  │ - Negative emotions│  │    │   │   customer pains  │  │
│  │ - Risks           │   │    │   │                    │  │
│  └──────────────────┘   │    │   └──────────────────┘  │
│                          │    │                          │
│  ┌──────────────────┐   │    │   ┌──────────────────┐  │
│  │ Gains             │   │←──→│   │ Gain Creators     │  │
│  │ - Required gains  │   │    │   │ - How we create   │  │
│  │ - Expected gains  │   │    │   │   customer gains  │  │
│  │ - Desired gains   │   │    │   │                    │  │
│  └──────────────────┘   │    │   └──────────────────┘  │
└─────────────────────────┘    └─────────────────────────┘

FIT = Pain Relievers address top Pains
    + Gain Creators address top Gains
    = Product-Market Fit signal

Quy trình:
1. Bắt đầu với Customer Profile (PHẢI dùng data từ interview, không guess)
2. Rank Jobs, Pains, Gains theo importance
3. Map Value Map: product/service nào address top items?
4. Check FIT: có gap nào không?
5. Iterate: nếu gap lớn → pivot hoặc add feature
```

> **Nguồn:** [Value Proposition Design — Alexander Osterwalder](https://www.strategyzer.com/books/value-proposition-design), [IIBA Guide to POA, Chapter 6](https://www.iiba.org/)

### D2.5: Product-Market Fit ⭐ NEW

```
Sean Ellis PMF Test:
"Bạn sẽ cảm thấy thế nào nếu không còn được dùng sản phẩm này nữa?"
- Rất thất vọng
- Hơi thất vọng
- Không thất vọng (nó không thực sự hữu ích)
- N/A — Tôi không còn dùng nữa

Ngưỡng PMF: ≥ 40% trả lời "Rất thất vọng" = ĐÃ ĐẠT PMF

Pre-PMF Indicators (trước khi có đủ survey data):
- Retention curve flattens (không rơi về 0)
- Organic growth > 0 (word of mouth)
- Users complain when feature is down
- NPS > 40
- Willingness to pay demonstrated

Post-PMF Actions:
- PMF < 40%: Quay lại Discovery, interview churned users
- PMF 40-60%: Đang tốt, focus retention + activation
- PMF > 60%: Strong fit, focus Growth + Scale
```

> **Nguồn:** [The Startup Pyramid — Sean Ellis](https://www.startup-marketing.com/the-startup-pyramid/), [IIBA Guide to POA, Chapter 6](https://www.iiba.org/)

### D2.6: Human-Centred Design ⭐ NEW

```
5 Phases (PO vai trò từng phase):

1. EMPATHIZE → PO lead
   Input: Customer interviews, observations, data
   Tool: Empathy Maps, Customer Journey Maps
   PO: Tổng hợp insight, identify patterns

2. DEFINE → PO lead
   Input: Empathy insights
   Tool: Problem Statement, Point of View (POV)
   PO: Frame the problem correctly
   POV format: "[User] needs [need] because [insight]"

3. IDEATE → PO participate, Designer lead
   Tool: Brainstorming, How Might We, Crazy 8s
   PO: Evaluate ideas against business goals & constraints

4. PROTOTYPE → Designer lead, PO review
   Tool: Paper prototypes, Figma, clickable mockups
   PO: Verify prototype addresses defined problem

5. TEST → PO + Designer co-lead
   Tool: Usability testing, A/B testing
   PO: Interpret results, decide iterate/pivot/proceed
```

> **Nguồn:** [IDEO Design Thinking](https://designthinking.ideo.com/), [IIBA Guide to POA, Chapter 6](https://www.iiba.org/)

### D2.7: Focus Groups ⭐ NEW

```
Khi nào dùng Focus Groups vs 1-1 Interview:

| Aspect | Focus Group | 1-1 Interview |
|--------|------------|----------------|
| Participants | 6-10 people | 1 person |
| Duration | 60-90 min | 30-45 min |
| Best for | Concept reactions, feature voting | Deep stories, sensitive topics |
| Risk | Groupthink, dominant voices | Interviewer bias |
| Output | Patterns, priorities, reactions | Rich narratives, edge cases |

Facilitation Rules:
1. Mix participants: power users + new users + churned users
2. Start with individual writing → then group discussion (avoid anchoring)
3. Record (with consent) — PO facilitates, not dominates
4. Use structured exercises: dot voting, card sorting, Buy a Feature
5. Debrief immediately: What surprised us? What confirmed assumptions?
```

---

## Domain 3: Engage the Whole Team (15%)

### D3.1: Stakeholder Management

#### Power × Interest Matrix
```
             High Power
                │
 KEEP SATISFIED │ MANAGE CLOSELY
 (Regular 1:1)  │ (Co-create, involve)
────────────────┼────────────────────
 MONITOR        │ KEEP INFORMED
 (Minimal)      │ (Newsletter, demos)
                │
             Low Power
   Low Interest ←──→ High Interest
```

#### Conflict Resolution Protocol
```
Khi 2 stakeholders muốn ngược nhau:
1. DOCUMENT both perspectives
2. DATA check: "User data/analytics support A hay B?"
3. PROPOSE compromise: "Option C giải quyết 80% cả 2 concern"
4. ESCALATE if needed: Lên PM/Sponsor với options + recommendation
5. DOCUMENT decision: "Decision: [X], by: [Name], date: [Date], trade-off accepted: [Y]"
```

#### Nói NO Đúng Cách
```
KHÔNG: "Không được, team đang bận"
ĐÚNG:  "Feature X có RICE score = 12. So với 4 item đang prioritize (score 24-45),
        nó sẽ phải chờ đến Q[N]. Đề xuất review lại khi [điều kiện].
        Trong thời gian đó, [alternative Y] giải được 70% nhu cầu với effort thấp hơn."
```

### D3.2: Cross-functional Collaboration ⭐ NEW

```
Pattern 1: Dual-Track Agile
┌──────────────────────────────────────┐
│ DISCOVERY TRACK          DELIVERY TRACK │
│ (PO + Designer + BA)    (Dev + QA)      │
│                                         │
│ Research → Ideate →     Backlog → Build │
│ Prototype → Test        → Test → Ship   │
│         ↓                    ↑          │
│    Validated ideas ──────────┘          │
└──────────────────────────────────────┘

→ Discovery always 1-2 sprints ahead of Delivery
→ Output của Discovery = input cho Delivery backlog

Pattern 2: Three Amigos
Before sprint:
PO (WHAT & WHY) + Dev (HOW) + QA (WHAT IF) → Review mỗi story
Output: Shared understanding, refined AC, identified risks

Pattern 3: Product Trio (Teresa Torres)
PO + Designer + Tech Lead = weekly customer interview + OST update
→ Continuous Discovery, không phải 1 lần

Anti-patterns:
❌ PO writes stories alone → Dev confused → rework
❌ PO decides architecture → SA/Dev frustrated → wrong tech
❌ PO skips QA → "Works on my machine" → production bugs
❌ Dev never meets users → builds what PO says, not what user needs
```

> **Nguồn:** [Dual Track Agile — Jeff Patton](https://www.jpattonassociates.com/dual-track-development/), [Continuous Discovery Habits — Teresa Torres](https://www.producttalk.org/)

### D3.3: Collaborative Games ⭐ NEW

```
┌────────────────────────────────────────────────────┐
│ Game              │ Purpose          │ Duration │ When │
├───────────────────┼──────────────────┼──────────┼──────┤
│ Buy a Feature     │ Priority voting  │ 30-60m   │ Backlog refinement │
│ Speedboat         │ Identify blockers│ 30m      │ Retro/Discovery │
│ Product Box       │ Find core value  │ 45m      │ Vision workshop │
│ Prune the Tree    │ Categorize       │ 30m      │ Roadmap planning │
│ Dot Voting        │ Quick consensus  │ 10m      │ Any meeting │
│ How Might We      │ Reframe problems │ 20m      │ Ideation │
│ Crazy 8s          │ Rapid ideation   │ 8 min    │ Design sprint │
│ 20/20 Vision      │ Force rank       │ 20m      │ Priority conflicts │
└───────────────────┴──────────────────┴──────────┴──────┘

Buy a Feature — Chi tiết:
1. List 10-15 features với "price" (effort points)
2. Give each participant budget = 30% of total price
3. Rule: "Bạn phải pool budget với người khác để mua feature đắt"
4. Observe: feature nào nhiều người góp tiền nhất? → True priority
5. Debrief: "Tại sao bạn chọn feature X mà không chọn Y?"
```

> **Nguồn:** [Innovation Games — Luke Hohmann](https://www.innovationgames.com/), [IIBA Guide to POA, Chapter 6](https://www.iiba.org/)

### D3.4: Shared PO Responsibilities ⭐ NEW

```
Solo PO (Small team, 1 product):
→ PO own everything: discovery, backlog, stakeholder, release

Multiple POs (Large product, multiple teams):
Chief PO → Product vision, portfolio priority, cross-team alignment
  ├── Feature PO A → Own feature area A (Discovery + Backlog)
  ├── Feature PO B → Own feature area B
  └── Feature PO C → Own feature area C

Rules:
- 1 Backlog = 1 PO accountable (không shared ownership)
- Analysis work CAN be shared (BA, Designer help with research)
- Decision authority CANNOT be shared (1 person decides)
- Chief PO resolves conflicts between Feature POs

Anti-pattern: "PO Committee" — 3 POs vote on every story → deadlock
```

---

## Domain 4: Make an Impact (15%)

### D4.1: Product Vision & Strategy

→ Templates tại `.agents/skills/po/templates/product-templates.md` (Vision Board, Strategic Roadmap)

### D4.2: Product Metrics & OKR

#### Output vs Outcome
```
Output (Vanity):  "Đã ship 5 tính năng, 3 sprint liên tiếp on-time"
Outcome (Value):  "D30 retention tăng 12%, AHT giảm 45 giây, Revenue +15%"
```

#### North Star Metric
```
Câu hỏi: "Khi người dùng 'thành công', điều gì xảy ra?" → Đó là North Star Metric

Ví dụ:
- Spotify: "Time spent listening"
- Airbnb: "Nights booked"
- Slack: "Messages sent within teams"
- SaaS CRM: "Deals closed using the platform"
```

#### Pirate Metrics — AARRR Framework
```
A - Acquisition:   User đến từ đâu? (Channel, CAC)
A - Activation:    Có trải nghiệm "AHA moment" không? (Onboarding completion)
R - Retention:     Có quay lại không? (D1/D7/D30 retention, Churn rate)
R - Referral:      Có giới thiệu người khác không? (NPS, Viral coefficient)
R - Revenue:       Có trả tiền không? (Conversion rate, LTV, MRR/ARR)
```

#### HEART Framework (Google)
```
H - Happiness:    CSAT, NPS, App Store rating
E - Engagement:   DAU/MAU, Sessions/user, Feature usage frequency
A - Adoption:     % user dùng feature mới trong 30 ngày
R - Retention:    D30/D90 retention, Churn
T - Task Success: Completion rate, Time-on-task, Error rate
```

### D4.3: Impact Mapping ⭐ NEW

```
Impact Mapping (Gojko Adzic):

WHY? ─── Business Goal (measurable)
 │
 ├── WHO? ─── Actor 1 (persona)
 │    ├── HOW? ─── Impact 1 (behavior change)
 │    │    ├── WHAT? ─── Deliverable A
 │    │    └── WHAT? ─── Deliverable B
 │    └── HOW? ─── Impact 2
 │         └── WHAT? ─── Deliverable C
 │
 └── WHO? ─── Actor 2
      └── HOW? ─── Impact 3
           └── WHAT? ─── Deliverable D

Ví dụ SaaS B2B:
WHY: "Tăng MRR 20% trong Q3"
├── WHO: Sales Manager
│    ├── HOW: Shorten deal cycle time
│    │    ├── WHAT: Auto-generate proposals
│    │    └── WHAT: Pipeline dashboard
│    └── HOW: Increase win rate
│         └── WHAT: Competitor comparison tool
└── WHO: Customer
     └── HOW: Self-serve onboarding
          └── WHAT: Interactive product tour

Quy tắc:
- Mỗi deliverable PHẢI trace được về business goal
- Nếu không trace được → Kill hoặc deprioritize
- Review Impact Map hàng quý → prune dead branches
```

> **Nguồn:** [Impact Mapping — Gojko Adzic](https://www.impactmapping.org/), [IIBA Guide to POA](https://www.iiba.org/)

### D4.4: Business Case (per feature) ⭐ NEW

```markdown
## Business Case: [Feature Name]

**Problem:** [What problem does this solve?]
**Proposed Solution:** [High-level description]

**Cost Estimate:**
| Item | Cost | Notes |
|------|------|-------|
| Development | [X person-days] | [Team members needed] |
| Design | [X person-days] | |
| QA | [X person-days] | |
| Infrastructure | [Monthly cost] | |
| **Total** | **[Sum]** | |

**Expected Benefits:**
| Benefit | Metric | Current | Target | Timeline |
|---------|--------|---------|--------|----------|
| [Revenue increase] | MRR | $X | $Y | 3 months |
| [Cost reduction] | Support tickets | X/mo | Y/mo | 1 month |

**ROI:** [Expected benefit / Cost] = [X]%
**Payback Period:** [X months]

**Risks:**
1. [Risk] → Mitigation: [How]

**Decision:** ✅ Approved / ❌ Rejected / 🔄 Needs more data
```

### D4.5: Decision Modelling ⭐ NEW

```
Technique 1: Decision Matrix (Weighted Scoring)

| Criteria | Weight | Option A | Option B | Option C |
|----------|--------|----------|----------|----------|
| User value | 30% | 8 (2.4) | 6 (1.8) | 9 (2.7) |
| Dev effort | 25% | 5 (1.25)| 8 (2.0) | 3 (0.75)|
| Time to market| 20% | 7 (1.4) | 9 (1.8) | 4 (0.8) |
| Strategic fit | 15% | 9 (1.35)| 5 (0.75)| 7 (1.05)|
| Risk | 10% | 6 (0.6) | 7 (0.7) | 5 (0.5) |
| **Total** | **100%** | **7.0** | **7.05** | **5.8** |

→ Option B wins (barely). Review: is the gap significant enough?

Technique 2: 6 Thinking Hats (Edward de Bono)
🎩 White: Facts & data only
🎩 Red: Emotions & gut feeling
🎩 Black: Caution & risks
🎩 Yellow: Benefits & optimism
🎩 Green: Creativity & alternatives
🎩 Blue: Process & next steps
→ Dùng khi team stuck trong 1 perspective
```

> **Nguồn:** [Decision Analysis — BABOK v3, Chapter 10](https://www.iiba.org/), [Six Thinking Hats — Edward de Bono](https://www.debonogroup.com/)

---

## Domain 5: Deliver Often (15%)

### D5.1: Backlog Management

```
Epic (Mục tiêu business lớn, ~1 quarter)
├── Feature (Nhóm chức năng phục vụ Epic, ~1-3 sprint)
│   ├── User Story (Đơn vị nhỏ nhất, có thể demo, ~1-5 days)
│   │   └── Task (Dev breakdown, do Dev tự tạo)
```

**INVEST Check:** Independent | Negotiable | Valuable | Estimable | Small | Testable
**Story Splitting (SPIDR):** Spike | Path | Interface | Data | Rules

### D5.2: Story Mapping (Jeff Patton) ⭐ NEW

```
User Story Mapping Layout:

← User Journey (left to right) →

[Activity 1]      [Activity 2]      [Activity 3]
   │                  │                  │
[Task 1.1]        [Task 2.1]        [Task 3.1]     ← Backbone
[Task 1.2]        [Task 2.2]        [Task 3.2]
   │                  │                  │
────── Release 1 (Walking Skeleton / MVP) ──────
[Story A]         [Story D]         [Story G]
[Story B]         [Story E]         [Story H]
────── Release 2 ──────────────────────────
[Story C]         [Story F]         [Story I]
────── Release 3 (Full Feature) ───────────

Quy trình tạo Story Map:
1. Identify User Activities (big user goals) → top row
2. Break Activities into Tasks (steps user takes) → backbone
3. Brainstorm Stories under each Task → detail rows
4. Prioritize vertically: most important on top
5. Draw release lines: thin horizontal slices
6. Validate: "Có thể demo Release 1 cho user không?"

Nguyên tắc cốt lõi:
- Cắt NGANG (thin slice across activities) thay vì cắt DỌC (full depth 1 activity)
- Release 1 = Walking Skeleton: toàn bộ journey ở mức tối thiểu
- "Nếu user không thể walk through cả journey → chưa phải MVP"
```

> **Nguồn:** [User Story Mapping — Jeff Patton](https://www.jpattonassociates.com/user-story-mapping/), [IIBA Guide to POA, Chapter 6](https://www.iiba.org/)

### D5.3: Job Stories ⭐ NEW

```
Format: "When [situation/context], I want to [motivation], so I can [expected outcome]"

User Story vs Job Story:
| | User Story | Job Story |
|---|---|---|
| Format | As a [role], I want [action], so that [benefit] | When [situation], I want [motivation], so I can [outcome] |
| Focus | Role-based | Situation-based |
| Best for | Multiple user types | Context-driven behavior |
| Example | "As a sales manager, I want to see pipeline dashboard, so that I can forecast revenue" | "When I have a meeting with C-suite tomorrow, I want to see deal progress at a glance, so I can present accurate forecasts without manual calculations" |

Khi nào dùng Job Stories thay User Stories:
- "As a user" quá generic (1 loại user duy nhất)
- Situation/context quan trọng hơn role
- Internal tools (mọi người cùng 1 role)
- Khi muốn focus vào causality (WHY this situation triggers need)

⚠️ Có thể dùng kết hợp: User Stories cho external-facing features,
   Job Stories cho internal tools hoặc context-heavy flows.
```

> **Nguồn:** [Replacing The User Story With The Job Story — Alan Klement](https://jtbd.info/replacing-the-user-story-with-the-job-story-af7cdee10c27)

### D5.4: Release Management
→ Templates tại `.agents/skills/po/templates/product-templates.md` (Release Plan)

### D5.5: Definition Concepts (DoR / DoV / DoD) ⭐ ENHANCED

```
3 Definitions theo IIBA POA:

┌─── Definition of Ready (DoR) ───────────────────┐
│ Story sẵn sàng vào sprint?                      │
│ □ User Story format đúng (As/I want/So that)    │
│ □ AC đủ (Happy + Alternative + Exception)        │
│ □ INVEST pass                                     │
│ □ Team đã estimate và confirm hiểu               │
│ □ Dependencies identified và không blocking       │
│ □ UI mockup available (nếu có UI change)         │
│ □ NFR specified (nếu có)                         │
└──────────────────────────────────────────────────┘
            ↓ Sprint execution ↓
┌─── Definition of Delivery (DoV) ⭐ NEW ─────────┐
│ Increment sẵn sàng review/demo?                  │
│ □ Code complete & unit tested                    │
│ □ Feature deployable to review environment       │
│ □ Demo-ready (có thể show cho stakeholder)       │
│ □ No known critical bugs                         │
│ □ AC verifiable (QA có thể bắt đầu test)        │
│ □ Basic documentation available                  │
└──────────────────────────────────────────────────┘
            ↓ QA & validation ↓
┌─── Definition of Done (DoD) ────────────────────┐
│ Feature hoàn tất, có thể release?                │
│ □ Code reviewed và merge                         │
│ □ Unit test pass, coverage đủ                    │
│ □ AC đã QA verify                                │
│ □ Không regression                               │
│ □ Documentation updated                          │
│ □ Deployed to staging, smoke test pass           │
│ □ PO đã demo và accept                           │
└──────────────────────────────────────────────────┘

Enforcement:
- DoR: PO (primary) + Dev Lead (secondary). Fail = KHÔNG vào Sprint.
- DoV: Dev Lead (primary). Fail = chưa demo được.
- DoD: QA (verify) + PO (accept). Fail = quay lại In Progress.
```

> **Nguồn:** [IIBA Guide to POA, Chapter 6 — Definition Concepts](https://www.iiba.org/)

---

## Domain 6: Learn Fast (15%)

### D6.1: Experiment & MVP Thinking

#### Assumption → Hypothesis Framework
```
Assumption: "Chúng ta giả định rằng [X là thật]"

Hypothesis: "Chúng ta tin rằng [làm A] sẽ dẫn đến [kết quả B]
vì [lý do C]
Chúng ta sẽ biết điều này đúng khi [metric D đạt E trong F ngày]"

MCS: "Experiment ĐẠT nếu: [metric X ≥ Y] trong [Z ngày]"
"Nếu KHÔNG đạt → Kill idea hoặc Pivot — không kéo dài vô thời hạn"
```

#### Các Loại MVP

| Loại MVP | Mô tả | Khi nào dùng | Effort |
|---------|-------|-------------|--------|
| **Fake Door** | Landing page / nút CTA — đo click/sign-up | Validate demand trước khi build | 🟢 Rất thấp |
| **Email/Manual** | Offer dịch vụ bằng email thủ công | Validate willingness to pay | 🟢 Thấp |
| **Concierge** | Làm thủ công cho 5-10 early users | Validate solution trước automate | 🟡 Trung bình |
| **Wizard of Oz** | User thấy "tự động", backend là người | Validate UX chi phí thấp | 🟡 Trung bình |
| **Shadow** | Chạy song song hệ thống cũ, so sánh | Validate accuracy/reliability | 🟡 Trung bình |
| **Prototype** | Figma prototype, không code | Validate UX flow, IA | 🟡 Trung bình |
| **Tracer Bullet** | Build vertical slice nhỏ end-to-end | Validate tech feasibility + UX | 🔴 Cao |

#### Đọc Kết Quả
```
MCS ĐẠT → Persevere (tiếp tục, build thêm)
MCS GẦN ĐẠT → Iterate (điều chỉnh nhỏ, chạy lại)
MCS KHÔNG ĐẠT → Pivot (thay đổi approach) hoặc Kill (dừng hẳn)

⚠️ "Kill" không phải thất bại — là tiết kiệm dev effort
⚠️ Đừng "goalpost shifting" — không thay đổi MCS sau khi chạy
```

### D6.2: Opportunity Solution Tree
→ Chi tiết tại `SKILL.md` POA-D6.2

### D6.3: Real Options ⭐ NEW

```
3 Nguyên tắc Real Options:

1. OPTIONS HAVE VALUE
   - Càng nhiều options = càng ít rủi ro
   - Đừng commit sớm vào 1 vendor, 1 architecture, 1 approach
   - "Giữ 2-3 options sống cho đến khi có đủ data"

2. OPTIONS EXPIRE
   - Options không sống mãi — cost of maintaining options increases
   - "Last Responsible Moment" = thời điểm cuối cùng có thể quyết định
     mà không mất opportunity
   - Ví dụ: Chọn payment provider → Last Responsible Moment = trước khi
     integrate API (không phải trước khi viết PRD)

3. NEVER COMMIT EARLY UNLESS YOU KNOW WHY
   - Early commit = tăng risk (bạn biết ít nhất ở thời điểm sớm)
   - Late commit = có nhiều data hơn → quyết định tốt hơn
   - Exception: time-critical opportunity (first-mover advantage)

Ứng dụng trong Product:
- Architecture: Delay vendor lock-in, prefer APIs over direct integration
- Features: Run experiments before committing to full build
- Contracts: Prefer short-term commitments with option to extend
- Team: Cross-train team members to keep staffing options open

Decision Journal Template:
| Decision | Options | Last Responsible Moment | Data Needed | Current Lean |
|----------|---------|------------------------|-------------|-------------|
| [What] | [A, B, C] | [Date/Trigger] | [Evidence] | [Preference] |
```

> **Nguồn:** [Real Options — Chris Matts & Olav Maassen](https://www.infoq.com/articles/real-options-enhance-agility/), [IIBA Guide to POA](https://www.iiba.org/)

### D6.4: Spikes ⭐ ENHANCED

```
2 Loại Spike:

Technical Spike:
- Purpose: Validate tech feasibility
- Example: "Can we integrate OpenAI API within our latency budget?"
- Output: Technical recommendation + PoC code (NOT production code)
- Timebox: 1-2 days max

Functional Spike:
- Purpose: Validate value/usability
- Example: "Will users understand the new onboarding flow?"
- Output: User test results + recommendation
- Timebox: 2-3 days max

Spike Rules:
□ ALWAYS timebox (no open-ended research)
□ ALWAYS define success criteria upfront ("We'll know enough when...")
□ Output = recommendation document, NOT production code
□ Spike creates knowledge, not features
□ If spike fails → that's valuable info (kill bad ideas early)

Spike Template:
## Spike: [Question to answer]
**Type:** Technical / Functional
**Timebox:** [X days]
**Success Criteria:** "We'll know enough when [specific condition]"
**Result:** [Finding + Recommendation]
**Decision:** Proceed / Modify approach / Kill idea
```

### D6.5: Learning Loops ⭐ NEW

```
3 Tầng Learning Loops:

┌─── Loop 1: DAILY (Micro) ───────────────────┐
│ Standup: "Hôm qua tôi học được gì?"         │
│ → Adjust today's focus                       │
│ Cadence: Daily                               │
└──────────────────────────────────────────────┘

┌─── Loop 2: SPRINT (Meso) ───────────────────┐
│ Retro: "Sprint này validate/invalidate gì?" │
│ → Adjust next sprint approach                │
│ Cadence: Every 2 weeks                       │
└──────────────────────────────────────────────┘

┌─── Loop 3: RELEASE (Macro) ─────────────────┐
│ Post-release: "Metric nào thay đổi?"         │
│ → Adjust product strategy                    │
│ Cadence: Every release (monthly/quarterly)   │
└──────────────────────────────────────────────┘

Learning Log Template:
| Date | We assumed... | We tested by... | We learned... | Next action |
|------|--------------|-----------------|---------------|-------------|
| [Date] | [Assumption] | [Experiment/data] | [Insight] | [Action] |

Nguyên tắc:
- Log EVERY learning, even "obvious" ones
- Review log monthly — patterns emerge over time
- Share learnings cross-team (avoid repeated mistakes)
- "Learning without action = waste. Action without learning = risk."
```

---

## Domain 7: Obsess About Value (15%)

### D7.1: Prioritization Frameworks

#### RICE Score (Daily use)
```
RICE = (Reach × Impact × Confidence) / Effort

Reach: Bao nhiêu user bị ảnh hưởng trong 1 quý? (con số tuyệt đối)
Impact: Ảnh hưởng individual user (0.25/0.5/1/2/3)
Confidence: Tin tưởng estimate (50%/80%/100%)
Effort: Số người-tháng để hoàn thành
```

#### WSJF — Weighted Shortest Job First (SAFe)
```
WSJF = Cost of Delay / Job Duration
Cost of Delay = User/Business Value + Time Criticality + Risk Reduction/Opportunity Enablement
(Thang 1-10 cho mỗi chiều, relative sizing)
```

#### Kano Model
| Loại | Mô tả | Ví dụ |
|------|-------|-------|
| **Basic (Must-have)** | Không có → user bực, có → bình thường | Login, Search |
| **Performance** | Càng tốt → càng hài lòng tuyến tính | Loading speed, Accuracy |
| **Delight (Wow)** | Không mong đợi, nhưng thích khi có | Smart suggestions |
| **Indifferent** | Có hay không user không quan tâm | → Kill |
| **Reverse** | Một số user ghét khi có | → Careful |

### D7.2: Value Stream Mapping ⭐ NEW

```
Value Stream Mapping Process:

Step 1: Define boundaries
- Start point: [Trigger — e.g., user request feature]
- End point: [Value delivered — e.g., user uses feature in production]

Step 2: Map current state
┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐
│ Ideate │──→│ Specify│──→│ Build  │──→│ Deploy │
│ 2 days │   │ 3 days │   │ 10 days│   │ 1 day  │
└────────┘   └────────┘   └────────┘   └────────┘
   Wait: 5d    Wait: 3d    Wait: 2d    Wait: 1d

Process Time: 16 days
Wait Time: 11 days
Lead Time: 27 days
Efficiency: 16/27 = 59%

Step 3: Identify waste
- WAITING: Approval queues, blocked dependencies
- HANDOFFS: Knowledge lost between teams
- REWORK: Bugs, scope changes, misunderstandings
- OVER-PROCESSING: Gold-plating, unnecessary features

Step 4: Design future state
Target: Reduce wait time 50% → Lead time = 21.5 days → Efficiency = 74%
Actions: [Specific improvements per wait point]

Step 5: Implement & measure
Track lead time weekly → validate improvements
```

> **Nguồn:** [Value Stream Mapping — Karen Martin & Mike Osterling](https://www.ksmartin.com/books/value-stream-mapping/), [IIBA Guide to POA, Chapter 6](https://www.iiba.org/)

### D7.3: Value Modelling ⭐ NEW

```
Value Modelling Framework:

Dimension 1: CUSTOMER VALUE
- Problem severity: Low (1) / Medium (2) / High (3) / Critical (5)
- Frequency: Rarely (1) / Monthly (2) / Weekly (3) / Daily (5)
- Willingness to pay: Free only (0) / Maybe (1) / Yes (3) / Premium (5)
→ Customer Value = Severity × Frequency × WTP

Dimension 2: BUSINESS VALUE
- Revenue impact: None (0) / Indirect (1) / Direct (3) / Core (5)
- Cost reduction: None (0) / Minor (1) / Significant (3) / Major (5)
- Strategic alignment: Off-strategy (0) / Tangential (1) / Aligned (3) / Core (5)
→ Business Value = Revenue + Cost + Strategic

Dimension 3: TIME VALUE
- Cost of delay: Low (1) / Medium (3) / High (5) / Critical (10)
- First-mover advantage: No (0) / Maybe (1) / Yes (3) / Decisive (5)
→ Time Value = CoD + FMA

TOTAL VALUE SCORE = Customer Value + Business Value + Time Value
→ Use this score alongside RICE for prioritization
```

### D7.4: Continuous Value Optimization ⭐ NEW

```
Value Optimization Cycle:

     MEASURE              ANALYZE
   (Collect data)    (Find patterns)
        ↓                   ↓
        └──────→ ←──────────┘
                 ↓
            HYPOTHESIZE
         (Form theories)
                 ↓
              TEST
          (Run experiment)
                 ↓
         SCALE or KILL
      (Double down or remove)

Cadence:
- Weekly: Feature usage analytics review
- Monthly: Underperforming features audit
  → "Nếu feature X được < 5% users dùng sau 3 tháng → sunset candidate"
- Quarterly: Value realization tracking vs business case
  → "Feature Y cost 30 man-days. Expected +15% MRR. Actual: +8%. Gap: 7%."
- Semi-annual: Portfolio value assessment
  → "Tổng product portfolio có đang maximize value cho company?"

Feature Health Check:
| Feature | Users (MAU) | Trend | Business Impact | Verdict |
|---------|:-----------:|:-----:|:---------------:|---------|
| [Name]  | [Count]     | ↑↓→   | [High/Med/Low]  | Keep/Enhance/Sunset |
```

> **Nguồn:** [Inspired — Marty Cagan, Chapter 22](https://www.svpg.com/inspired-how-to-create-products-customers-love/), [Lean Analytics — Alistair Croll](http://leananalyticsbook.com/)
