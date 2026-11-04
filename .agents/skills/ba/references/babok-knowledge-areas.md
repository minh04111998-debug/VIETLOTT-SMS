# BABOK Knowledge Areas — Chi Tiết (BA Skill Reference)

> **Nguồn:** BABOK® v3 (IIBA) — 6 Knowledge Areas
> **Mục đích:** Tài liệu tham chiếu chi tiết cho các kỹ thuật BA. Được gọi (lazy-load) khi workflow hoặc SKILL.md cần.

---

## KA1: BA Planning & Monitoring

> **Nguồn:** BABOK® v3, Chapter 2

### Plan BA Approach
Trước khi bắt đầu phân tích, BA PHẢI xác định:
```
1. Methodology phù hợp:
   - Agile (iterative) → User Stories + BDD (GWT) + Sprint-based elicitation
   - Waterfall (predictive) → Use Cases + SRS + Phase-gate sign-off
   - Hybrid → Kết hợp tùy context (VD: Agile dev + formal SRS cho compliance)

2. Deliverables cần tạo:
   - Agile: PRD → User Stories + AC → Diagrams
   - Waterfall: BRD → SRS → Use Case Specifications → Interface Specs

3. Kỹ thuật elicitation phù hợp (chọn từ KA2):
   - Requirement rõ ràng → Document Analysis + Interview
   - Requirement mơ hồ → Workshop + Prototyping
   - Requirement phức tạp → Observation + Process Modeling
```

### Plan Stakeholder Engagement
```
Stakeholder Analysis Matrix (Power/Interest):
┌────────────────────┬──────────────────────┐
│ High Power,        │ High Power,          │
│ Low Interest       │ High Interest        │
│ → Keep Satisfied   │ → Manage Closely     │
│ (Sponsor, CFO)     │ (PO, Key User, CTO)  │
├────────────────────┼──────────────────────┤
│ Low Power,         │ Low Power,           │
│ Low Interest       │ High Interest        │
│ → Monitor          │ → Keep Informed      │
│ (IT Support)       │ (End Users, QA)      │
└────────────────────┴──────────────────────┘

Với mỗi stakeholder quan trọng, xác định:
- Communication preference (email/meeting/Slack/report)
- Tần suất update (daily/weekly/milestone-based)
- Decision authority level (approve/review/inform)
```

### BA Effort Estimation
```
Rule of thumb:
- Elicitation: 30-40% tổng effort BA
- Analysis & Modeling: 25-30%
- Documentation: 20-25%
- Review & Validation: 10-15%
```

### Plan BA Governance
> **Nguồn:** BABOK® v3, KA1 Task 1.3

Xác định cơ chế quản trị requirements — ai approve, ai review, quy trình escalation:
```
Governance Elements:
1. Decision Authority: Ai có quyền approve từng loại requirement? (BR→PO, FR→BA+SA, NFR→SA)
2. Approval Process: Workflow approve → reject → rework
3. Escalation Path: BA → PM → PO → Sponsor (khi conflict giữa stakeholders)
4. Change Control: Threshold nào cần formal CR? (ref: ba-rules.md §7)
5. Communication Plan: Ai cần biết khi requirement thay đổi?

Output: RACI Matrix (ref: ba-rules.md §2.5)
```
→ Template: `.agents/skills/ba/templates/document-templates.md` §10

### Plan BA Information Management
> **Nguồn:** BABOK® v3, KA1 Task 1.4

Xác định cách lưu trữ, tổ chức, và truy cập requirement artifacts:
```
Information Management Plan:
1. Repository: Nơi lưu trữ requirements (file system / Wiki / Jira)
2. Organization: Cấu trúc thư mục, naming convention
3. Access Control: Ai được đọc/sửa? (mặc định: mọi team member)
4. Version Control: Major.Minor + change log header
5. Traceability Tool: Traceability matrix format + maintenance frequency
6. Retention Policy: Bao lâu giữ draft? Archived docs xử lý thế nào?

Output: Info Management section trong Scope Document
```
→ Chi tiết: `ba-rules.md` §2.6

### Identify BA Performance Improvements
> **Nguồn:** BABOK® v3, KA1 Task 1.5

Sau mỗi dự án/release, BA PHẢI retrospective:
```
BA Retrospective — Câu hỏi bắt buộc:
1. Elicitation effectiveness: "Có requirement nào bị miss mà phát hiện muộn?"
2. Documentation quality: "DEV/QA có phải hỏi lại nhiều không? Top 3 câu hỏi lặp?"
3. Change frequency: "Bao nhiêu % requirements bị thay đổi sau baseline? Nguyên nhân?"
4. Cycle time: "Từ lúc nhận yêu cầu → baseline SRS mất bao lâu? Có bottleneck?"
5. Stakeholder satisfaction: "Stakeholder có hài lòng với output BA không?"
6. Technique effectiveness: "Kỹ thuật elicitation nào hiệu quả nhất? Nào nên bỏ?"

Output: Lessons Learned Report (ref: templates/document-templates.md §12)
Timing: Chạy tại Step 8 (Solution Evaluation) hoặc Sprint Retrospective
```
→ Nguồn: [Lessons Learned — PMI](https://www.pmi.org/learning/library/lessons-learned-next-level-7991)

---

## KA2: Elicitation & Collaboration

### Kỹ Thuật Elicitation — Chọn Đúng Tool

| Kỹ thuật | Khi nào dùng | Output | Effort |
|---------|-------------|--------|--------|
| **Interview** (5W1H) | Requirement chưa rõ, cần deep-dive 1-1 | Notes + implicit requirements | 🟡 Medium |
| **Workshop** | Nhiều stakeholder, cần consensus | Agreed requirements, resolved conflicts | 🔴 High |
| **Document Analysis** | Có tài liệu legacy, SOP, Excel, Word | As-Is process, hidden business rules | 🟢 Low |
| **Observation** | Cần hiểu actual workflow (không chỉ stated) | Pain points thật, workarounds | 🟡 Medium |
| **Survey/Questionnaire** | Nhiều end-users, cần quantitative data | Trends, priorities, satisfaction | 🟢 Low |
| **Focus Group** | Validate concept với nhóm users đại diện | Feedback patterns, concerns | 🟡 Medium |
| **Prototyping** | Requirement phức tạp, user không thể articulate | Validated UX flow, refined requirements | 🔴 High |
| **Interface Analysis** | Tích hợp bên thứ 3, API boundary | Interface specs, data contracts | 🟡 Medium |
| **Process Modeling** | Luồng nghiệp vụ phức tạp, nhiều nhánh | BPMN/Activity Diagram, swimlane | 🟡 Medium |
| **Brainstorming** | Giai đoạn đầu, cần diverge ý tưởng | Feature list, idea pool | 🟢 Low |

### Brainstorm Ngược (Interactive Elicitation)

**Bước 1 — Hỏi 5W1H có chủ đích:**
```
- Who: Ai thực hiện? Ai phê duyệt cuối cùng?
- What: Đầu vào? Đầu ra? Ngoại lệ?
- When: Trigger event? Deadline business?
- Where: Context nào?
- Why: Mục tiêu business thực sự? Metric nào thay đổi?
- How many: Volume? Frequency? Scale?
```

**Bước 2 — Challenge với "What If":**
```
- "Nếu người phê duyệt đi vắng 3 ngày, xử lý thế nào?"
- "Nếu cùng lúc 100 user submit, có race condition không?"
- "Nếu dữ liệu đầu vào sai format, thông báo lỗi như thế nào?"
- "Nếu third-party API timeout, flow tiếp tục hay hủy?"
```

**Bước 3 — Cross-Review bắt buộc:**
Sau khi draft → đọc `evaluations/agents/cross-review-protocol.md` → challenge với DEV + QA perspective.

### Phân Loại Yêu Cầu (BABOK Classification)
```
Business Requirement (BR)    → Tại sao dự án tồn tại? (Level CEO)
Stakeholder Requirement (SR) → Stakeholder cần gì để đạt BR? (Level Manager)
Solution Requirement:
  - Functional (FR)          → Hệ thống làm gì? (Level User/System)
  - Non-Functional (NFR)     → Hệ thống tốt như thế nào? (Performance, Security, UX)
Transition Requirement (TR)  → Cần làm gì để chuyển từ AS-IS sang TO-BE?
```

---

## KA3: Requirements Life Cycle Management

> **Nguồn:** BABOK® v3, Chapter 5 — 5 Tasks
> **Các task đã cover:** Trace (ba-rules §2.1), Maintain (SKILL §23), Prioritize (ba-rules §2.4), Assess Changes (ba-rules §7)

### Approve Requirements
> **Nguồn:** BABOK® v3, KA3 Task 5.5

Quy trình phê duyệt requirements trước khi baseline:
```
Approval Workflow:
1. BA hoàn thành draft → đặt status [In Review]
2. Cross-review (DEV + QA + SA perspective) → ba-rules §5 Self-Check
3. Verify: BA kiểm tra quality checklist (completeness, consistency, clarity)
4. Validate: Stakeholder xác nhận "đúng thứ họ cần" (walkthrough/demo)
5. Approver (theo RACI) ký duyệt → status [Approved/Baselined]
6. Nếu reject → status [Rework Needed] + ghi rõ lý do → BA fix → quay lại bước 2

Approval Authority (mặc định):
- Business Requirements (BR): PO / Sponsor
- Functional Requirements (FR): PO + SA
- Non-Functional Requirements (NFR): SA + PM
- Change Request (CR): PM + PO (ref: ba-rules §7.2)

Không được approve nếu:
🚩 Traceability matrix chưa cập nhật
🚩 Còn open question chưa resolve
🚩 Self-check chưa pass (ba-rules §5)
🚩 Cross-review chưa thực hiện
```
→ Nguồn: [BABOK® v3, Chapter 5.5](https://www.iiba.org/standards-and-resources/babok/)

---

## KA4: Strategy Analysis

> **Nguồn:** BABOK® v3, Chapter 6 — Đây là KA thường bị bỏ qua nhưng CỰC KỲ quan trọng.

### Analyze Current State (As-Is)
**PHẢI thực hiện TRƯỚC KHI viết bất kỳ requirement nào:**
```
1. Business Context: Tổ chức đang ở đâu? Mục tiêu business?
2. People & Processes: Ai làm gì? Quy trình hiện tại? Pain points?
3. Technology: Hệ thống hiện tại? Tech debt? Integration points?
4. Data: Dữ liệu hiện có? Chất lượng data? Data flow?
5. Performance: KPIs hiện tại? Benchmark với industry?

Output: As-Is Assessment Report
```

### Define Future State (To-Be)
```
1. Business Goals: Mục tiêu cụ thể, đo lường được (SMART)
2. Gap Identification: Current State vs Future State → Gap Matrix
3. Solution Approach:
   - Option A: Build custom → Pros/Cons/Cost/Risk
   - Option B: Buy/SaaS → Pros/Cons/Cost/Risk
   - Option C: Hybrid → Pros/Cons/Cost/Risk
4. Recommendation: Kèm rationale dựa trên data
```

### Assess Risks
```
Risk Register Template:
| ID | Mô tả rủi ro | Xác suất | Tác động | Mức độ | Biện pháp | Owner |
|----|-------------|---------|---------|--------|----------|-------|

Các loại rủi ro BA phải quét:
🔴 Business: Thay đổi thị trường, regulation, competitor
🟡 Technical: Legacy, tích hợp phức tạp, performance bottleneck
🟡 Organizational: Resistance to change, thiếu resource, skill gap
🔴 Requirements: Ambiguity, scope creep, conflicting needs
```

### Define Change Strategy
```
Transition Requirements — AS-IS sang TO-BE:
- Data Migration: Dữ liệu cũ chuyển thế nào?
- Training: Ai cần? Nội dung? Timeline?
- Parallel Run: Chạy song song bao lâu?
- Rollback Plan: Nếu fail, quay về thế nào?
- Communication Plan: Ai cần biết? Khi nào?
```

---

## KA5: Requirements Analysis & Design Definition

### Modeling Techniques — Chọn Đúng Model

| Tình huống | Model phù hợp | Tool |
|-----------|---------------|------|
| Business logic phức tạp (nhiều if-else) | **Decision Table / Decision Tree** | Markdown table / Mermaid |
| Object có nhiều trạng thái (order, ticket) | **State Diagram** | Mermaid stateDiagram |
| Luồng nghiệp vụ cross-department | **BPMN / Swimlane** | Mermaid flowchart with subgraph |
| Data entities & relationships | **ERD (Entity Relationship)** | Mermaid erDiagram |
| System interactions | **Sequence Diagram** | Mermaid sequenceDiagram |
| System boundary & scope | **Context Diagram** | Mermaid flowchart |
| User perspective | **Use Case Diagram** | Mermaid graph |
| Luồng chức năng | **Activity Diagram** | Mermaid flowchart TD |

**Nguyên tắc:** Chọn model đơn giản nhất đủ để diễn đạt. Không over-model.

### NFR Analysis — FURPS+ Framework
```
F — Functionality: Features, Capabilities, Security
U — Usability: UX, Accessibility, Learnability, Onboarding time
R — Reliability: Uptime SLA, MTBF, Recoverability, Data integrity
P — Performance: Response time, Throughput, Scalability, Resource usage
S — Supportability: Maintainability, Testability, Configurability

+ (Plus):
- Design constraints (platforms, standards, regulations)
- Implementation constraints (languages, tools, third-party)
- Interface requirements (external system APIs, data formats)
- Physical requirements (hardware, deployment environment)

Mỗi NFR PHẢI có:
- Measurable threshold: "Response time < 2 giây cho 95th percentile"
- Measurement method: "Đo bằng APM tool tại production"
- Priority: Must/Should/Could
```

### Define Requirements Architecture
> **Nguồn:** BABOK® v3, KA5 Task 6.4

Tổ chức requirements thành cấu trúc logic — TRƯỚC khi viết chi tiết:
```
Requirements Architecture:
1. Grouping: Phân nhóm requirements theo module/feature area
   Ví dụ: [Authentication] [Payment] [Notification] [Reporting]

2. Viewpoints: Mỗi nhóm mô tả từ nhiều góc nhìn
   - Functional view: Features + Use Cases
   - Data view: Entities + Relationships (ERD)
   - Process view: Business flows (BPMN)
   - Interface view: System interactions (Context Diagram)

3. Dependencies: Map mối quan hệ giữa các nhóm
   [Payment] → depends on → [Authentication]
   [Notification] → triggered by → [Payment]

4. Priority Mapping: MoSCoW per package

Output: Requirements Package Diagram (Mermaid graph)
```
**Áp dụng tại:** Step 4 (BRD) hoặc Step 5 (SRS) — khi cấu trúc tài liệu

### Define Design Options
> **Nguồn:** BABOK® v3, KA5 Task 6.5

BA đề xuất 2-3 phương án **giải pháp nghiệp vụ** (KHÔNG phải tech design — đó là SA):
```
Solution Options Comparison:
| Tiêu chí          | Option A              | Option B              | Option C              |
|-------------------|-----------------------|-----------------------|-----------------------|
| Mô tả             | [Giải pháp A]         | [Giải pháp B]         | [Giải pháp C]         |
| Ưu điểm           | [...]                 | [...]                 | [...]                 |
| Nhược điểm        | [...]                 | [...]                 | [...]                 |
| Effort ước tính    | [X man-days]          | [Y man-days]          | [Z man-days]          |
| Risk              | 🟢/🟡/🔴              | 🟢/🟡/🔴              | 🟢/🟡/🔴              |
| Stakeholder impact | [...]                 | [...]                 | [...]                 |
| Recommendation    | ★ (recommended)       |                       |                       |

BA recommendation kèm rationale dựa trên data, KHÔNG dựa trên opinion.
```
**Áp dụng tại:** Step 4 (BRD) hoặc Step 5 (SRS) — trước khi chốt giải pháp
→ Template: `.agents/skills/ba/templates/document-templates.md` §13

### Analyze Potential Value
> **Nguồn:** BABOK® v3, KA5 Task 6.6

Đánh giá giá trị tiềm năng TRƯỚC khi build — tránh build thứ không ai dùng:
```
Value Proposition Canvas (Lightweight):
| Mục                | Nội dung                                    |
|--------------------|--------------------------------------------||
| Problem            | Vấn đề nghiệp vụ cần giải quyết            |
| Proposed Solution  | Giải pháp đề xuất (high-level)              |
| Target Users       | Ai là người dùng chính? Số lượng?           |
| Expected Benefit   | Lợi ích cụ thể (quantify nếu có thể)       |
| Success KPI        | Metric đo lường thành công                  |
| Cost Estimate      | Effort ước tính (man-days/budget)           |
| Risk               | Rủi ro chính nếu KHÔNG làm                 |
| Alternative        | Nếu không build, có workaround nào?         |

Decision: GO / NO-GO / NEED MORE DATA
```
**Áp dụng tại:** Step 1 (Scope Definition) — section cuối cùng
→ Nguồn: [Value Proposition Design — Strategyzer](https://www.strategyzer.com/library/the-value-proposition-canvas)

### Validate Requirements (Phân biệt với Verify)
> **Nguồn:** BABOK® v3, KA5 Task 6.3

```
Verify vs Validate — PHẢI phân biệt rõ:

┌──────────────────────────────────────────────────────────┐
│ VERIFY ("Viết đúng cách?")                              │
│ - Ai làm: BA tự review + Cross-review (DEV, QA, SA)    │
│ - Kiểm tra: Completeness, Consistency, Clarity          │
│ - Phương pháp: Checklist, Traceability check            │
│ - Câu hỏi: "Requirement có rõ ràng, nhất quán không?"  │
├──────────────────────────────────────────────────────────┤
│ VALIDATE ("Viết đúng thứ?")                             │
│ - Ai làm: Stakeholder/PO + End User                    │
│ - Kiểm tra: Business need alignment, User acceptance    │
│ - Phương pháp: Walkthrough, Prototype, User testing     │
│ - Câu hỏi: "Đây có phải thứ stakeholder thật sự cần?"  │
└──────────────────────────────────────────────────────────┘

Validation Techniques:
1. Stakeholder Walkthrough: Trình bày requirements, stakeholder confirm
2. Prototype Review: Demo mockup/wireframe, thu thập feedback
3. Traceability to BR: Mỗi FR PHẢI trace về ≥1 Business Requirement
4. Acceptance Criteria Test: "Nếu AC này pass, stakeholder có happy?"
```
**Áp dụng tại:** Step 6 (Requirements Review) — sub-step Validate

---

## KA6: Solution Evaluation

### Measure Solution Performance
```
Post-delivery, BA PHẢI kiểm tra:
1. "Requirement X đã implement đúng chưa?" → Validate with AC
2. "Feature đã tạo business value chưa?" → Check Tracking Metrics
3. "User có thực sự dùng feature không?" → Check Telemetry Events
4. "Có side-effect nào không lường trước?" → Monitor error rate, support tickets
```

### Assess Solution Limitations
```
Sau 2-4 tuần post-release, đánh giá:
- Feature adoption rate vs expectation
- User feedback / pain points mới
- Performance trong production vs NFR
- Workarounds user vẫn đang dùng (dấu hiệu requirement thiếu)
```

### Recommend Actions to Increase Value
```
Based on evaluation:
1. KEEP: Feature đang deliver value → maintain
2. ENHANCE: Feature cần cải thiện → new user stories
3. REMOVE: Feature không ai dùng → deprecate
4. PIVOT: Feature sai hướng → change request
```

### Analyze Performance Measures
> **Nguồn:** BABOK® v3, KA6 Task 8.2

Sau khi đo performance (task trên), BA PHẢI phân tích sâu:
```
Performance Analysis Framework:
1. Trend Analysis: Metric đang tăng hay giảm theo thời gian?
2. Root Cause: Nếu metric không đạt target, nguyên nhân gốc?
   - Technical: Performance bottleneck? Bug? Integration issue?
   - Process: Workflow phức tạp? Quá nhiều bước?
   - People: Training thiếu? Resistance to change?
   - Data: Data quality issue? Missing data?
3. Correlation: Metric A thay đổi có ảnh hưởng Metric B?
4. Benchmark: So với industry standard, performance ở mức nào?

Output: Performance Analysis trong Evaluation Report
```

### Assess Enterprise Limitations
> **Nguồn:** BABOK® v3, KA6 Task 8.4

Xác định giới hạn tổ chức ngăn solution đạt full value:
```
Enterprise Limitations Checklist:
□ Culture: Tổ chức có sẵn sàng thay đổi cách làm việc?
□ Process: Quy trình hiện tại có block adoption?
□ Skills: Nhân sự có đủ kỹ năng sử dụng solution mới?
□ Technology: Hạ tầng hiện tại có support đầy đủ?
□ Data: Dữ liệu đủ chất lượng để solution hoạt động?
□ Budget: Có đủ ngân sách vận hành ongoing?
□ Governance: Chính sách nội bộ có cản trở?

Với mỗi limitation, xác định:
- Impact level: 🔴 Blocking / 🟡 Degrading / 🟢 Minor
- Mitigation: Giải pháp khắc phục
- Owner: Ai chịu trách nhiệm khắc phục?
- Timeline: Bao lâu để giải quyết?

Output: Enterprise Limitations section trong Evaluation Report
```
→ Nguồn: [BABOK® v3, Chapter 8.4](https://www.iiba.org/standards-and-resources/babok/)

---

## Tư Duy Phân Tích Expert — Câu Hỏi Phải Tự Hỏi

### Khi phân tích luồng nghiệp vụ:
```
1. "Ai là actor thực sự? Có actor ẩn nào không?" (VD: cron cũng là actor)
2. "Tiền điều kiện? Có thể bị skip không?"
3. "Nếu luồng bị interrupt giữa chừng?"
4. "Business rule nào đang implicit?"
5. "Luồng này conflict với luồng nào khác không?"
6. "Data gì được tạo / thay đổi / xóa?"
7. "State nào có thể chuyển? State nào là dead-end?"
```

### Meeting Notes → Structured AC
```
1. PARSE: Tách thành Decisions / Open Items / Action Items
2. EXTRACT: Từ Decisions, trích xuất requirements ngầm + business rules ẩn
3. STRUCTURE: Chuyển thành AC format Given/When/Then
4. CROSS-REVIEW [QA hat]: "Có edge case nào? Có mâu thuẫn?"
5. VALIDATE: Gửi lại AC cho participants xác nhận
6. HIGHLIGHT: Open Items cần clarify TRƯỚC KHI viết SRS
7. OUTPUT: AC structured + câu hỏi còn mở
```
