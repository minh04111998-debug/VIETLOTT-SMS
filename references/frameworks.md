# 📚 Shared Frameworks — Single Source of Truth

> Tài liệu này là nguồn tham chiếu duy nhất cho các frameworks dùng chung.
> **KHÔNG** lặp lại nội dung này trong bất kỳ rules/skills file nào.
> Cập nhật tại đây → áp dụng cho toàn bộ hệ thống.

---

## 1. INVEST — Tiêu Chuẩn Chất Lượng User Story

> **Nguồn:** Bill Wake, 2003 — [XP123](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)

| Chữ cái | Tiêu chí | Câu hỏi kiểm tra | Dấu hiệu vi phạm |
|---------|---------|-----------------|-----------------|
| **I** — Independent | Story không phụ thuộc vào story khác để implement | "Story này có thể được đưa vào sprint bất kỳ không?" | Phải làm A trước B, C trước D → Design issue |
| **N** — Negotiable | Chi tiết là cuộc đàm thoại, không phải hợp đồng cố định | "Team có thể đề xuất cách implement khác không?" | Story quá chi tiết về solution thay vì problem |
| **V** — Valuable | Mỗi story phải deliver value cho user hoặc business | "Nếu dừng ở story này, user có được gì không?" | "Infrastructure story" không có user outcome |
| **E** — Estimable | Team có thể ước lượng được effort | "Tại sao không estimate được?" | Quá lớn (split) hoặc quá mơ hồ (clarify) |
| **S** — Small | Hoàn thành trong 1 sprint | "Có thể split nhỏ hơn mà vẫn giữ được value không?" | > 8 story points thường là dấu hiệu cần split |
| **T** — Testable | Có acceptance criteria rõ ràng để verify | "Làm sao biết story này hoàn thành?" | Không có AC = không phải story |

**Expert insight:** INVEST vi phạm thường là triệu chứng của vấn đề sâu hơn:
- Vi phạm **I** → Kiến trúc hệ thống bị coupled (SA cần review)
- Vi phạm **V** → Product direction chưa rõ (PO cần clarify)
- Vi phạm **E** → Unknown risk, cần spike/PoC trước

---

## 2. Given / When / Then — BDD Acceptance Criteria

> **Nguồn:** Dan North, 2006 — [Behaviour-Driven Development](https://dannorth.net/introducing-bdd/)

**Cú pháp:**
```
Given [trạng thái hệ thống / context ban đầu]
  And [điều kiện bổ sung nếu cần]
When  [1 hành động duy nhất của actor]
Then  [kết quả quan sát được — không phải implementation detail]
  And [kết quả bổ sung nếu cần]
```

**Nguyên tắc expert:**

| ✅ Đúng | ❌ Sai | Tại sao |
|---------|--------|---------|
| `Then user thấy thông báo "Gửi thành công"` | `Then hệ thống lưu vào database` | Observable outcome vs implementation detail |
| 1 `When` per scenario | Nhiều `When` trong 1 scenario | Mỗi When = 1 scenario riêng |
| `Given user đã đăng nhập` | `Given user vào trang login và nhập password` | Given = state, không phải flow |

**Pattern phổ biến cần viết:**
- **Happy path:** Kịch bản chính, data hợp lệ
- **Alternative path:** User chọn hướng khác nhưng vẫn hợp lệ
- **Exception path:** Dữ liệu invalid, hệ thống lỗi, timeout
- **Edge case:** Boundary values (empty, null, max length, 0, -1, concurrent)

---

## 3. MoSCoW — Prioritization Framework

> **Nguồn:** Dai Clegg, 1994 — Oracle Method (nay là DSDM)

| Level | Nghĩa thực sự | Câu hỏi để phân loại | Expert note |
|-------|--------------|---------------------|------------|
| **Must Have** | Nếu thiếu → MVP không release được | "Release mà không có cái này thì sao?" | < 60% total scope |
| **Should Have** | Quan trọng nhưng có workaround | "Có cách khác để user đạt được mục tiêu không?" | Cắt nếu hết time |
| **Could Have** | Nice-to-have | "Ai yêu cầu điều này và tần suất?" | **Luôn bị cắt** — nếu thực sự quan trọng, nó phải là Should |
| **Won't Have** | Không làm lần này | "Có thể làm sau phiên bản này không?" | Ghi lại để không bị hỏi lại |

**Expert insight:** MoSCoW là công cụ đàm phán, không phải danh sách mong muốn. Trong thực tế: Must + Should thường chiếm hết sprint capacity → Could sẽ bị cắt. Stake holder hay "game" MoSCoW bằng cách đưa mọi thứ vào Must → PO/BA phải pushback dựa trên data.

---

## 4. RICE — Feature Prioritization Scoring

> **Nguồn:** Intercom Product Team — [RICE Scoring Model](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/)

**Công thức:**
```
RICE Score = (Reach × Impact × Confidence) / Effort
```

| Yếu tố | Định nghĩa | Thang đo |
|--------|-----------|---------|
| **Reach** | Số user bị ảnh hưởng trong 1 quý | Số thực (VD: 1000 users) |
| **Impact** | Mức độ tác động lên mỗi user | 3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal |
| **Confidence** | Mức tự tin vào các ước tính | 100%=data-backed, 80%=informed guess, 50%=gut feel |
| **Effort** | Person-weeks để hoàn thành | Số thực (VD: 2 person-weeks) |

**Expert insight:** RICE chỉ đúng khi estimates trung thực. Sanity check: "Nếu Confidence giảm từ 80% xuống 50%, thứ tự priority có thay đổi không?" Nếu có → cần thu thập thêm data trước khi quyết định.

---

## 5. Fibonacci Story Points

**Scale:** 1, 2, 3, 5, 8, 13, 20, 40, 100

| Points | Nghĩa | Ví dụ |
|--------|-------|-------|
| 1-2 | Trivial, rõ ràng, ít rủi ro | Fix typo, thay đổi màu button |
| 3-5 | Small, một số complexity | CRUD API mới, form validation |
| 8 | Medium, cần nghiên cứu | Integrate third-party API |
| 13 | Large, nhiều unknown | Refactor authentication system |
| 20+ | Quá lớn → **phải split** | Epic, không phải story |

**Nguyên tắc:** Story points đo **độ phức tạp tương đối** (relative complexity), không phải giờ công. Team phải đồng thuận về "reference story" để calibrate.

---

## 6. Conventional Commits

> **Nguồn:** [conventionalcommits.org](https://www.conventionalcommits.org/)

**Format:** `<type>(<scope>): <description>`

| Type | Khi nào dùng | Ví dụ |
|------|-------------|-------|
| `feat` | Tính năng mới | `feat(auth): add OTP verification` |
| `fix` | Sửa bug | `fix(payment): correct rounding error` |
| `docs` | Chỉ thay đổi tài liệu | `docs(api): update endpoint description` |
| `refactor` | Tái cấu trúc, không thay đổi behavior | `refactor(user): extract validation logic` |
| `test` | Thêm/sửa test | `test(auth): add edge case for expired token` |
| `chore` | Công việc maintenance | `chore(deps): upgrade express to v5` |
| `perf` | Cải thiện performance | `perf(query): add index on user_id` |
| `ci` | Thay đổi CI/CD config | `ci: add staging deploy workflow` |

**Breaking change:** Thêm `!` sau type: `feat(api)!: change response format`

---

## 7. FURPS+ — NFR Quality Model

> **Nguồn:** Robert Grady, HP (1992) — [FURPS Model](https://en.wikipedia.org/wiki/FURPS)

| Category | Mô tả | Ví dụ Metrics |
|---------|--------|--------------|
| **F** — Functionality | Feature set, Security, Capabilities | Feature coverage, Security audit pass |
| **U** — Usability | UX, Accessibility, Learnability | Onboarding time < 5 min, WCAG 2.1 AA |
| **R** — Reliability | Uptime, Recovery, Data integrity | SLA ≥ 99.5%, MTTR < 30 min |
| **P** — Performance | Speed, Throughput, Scalability | P95 < 2s, 500 req/s, 200 concurrent |
| **S** — Supportability | Maintainability, Testability, Config | Structured logging, zero-downtime deploy |

**Plus (+) Categories:**
- **Design constraints:** Platforms, standards, regulations (PCI-DSS, GDPR)
- **Implementation constraints:** Languages, tools, third-party libraries
- **Interface requirements:** External API contracts, data formats
- **Physical requirements:** Hardware, deployment environment

**Expert insight:** Mỗi NFR **PHẢI có** 3 thuộc tính:
1. **Measurable threshold** (con số cụ thể, không phải "nhanh")
2. **Measurement method** (đo bằng gì: APM, load test, audit)
3. **Priority** (Must / Should / Could)

---

## 8. Lean Canvas — Lightweight Business Model

> **Nguồn:** Ash Maurya, 2010 — [Running Lean](https://leanstack.com/lean-canvas)

```
┌────────────────┬───────────────┬─────────────────────┐
│ PROBLEM        │ SOLUTION      │ UNIQUE VALUE        │
│ Top 3 problems │ Top 3 features│ PROPOSITION         │
│                │               │ Single clear message│
├────────────────┼───────────────┤                     │
│ KEY METRICS    │ CHANNELS      │                     │
│ Key numbers    │ Path to users │                     │
├────────────────┼───────────────┼─────────────────────┤
│ COST STRUCTURE                 │ REVENUE STREAMS     │
│ Fixed + Variable costs         │ Pricing model       │
└────────────────────────────────┴─────────────────────┘
```

**Khi nào dùng:**
- PO evaluate new product idea (trước `/product-discovery`)
- Pitch feature cho stakeholder
- Build vs Buy vs Partner analysis

**Expert insight:**
- Điền "Riskiest Assumption" cuối cùng → đây là thứ cần validate TRƯỚC
- Lean Canvas không phải business plan — nó là hypothesis document
- Review và update mỗi 2-4 tuần khi có data mới
