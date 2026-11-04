# SYSTEM REQUIREMENT SPECIFICATION (SRS)
**Dự án:** Hệ Sinh Thái Thanh Toán & Tài Chính Số (Fintech Payment Ecosystem)
**Phiên bản:** v1.0

---

## 1. INTRODUCTION (GIỚI THIỆU)
### 1.1 Purpose (Mục đích)
Tài liệu này đặc tả các yêu cầu hệ thống (System Requirements) cho việc xây dựng và phát triển Hệ sinh thái thanh toán và tài chính số trên Super App. Tài liệu phục vụ cho đội ngũ Phát triển (Dev), Kiểm thử (QA), và các bên liên quan (Stakeholders) nắm rõ luồng nghiệp vụ, kịch bản người dùng và các xử lý ngoại lệ.

### 1.2 Scope (Phạm vi dự án)
Phạm vi của hệ thống bao gồm:
* **Core Payment:** Đối soát, Hoàn tiền, Thu/Chi hộ, Tra soát.
* **User-facing Features:** Chuyển tiền, QR Payment, Thanh toán hóa đơn, Split Bill, Cashback.
* **Extended Fintech Domains:** eKYC, Digital Lending (Tín dụng số), Digital Savings (Tiết kiệm số), Security & AML.

### 1.3 Definitions, Acronyms, and Abbreviations (Định nghĩa & Viết tắt)
* **SRS:** System Requirement Specification
* **eKYC:** Electronic Know Your Customer
* **PG:** Payment Gateway (Cổng thanh toán)
* **AML:** Anti-Money Laundering (Chống rửa tiền)
* **MFA:** Multi-Factor Authentication

---

## 2. OVERALL DESCRIPTION (MÔ TẢ TỔNG QUAN)
### 2.1 Product Perspective (Góc nhìn sản phẩm)
Hệ thống là một Module độc lập (Microservice) tích hợp trực tiếp vào Super App hiện tại, giao tiếp với Core Banking và các đối tác thứ 3 (Napas, EVN, Telcos) thông qua Open API.

### 2.2 User Classes and Characteristics (Phân loại người dùng)
* **End-User (Khách hàng cá nhân):** Thực hiện giao dịch tài chính, yêu cầu thao tác hoàn tất trong 3 bước và xác thực sinh trắc học theo Quyết định 2345/QĐ-NHNN.
* **Merchant (Đối tác bán hàng):** Nhận thanh toán, cần báo cáo đối soát real-time.
* **Admin / Operation Team:** Nhân sự vận hành, kế toán, CSKH. Cần công cụ quản lý tra soát, đối soát và AML.

### 2.3 Operating Environment (Môi trường vận hành)
* Client: iOS 12.0+, Android 8.0+
* Backend: Microservices Architecture (Java/Go/NodeJS)
* Database: Oracle / PostgreSQL

---

## 3. SYSTEM FEATURES (TÍNH NĂNG HỆ THỐNG - FUNCTIONAL REQUIREMENTS)

### 3.1. Phân hệ Core Payment (Nghiệp vụ lõi)
*(Sử dụng lại các Sequence Diagram và Bảng mô tả từ tài liệu nghiệp vụ)*

#### 3.1.1 Yêu cầu Đối soát (Reconciliation)
* **FR-01:** Hệ thống tự động fetch file settlement từ đối tác vào 23:59 (T+1).
* **FR-02:** Chạy thuật toán Matching tự động (Theo Mã GD, Số tiền, Trạng thái).
* **FR-03:** Xuất báo cáo danh sách giao dịch lệch (Mismatched) cho Operation Team xử lý thủ công.

#### 3.1.2 Yêu cầu Hoàn tiền (Refund)
* **FR-04:** Hỗ trợ hoàn tiền toàn phần (Full-refund) và một phần (Partial-refund).
* **FR-05:** Hệ thống phải đảm bảo Tổng tiền hoàn <= Tổng tiền giao dịch gốc.

#### 3.1.3 Yêu cầu Tra soát (Investigation)
* **FR-06:** Tạo Ticket tra soát từ yêu cầu của User với SLA cảnh báo tự động.
* **FR-07:** Tạm khóa trạng thái giao dịch trong thời gian điều tra (tối đa 45 ngày).

### 3.2. Phân hệ Tính năng người dùng (User Features)

#### 3.2.1 Thanh toán QR (QR Payment)
* **FR-08:** Hỗ trợ quét và giải mã Static QR và Dynamic QR theo chuẩn VietQR.
* **FR-09:** Khóa luồng (Idempotency Key) để ngăn chặn giao dịch trùng lặp (Double Payment) nếu User quét 2 lần liên tiếp.

#### 3.2.2 Chuyển tiền (Money Transfer)
* **FR-10:** Chuyển tiền P2P nội bộ realtime, đảm bảo tính nguyên tử (Atomicity) - Trừ tiền người gửi và cộng tiền người nhận phải thực hiện trong 1 transaction DB.
* **FR-11:** Yêu cầu xác thực MFA (OTP/Biometrics) trước khi ghi nhận giao dịch.

#### 3.2.3 Thanh toán Hóa đơn & Split Bill
* **FR-12:** Cho phép lưu trữ Mã khách hàng để tự động nhắc nợ kỳ sau.
* **FR-13:** Split Bill hỗ trợ tự động chia đều hoặc cho phép nhập số tiền customize cho từng thành viên.

### 3.3. Phân hệ Mở rộng (Extended Domains)

#### 3.3.1 eKYC & Định danh
* **FR-14:** Hỗ trợ bóc tách OCR từ CMND/CCCD/Hộ chiếu với độ chính xác > 95%.
* **FR-15:** Bắt buộc thực hiện Liveness check và Face matching trước khi phê duyệt tài khoản.

#### 3.3.2 Digital Lending (Tín dụng)
* **FR-16:** Tự động gọi API CIC lấy điểm tín dụng và đối chiếu với Rule Engine nội bộ để duyệt hạn mức.
* **FR-17:** Hỗ trợ cơ chế Auto-debit (Thu nợ tự động) khi đến hạn thanh toán.

---

## 4. EXTERNAL INTERFACE REQUIREMENTS (GIAO DIỆN TÍCH HỢP NGOÀI)
### 4.1 API & Communications
* Mọi giao tiếp với đối tác thứ 3 (PG, NAPAS, CIC) phải thông qua HTTPS/TLS 1.2+.
* Webhook/IPN trả về từ đối tác phải được xác thực bằng RSA Signature hoặc HMAC-SHA256 để chống Fake IPN.

---

## 5. NON-FUNCTIONAL REQUIREMENTS (YÊU CẦU PHI CHỨC NĂNG)
### 5.1 Performance (Hiệu năng)
* **NFR-01:** Response time cho giao dịch thanh toán nội bộ < 1 giây.
* **NFR-02:** Hệ thống chịu tải tối thiểu 1,000 TPS (Transactions per second) trong thời gian cao điểm.

### 5.2 Security (Bảo mật)
* **NFR-03:** Data-at-rest: Toàn bộ thông tin thẻ, số dư tài khoản phải được mã hóa dưới DB (AES-256).
* **NFR-04:** Rate Limiting: Giới hạn số lần gọi API login/OTP để chống Brute-force (Max 5 lần/phút).

---

## 6. EXCEPTION HANDLING (XỬ LÝ NGOẠI LỆ / FALLBACKS)
*(Phần này kế thừa toàn bộ Section VI từ Tài liệu Nghiệp Vụ)*
* **Lỗi Timeout thanh toán:** Tạm giữ trạng thái `Pending`, kích hoạt Auto-Polling (1m, 3m, 5m). Không tự động hoàn tiền khi chưa chốt trạng thái cuối.
* **Liveness check fail quá 3 lần:** Chuyển sang luồng Hậu kiểm thủ công (Manual review).
* **Nghi ngờ gian lận (AML Hit Rule):** Tự động Freeze (đóng băng) tài khoản và alert cho bộ phận Risk.
