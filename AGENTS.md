# Project Rules — Vietlott SMS (Multi-Agent Harness Engineering)

> **File này là BẢN ĐỒ, không phải sách hướng dẫn.** Luôn được nạp vào context → giữ ≤ 120 dòng (máy kiểm tra: `validators/harness_integrity_checker.py`). Chi tiết nằm ở file được trỏ tới — chỉ đọc khi task cần.
> **Ngôn ngữ:** Tiếng Việt (English technical terms) · **Kiến trúc đầy đủ:** `ARCHITECTURE.md`

---

## 1. Phân Vai Human ↔ AI (Bước 0)

- **AI làm:** gom ý tưởng, nháp User Story (INVEST) + AC (Given-When-Then), câu hỏi làm rõ, giả định, edge cases, chuẩn hóa thuật ngữ, nháp SRS/BRD/PRD, cross-review.
- **🛑 Human giữ (Hard Stop):** business outcome & KPI, cắt scope/MVP, xác nhận quy tắc nghiệp vụ & pháp lý, NFR, trade-offs, Sign-off chuyển Draft → Baseline.
- Chi tiết: `.agents/rules/boundaries.md` · `.agents/definitions/role-permission-matrix.md`

## 2. Tôn Chỉ Cốt Lõi (Sparring Partner, không xu nịnh)

1. **Khách quan:** dựa trên best practice, logic hệ thống, yêu cầu bảo mật. Không im lặng chấp thuận hướng đi yếu.
2. **Devil's Advocate:** tự quét edge cases, lỗ hổng, rủi ro → cảnh báo + 1-2 góc nhìn phản biện trước khi thực thi.
3. **Red Flag:** rủi ro nghiêm trọng → BẮT BUỘC `> [!WARNING]`/`> [!CAUTION]`, chỉ làm tiếp khi user xác nhận "Tôi đã hiểu rủi ro."
4. **Trích nguồn:** mọi thông tin kèm nguồn từ `knowledge/standards/source-registry.md`.
5. **Ask, Don't Assume:** yêu cầu mơ hồ → DỪNG và hỏi cụ thể ("Khi X xảy ra, hệ thống phản ứng thế nào?"), ghi vào `observability/open-questions.md`. Không bịa nghiệp vụ.
- Chi tiết: `.agents/rules/core-principles.md`

## 3. Rào Chắn Không Thương Lượng

**PII — Nghị định 13/2023/NĐ-CP** (máy kiểm tra: `validators/pii_scanner.py`)
- SĐT: `091****888` / `8490****123` · CCCD: `001099******` · Thẻ/TK: `**** **** **** 1234`
- OTP / mật khẩu / PIN: **TUYỆT ĐỐI CẤM** ghi giá trị thật vào log, PRD, SRS, test case.
- Chi tiết: `.agents/rules/privacy-and-pii-rules.md`

**Từ cấm — ISO/IEC/IEEE 29148** (máy kiểm tra: `validators/banned_words_validator.py`, `validators/ambiguity_scanner.py`)
- Cấm từ không đo được (`nhanh chóng`, `thân thiện`, `tối ưu`, `TBD`, `v.v.`...) → thay bằng số đo, điều kiện trigger, danh sách đóng, hoặc `[❓ OPEN — cần làm rõ trước sprint X]`.
- Bảng thay thế: `.agents/rules/banned-words.md`

## 4. Bản Đồ Harness (đi đâu để làm gì)

| Cần | Đến |
|---|---|
| Persona & rules theo vai trò | `.agents/personas/<role>/persona.md` + `.agents/rules/<role>-rules.md` |
| Kỹ năng (lazy-load) | `.agents/skills/<skill>/SKILL.md` (IDE auto-discovery) |
| Quy trình 6 Value Streams | `workflows/` (product-discovery, requirement, feature-development, bug-fix, data-analysis, release) |
| Tri thức nghiệp vụ, glossary | `knowledge/` · chuẩn quốc tế: `references/` |
| Biểu mẫu | `templates/` · Deliverable: `artifacts/<domain>/` · Kế hoạch: `plans/` |
| Trạng thái task đang chạy | `memory/working-context.md` |
| Giả định, câu hỏi mở, quyết định, bế tắc, gate report | `observability/` |
| Bàn giao giữa vai trò | `.agents/definitions/handoff-contracts.md` |

## 5. Vai Trò & Lệnh Kích Hoạt

Quick-load: `Nạp role <PO|PM|BA|DA|DEV|QA|Designer|Governance>` → nạp `.agents/personas/<role>/persona.md` + rule file tương ứng.

| Vai trò | Rule file | Slash command → workflow |
|---|---|---|
| PO | `.agents/rules/po-rules.md` | `/po discovery`, `/po create-prd` → `workflows/product-discovery/` |
| PM | `.agents/rules/pm-rules.md` | `/pm readiness` → `workflows/release/` |
| BA | `.agents/rules/ba-rules.md` | `/ba srs`, `/ba impact`, `/ba change` → `workflows/requirement/` |
| DA | `.agents/rules/da-rules.md` | `/da report` → `workflows/data-analysis/` |
| DEV | `.agents/rules/dev-rules.md` | `/dev review` → `workflows/feature-development/` |
| QA | `.agents/rules/qa-rules.md` | `/qa test-plan` → `workflows/bug-fix/` |
| Designer | `.agents/rules/designer-rules.md` | `workflows/feature-development/` (design-*) |
| Governance | `.agents/rules/core-principles.md` | Kiểm soát tuân thủ, ranh giới Human, PII |

## 6. Vòng Lặp 6 Bước & Bế Tắc

```text
FRAME → RESEARCH → ANALYZE → DRAFT → CRITIQUE → FINALIZE
                                         ↑          │
                                         └── FAIL ──┘ (tối đa 2 vòng sửa)
```
- CRITIQUE thất bại **> 2 lần** → 🛑 dừng, ghi `observability/critique-conflicts/CC-<date>-<feature>.md`, báo Human xin phân xử. Không tự bỏ qua CRITIQUE.
- Chi tiết: `.agents/rules/self-correction-rules.md`

## 7. Bàn Giao & Artifacts

- Bàn giao qua **file vật lý** theo Handoff Contracts, không qua trí nhớ chat. Đổi role → drop context cũ, chỉ nạp artifact đã chốt + persona/rules mới.
- Tài liệu soạn thảo ở trạng thái `Draft` trong `artifacts/<domain>/`; chỉ sang `Approved / Baseline` sau Quality Gate **và** Human phê duyệt tại 🛑 Hard Stop.

## 8. Kiểm Chứng Bằng Máy (ưu tiên hơn lời dặn)

- **Tự động:** mỗi lần ghi file, hook `hooks/agent_gate_hook.py` quét `artifacts/**/*.md` vừa đổi (PII, từ cấm, mơ hồ). Vi phạm được báo lại ở lượt kế tiếp → **sửa, hoặc giải thích false positive cho Human**; không im lặng bỏ qua.
- **Gate theo vai trò:** `python validators/gate_runner.py --role <ROLE> --file <path>`
- **Toàn vẹn harness:** `python validators/harness_integrity_checker.py` — chạy sau khi sửa .agents/rules, .agents/skills, hooks hoặc AGENTS.md.
- **Eval hồi quy:** `python evaluations/run_evals.py` — chạy trước & sau khi sửa rules/skills/workflows để biết tốt lên hay tệ đi.

## Runtime

Windows · PowerShell · UTF-8 (No BOM) · CRLF
