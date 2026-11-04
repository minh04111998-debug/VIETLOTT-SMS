# [Tên Tính Năng] — System Requirement Specification (SRS)

> **Mã SRS:** SRS-[FEATURE-CODE] | **Phiên bản:** 1.0  
> **Tác giả:** Business Analyst (BA) | **Trạng thái:** Draft / In Review / Baseline  
> **Nguồn liên đới:** PRD-[FEATURE-CODE], BR-[CODE]

---

## 1. Giới Thiệu & Mục Đích (Introduction)
- **Mục tiêu:** Đặc tả chi tiết hành vi hệ thống cho tính năng...
- **Phạm vi áp dụng:** Web, Mobile App (Android/iOS), Backend API, Đối tác Telco/Bank.

---

## 2. Danh Mục Yêu Cầu Chức Năng (Functional Requirements)

### FR-001: [Tên Yêu Cầu Chức Năng]
- **Tác nhân (Actor):** Khách hàng / Quản trị viên / Hệ thống.
- **Tiền điều kiện (Pre-conditions):** Đã đăng nhập, số dư khả dụng >= ...
- **Luồng sự kiện chính (Main Flow):**
  1. Người dùng bấm chọn...
  2. Hệ thống kiểm tra điều kiện...
  3. Hệ thống trả về kết quả...
- **Luồng ngoại lệ & lỗi (Exceptions & Errors):**
  - *EX-01 (Timeout Telco):* Hệ thống retry tối đa 3 lần sau đó chuyển sang trạng thái chờ xử lý...
  - *EX-02 (Không đủ số dư):* Thông báo người dùng nạp tiền qua kênh liên kết...
- **Hậu điều kiện (Post-conditions):** Trạng thái vé được lưu trữ an toàn...

---

## 3. Tiêu Chí Nghiệm Thu (Acceptance Criteria — Given-When-Then)
```gherkin
Scenario: Khách hàng mua vé thành công
  Given Khách hàng đã hoàn thành eKYC và có số dư TKDT >= 10,000 VND
  When Khách hàng chọn bộ số Mega 6/45 và bấm "Thanh Toán"
  Then Hệ thống trừ tiền 10,000 VND từ TKDT
  And Hệ thống sinh mã vé và gửi tin nhắn SMS xác nhận tới số điện thoại của khách hàng
```

---

## 4. Yêu Cầu Phi Chức Năng (Non-Functional Requirements — NFR)
- **Hiệu năng:** Thời gian phản hồi API <= 500ms tại p95.
- **Bảo mật:** Tuân thủ mã hóa dữ liệu đường truyền TLS 1.3 và lưu trữ AES-256.
- **Tính sẵn sàng:** 99.9% uptime trong khung giờ quay thưởng (18h00 - 18h30 hàng ngày).

---

## 5. Ma Trận Truy Vết (Traceability Matrix)
| User Story / FR | Business Rule ID | Use Case ID | Test Case ID |
|---|---|---|---|
| FR-001 | BR-PAY-01 | UC-01 | TC-BUY-001 |
