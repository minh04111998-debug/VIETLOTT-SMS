# [Tên Tính Năng] — Test Plan & Strategy

> **Mã Test Plan:** TP-[FEATURE-CODE] | **Phiên bản:** 1.0  
> **Tác giả:** Quality Assurance (QA) | **Trạng thái:** Draft / In Review / Approved  
> **Tài liệu căn cứ:** SRS-[FEATURE-CODE], BRD-[FEATURE-CODE]

---

## 1. Mục Tiêu & Phạm Vi Kiểm Thử (Objectives & Scope)
### 1.1 In-Scope
- Kiểm thử chức năng (Functional Testing)
- Kiểm thử tích hợp cổng Telco/Bank (Integration Testing)
- Kiểm thử kịch bản ngoại lệ & biên (Edge & Boundary Cases)

### 1.2 Out-of-Scope
- Stress test vượt 50,000 CCU (thực hiện ở giai đoạn sau).

---

## 2. Chiến Lược Kiểm Thử (Test Strategy & Levels)
- **Cấp độ:** Unit Test (DEV) -> Component / API Test (QA) -> E2E & UI Test (Playwright) -> UAT.
- **Rủi ro chất lượng cần tập trung (Risk-Based Testing):**
  - Mất đồng bộ số dư giữa Vietlott SMS và Cổng thanh toán.
  - Chậm trễ gửi SMS thông báo mã dự thưởng.

---

## 3. Môi Trường & Dữ Liệu Kiểm Thử (Environment & Test Data)
- **Môi trường:** Staging / Sandbox telco giả lập.
- **Dữ liệu test:** Tài khoản eKYC đã xác thực, tài khoản chưa eKYC, tài khoản hết tiền.

---

## 4. Tiêu Chí Dừng & Nghiệm Thu (Entry & Exit Criteria)
- **Điều kiện bắt đầu test:** DEV đã bàn giao code kèm kết quả Unit Test Pass 100%.
- **Điều kiện nghiệm thu:** 100% test case Critical/High đạt PASS, Zero bug Critical.
