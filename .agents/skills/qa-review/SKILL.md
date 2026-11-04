---
name: qa-review
description: Thẩm định và đánh giá output QA (Test Strategy, Test Plan, Test Matrix, Bug Report) theo chuẩn Senior ISTQB Advanced và Risk-Based Testing
---

# Kỹ Năng: QA Output Review & Senior Testing Audit

## 1. Mô Tả & Kích Hoạt
Kỹ năng dùng để thẩm định chất lượng các tài liệu và tài sản kiểm thử của QA (Test Strategy, Test Plan, Test Matrix, Test Cases, Bug Report, Quality Gate Sign-off).
- **Thời điểm kích hoạt:** Trong bước `CRITIQUE` của quy trình kiểm thử và xử lý bug (`workflows/bug-fix/`), trước khi bắt đầu giai đoạn Test Execution hoặc trước khi ký biên bản nghiệm thu phát hành (Release Readiness).
- **Tiêu chuẩn đối chiếu:** ISTQB Certified Tester Advanced Level (CTAL), Risk-Based Testing (RBT), James Bach / Michael Bolton (Exploratory Testing).

---

## 2. Bảng So Sánh Cấp Độ Đầu Ra QA

| Tiêu chí | Junior / Mid QA Output | Senior QA Output (Target) |
|---|---|---|
| **Thời điểm can thiệp** | Chờ DEV bàn giao code xong mới bắt đầu viết test và kiểm thử (Shift-Right). | Can thiệp từ sớm (Shift-Left), Static Testing review spec và bẫy lỗi ngay từ tài liệu PRD/SRS. |
| **Phân bổ tài nguyên test**| Test dàn trải hoặc chỉ tập trung bấm thử Happy Path trên giao diện UI. | Kiểm thử theo rủi ro (Risk-Based Testing): Ưu tiên 80% thời gian cho luồng rủi ro kinh doanh cao nhất. |
| **Bao phủ kịch bản** | Chỉ test đúng như AC mô tả; bỏ sót các lỗi đồng thời, rớt mạng, tràn số. | Áp dụng Error Guessing Taxonomy: Race conditions, network drop, timeout, session tamper, security injections. |
| **Chất lượng Bug Report**| Mô tả sơ sài ("Lỗi nút không bấm được"); thiếu logs, thiếu curl, thiếu payload. | Đầy đủ Reproduction steps (5 bước), Expected vs Actual, Network payload, Server logs, Mức độ nghiêm trọng chuẩn xác. |
| **Cổng kiểm soát (Gate)**| Dễ dàng thỏa hiệp bỏ qua gate kiểm thử khi PM/DEV hối thúc deadline. | Kiên quyết giữ vững Quality Gatekeeper; chỉ release khi có văn bản chấp thuận rủi ro có thẩm quyền. |

---

## 3. Senior QA Output Checklist (15 Điểm Thẩm Định)

### A. Shift-Left & Yêu Cầu Kiểm Thử Được (Static Testing & Testability)
- [ ] **QA-CHK-01 [Requirements Review Evidence]**: Có bằng chứng QA đã review tài liệu SRS/PRD của BA/PO và chỉ ra các điểm thiếu khả năng kiểm thử (Untestable requirements) trước khi dev code.
- [ ] **QA-CHK-02 [Traceability Coverage]**: 100% Functional Requirements (FR) và Non-Functional Requirements (NFR) đều có ít nhất một Test Case tương ứng (0 orphan requirements).

### B. Kiểm Thử Dựa Trên Rủi Ro (Risk-Based Testing Matrix)
- [ ] **QA-CHK-03 [Risk Categorization]**: Test Matrix phân loại rõ ràng mức độ rủi ro theo ma trận **Tác động kinh doanh (Impact) × Khả năng xảy ra lỗi (Likelihood)**.
- [ ] **QA-CHK-04 [Critical Flows Coverage]**: Các luồng tài chính cốt lõi (Nạp tiền, Đặt vé Vietlott, Trừ số dư, Khấu trừ thuế TNCN, Nhận OTP) được gán mức độ rủi ro **CRITICAL** và đạt tỷ lệ bao phủ kịch bản 100%.

### C. Phân Loại Error Guessing Chuyên Sâu (Deep Edge-Case Taxonomy)
- [ ] **QA-CHK-05 [Concurrency & Race Conditions]**: Có test case kiểm tra thao tác đồng thời (ví dụ: gửi 2 request đặt vé cùng 1 tài khoản trong cùng 1 mili-giây, hoặc 2 thiết bị đăng nhập cùng lúc).
- [ ] **QA-CHK-06 [Network & State Chaos]**: Có kịch bản kiểm tra ngắt kết nối mạng bất ngờ (Network drop), mạng trễ (High latency), gói tin bị mất giữa các bước thanh toán.
- [ ] **QA-CHK-07 [Boundary Value Analysis (BVA)]**: Kiểm tra triệt để các ranh giới: Số tiền 0đ, số tiền vượt hạn mức ngày, số điện thoại có dấu phân cách, ký tự đặc biệt XSS/SQLi.
- [ ] **QA-CHK-08 [Session & Security Tampering]**: Kiểm tra thao tác sửa đổi payload HTTP (sửa giá tiền trong request, đổi `account_id` người khác, tái sử dụng token đã hết hạn).

### D. Tự Động Hóa & Quản Trị Test Data (Automation & Regression Readiness)
- [ ] **QA-CHK-09 [Smoke Test Suite Definition]**: Định nghĩa rõ ràng bộ kiểm thử nhanh Smoke Test (thời gian chạy $\le 5$ phút trên CI/CD) để xác định bản build có đủ điều kiện test tiếp hay không.
- [ ] **QA-CHK-10 [Regression Test Suite]**: Các ca kiểm thử cốt lõi được gắn nhãn Regression và chuẩn bị cho tự động hóa (API automation qua Playwright/Postman/Pytest).
- [ ] **QA-CHK-11 [Test Data Independence]**: Bộ test data được chuẩn bị độc lập, có cơ chế dọn dẹp (cleanup/teardown) sau khi chạy, không gây ô nhiễm môi trường staging.

### E. Đo Lường Chất Lượng & Kỷ Luật Cổng Kiểm Soát (Metrics & Gatekeeping)
- [ ] **QA-CHK-12 [Bug Report Reproducibility]**: Mọi bug report đều có thể tái hiện trong $\le 5$ phút bởi DEV (có curl request, payload JSON, ảnh chụp/video bằng chứng, log server).
- [ ] **QA-CHK-13 [Defect Metrics Tracking]**: Theo dõi các chỉ số đo lường chuẩn: Tỷ lệ phát hiện lỗi nội bộ (**DDP $\ge 80\%$**) và tỷ lệ lỗi lọt ra môi trường thật (**Defect Leakage $< 5\%$**).
- [ ] **QA-CHK-14 [Rollback & Verification Plan]**: Có kế hoạch kiểm tra nhanh sau khi triển khai (Sanity Check trên Production) và kịch bản Rollback chi tiết nếu gặp sự cố.
- [ ] **QA-CHK-15 [Gate Sign-Off Integrity]**: Báo cáo kiểm thử thể hiện rõ: Số lượng test đã chạy, tỷ lệ Pass/Fail, danh sách các Known Bugs (chưa fix) kèm phân tích rủi ro và xác nhận từ Product Owner.

---

## 4. Hướng Dẫn Sửa Lỗi Nhanh Khi Bị Đánh Rớt (Actionable Fix Guide)

1. **Lỗi Test Plan chỉ toàn Happy Path:**
   - Áp dụng ma trận 5 chiều: *Happy + Alternative + Negative/Validation + Security/Tamper + Concurrency/Timeout*.
2. **Lỗi Bug Report bị DEV reject do thiếu thông tin:**
   - Bổ sung ngay: Cấu hình môi trường (OS, Browser, Device), Bước tái hiện 1-2-3, Expected vs Actual, và Server Log snippet tại thời điểm xảy ra lỗi.
3. **Lỗi không đủ thời gian test toàn bộ:**
   - Dùng nguyên tắc *Risk-Based Pruning*: Cắt giảm kiểm thử ở các khu vực rủi ro thấp (UI layout, nhãn chữ), dồn toàn lực bảo vệ các luồng tài chính và dữ liệu khách hàng.
