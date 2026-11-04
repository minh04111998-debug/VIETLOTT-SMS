# Telecom SMS Protocols & Gateway Integration Primer

> **Phạm vi:** Giao thức kết nối tin nhắn SMS qua các nhà mạng viễn thông Viettel, Mobifone, Vinaphone phục vụ gửi mã xác thực OTP và mã vé dự thưởng Vietlott SMS.

---

## 1. Các Khái Niệm Viễn Thông Cốt Lõi

- **MO (Mobile Originated):** Tin nhắn xuất phát từ điện thoại của người chơi gửi tới đầu số dịch vụ (Shortcode 9969) của Vietlott SMS.
- **MT (Mobile Terminated):** Tin nhắn từ hệ thống Vietlott SMS gửi tới thuê bao của người chơi (thông báo mã vé, thông báo trúng thưởng, gửi OTP).
- **Brandname SMS:** Tin nhắn hiển thị tên thương hiệu "VIETLOTT" thay vì đầu số số lạ, đảm bảo độ tin cậy và chống lừa đảo.
- **SMPP (Short Message Peer-to-Peer Protocol):** Giao thức chuẩn công nghiệp mức TCP/IP dùng để kết nối giữa máy chủ Vietlott SMS Gateway và SMSC (Short Message Service Center) của các nhà mạng viễn thông.

---

## 2. Các Rủi Ro Kỹ Thuật & Ngoại Lệ Cần Xử Lý

1. **Nghẽn mạng giờ cao điểm (SMS Throttling / Queue Congestion):**
   - Trước giờ quay thưởng 17h30 - 17h45, lưu lượng gửi MT tăng đột biến.
   - *Kiểm soát:* Áp dụng cơ chế phân luồng ưu tiên (Priority Queue): OTP xác thực được ưu tiên mức cao nhất, thông báo trúng thưởng/khuyến mại xếp sau.
2. **DLR (Delivery Report) Timeout:**
   - Tin nhắn đã bắn sang nhà mạng nhưng chưa nhận được phản hồi DLR xác nhận người dùng đã thực nhận.
   - *Kiểm soát:* Đặt timeout 60 giây; nếu chưa có DLR, hệ thống cho phép người dùng bấm "Gửi lại mã OTP" (tối đa 3 lần/phiên).
