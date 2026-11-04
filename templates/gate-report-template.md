# Quality Gate Report — [Artifact Name]

> **Mã báo cáo:** QGR-[YYYYMMDD]-[ROLE]-[FEATURE]  
> **Thời điểm thực thi:** YYYY-MM-DD HH:MM:SS  
> **Role thực thi:** [PO / BA / DEV / QA / DA / Governance]  
> **Trạng thái cổng:** **[PASS / FAIL / BLOCKED]**

---

## 1. Thông Tin Kiểm Tra (Inspection Meta)
- **Tài liệu kiểm tra:** `artifacts/...`
- **Phiên bản tài liệu:** 1.0
- **Checklist áp dụng:** `evaluations/skills/...-checklist.md`
- **Validators tự động đã chạy:** `validators/ambiguity_scanner.py`, `validators/traceability_checker.py`

---

## 2. Kết Quả Kiểm Tra Tự Động (Automated Validation Results)
| Tiêu chí | Tool thực thi | Trạng thái | Chi tiết phát hiện |
|---|---|:---:|---|
| Quét từ mơ hồ (Ambiguity Scan) | `ambiguity_scanner.py` | PASS / FAIL | Phát hiện X từ cấm... |
| Tính truy vết (Traceability) | `traceability_checker.py` | PASS / FAIL | 100% FR có gắn BR và UC... |
| Cấu trúc tài liệu (Structure) | `doc_structure_validator.py` | PASS / FAIL | Đủ các mục bắt buộc... |

---

## 3. Kết Quả Rà Soát Tiêu Chí Thủ Công (Checklist Review)
| # | Tiêu chí nghiệm thu | Mức độ | Kết quả (PASS/FAIL/NA) | Ghi chú / Dẫn chứng |
|---|---|:---:|:---:|---|
| 1 | Nguồn gốc nghiệp vụ rõ ràng | Blocking | PASS | Trích dẫn BR-01 |
| 2 | Kịch bản ngoại lệ đầy đủ | Blocking | PASS | Có luồng Timeout |
| 3 | Không tự gán NFR của Human | Blocking | PASS | Đúng thẩm quyền |

---

## 4. Kết Luận & Quyết Định
- [ ] **ĐẠT (PASS):** Cho phép chuyển sang bước tiếp theo hoặc bàn giao cho downstream role.
- [ ] **KHÔNG ĐẠT (FAIL):** Kích hoạt vòng lặp Self-Correction (Lần 1 / Lần 2).
- [ ] **BẾ TẮC (BLOCKED):** Chuyển sang Deadlock Escalation lên Human.
