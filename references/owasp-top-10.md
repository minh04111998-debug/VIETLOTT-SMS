# OWASP Top 10 Security Reference — Vietlott SMS

> **Áp dụng cho:** DEV, QA, Governance Agent trong mọi vòng lặp Code Review, Test Design và Security Audit.

---

## 1. Top 10 Rủi Ro Bảo Mật Ứng Dụng Web & API (OWASP 2021)

1. **A01: Broken Access Control (Lỗi kiểm soát truy cập):**
   - *Nguy cơ:* Người chơi này xem/hủy vé của người chơi khác qua thay đổi tham số `ticket_id` hoặc `user_id` trên API (IDOR).
   - *Kiểm soát:* Bắt buộc kiểm tra quyền sở hữu vé dựa trên Session/JWT hiện tại của người dùng.

2. **A02: Cryptographic Failures (Lỗi mã hóa):**
   - *Nguy cơ:* Truyền dữ liệu số điện thoại, mật khẩu, OTP dạng cleartext qua HTTP.
   - *Kiểm soát:* Ép buộc HTTPS/TLS 1.3, mã hóa AES-256 đối với trường dữ liệu CCCD/Số tài khoản.

3. **A03: Injection (Lỗi tiêm mã):**
   - *Nguy cơ:* SQL Injection, Command Injection qua các form tìm kiếm hoặc filter kỳ quay.
   - *Kiểm soát:* Sử dụng hoàn toàn ORM hoặc Parameterized Queries.

4. **A04: Insecure Design (Thiết kế không an toàn):**
   - *Nguy cơ:* Thiếu cơ chế rate limiting cho API gửi SMS OTP dẫn đến cạn kiệt tài khoản telco và spam khách hàng.
   - *Kiểm soát:* Áp dụng Rate Limit (tối đa 1 OTP / 60s / SĐT, tối đa 5 OTP / ngày / IP).

5. **A07: Identification and Authentication Failures (Lỗi định danh & xác thực):**
   - *Nguy cơ:* Cho phép brute-force mã PIN / OTP.
   - *Kiểm soát:* Khóa tài khoản tạm thời sau 5 lần nhập sai mã PIN/OTP liên tiếp.
