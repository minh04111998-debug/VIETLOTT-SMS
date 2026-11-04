# Quyết Định 2345/QĐ-NHNN — Tiêu Chuẩn An Toàn Thanh Toán Trực Tuyến

> **Cơ quan ban hành:** Ngân hàng Nhà nước Việt Nam  
> **Hiệu lực thi hành:** Từ ngày 01/07/2024  
> **Áp dụng cho Vietlott SMS:** Các giao dịch nạp tiền, rút tiền trúng thưởng và chuyển tiền qua tài khoản ngân hàng / ví điện tử.

---

## 1. Các Phân Tầng Giao Dịch & Yêu Cầu Xác Thực (Authentication Tiers)

| Hạn mức giao dịch | Yêu cầu xác thực tối thiểu | Áp dụng trên Vietlott SMS |
|---|---|---|
| **Dưới 10,000,000 VND / lần** và tổng giao dịch ngày **dưới 20,000,000 VND** | OTP qua SMS / Smart OTP / Sinh trắc học thiết bị | Mua vé, nạp tiền tài khoản dự thưởng thông thường. |
| **Từ 10,000,000 VND / lần** trở lên HOẶC tổng giao dịch ngày **trên 20,000,000 VND** | **BẮT BUỘC sinh trắc học khuôn mặt** khớp dữ liệu CCCD gắn chip (NFC) | Rút tiền trúng thưởng lớn, giao dịch nạp hạn mức cao. |
| **Giao dịch đầu tiên sau khi kích hoạt thiết bị mới** | **BẮT BUỘC sinh trắc học khuôn mặt** khớp dữ liệu CCCD gắn chip | Đăng nhập trên thiết bị điện thoại khác hoặc đổi số điện thoại. |

---

## 2. Ràng Buộc Kỹ Thuật Đối Với Kiến Trúc & API

1. **Chống giả mạo sinh trắc học (Liveness Detection):** SDK eKYC tích hợp phải có khả năng phát hiện khuôn mặt thực (active/passive liveness), ngăn chặn tấn công phát lại ảnh hoặc video giả mạo (deepfake).
2. **Bảo vệ toàn vẹn thông điệp giao dịch (Message Integrity):** Mọi request chuyển tiền/rút tiền phải được ký số (Digital Signature / HMAC SHA-256) kèm Timestamp và Nonce để chống replay attack.
3. **Mã hóa dữ liệu nhạy cảm:** Không lưu trữ thông tin sinh trắc học thô trên server ứng dụng. Chỉ lưu hash và token định danh từ cơ quan chức năng hoặc đối tác ngân hàng/ví điện tử đã được cấp phép.
