# Các Framework Phân Tích Chuyên Sâu (BA)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — Sections 1, 8, 10, 11, 12, 13, 14, 15

---

## 1. Kỹ Thuật Thu Thập Yêu Cầu (Section 1)

### Phỏng Vấn Stakeholder — Template Câu Hỏi

```markdown
## Câu Hỏi Phỏng Vấn - [Chủ đề]

### Hiểu nghiệp vụ hiện tại (As-Is)
1. Quy trình hiện tại của [chức năng] diễn ra như thế nào?
2. Ai tham gia vào quy trình này? Vai trò của họ?
3. Công cụ / hệ thống hiện tại đang sử dụng?
4. Khó khăn, pain point hiện tại là gì?
5. Mất bao lâu để hoàn thành quy trình?

### Mong muốn tương lai (To-Be)
6. Bạn kỳ vọng hệ thống mới giải quyết vấn đề gì?
7. Chức năng nào là quan trọng nhất (must-have)?
8. Chức năng nào là "nice to have"?
9. KPI/metric nào để đo lường thành công?

### Ràng buộc
10. Có hệ thống nào cần tích hợp không?
11. Có quy định pháp lý nào cần tuân thủ không?
12. Timeline mong muốn?
```

### Workshop Facilitation
1. Gửi agenda trước 2-3 ngày
2. Giới hạn 5-8 người tham gia
3. Sử dụng các technique: Brainstorming, Affinity Mapping, Dot Voting
4. Ghi nhận tất cả ý kiến, không đánh giá
5. Tổng hợp kết quả trong 24h

---

## 2. Phân Tích Ngoại Lệ & Rủi Ro — Edge Case Analyzer (Section 8)

Quét qua yêu cầu nghiệp vụ và tự động suy luận để tìm ra các rủi ro thuộc **8 nhóm** sau:

| Nhóm | Mô tả | Ví dụ câu hỏi cần đặt ra |
|------|--------|--------------------------| 
| 🔲 **Empty States** | Trạng thái rỗng | Người dùng mới chưa có dữ liệu, danh sách trống hiển thị gì? |
| 🔴 **Error States** | Trạng thái lỗi | Mất mạng, API timeout, bên thứ 3 lỗi, nhập sai định dạng? |
| 📏 **Limits & Constraints** | Giới hạn | Upload file quá nặng, text quá dài, phân trang, hết hạn token? |
| 🔐 **Permissions/Roles** | Phân quyền | User chưa đăng nhập, không đủ thẩm quyền mà cố thao tác? |
| ⚡ **Concurrency** | Thao tác đồng thời | 2 users cùng mua 1 món cuối, cùng chỉnh sửa 1 form? |
| ⏱️ **Timeout & Latency** | Quá thời gian chờ | API đối tác không phản hồi sau X giây? User chờ quá lâu? Job chạy quá thời gian dự kiến? Giao dịch pending quá N phút? |
| 🔄 **Retry & Recovery** | Thử lại & khôi phục | Retry bao nhiêu lần? Backoff strategy? Rollback nếu retry fail? Compensating transaction cho bước đã commit? Idempotency key tránh duplicate? |
| 🔗 **Integration Failure** | Lỗi tích hợp bên ngoài | Đối tác trả HTTP 500? Certificate hết hạn? Format response thay đổi? Rate limit bị chặn? VPN/firewall đứt? Đối soát file không đến đúng giờ? |

> [!IMPORTANT]
> **Đặc biệt với hệ thống tích hợp nhiều đối tác (Bank, Ví, Nhà mạng, Cổng thanh toán):**
> 3 nhóm cuối (⏱️ 🔄 🔗) là **BẮT BUỘC** phải phân tích cho mỗi luồng gọi external system. BA **KHÔNG ĐƯỢC** bỏ qua.

**Output mong đợi:**
`| Nhóm ngoại lệ | Mô tả kịch bản (Scenario) | Đề xuất hướng xử lý cho PO/Dev |`

### 2b. Timeout & Hung State Deep-Dive Protocol

> **Kích hoạt BẮT BUỘC khi:** Luồng nghiệp vụ có bất kỳ bước nào gọi external system (API, DB heavy query, file transfer, message queue).

Cho **MỖI bước** trong luồng có gọi external, BA PHẢI trả lời 7 câu hỏi sau:

```markdown
⏱️ TIMEOUT & HUNG STATE CHECKLIST — [Tên Use Case] — Bước [N]:

1. [ ] TIMEOUT VALUE: Nếu bước này mất > X giây, hệ thống phản hồi gì cho user?
       → Giá trị X = ??? (PHẢI định lượng cụ thể, ví dụ: 30s, 60s, 5m)
2. [ ] HUNG DETECTION: Nếu bước này KHÔNG BAO GIỜ nhận response, timeout sau bao lâu?
       → Cơ chế detect: polling / heartbeat / circuit breaker?
3. [ ] POST-TIMEOUT STATE: Sau timeout, giao dịch ở trạng thái gì?
       → Cancelled / Pending / Retry / Requires Manual Intervention?
4. [ ] RECOVERY OWNER: Ai xử lý giao dịch treo?
       → Auto-recovery (job/scheduler) / Manual (Operator trên Admin) / Escalation?
5. [ ] USER NOTIFICATION: User có được thông báo không? Qua kênh nào?
       → Push notification / SMS / In-app message / Email / Không thông báo?
6. [ ] IDEMPOTENCY: Có cần cơ chế idempotency để tránh duplicate khi retry?
       → Idempotency key strategy: request ID / transaction ID / hash?
7. [ ] RECONCILIATION: GD treo có xuất hiện trong báo cáo đối soát không?
       → File đối soát hàng ngày bao gồm trạng thái nào? Pending có nằm trong đó?
```

**Output mong đợi — Exception Analysis Table:**

```markdown
### Exception Analysis — [Tên Use Case]

| # | Bước | Trigger | Exception Type | Hệ thống phản hồi | Timeout | Retry Policy | Compensating Action |
|---|------|---------|---------------|-------------------|---------|-------------|---------------------|
| E1 | Bước 3: Gọi API Bank | HTTP 500 từ Bank | Integration Error | Hiển thị "GD thất bại" | 30s | 3 lần, backoff 5s/10s/20s | Rollback HMDT |
| E2 | Bước 3: Gọi API Bank | No response (hung) | Timeout/Hung | GD chuyển "Đang xử lý" | 60s | Job check mỗi 5m | Auto-cancel sau 30m, hoàn HMDT |
| E3 | Bước 4: User confirm | User không thao tác | User Timeout | Link hết hạn | 15m | Không retry | Hủy GD pending, thông báo CTV |
| E4 | Bước 5: Ghi DB | DB connection pool hết | System Error | 503 + retry | 10s | Auto-retry 2 lần | Queue request, process khi DB available |
```

> **Nguồn tham chiếu:**
> - [Microsoft — Retry Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)
> - [Microsoft — Circuit Breaker Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)
> - [Microsoft — Compensating Transaction Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction)
> - [AWS — Saga Pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/saga-pattern.html)

---

## 3. Meeting Notes → Structured Acceptance Criteria (Section 10)

### Quy Trình Xử Lý

**Bước 1 — Parse (Phân loại notes):**
```
Chia notes thành 3 bucket:
✅ DECISIONS  → Những gì đã được quyết định trong cuộc họp
❓ OPEN ITEMS → Câu hỏi chưa có câu trả lời, cần follow-up
📋 ACTIONS    → Ai làm gì trước khi nào
```

**Bước 2 — Extract Business Rules Ẩn:**
```
Từ Decisions, tìm:
- Business rule ngầm ("Chỉ manager mới được duyệt" → permission rule)
- Constraint ngầm ("Phải xong trước ngày X" → deadline constraint)
- Exception chưa được ghi rõ ("nhưng trừ trường hợp..." → exception flow)
```

**Bước 3 — Draft AC (Given/When/Then):**
Chuyển mỗi Decision thành ≥ 1 AC theo format BDD chuẩn.

**Bước 4 — Cross-Review [QA Hat]:**
_"Có edge case nào trong notes không? Có AC nào thiếu exception path không?"_

**Bước 5 — Highlight Open Items:**
```markdown
## ⚠️ Cần Clarify Trước Khi Viết SRS

| # | Câu hỏi mở | Owner | Deadline |
|---|-----------|-------|---------| 
| 1 | [...] | [...] | [...] |
```

### Output Format Mẫu

```markdown
# Meeting Notes Analysis — [Tên cuộc họp] [DD/MM/YYYY]

## ✅ Quyết Định → Acceptance Criteria

### Feature: [Tên tính năng]

**AC-01 [Happy Path]**
Given user đã đăng nhập với role Manager
When user nhấn nút "Duyệt đơn hàng #XYZ"
Then hệ thống chuyển trạng thái đơn hàng từ "Chờ duyệt" → "Đã duyệt"
 And gửi email thông báo cho người tạo đơn trong vòng 5 phút
 And ghi log với thông tin: UserID, Timestamp, OrderID, Action

**AC-02 [Exception: Không đủ quyền]**
Given user đã đăng nhập với role Staff (không phải Manager)
When user cố gắng access URL /orders/{id}/approve
Then hệ thống trả về 403 Forbidden
 And hiển thị message "Bạn không có quyền thực hiện hành động này"

## ❓ Open Items (Cần Clarify Trước Khi Code)

| # | Câu hỏi | Owner | Deadline |
|---|---------|-------|---------| 
| 1 | Nếu Manager đi vắng, ai có quyền approve thay? | PO + BA | DD/MM/YY |

## 📋 Action Items

| # | Việc làm | Owner | Deadline |
|---|---------|-------|---------| 
| 1 | [...] | [...] | [...] |
```

---

## 4. Đánh Giá Tác Động — Impact Analysis Analyzer (Section 11)

Quét hệ thống và tài liệu để trả về bảng đánh giá tác động 4 chiều:
1. **Tác động Logic:** Core business flow nào bị gãy/thay đổi?
2. **Tác động Dữ liệu (DB):** Có cần thêm/xóa bảng, trường dữ liệu không? Migration data cũ ra sao?
3. **Tác động API/Tích hợp:** Các hệ thống 3rd-party hoặc Microservices khác có bị ảnh hưởng?
4. **Tác động Tài liệu:** Liệt kê các file (PRD, User Story, Test Case) cần phải cập nhật lại.

**Output mong đợi:** Bảng Markdown tóm tắt 4 khía cạnh trên kèm cảnh báo rủi ro `> [!WARNING]` nếu tác động chéo lớn.

---

## 5. Phân Tích Dữ Liệu & Tài Liệu (Section 12)

1. **Phân tích As-Is Data:** Đọc file dữ liệu để nội suy ra Data Dictionary (lược đồ dữ liệu sơ bộ).
2. **Khai phá Business Rule:** Chỉ ra các quy tắc nghiệp vụ ngầm định (VD: "Cột A luôn lớn hơn cột B").
3. **Phát hiện Anomaly:** Tìm các ngoại lệ, dữ liệu lỗi trong lịch sử để bổ sung vào Edge Cases của User Story.

---

## 6. Wireframe Dạng Text — Low-Fidelity ASCII Wireframe (Section 13)

Sử dụng Text/ASCII block để mô tả giao diện chức năng. Chỉ tập trung vào Content (thông tin cần có) và Call-to-Action (nút bấm), KHÔNG quan tâm cái đẹp.

**Ví dụ Output:**
```text
[Header: Logo công ty]             [User Profile]
-------------------------------------------------
[ Breadcrumb: Home > Đăng ký thẻ ]

* Họ và tên: [________________________] (bắt buộc)
* Số CCCD:   [________________________] (bắt buộc)
  ( ) Nam  ( ) Nữ

[ Vui lòng upload ảnh chụp mặt trước & sau CCCD ]
[          UPLOAD FILE BUTTON        ]

-------------------------------------------------
[   LƯU NHÁP   ]          [    GỬI YÊU CẦU    ]
```

---

## 7. Phân Tích Nguyên Nhân Gốc Rễ — Root Cause Analysis 5 Whys (Section 14)

> **Kích hoạt khi:** Stakeholder/User đến và yêu cầu một "Giải pháp/Tính năng" cụ thể thay vì đưa ra một "Vấn đề nghiệp vụ".

Áp dụng kỹ thuật 5 Whys (Hỏi "Tại sao" liên tục) để lột bỏ lớp vỏ giải pháp bề mặt, chạm đến vấn đề lõi. BA tuyệt đối không lập tức viết Use Case cho các yêu cầu dạng này.

**Cách Output:**
```markdown
⚠️ **Phân Tích Vấn Đề Gốc Của Yêu Cầu (Problem Framing):**

- **Yêu cầu bề mặt (Symptom/Solution):** [Khách hàng muốn X]
- **Core 5-Whys Analysis:**
  1. *Tại sao cần tính năng X?* -> [Vì sự kiện A]
  2. *Tại sao sự kiện A lại xảy ra?* -> [Vì lỗi B]
  3. *Tại sao có lỗi B?* -> [Vì data C bị lệch]
- **Root Cause thật sự (Nguyên nhân gốc):** [Vấn đề D]
  
💡 **Đề xuất của BA:** Thay vì làm [Tính năng X], phương án Rẻ + Nhanh hơn là giải quyết trực tiếp [Vấn đề D] bằng cách sửa [Code/Logic/Process Y].
```

---

## 8. Tự Động Tạo Jira Task (Section 15)

> **Kích hoạt khi:** User yêu cầu "tạo task", "đẩy lên Jira", "mở một thẻ Jira mới" hoặc sử dụng lệnh `/create-jira-task`.

**Hướng dẫn thực thi:**
1. Thu thập đủ các thông tin: **Tên dự án** (hoặc Project Key), **Tiêu đề** (Summary), **Mô tả chi tiết** (Description). Nếu có **Assignee** hoặc **Issue Type** (mặc định là Task) thì thu thập thêm.
2. Nếu User dùng từ ngữ tự nhiên cho tên dự án, hãy tự động map sang Project Key thông dụng:
   - Xăng dầu / Xăng dầu ATC -> `XDA`
   - Phần mềm bán hàng -> `PMBH`
   - Quản lý bán hàng -> `QLBH`
   - Hóa đơn điện tử -> `HDDT`
   - Tổng đài -> `QTA`
   - Công chứng -> `CC`
3. Gọi Python script bằng lệnh:
   ```powershell
   $env:PYTHONIOENCODING="utf-8"; python "F:\BA-Antigravity\.agent\scripts\jira\create_task.py" --project "[ProjectKey]" --summary "[Tiêu đề]" --description "[Mô tả]" --assignee "[Username]"
   ```
4. Đọc Output từ terminal (chứa Key và URL của Task) và báo cáo lại cho người dùng bằng giao diện thân thiện.

---

## 9. Functional Decomposition Framework (BABOK Technique #22)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — §32

### Khi nào dùng
- Ước lượng effort cho module lớn
- Xác định scope boundaries
- Input cho User Story Mapping

### Quy trình
```
1. Xác định hệ thống cấp cao nhất (Level 0)
2. Phân rã thành Modules (Level 1): 3-7 modules
3. Mỗi Module → Features (Level 2): 2-5 features per module
4. Mỗi Feature → Sub-features (Level 3): nếu cần thiết
5. Mỗi leaf = 1 potential Epic / User Story

Quy tắc:
- MECE: Mutually Exclusive, Collectively Exhaustive
- Không quá 4 cấp (sâu hơn → over-decomposition)
- Mỗi leaf phải estimatable (có thể ước lượng)
```

### Output
- Functional Decomposition Diagram (Mermaid graph TD)
- Requirements Coverage Matrix: Function → Requirement IDs

→ Nguồn: [BABOK® v3, Chapter 10 — Functional Decomposition](https://www.iiba.org/standards-and-resources/babok/)

---

## 10. SWOT Analysis Framework (BABOK Technique #46)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — §42

### Khi nào dùng
- Đánh giá chiến lược cho dự án mới
- So sánh giải pháp nghiệp vụ
- Input cho Strategy Analysis (KA4)

### Template
```
SWOT — [Tên Dự Án/Giải Pháp]

┌─ INTERNAL ─────────────────────────────────────────────┐
│ STRENGTHS (Điểm mạnh)     │ WEAKNESSES (Điểm yếu)     │
│ - [S1: ...]                │ - [W1: ...]                │
│ - [S2: ...]                │ - [W2: ...]                │
├─ EXTERNAL ─────────────────────────────────────────────┤
│ OPPORTUNITIES (Cơ hội)     │ THREATS (Rủi ro)           │
│ - [O1: ...]                │ - [T1: ...]                │
│ - [O2: ...]                │ - [T2: ...]                │
└────────────────────────────────────────────────────────┘

TOWS Strategies:
- SO (Strength-Opportunity): Tận dụng [S] để khai thác [O]
- WO (Weakness-Opportunity): Khắc phục [W] để khai thác [O]
- ST (Strength-Threat): Dùng [S] để phòng ngừa [T]
- WT (Weakness-Threat): Giảm thiểu [W] để tránh [T]
```

→ Nguồn: [SWOT Analysis — Albert Humphrey, Stanford Research Institute](https://en.wikipedia.org/wiki/SWOT_analysis)

---

## 11. Business Case / Financial Analysis Framework (BABOK Techniques #7 + #20)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — §36, §39

### Khi nào dùng
- Justify đầu tư cho dự án/feature
- So sánh Build vs Buy vs Partner
- Trình ban lãnh đạo xin budget

### Template
```markdown
## Business Case — [Tên Dự Án/Feature]

### 1. Problem Statement
[Vấn đề nghiệp vụ cần giải quyết — quantify nếu có thể]

### 2. Proposed Solution
[Giải pháp đề xuất — high-level]

### 3. Financial Analysis
| Metric | Year 1 | Year 2 | Year 3 | Total |
|--------|--------|--------|--------|-------|
| Cost (Implementation) | [X] | - | - | [X] |
| Cost (Operation/yr) | - | [Y] | [Y] | [2Y] |
| Revenue/Savings | [A] | [B] | [C] | [A+B+C] |
| **Net Benefit** | [A-X] | [B-Y] | [C-Y] | **[Total]** |

ROI = (Total Net Benefit / Total Cost) × 100% = [N]%
Payback Period = [N] months

### 4. Risk Assessment
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|

### 5. Recommendation
[GO / NO-GO / CONDITIONAL GO]
```

→ Nguồn: [BABOK® v3, Chapter 10](https://www.iiba.org/standards-and-resources/babok/)

---

## 12. Vendor Assessment Framework (BABOK Technique #49)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — §43

### Khi nào dùng
- Quyết định Build vs Buy vs Partner
- Chọn nhà cung cấp cho module cụ thể
- Đánh giá third-party integration

### Template
```markdown
## Vendor Assessment — [Tên Nhu Cầu]

### Tiêu chí đánh giá (Weighted Scoring)
| # | Tiêu chí | Weight | Vendor A | Vendor B | Build In-house |
|---|----------|--------|----------|----------|----------------|
| 1 | Functionality fit | 25% | [1-5] | [1-5] | [1-5] |
| 2 | Cost (TCO 3 years) | 20% | [1-5] | [1-5] | [1-5] |
| 3 | Integration ease | 15% | [1-5] | [1-5] | [1-5] |
| 4 | Vendor stability | 15% | [1-5] | [1-5] | [1-5] |
| 5 | Support & SLA | 10% | [1-5] | [1-5] | [1-5] |
| 6 | Customization | 10% | [1-5] | [1-5] | [1-5] |
| 7 | Security/Compliance | 5% | [1-5] | [1-5] | [1-5] |
| | **Weighted Total** | 100% | **[X.X]** | **[Y.Y]** | **[Z.Z]** |

### Decision Matrix
| Dimension | Vendor A | Vendor B | Build |
|-----------|----------|----------|-------|
| Time to market | [N weeks] | [N weeks] | [N weeks] |
| Lock-in risk | Low/Med/High | Low/Med/High | None |
| Customization | Limited/Medium/Full | ... | Full |

### Recommendation
[Vendor X / Build In-house]
Rationale: [Data-driven reasoning]
```

→ Nguồn: [BABOK® v3, Chapter 10 — Vendor Assessment](https://www.iiba.org/standards-and-resources/babok/)

