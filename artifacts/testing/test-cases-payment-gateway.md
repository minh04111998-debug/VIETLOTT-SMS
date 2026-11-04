# Danh Sách Test Cases: Cổng Thanh Toán & Khóa Chống Trùng Đơn (Payment Gateway)

| Version | Ngày | Người thực hiện | Mô tả |
|:---:|:---:|:---:|---|
| 1.0 | 2026-10-08 | Quality Assurance (QA) | Bộ test cases kiểm thử cổng thanh toán Fintech và Idempotency |

> **Mã bộ test:** `TC-SUITE-PAY-01` | **Trạng thái:** `Approved`  
> **Tài liệu căn cứ:** [SRS_He_Sinh_Thai_Thanh_Toan_Fintech_v1.0.md](file:///f:/VIETLOTT-SMS/artifacts/requirements/SRS_He_Sinh_Thai_Thanh_Toan_Fintech_v1.0.md)

---

## Ma Trận Truy Vết Kiểm Thử (Traceability Matrix)

| Test Case ID | Tên Kịch Bản Kiểm Thử | Yêu Cầu Chức Năng (SRS) | Mức Độ Ưu Tiên | Trạng Thái |
|:---:|---|:---:|:---:|:---:|
| `TC-PAY-001` | Quét mã VietQR động thanh toán đơn hàng vé số | `FR-08` | High | PASS |
| `TC-PAY-002` | Chống trừ tiền 2 lần bằng Idempotency Key | `FR-09` | Critical | PASS |
| `TC-PAY-003` | Chuyển tiền nội bộ P2P đảm bảo tính nguyên tử DB | `FR-10` | High | PASS |
| `TC-PAY-004` | Xác thực MFA bắt buộc trước khi ghi nhận giao dịch | `FR-11` | Critical | PASS |
| `TC-PAY-005` | Tự động tải file settlement đối soát lúc 23:59 | `FR-01` | Medium | PASS |
| `TC-PAY-006` | Lưu trữ Mã khách hàng và tự động nhắc nợ hóa đơn | `FR-12` | Medium | PASS |
| `TC-PAY-007` | Chia hóa đơn thanh toán nhóm (Split Bill) tùy biến | `FR-13` | Medium | PASS |

---

## Chi Tiết Kịch Bản Kiểm Thử (Given - When - Then)

### TC-PAY-001: Quét mã VietQR động thanh toán đơn hàng vé số
- **Truy vết SRS:** `FR-08`
- **Mức độ:** High
- **Điều kiện tiền đề (Given):** Người chơi đã chọn 01 bộ số Mega 6/45 trị giá 10,000 VNĐ tại màn hình thanh toán.
- **Hành động (When):** Người chơi chọn phương thức thanh toán VietQR và ứng dụng ngân hàng quét mã QR động được sinh ra.
- **Kết quả kỳ vọng (Then):**
  - Hệ thống giải mã chính xác số tiền 10,000 VNĐ và nội dung chuyển khoản chứa mã đơn hàng duy nhất.
  - Sau khi chuyển tiền thành công, trạng thái đơn hàng tự động chuyển sang `SUCCESS` trong vòng 3 giây.

---

### TC-PAY-002: Chống trừ tiền 2 lần bằng Idempotency Key (Idempotent Payment Engine)
- **Truy vết SRS:** `FR-09`
- **Mức độ:** Critical
- **Điều kiện tiền đề (Given):** Người chơi nhấn nút "Thanh Toán Ngay" trên ứng dụng khi kết nối mạng di động chập chờn.
- **Hành động (When):** Người chơi bấm liên tiếp 2 lần nút thanh toán trong vòng 500ms với cùng 1 `Idempotency-Key`.
- **Kết quả kỳ vọng (Then):**
  - API Gateway nhận diện khóa `Idempotency-Key` trùng lặp và từ chối request thứ 2 với mã lỗi `409 Conflict`.
  - Tài khoản ngân hàng của người chơi chỉ bị trừ tiền duy nhất 1 lần (10,000 VNĐ).
  - Không phát sinh 2 vé trùng lặp trên hệ thống Core.

---

### TC-PAY-003: Chuyển tiền nội bộ P2P đảm bảo tính nguyên tử (Atomicity Transaction)
- **Truy vết SRS:** `FR-10`
- **Mức độ:** High
- **Điều kiện tiền đề (Given):** Tài khoản A có số dư 100,000 VNĐ thực hiện chuyển 50,000 VNĐ cho Tài khoản B.
- **Hành động (When):** Quá trình trừ tiền Tài khoản A thành công nhưng server gặp sự cố crash trước khi cộng tiền cho Tài khoản B.
- **Kết quả kỳ vọng (Then):**
  - Transaction Database tự động Rollback toàn bộ trạng thái.
  - Số dư Tài khoản A giữ nguyên 100,000 VNĐ, không xảy ra hiện tượng thất thoát hoặc mất cân đối số dư.

---

### TC-PAY-004: Xác thực MFA bắt buộc trước khi ghi nhận giao dịch
- **Truy vết SRS:** `FR-11`
- **Mức độ:** Critical
- **Điều kiện tiền đề (Given):** Người chơi thực hiện giao dịch thanh toán hoặc rút tiền từ tài khoản dự thưởng.
- **Hành động (When):** Người chơi không nhập mã OTP / Biometrics hoặc nhập sai quá 3 lần liên tiếp.
- **Kết quả kỳ vọng (Then):**
  - Hệ thống chặn giao dịch và tạm khóa phiên giao dịch trong vòng 15 phút.
  - Tuyệt đối không ghi nhận giao dịch thành công khi chưa vượt qua bước xác thực MFA.

---

### TC-PAY-005: Tự động tải file settlement đối soát lúc 23:59
- **Truy vết SRS:** `FR-01`
- **Mức độ:** Medium
- **Điều kiện tiền đề (Given):** Cronjob hệ thống đối soát được kích hoạt vào thời điểm 23:59:00 hàng ngày.
- **Hành động (When):** Service Settlement gửi yêu cầu fetch file đối soát sang SFTP server của đối tác trung gian thanh toán.
- **Kết quả kỳ vọng (Then):**
  - File đối soát định dạng `.csv` được tải về thư mục mã hóa AES-256.
  - Checksum MD5 của file tải về khớp 100% với mã băm do đối tác cung cấp.

---

### TC-PAY-006: Lưu trữ Mã khách hàng và tự động nhắc nợ hóa đơn
- **Truy vết SRS:** `FR-12`
- **Mức độ:** Medium
- **Điều kiện tiền đề (Given):** Người chơi đã thanh toán hóa đơn cước viễn thông hoặc dịch vụ định kỳ trên ứng dụng Vietlott SMS.
- **Hành động (When):** Người chơi tích chọn "Lưu thông tin thanh toán cho kỳ sau".
- **Kết quả kỳ vọng (Then):**
  - Hệ thống mã hóa và lưu trữ Mã khách hàng vào hồ sơ người dùng.
  - Đến kỳ thanh toán tiếp theo (T+30), hệ thống gửi thông báo nhắc nợ chính xác số tiền phát sinh.

---

### TC-PAY-007: Chia hóa đơn thanh toán nhóm (Split Bill) tùy biến
- **Truy vết SRS:** `FR-13`
- **Mức độ:** Medium
- **Điều kiện tiền đề (Given):** Một nhóm 3 người chơi cùng tham gia mua bao vé số tổng trị giá 300,000 VNĐ.
- **Hành động (When):** Trưởng nhóm khởi tạo yêu cầu Split Bill với tùy chọn chia đều (100,000 VNĐ/người) hoặc nhập số tiền tùy biến.
- **Kết quả kỳ vọng (Then):**
  - Hệ thống sinh 3 liên kết yêu cầu thanh toán riêng biệt với đúng định mức tiền từng người.
  - Sau khi đủ 3 giao dịch thành công, vé chung tự động được kích hoạt phát hành trên hệ thống Core.
