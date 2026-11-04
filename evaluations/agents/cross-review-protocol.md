# 🔄 Cross-Role Adversarial Review Protocol

> **Mục đích:** Phá vỡ silo giữa các role. Sau khi viết xong draft, AI PHẢI tự động
> "đội mũ" của role liên quan để challenge trước khi trình user.
>
> **Nguồn cơ sở:** Multi-agent debate pattern ([DeepMind Debate paper](https://arxiv.org/abs/1805.00899))
> — nhiều perspective phản biện nhau → output tốt hơn đáng kể so với single-agent.

---

## Ma Trận Cross-Review — Ai Review Ai?

| Role tạo draft | Phải review bằng perspective | Câu hỏi challenge bắt buộc |
|----------------|------------------------------|---------------------------|
| **BA** (SRS, User Story, AC) | 🟠 **DEV perspective** | "API cần endpoint nào? Data type của field X? Có race condition khi 2 user submit cùng lúc? **Timeout xử lý thế nào? Timeout value = bao lâu? Retry policy? Compensating action nếu fail giữa multi-step?** Tác động schema DB & performance ở 10x traffic? **Idempotency key strategy?**" |
| **BA** (SRS, User Story, AC) | 🔴 **QA perspective** | "Test case nào từ AC này? Edge case: empty input, null, max length (10k chars), negative number, Unicode? Concurrent users? User bị revoke giữa chừng? **GD bị timeout/treo thì test thế nào? Đối tác không response thì verify ra sao? Retry exhausted thì expected behavior?**" |
| **BA** (SRS, User Story, AC) | 🔵 **PO perspective** | "Feature này match product strategy không? User segment nào benefit? Priority relative so với backlog? Metric nào move khi ship?" |
| **BA** (Impact analysis, Change Request) | 🔴 **QA perspective** | "Test cases nào cần update? Regression scope đủ chưa? Test data bị ảnh hưởng?" |
| **BA** (Impact analysis, Change Request) | 🟠 **DEV perspective** | "Thay đổi này ảnh hưởng schema DB / kiến trúc không? Cần update ADR không? Breaking change cho API consumers không?" |
| **DEV** (Code, Architecture/ADR, API) | 🔴 **QA perspective** | "Unit test cover edge case chưa? Error handling đủ chưa? Input validation đủ không? Test environment ready chưa?" |
| **DEV** (Code, Architecture/ADR, API) | 🟢 **BA perspective** | "Code/API này có phản ánh đúng business rules và AC không? Error message có đối chiếu glossary chưa?" |
| **DEV** (Code, Architecture/ADR, API) | ⚪ **PM perspective** | "Effort & tech debt có ảnh hưởng delivery milestone không? Rollback strategy khi deploy có rủi ro gì?" |
| **Designer** (UI/UX, Wireframe) | 🟢 **BA perspective** | "Flow này match với AC không? State nào bị thiếu (loading, error, empty)? Accessibility đủ chưa?" |
| **Designer** (UI/UX, Wireframe) | 🔴 **QA perspective** | "Responsive trên mobile/tablet? Error state có design chưa? Touch target ≥ 44px (project standard)?" |
| **Designer** (UI/UX, Wireframe) | 🔵 **PO perspective** | "Design này serve đúng target persona không? Có over-design cho edge case mà 1% user gặp? Priority element nào cho mobile-first?" |
| **Designer** (UI/UX, Wireframe) | 💻 **DEV perspective** | "Component này có tái sử dụng được design system không? Animation/Layout có khả thi với tech stack hiện tại không?" |
| **QA** (Test plan, Test cases) | 💻 **DEV perspective** | "Test case này feasible để automate không? Mock data cần gì? Môi trường test và CI pipeline run được test suite này không?" |
| **QA** (Test plan, Test cases) | 🟢 **BA perspective** | "Test cases đã cover hết các Acceptance Criteria, Business Rules và Exception Cases chưa?" |
| **QA** (Test plan, Test cases) | ⚪ **PM perspective** | "Thời gian chạy test có kịp release cycle không? Rủi ro nào còn open trước ngày UAT/Launch?" |
| **PO** (PRD, Roadmap, OKR) | 🟢 **BA perspective** | "Requirement đủ chi tiết để viết AC chưa? Edge case nào chưa tính? Scope có vượt MVP không?" |
| **PO** (PRD, Roadmap, OKR) | 🟠 **DEV perspective** | "Feature này technically feasible với timeline đề xuất không? API nào cần build mới? Có constraint kiến trúc/hạ tầng hay tech debt nào cần giải quyết trước?" |
| **PO** (PRD, Roadmap, OKR) | ⚪ **PM perspective** | "Timeline realistic với resource hiện tại? Dependencies nào block? Risk nào chưa address?" |
| **PO** (PRD, Roadmap, OKR) | 🔴 **QA perspective** | "Feature này testable không? AC có đủ measurable để viết test case? Có scenario nào chưa define expected behavior? Regression risk với feature hiện tại?" |
| **PO** (PRD, Roadmap, OKR) | 📊 **DA perspective** | "Có số liệu lịch sử hay dữ liệu hành vi người dùng nào chứng minh tính cần thiết của feature này không? Baseline metric đo lường thành công là bao nhiêu?" |
| **PM** (Project plan, Risk register) | 🔵 **PO perspective** | "Priority đúng product strategy chưa? Feature nào cut được nếu trễ? Outcome metric rõ ràng?" |
| **PM** (Project plan, Risk register) | 💻 **DEV perspective** | "Technical risk nào chưa có trong register? Dependency kỹ thuật/hạ tầng nào hidden? Estimate có buffer cho unknowns?" |
| **PM** (Project plan, Risk register) | 🔴 **QA perspective** | "Quality gate criteria đã rõ chưa? Có đủ thời gian cho regression và UAT không?" |
| **DA** (Dashboard, Insight, Report) | 🔵 **PO perspective** | "Insight này có tác động trực tiếp đến OKR/Product Strategy không? Hành động đề xuất có khả thi cho product roadmap không? User segment bị ảnh hưởng là ai?" |
| **DA** (Dashboard, Insight, Report) | 🟢 **BA perspective** | "Số liệu bất thường này có do thay đổi Business Rule hay lỗi dữ liệu không? Có tính năng nào trong app đang bị ảnh hưởng?" |

---

## Output Format Sau Cross-Review

Khi hoàn thành cross-review, AI PHẢI trình bày theo format:

```markdown
## 📝 Draft Output
[Output chính từ role gốc]

---

## 🔍 Cross-Review Findings
| # | Góc nhìn | Phát hiện | Mức độ | Đề xuất xử lý |
|---|---------|-----------|--------|---------------|
| 1 | 🟠 DEV | Field `amount` không rõ data type (int hay decimal?) | 🔴 Phải bổ sung | Thêm vào Interface Spec |
| 2 | 🔴 QA | Thiếu AC cho case user offline khi submit | 🟡 Nên bổ sung | Thêm AC-05 |
| 3 | 🔵 PO | Flow checkout thêm bước OTP có thể làm tăng tỷ lệ drop-off | 🟡 Cần cân nhắc | Đo lường drop-off rate |

**Mức độ:** 🔴 Blocking (phải fix trước khi submit) | 🟡 Important (nên fix) | 🟢 Minor (nice to have)
```

---

## ✅ Draft Đã Cập Nhật (sau khi xử lý findings)
[Output đã sửa — chỉ hiển thị nếu có Blocking findings được fix]

---

## 3 Pattern Sử Dụng Thực Tế

### Pattern 1: Brainstorm Ngược (Elicitation)
> *Trigger: User mô tả bối cảnh nghiệp vụ nhưng chưa có yêu cầu cụ thể*

```
❌ Old: AI ngồi brainstorm requirement từ đầu → output nông
✅ New: AI [BA mode] đặt 5-10 câu hỏi có chủ đích để kéo ra requirement ẩn

Câu hỏi tốt:
- "Khi [nghiệp vụ X] xảy ra, ai là người thực hiện bước đầu tiên?"
- "Có trường hợp nào ngoại lệ mà quy trình này không áp dụng không?"
- "Nếu người phê duyệt đi vắng 3 ngày, hệ thống xử lý thế nào?"
- "Volume hiện tại bao nhiêu transaction/ngày? Dự kiến 1 năm nữa?"
```

### Pattern 2: Draft → Cross-Review → Submit
> *Trigger: BA đã viết xong user story/AC draft*

```
BA viết draft → [DEV hat]: challenge feasibility, data model & schema changes
              → [QA hat]: challenge edge cases & testability
              → [PO hat]: challenge priority & business value
              → Cập nhật draft
              → Submit bản đã enriched
```

### Pattern 3: Meeting Notes → Structured AC
> *Trigger: User paste notes lộn xộn từ buổi họp*

```
1. Parse: Tách thành Decisions / Open Items / Action Items
2. Extract: Từ decisions, trích xuất requirements ngầm
3. Structure: Chuyển thành AC format Given/When/Then
4. Challenge [QA hat]: "Notes có ghi edge case nào không? Có gì mâu thuẫn?"
5. Highlight OPEN items cần clarify trước khi code
6. Output: AC structured + danh sách câu hỏi còn mở
```

---

## Nguyên Tắc Áp Dụng

1. **Luôn luôn cross-review** trước khi trình bất kỳ draft quan trọng nào
2. **Không giả mạo findings** — chỉ raise issue thực sự, không review cho có
3. **Blocking findings = hard stop** — phải resolve trước khi move forward
4. **Số lượng findings không quan trọng** — 1 finding quan trọng > 10 findings trivial

---

## Conflict Resolution Protocol — Khi 2 Roles Xung Đột

> **Vấn đề:** Cross-review có thể reveal conflict giữa perspectives.
> VD: SA muốn microservices nhưng DEV nói team không đủ skill. Ai thắng?

### Nguyên tắc: Không Có "Ai Thắng" — Chỉ Có "Data Thắng"

**Bước 1 — Identify loại xung đột:**

| Loại conflict | Ví dụ | Ai quyết định |
|--------------|-------|---------------|
| **Business vs Technical** | PO muốn ship nhanh, SA nói cần refactor trước | PO quyết → sau khi nghe SA quantify risk |
| **Architecture vs Timeline** | SA propose kiến trúc tốt nhưng cần 3 tháng, PM chỉ có 1 tháng | SA propose 2 options (ideal + pragmatic), PM + PO chọn |
| **Quality vs Deadline** | QA nói cần thêm 1 tuần test, PM nói deadline cứng | PM escalate lên stakeholder với data từ QA (risk of not testing) |
| **Security vs UX** | Security yêu cầu MFA mỗi login, Designer nói friction quá cao | SA arbitrate — propose middle ground (MFA session remember 30 ngày) |
| **Cost vs Reliability** | DevOps đề xuất multi-region DR, PM nói budget không cho phép | SA quantify: "Nếu không DR, downtime cost = X/giờ. DR cost = Y/tháng" → Data decide |

**Bước 2 — Escalation Ladder:**
```
Level 1: Roles tự thương lượng dựa trên data
         → Mỗi bên trình bày: "Nếu chọn option A, consequence = X. Nếu B, consequence = Y."

Level 2: SA arbitrate (cho technical conflicts)
         → SA là tie-breaker cho decisions liên quan kiến trúc + infrastructure
         → SA PHẢI document quyết định trong ADR

Level 3: PM/PO escalate lên stakeholder (cho business/timeline conflicts)
         → PM present: Option A (risk + cost) vs Option B (risk + cost)
         → Stakeholder quyết, PM + PO document

Level 4: User (Sếp) quyết định — Hard Stop
         → Chỉ khi Level 1-3 không đạt consensus
         → Trình Human trực tiếp trong phiên làm việc: summary 2 options + hệ quả từng option
```

**Bước 3 — Document Decision:**
Mọi conflict resolution phải được ghi lại:
```markdown
## Conflict Resolution — [Ngày]
**Giữa:** [Role A] vs [Role B]
**Về:** [Chủ đề xung đột]
**Option A:** [Mô tả] — Proposed bởi [Role]
**Option B:** [Mô tả] — Proposed bởi [Role]
**Quyết định:** [A hoặc B hoặc C (compromise)]
**Lý do:** [Data point / business justification]
**Arbitrator:** [SA / PM / Stakeholder]
**Hệ quả chấp nhận:** [Trade-off được conscious accept]
```

### RACI Cho Cross-Review Conflicts

| Loại quyết định | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|-----------------|-----------------|-----------------|---------------|-------------|
| Architecture & Tech Stack | SA | SA | DEV, DevOps | PM, PO |
| Feature Priority | PO | PO | BA, PM | DEV, QA, Designer |
| Timeline & Resource | PM | PM | PO, DEV Lead | Team |
| Quality Gate | QA | PM/PO | DEV, SA | Stakeholder |
| Security | SA | SA | DevOps, DEV | PM, PO |
| UX Decision | Designer | PO | BA, QA | DEV |
