# Automated Validators — Vietlott SMS Quality Gates

> **Mục tiêu:** Cung cấp bộ công cụ dòng lệnh (CLI Validators) tự động cưỡng chế chất lượng tài liệu, tính truy vết, cấu trúc chuẩn, và bảo mật thông tin trước khi chuyển sang Baseline.

---

## 1. Danh Mục Validators Khả Dụng

| Validator | Script | Mục đích kiểm tra | Exit Code |
|---|---|---|:---:|
| **Ambiguity Scanner** | `ambiguity_scanner.py` | Quét từ ngữ mơ hồ định tính, thiếu số liệu định lượng | 0: Pass, 1: Fail |
| **Banned Words Validator**| `banned_words_validator.py` | Kiểm tra từ cấm theo `.agents/rules/banned-words.md` | 0: Pass, 1: Fail |
| **PII Scanner** | `pii_scanner.py` | Phát hiện số điện thoại, CCCD, OTP chưa được masked | 0: Pass, 1: Fail |
| **Doc Structure Validator**| `doc_structure_validator.py` | Kiểm tra tài liệu có đủ các section bắt buộc theo template | 0: Pass, 1: Fail |
| **Traceability Checker** | `traceability_checker.py` | Kiểm tra ma trận truy vết giữa BR, FR, UC, TC | 0: Pass, 1: Fail |
| **Quality Gate Runner** | `gate_runner.py` | Điều phối tổng thể các validator theo từng vai trò | 0: Pass, 1: Fail |
| **Harness Integrity Checker** | `harness_integrity_checker.py` | Toàn vẹn khung harness: hard link `rules/`↔`.agents/rules/`, junction `skills/<role>/`→`.agents/skills/`, `.agents/hooks.json`, AGENTS.md ≤ 120 dòng, đường dẫn chết | 0: Pass, 1: Fail |

> Validator được kiểm thử bằng golden cases tại `evaluations/regression/validator_cases.py` — chạy `python evaluations/run_evals.py --suite validators`. Lỗ hổng đã biết được đánh dấu `XFAIL`.

---

## 2. Hướng Dẫn Chạy Kiểm Tra

### Quét một file cụ thể:
```bash
python validators/pii_scanner.py --file "artifacts/requirements/srs-campaign-tang-ve-bank.md"
python validators/banned_words_validator.py --file "artifacts/requirements/srs-campaign-tang-ve-bank.md"
python validators/ambiguity_scanner.py --file "artifacts/requirements/srs-campaign-tang-ve-bank.md"
```

### Quét toàn bộ thư mục artifacts:
```bash
python validators/pii_scanner.py --dir "artifacts"
python validators/banned_words_validator.py --dir "artifacts"
```
