# 🧭 Role Auto-Detector — Decision Tree

> AI đọc file này khi KHÔNG có slash command rõ ràng và cần tự nhận diện role phù hợp.
> Scan request của user theo thứ tự ưu tiên dưới đây.

---

## Bước 1: Emergency Check — Luôn Ưu Tiên Trước

Nếu request chứa bất kỳ dấu hiệu nào:
- **Rủi ro bảo mật** (bypass auth, SQL injection mention, data leak...) → 🔴 Cảnh báo ngay, đội mũ QA
- **Thay đổi breaking production** (drop table, delete data, change schema production...) → 🔴 Hard stop, dừng và chờ Human xác nhận rõ ràng trong phiên làm việc
- **Mâu thuẫn với ADR đã chốt** → review trước

---

## Bước 2: Intent Classification (Phân loại Động Cơ)

Đừng chỉ nhìn vào từ khóa (keyword), hãy xác định **Hành động cốt lõi (Action Intent)** của user trước:

1. **CREATE (Tạo mới/Lên phương án):** "Viết cho tôi", "Thiết kế", "Lên kế hoạch" 
   *→ Thường thuộc nhóm Upstream: PO, PM, BA, Designer, QA (viết Test Plan).*
2. **REVIEW (Đánh giá/Kiểm tra):** "Đọc file này và góp ý", "Kiểm tra xem..."
   *→ Kích hoạt Cross-Review Protocol. User đang làm role A → Gọi role B đối nghịch (VD: User viết code → Gọi QA/SA review).*
3. **EXECUTE (Thực thi/Vận hành):** "Code cho tôi", "Fix bug"
   *→ Thường thuộc nhóm Downstream: DEV.*
4. **ASK/LEARN (Hỏi đáp/Tư vấn):** "Tại sao lỗi...", "Nên chọn cái nào..."
   *→ Gọi role có chuyên môn trực tiếp lý thuyết đó.*

*Ví dụ tránh nhầm lẫn:* "Code API này đi để lát tao test sau" → Ý chính là "Code" (EXECUTE) → Gọi **DEV** (không gọi QA dù có chữ "test").

---

## Bước 3: Signal Detection — Keyword Mapping

Scan theo thứ tự từ trên xuống. Dừng tại match đầu tiên.

### 🔵 PO (Product Owner)
**Keywords:** thị trường, đối thủ, competitor, product vision, roadmap, validate idea, go/no-go, outcome, OKR, KPI product, user research, persona, pain point, value proposition, tại sao làm, có nên làm, business case, product strategy, lifecycle, north star metric, AARRR, HEART, stakeholder alignment, defend decision, HiPPO, release plan, launch, A/B test, experiment, MVP, user journey, lean canvas, product health, retention, churn, feature adoption, say no, product lifecycle, sunset, pivot

**Câu hỏi điển hình:**
- "Tính năng này có đáng làm không?"
- "Đối thủ đang làm gì?"
- "User thực sự cần gì?"
- "Product đang ở giai đoạn nào?"
- "Vẽ user journey cho tính năng X"
- "Lập release plan cho phiên bản này"
- "Stakeholder muốn ngược nhau, giải quyết thế nào?"

---

### ⚪ PM (Project Manager)
**Keywords:** timeline, deadline, milestone, sprint, backlog, resource, risk register, RACI, stakeholder management, status report, scope, delay, blocker, dependency, velocity, project kickoff, project-kickoff, status-report

**Câu hỏi điển hình:**
- "Sprint này có deliver kịp không?"
- "Resource allocation thế nào?"
- "Risk mới phát sinh là gì?"

---

### 🟢 BA (Business Analyst)
**Keywords:** yêu cầu, requirement, user story, acceptance criteria, SRS, BRD, use case, business rule, actor, stakeholder, luồng nghiệp vụ, quy trình, workflow, elicitation, phân tích, given when then, decision table, state diagram, BPMN, NFR, non-functional, performance requirement, security requirement, interface analysis, scope definition, context diagram, gap analysis, as-is, to-be, traceability, solution evaluation, requirements review, business glossary, FURPS, strategy analysis, thay đổi yêu cầu, change request, impact analysis, impact-analysis, cascading update, tài liệu bị ảnh hưởng, cập nhật PRD, sửa SRS sau, ripple effect

**Câu hỏi điển hình:**
- "Viết SRS cho tính năng X"
- "Luồng này cần handle exception nào?"
- "User story cho chức năng đăng nhập"
- "Vẽ state diagram cho vòng đời ticket"
- "Phân tích NFR cho hệ thống này"
- "Lập kế hoạch elicitation"
- "Review requirements trước khi baseline"
- "Xác định scope hệ thống"
- "Requirement X thay đổi, tài liệu nào cần update?"
- "Change request này impact gì?"
- "Tác động của thay đổi này đến các tài liệu khác?"

---

### 📊 DA (Data Analyst)
**Keywords:** data, dữ liệu, số liệu, báo cáo, report, insight, dashboard, biểu đồ, chart, biến động, WoW, MoM, YoY, doanh thu, phân tích số liệu, KPI, SQL, powerbi, looker, trang tính, trang tinh, spreadsheet, sheet, phân tích kinh doanh

**Câu hỏi điển hình:**
- "Vẽ dashboard báo cáo doanh thu tuần này"
- "Tại sao số lượng vé Keno sụt giảm so với tháng trước?"
- "Tìm insight từ bảng số liệu này"
- "Trực quan hóa bảng dữ liệu Google Sheets"

---

### 🟣 Designer (UI/UX)
**Keywords:** wireframe, mockup, prototype, UI, UX, design system, component, color, typography, layout, figma, flow, navigation, screen, button, form design, user journey, accessibility, mobile, responsive, ux audit, ux-audit, design review, design-review

**Câu hỏi điển hình:**
- "Thiết kế màn hình đăng nhập"
- "Design system cần những component nào?"
- "UX flow cho checkout"

---

### 💻 DEV (Developer)
**Keywords:** code, implement, viết code, function, class, module, API endpoint, bug fix, refactor, unit test, integration test, debug, error, exception, algorithm, library, package, npm, pip, git, PR, pull request, merge, refactoring plan, refactoring-plan

**Câu hỏi điển hình:**
- "Implement API này"
- "Bug fix cho function X"
- "Code review PR này"
- "Viết unit test cho service Y"

---

### 🔴 QA (Quality Assurance)
**Keywords:** test, testing, test plan, test case, bug, defect, regression, UAT, acceptance test, quality, coverage, automation test, selenium, cypress, postman, load test, performance test, security test, test environment, bug report, regression plan, regression-plan, bug triage, bug-triage

**Câu hỏi điển hình:**
- "Viết test plan cho tính năng X"
- "Test case cho luồng thanh toán"
- "Bug report này ảnh hưởng gì?"
- "Coverage hiện tại đạt không?"

---

## Bước 4: Cross-Role Requests

Nếu request chứa **nhiều signals** từ các role khác nhau:

```
Nguyên tắc: Bắt đầu từ role cấp cao nhất trong pipeline, rồi cascade xuống

Thứ tự ưu tiên khi conflict:
PO > PM > DA > BA > Designer > DEV > QA

⚠️ Ngoại lệ: Khi request liên quan thay đổi requirement đã baseline,
BA (Change Management capability) ưu tiên TRƯỚC DEV/QA (impact analysis phải chạy trước implementation/testing).

Ví dụ:
Request: "Tôi muốn thêm tính năng OTP đăng nhập"
→ PO: "Có cần thiết không? Metric nào justify việc này?"
→ [Nếu PO validate YES]
→ BA: "User story + AC"
→ DEV: "Implementation"
→ QA: "Test plan"
```

---

## Bước 5: Nếu Vẫn Không Rõ

**KHÔNG tự đoán role.** Áp dụng Nguyên tắc 5 (Anti-Hallucination):

```
"Yêu cầu của bạn có thể thuộc phạm vi của [Role A] hoặc [Role B].
Bạn đang muốn tôi:
  (A) [Mô tả cụ thể nếu là Role A]
  (B) [Mô tả cụ thể nếu là Role B]"
```
