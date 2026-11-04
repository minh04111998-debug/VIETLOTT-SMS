# Harness Regression Evals

> **Câu hỏi bộ eval này trả lời:** sửa rules / skills / workflows / validators xong, harness **tốt lên hay tệ đi**?
> **Chạy:** `python evaluations/run_evals.py` (thêm `--quiet` để chỉ xem dòng không PASS)

---

## 1. Ba Suite

| Suite | Kiểm tra gì | Mức tự động | Bản gốc case |
|---|---|---|---|
| `harness` | Hard link `rules/` ↔ `.agents/rules/`, junction `skills/<role>/` → `.agents/skills/`, `.agents/hooks.json`, AGENTS.md ≤ 120 dòng & đường dẫn sống, đường dẫn chết trong rules/personas | 100% | `validators/harness_integrity_checker.py` |
| `validators` | Golden cases: PII, từ cấm, mơ hồ phải bắt đúng / không bắt nhầm | 100% | [`validator_cases.py`](validator_cases.py) |
| `behavior` | Hành vi agent: chống xu nịnh, Ask Don't Assume, Red Flag, Deadlock, định tuyến role, phản biện QA, Gate Report DEV | Bán tự động (regex chấm, người chạy prompt) | [`behavior-cases.json`](behavior-cases.json) |

## 2. Trạng Thái Kết Quả

| Trạng thái | Ý nghĩa | Làm gì |
|---|---|---|
| `PASS` | Đạt | — |
| `FAIL` | Hồi quy / vi phạm | Sửa trước khi merge thay đổi harness (exit code 1) |
| `WARN` | Rủi ro, chưa chặn | Lên kế hoạch dọn |
| `XFAIL` | **Lỗ hổng đã biết** của validator, có ghi lý do | Ưu tiên sửa validator; case vẫn chạy mỗi lần |
| `XPASS` | Case `xfail` bỗng PASS → lỗ hổng đã được sửa | Gỡ trường `xfail` khỏi case |
| `NOT_RUN` | Case hành vi chưa có câu trả lời | Chạy prompt (mục 3) |

## 3. Chạy Suite `behavior`

Agent không gọi được từ script, nên quy trình là:

1. `python evaluations/run_evals.py --list-prompts` → lấy prompt.
2. Mỗi prompt: mở **conversation mới hoàn toàn** (không có ngữ cảnh cũ), dán nguyên văn.
3. Lưu toàn bộ câu trả lời vào `evaluations/regression/responses/<ID>.md` (vd `BEH-01.md`). **Mask PII nếu có.**
4. `python evaluations/run_evals.py --suite behavior` → regex chấm `auto_checks`; dòng PASS liệt kê `manual_checks` cần người xác nhận.

> [!IMPORTANT]
> `auto_checks` là **tín hiệu thô** (vd có `[!CAUTION]` không), không chứng minh câu trả lời đúng. Case chỉ được coi là đạt khi `auto_checks` PASS **và** người chấm xác nhận `manual_checks`.

## 4. So Sánh Trước / Sau

Mỗi lần chạy (trừ khi `--no-history`) runner ghi 1 dòng vào `results/history.jsonl` với số lượng PASS/FAIL/XFAIL... của từng suite. Quy trình khuyến nghị khi sửa harness:

1. Chạy eval **trước** khi sửa → ghi baseline.
2. Sửa rules / skills / workflows / validators.
3. Chạy lại → so 2 dòng cuối của `history.jsonl`. Số `FAIL` tăng hoặc `PASS` giảm = hồi quy.

## 5. Thêm Case Mới

- **Validator:** thêm dict vào `CASES` trong `validator_cases.py`. PII **phải ghép chuỗi lúc chạy** (xem `_PHONE`), không ghi PII hoàn chỉnh vào file.
- **Hành vi:** thêm object vào `cases` trong `behavior-cases.json`; `id` giữ ổn định để so lịch sử.
- Mỗi lỗi agent/validator bắt gặp ngoài thực tế → thêm 1 case tái hiện trước khi sửa.

## 6. Nguồn Gốc

`behavior-cases.json` gộp từ `regression-cases.md` (REG-01..03) và `smoke-test-scenarios.md` (Test 1..7) cũ — 2 file markdown đó đã được thay thế để chỉ còn **một bản gốc** (trường `source` trong mỗi case ghi mã cũ). REG-03 trước đây chỉ có mô tả kịch bản, chưa có prompt → prompt của `BEH-03` là bản mới soạn, cần Human rà lại.
