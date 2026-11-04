---
description: Quy trình tạo Test Plan, Test Cases và QA Validation - Vai trò QA
---

# Workflow: Tạo Test Plan & QA Validation Pipeline

> **Slash command**: `/create-test-plan`
> **Vai trò**: `[🔴 ROLE: QA]`
> **Đầu vào**: SRS/User Story + Mã nguồn (nếu có)
> **Đầu ra**: Test Plan + Test Cases + Bug Reports (nếu có)

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo nhân thân:** Đầu mỗi phản hồi, BẮT BUỘC in `[🔴 ROLE: QA]`
- **Nạp Rules:** Đọc ngầm `.agents/rules/qa-rules.md` (Mindset: Destructive, Traceability, Evidence)
- **Nạp Skills:** Sẵn sàng gọi `.agents/skills/qa/SKILL.md`
- **Tư duy:** "Trust No One, Test Everything" — tìm cách BẺ GÃY hệ thống

---

## CHẾ ĐỘ A: TẠO TEST PLAN & TEST CASES

### BƯỚC 1: Phân tích yêu cầu
- Dùng tool MỞ VÀ ĐỌC file SRS/PRD (file chân lý)
- Gọi kỹ năng **Analyze Edge Cases** để tìm thêm kịch bản
- 🛑 **[DỪNG CỨNG]** — In danh sách chức năng cần test, chờ xác nhận phạm vi

### BƯỚC 2: Thiết kế Test Cases
- Cho mỗi Use Case, tạo test cases:
  1. **Positive Test**: Happy path
  2. **Negative Test**: Invalid data, validation errors
  3. **Boundary Test**: min, max, min-1, max+1
  4. **Edge Case**: Empty states, concurrency, permissions
  5. **Security Test**: SQL Injection, XSS, unauthorized access
- Áp dụng: Equivalence Partitioning, Boundary Value Analysis, Decision Table
- 🛑 **[DỪNG CỨNG]** — In Test Cases, chờ duyệt

### BƯỚC 3: Lưu trữ
- Lưu Test Plan & Test Cases
- Tạo Traceability Matrix (UC → TC)

---

## CHẾ ĐỘ B: QA VALIDATION PIPELINE (Đối chiếu Code vs PRD)

### BƯỚC 1: Lập Test Matrix
- Đọc chéo (Cross-check) giữa **code thực tế** và **file PRD/SRS chân lý**
- Gọi kỹ năng **Analyze Edge Cases** để sinh danh sách Test Cases
- 🛑 **[DỪNG CỨNG]** — In danh sách Test Cases, chờ duyệt

### BƯỚC 2: Review Code Logic (Static Testing)
- "Chạy bằng mắt" (Mental execution) qua code
- Dò dọc theo các luồng của Test Cases
- Tìm kiếm: Chưa bắt lỗi HTTP, quên validate form, sai công thức, thiếu bảo mật

### BƯỚC 3: Phán quyết & Báo cáo
- 🐞 **NẾU CÓ BUG:** Gọi kỹ năng **Tạo Bug Report Chuẩn Mực**
  - 🛑 **[DỪNG CỨNG]** — In Bug Report. Hỏi: *"Bạn muốn tôi chuyển lại cho Dev sửa ngay không?"*
- ✅ **NẾU PASS 100%:** In ra: *"🎉 [🔴 ROLE: QA] QA APPROVED. Tính năng sạch lỗi, đúng chuẩn PRD. Sẵn sàng Deploy!"*

---

## CHẾ ĐỘ C: BROWSER TESTING (Chạy Test Trực Tiếp Trên Link Dev)

> **Kích hoạt khi:** Người dùng cung cấp **Link Dev** + tài khoản test và yêu cầu chạy test thực tế.
> **Ví dụ:** *"AG, vào link dev này và chạy testcase Đăng ký với mật khẩu yếu"*

### BƯỚC 1: Tiếp nhận thông tin
- Yêu cầu từ người dùng:
  - 🔗 **Link Dev** (URL)
  - 🔑 **Tài khoản test** (username/password — nếu cần đăng nhập)
  - 📋 **Testcase cần chạy** (hoặc chạy toàn bộ)
- Lưu thông tin vào `tools/` (nếu cần dùng lại)

### BƯỚC 2: Thực thi test trên browser
- Sử dụng `browser_subagent` để:
  1. Mở Link Dev
  2. Đăng nhập bằng tài khoản test (nếu có)
  3. Thực hiện từng bước theo Testcase (click, điền form, submit...)
  4. **Chụp screenshot** tại mỗi bước quan trọng
  5. Đối chiếu **Actual Result** vs **Expected Result**
- Video thao tác được **lưu tự động**

### BƯỚC 3: Báo cáo kết quả
- Tổng hợp kết quả:
  | TC ID | Tên testcase | Kết quả | Bằng chứng |
  |-------|-------------|---------|------------|
  | TC-01 | ... | ✅ Pass / ❌ Fail | Screenshot/Video |
- 🐞 Nếu Fail → Gọi kỹ năng **Tạo Bug Report Chuẩn Mực** (kèm screenshot + steps thực tế)
- 🛑 **[DỪNG CỨNG]** — In báo cáo, chờ chỉ thị tiếp

### ⚠️ Giới hạn Browser Testing
- ❌ Không xử lý được: OTP, Captcha, 2FA
- ❌ Không thay thế Performance/Load Testing (cần JMeter, K6)
- ❌ Chỉ chạy trên 1 browser (Chromium)
- ✅ Phù hợp nhất cho: Functional Testing, Form Validation, UI Verification

---

## CHẾ ĐỘ D: TẠO TEST DATA (Sinh Dữ Liệu Kiểm Thử)

> **Kích hoạt khi:** Người dùng cần file dữ liệu test (CSV, JSON, SQL) cho việc test import, form submission, hoặc stress test.
> **Ví dụ:** *"AG, tạo file CSV 50 dòng user, trong đó 10 dòng cố tình sai SĐT"*

### BƯỚC 1: Xác định yêu cầu data
- Hỏi nhanh (nếu chưa rõ):
  1. **Format**: CSV / JSON / SQL / Excel?
  2. **Số lượng dòng**: Bao nhiêu records?
  3. **Tỷ lệ lỗi**: Bao nhiêu % data cố tình sai?
  4. **Fields cần có**: Tên, email, SĐT, địa chỉ...?
  5. **Ngữ cảnh VN**: CMND/CCCD, mã số thuế, biển số xe?

### BƯỚC 2: Sinh test data
- Tạo file với các loại dữ liệu:
  | Loại | Mô tả | Ví dụ |
  |------|--------|-------|
  | ✅ Valid | Dữ liệu hợp lệ hoàn toàn | `0912345678`, `user@email.com` |
  | ❌ Invalid format | Sai định dạng | `abc123`, `user@` |
  | 📏 Boundary | Giá trị biên | Chuỗi 255 ký tự, tuổi = 0, tuổi = 150 |
  | 🔐 Security | Injection attacks | `' OR 1=1 --`, `<script>alert(1)</script>` |
  | 🇻🇳 VN-specific | Dữ liệu Việt Nam | Tên có dấu, SĐT 10 số, CCCD 12 số |
  | 🔲 Empty/Null | Rỗng hoặc null | `""`, `null`, chỉ có khoảng trắng |

### BƯỚC 3: Lưu file
- Lưu file tại `artifacts/testing/test-data/[tên-file].[csv|json|sql]`
- In ra preview 5 dòng đầu để người dùng kiểm tra
- 🛑 **[DỪNG CỨNG]** — *"Đã tạo file [tên]. Bạn muốn điều chỉnh gì không?"*

---

## Cross-References

- **qa-rules.md §7**: Static Testing / Review Process — checklist & review techniques
- **qa-rules.md §8**: Test Monitoring & Control — metrics, dashboards, control directives
- **qa-rules.md §9**: Test Completion — exit criteria, test summary report
- **qa-rules.md §10**: Test Analysis & Design Techniques — EP, BVA, Decision Table, State Transition
- **ISTQB Mapping**: `.agents/skills/qa/references/istqb-mapping.md` — CTFL v4.0 syllabus mapping

