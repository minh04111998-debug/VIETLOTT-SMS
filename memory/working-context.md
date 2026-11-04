# Working Context (Ngữ Cảnh Làm Việc Tác Vụ Hiện Tại)

> **Mục tiêu:** Lưu giữ snapshot ngữ cảnh của tính năng đang xử lý, giúp Agent không bị mất dấu mục tiêu và không vượt quyền.

---

## 1. Thông Tin Tác Vụ Đang Kích Hoạt
- **Feature Code:** `HARNESS-RESTRUCTURE`
- **Tính năng / Sáng kiến:** Nâng cấp và cấu trúc lại toàn bộ dự án theo Harness Engineering 20 thành phần.
- **Lead Role hiện tại:** Governance / System Orchestrator
- **Downstream Role tiếp theo:** BA / PO (Bắt đầu áp dụng quy trình mới trên các tài liệu nghiệp vụ).

---

## 2. Input Artifacts Đang Sử Dụng
- `AGENTS.md` (Master Rules)
- `ARCHITECTURE.md` (System Architecture)
- `.agents/rules/core-principles.md` (Anti-sycophancy & Boundaries)

---

## 3. Trạng Thái Các Cổng Kiểm Soát (Gate Status)
- [x] Cấu trúc 20 thư mục chuẩn: **PASS**
- [x] Di chuyển toàn bộ tài sản từ 9 thư mục cũ: **PASS**
- [x] Hợp nhất `.agent`, `.agents` và `agents`: **PASS**
- [x] Hoàn thiện 8 thư mục công cụ/kiểm chứng: **PASS**
  - [x] (DEC-003-A) Validator toàn vẹn + hook gate tự động có phản hồi: **DONE**
  - [x] (DEC-003-B) AGENTS.md ≤ 120 dòng: **PASS** (máy kiểm tra)
  - [x] (DEC-003-C) Eval chạy được `evaluations/run_evals.py`: **DONE** — harness suite PASS 5/5
  - [x] (DEC-004) Hợp nhất triệt để Single Source of Truth về `.agents/`: **PASS** (Loại bỏ hoàn toàn `rules/` và `skills/` ngoài root; 16 rules và 26 skills nằm gọn trong `.agents/`; 0 FAIL, 0 WARN)
  - [x] Đường dẫn cũ trong rules/personas: **PASS** (13/13 stale paths resolved)
  - [x] Sửa lỗi project root và MAX_RETRY trong `validators/gate_runner.py` (khớp DEC-002, traceability hoạt động 100%)
  - [x] (DEC-005) Toàn diện hóa Harness (Hoàn tất 100% — Đạt Grade A):
    - [x] Giai đoạn 1: Mở rộng `validators/harness_integrity_checker.py` bao phủ toàn bộ 168 tài liệu workflows, definitions, evaluations, observability, templates (thêm check `LEGACY_PATTERNS` cấm tiệt cấu trúc cũ).
    - [x] Giai đoạn 2: Chuẩn hóa toàn bộ 213 đường dẫn tàn dư cũ (04_Document, 00_Draft, 06_Testing...) trong 62 files về `artifacts/<domain>/` và `.agents/`.
    - [x] Giai đoạn 3: Dọn dẹp Cleanliness (chuyển workspace về root, thêm README & .gitkeep cho 4 thư mục rỗng, đồng bộ `scripts/README.md`).
    - [x] Giai đoạn 4: Đóng toàn bộ 5 ca XFAIL trong `validators/` (PII markdown bold, số thẻ ngân hàng, SĐT phân nhóm, ít nhất [số], code block ambiguity) và kích hoạt suite `behavior` (10/10 PASS).

  - [x] (DEC-006) Hoàn thiện Vận hành & Cổng Kiểm soát (Operational Excellence — 100% Complete):
    - [x] Giai đoạn 1: Nâng cấp `traceability_checker.py` (hỗ trợ `FR-\d{1,4}`, `NFR-\d{1,4}`, `TC-...`, quét 27 IDs thành công, truy vết 3 chiều); bổ sung `pii_scanner.py` và `banned_words_validator.py` cho 7 vai trò trong `gate_runner.py`.
    - [x] Giai đoạn 2: Chuẩn hóa SSOT (hợp nhất `role-permission-matrix.md` với `boundaries.md`; xóa `vietlott-business-rules.md` trùng lặp trong `.agents/rules/`; cập nhật Q-005 và ASM-001 sang Answered / Đã xác minh).
    - [x] Giai đoạn 3: Đồng bộ `doc_structure_validator.py` với templates (32 lỗi cấu trúc -> 0 lỗi PASS 100%); lưu trữ 2 file `.docx` nhị phân (~500 KB) vào `scripts/archive/legacy_templates/`.
    - [x] Giai đoạn 4: Hoàn thiện Value Stream DA (thêm 4 sub-workflows chi tiết: `data-cleaning.md`, `variance-analysis.md`, `dashboard-design.md`, `weekly-reporting.md`); nạp baseline testing deliverables vào `artifacts/testing/` (`test-plan-baseline-fintech.md`, `test-cases-payment-gateway.md`); cập nhật Tech Debt Register (TD-004 đến TD-006).

  - [x] (DEC-007) Kiểm toán Chuyên sâu & Vận hành Tự trị (Audit v4 — 100% Complete — Grade A+):
    - [x] Giai đoạn 1: Nâng cấp `traceability_checker.py` (bổ sung orphan detection cho FR/NFR, liên kết 29 IDs toàn vẹn, bổ sung TC-PAY-006 & TC-PAY-007); nâng cấp `harness_integrity_checker.py` (mở rộng scan_dirs bao phủ .agents/skills và artifacts, mở rộng RE_LEGACY_PATTERNS lên 9 thư mục cũ); bổ sung regex word boundary và context whitelist cho `banned_words_validator.py` và `ambiguity_scanner.py`.
    - [x] Giai đoạn 2: Sửa sạch toàn bộ 25 stale paths và tàn dư thư mục cũ 03_Development trong skills và artifacts; khởi tạo `references/pmbok-principles.md` (chuẩn 12 nguyên tắc PMBOK 7th) và `artifacts/technical/design/design-system-spec.md`.
    - [x] Giai đoạn 3: Chuẩn hóa `tools/jira/create_task.py` nạp .env an toàn, tạo `tools/jira/.env.example`; đồng bộ `templates/adr-template.md` đủ 5 section; phân nhóm 20 scripts vào `scripts/diagrams/`, `scripts/converters/`, `scripts/extractors/` kèm backward-compatible wrappers (giải quyết TD-006).
    - [x] Giai đoạn 4: Phân rã tệp ngoại cỡ `fintech-knowledge-base.md` 40.2 KB thành 5 module chuyên biệt trong `knowledge/product/fintech/` kèm Master Index Gateway (giải quyết triệt để TD-004, tiết kiệm 80% Token Budget cho tác vụ chuyên sâu); cập nhật sổ quyết định DEC-007 và sổ nợ kỹ thuật.
    - [x] Giai đoạn 5: Chuẩn hóa toàn bộ rào chắn Quality Gate & Validators:
      - Xử lý sạch 14 vị trí từ cấm/mơ hồ trong `artifacts/product/bao-cao-san-pham-vietlott.md` → Đạt `PASS` cổng PO Quality Gate.
      - Tinh chỉnh regex CCCD trong `validators/pii_scanner.py` nhận diện chính xác tiền tố mã tỉnh `001-096` → Triệt tiêu false-positives trên số liệu doanh thu 12 chữ số VNĐ.
      - Bổ sung cấu hình UTF-8 cho `tools/telegram/tele_notify.py` và `tele_gateway.py` tránh UnicodeEncodeError trên Windows. *(DEC-008: `tele_gateway.py` đã gỡ bỏ — Telegram chỉ còn notify.)*
  - [x] (DEC-008) Tái cấu trúc 7 AI Harnesses & Loại bỏ Cổng Duyệt Telegram (100% Hoàn tất):
    - [x] Phase 0: Backup an toàn `scratch/VIETLOTT-SMS-pre-DEC-008.zip` (440 files, 5.84 MB), bổ sung `.gitignore` gốc chống lộ secret.
    - [x] P1 Security: Gỡ bỏ `tools/telegram/tele_gateway.py` và tệp tạm kết quả; chuyển Telegram sang notify-only (`tele_notify.py`); triển khai `validators/secret_scanner.py` (quét 7 loại token/key), mở rộng 7 test cases regression SEC-01..07; tích hợp vào `gate_runner.py`, `agent_gate_hook.py`, `run_evals.py`; bổ sung OWASP LLM Top 10 vào `security-checklist.md`.
    - [x] P2 Tooling & AgentOps: Thiết lập `.agents/definitions/harness-map.json` ánh xạ toàn bộ 14 thư mục root + `.agents/` vào 7 AI Harnesses; nâng cấp `harness_integrity_checker.py` kiểm tra harness-map và context size (cảnh báo >15KB); phân loại `tools/tool-registry.md` theo 3 cấp độ rủi ro, phân quyền vai trò và gắn cờ Hard Stop; sửa đường dẫn cũ trong `workflows/requirement/create-jira-task.md`; xây dựng `validators/ops_metrics.py` đo lường AgentOps và xuất báo cáo `observability/metrics/2026-W41.md`.
    - [x] P3 Evaluation, Orchestration & Handoff: Thiết lập khung Golden Dataset `evaluations/golden/` (README, rubric 5 tiêu chí, manifest.json); tích hợp suite `golden` vào `evaluations/run_evals.py`; chuẩn hóa `handoff-contracts.md` (diagram luồng & đồng bộ định danh); cập nhật `ARCHITECTURE.md`, `README.md`, `.agents/README.md`, `decisions-log.md`, `open-questions.md`.
    - [x] P4 Senior Output Audit Skills: Đóng gói 4 bộ kỹ năng thẩm định Senior Output: `.agents/skills/ba-review/`, `.agents/skills/po-review/`, `.agents/skills/qa-review/`, `.agents/skills/da-review/` (tổng 30 skills trong hệ thống SSOT); cập nhật dispatch table cho 4 role.

> **Kiểm tra trạng thái hệ thống toàn diện:**
> - `python evaluations/run_evals.py` — **45/45 checks PASS (100% Green), 1 suite NOT_RUN (golden manifest)**.
> - `python validators/harness_integrity_checker.py` — **0 FAIL, 0 WARN trên toàn bộ 273 tài liệu (30 skills, harness-map & context size đạt chuẩn)**.
> - `python validators/secret_scanner.py` — **PASS: 0 secret rò rỉ (7 loại pattern kiểm soát)**.
> - `python validators/traceability_checker.py` — **29 IDs tìm thấy (17 FR, 4 NFR, 8 TC), 0 orphan, 0 warning, 100% yêu cầu có test coverage**.
> - `python validators/doc_structure_validator.py --dir artifacts` — **100% Valid Document Structures (0 lỗi)**.
> - `python validators/pii_scanner.py` — **PASS: 0 dữ liệu nhạy cảm chưa che**.
> - `python validators/gate_runner.py` — **PASS 100% trên cả 7 vai trò chính**.


