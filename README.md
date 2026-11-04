# Vietlott SMS — Multi-Agent Harness Engineering System

> **Hệ Thống Đa Vai Trò Tự Trị Cho Kỹ Thuật Phần Mềm & Phát Triển Sản Phẩm**  
> **Kiến trúc:** 20-Node Harness Engineering + 6 Value Stream Workflows + 7 Personas  
> **Ngôn ngữ giao tiếp:** Tiếng Việt (Thuật ngữ chuyên ngành Tiếng Anh)

---

## 🚀 Giới Thiệu Nhanh

Hệ thống được thiết kế theo chuẩn **Harness Engineering** tiên tiến, biến LLM từ một công cụ chat thông thường thành một đội ngũ phát triển phần mềm chuyên nghiệp (PO, PM, BA, DA, DEV, QA, Governance). Mọi hoạt động đều có ranh giới rõ ràng, kiểm soát chất lượng qua Quality Gate, và tuyệt đối bảo vệ quyền quyết định của con người (Human-in-the-Loop).

---

## 📂 Sơ Đồ Cấu Trúc Thư Mục & 7 AI Harnesses (DEC-008)

```text
multi-agent-engineering/
├── AGENTS.md               # Master rules & quy định vận hành chính (<= 120 dòng)
├── ARCHITECTURE.md         # Bản thiết kế kiến trúc toàn hệ thống
├── README.md               # Tài liệu hướng dẫn sử dụng (File này)
│
├── .agents/                # Unified Hub: Personas, Definitions, 26 Skills & 15 Flat Rules
│   ├── personas/           # pm, po, ba, da, dev, qa, designer, governance
│   ├── definitions/        # schemas, handoff contracts, permission matrix, harness-map.json
│   ├── skills/             # 26 Kỹ năng thực tế chuẩn hóa kebab-case (IDE auto-discovery)
│   └── rules/              # 15 Bộ quy tắc phẳng cấp 1 cho IDE Auto-load
│
├── workflows/              # 6 Luồng giá trị end-to-end (Orchestration Harness)
│   ├── product-discovery/  # PO: Khám phá nhu cầu, PRD
│   ├── requirement/        # BA: SRS, BRD, Change Request, Impact Analysis
│   ├── feature-development/# DEV: Kiến trúc, lập trình, review, refactor
│   ├── bug-fix/            # QA: Triage, Test Plan, Playwright, Regression
│   ├── data-analysis/      # DA: Trích xuất dữ liệu, variance, báo cáo
│   └── release/            # PM: Readiness, release planning, sign-off
│
├── knowledge/              # Tri thức tĩnh và quy tắc nghiệp vụ dự án (Context Harness, <= 15 KB/file)
│   ├── product/ | domain/ | business-rules/ | glossary/ | architecture/ | standards/
│
├── artifacts/              # Kết quả bàn giao chính thức
│   ├── product/ | requirements/ | analysis/ | technical/ | testing/ | decisions/
│
├── plans/                  # Kế hoạch và quản lý nợ kỹ thuật
│   ├── active/ | completed/ | tech-debt/
│
├── evaluations/            # Đánh giá hiệu năng và kiểm thử hồi quy 4 tầng (Evaluation Harness)
│   ├── agents/ | skills/ | workflows/ | regression/ | golden/
│
├── hooks/                  # Lifecycle hooks (agent_gate_hook.py tự động kiểm tra PII/Secret/Từ cấm)
├── validators/             # Scripts tự động kiểm tra chất lượng & AgentOps metrics
├── tools/                  # Tích hợp công cụ ngoài (Jira, Telegram notify, Confluence)
├── templates/              # Biểu mẫu chuẩn (Golden Templates)
├── references/             # Khung tham chiếu chuẩn (BABOK, CPOA, ISTQB, OWASP)
├── scripts/                # Scripts tiện ích & tự động hóa (diagrams, converters, extractors)
├── memory/                 # Bộ nhớ ngữ cảnh tác vụ (Scratchpad, Project state)
└── observability/          # Hệ thống giám sát (Assumptions, Questions, Decisions, Metrics)
    ├── assumptions-log.md
    ├── open-questions.md
    ├── decisions-log.md
    ├── critique-conflicts/
    ├── gate-reports/
    └── metrics/
```

---

## 🛠️ Hướng Dẫn Sử Dụng (Quick Start)

### 1. Kích Hoạt Nhanh Một Vai Trò (Quick-Load Role)
Gõ lệnh nạp vai trò để AI tự động cấu hình mindset, quy tắc và ranh giới tương ứng:
```text
Nạp role PO         # Bắt đầu khám phá sản phẩm, định nghĩa outcome
Nạp role BA         # Phân tích nghiệp vụ, mô hình hóa luồng, viết SRS
Nạp role DEV        # Thiết kế kỹ thuật, lập trình, code review
Nạp role QA         # Lập kế hoạch kiểm thử, thiết kế test cases
Nạp role DA         # Phân tích dữ liệu doanh thu, tìm kiếm insight
Nạp role PM         # Lập kế hoạch sprint, quản lý tiến độ, release
Nạp role Governance # Kiểm tra tuân thủ ranh giới, bảo mật PII, pháp lý
```

### 2. Kích Hoạt Luồng Giá Trị Bằng Slash Commands (Detailed Mode)
```text
/po discovery       # PO: Khám phá nhu cầu khách hàng & thị trường
/po create-prd      # PO: Soạn thảo PRD chuẩn
/ba srs             # BA: Xây dựng SRS hoàn chỉnh qua Loop 6 bước
/ba impact          # BA: Phân tích tác động thay đổi (Impact Analysis)
/ba change          # BA: Xử lý Change Request theo chuẩn Cascading
/da report          # DA: Lập báo cáo phân tích số liệu kinh doanh
/dev review         # DEV: Thực hiện Code Review chuyên sâu
/qa test-plan       # QA: Thiết kế Test Plan và ma trận truy vết
```

---

## 🔒 Cơ Chế An Toàn Cốt Lõi (Safety & Human Control)

1. **🛑 Hard Stop Tại Ranh Giới Quyết Định:** Mọi quyết định về cắt scope, phê duyệt NFR, hoặc chuyển giao tài liệu sang baseline (`artifacts/`) đều bắt buộc phải có sự xác nhận của Human.
2. **2 Vòng Sửa Tối Đa:** Nếu bước CRITIQUE thất bại > 2 lần, hệ thống tự động khóa và chuyển sang báo cáo bế tắc (`observability/critique-conflicts/`).
3. **Anti-Sycophancy (Chống Xu Nịnh):** AI là đối tác phản biện; luôn quét edge cases và cảnh báo rủi ro đỏ (`> [!CAUTION]`).
