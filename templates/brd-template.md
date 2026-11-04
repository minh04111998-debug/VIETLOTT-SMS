# [Tên Dự Án / Sáng Kiến] — Business Requirements Document (BRD)

> **Mã BRD:** BRD-[INITIATIVE-CODE] | **Phiên bản:** 1.0  
> **Tác giả:** Business Analyst (BA) | **Trạng thái:** Draft / In Review / Baseline  
> **Stakeholders:** Ban Lãnh Đạo Vietlott, Khối Kinh Doanh, Khối Vận Hành, Đối tác Telco

---

## 1. Tóm Tắt Dự Án (Executive Summary)
- **Bối cảnh kinh doanh:** Động lực dẫn đến việc triển khai sáng kiến kinh doanh này.
- **Tầm nhìn:** Mục tiêu chiến lược mà Vietlott SMS hướng tới trong 1-3 năm tới.

---

## 2. Mục Tiêu & Lợi Ích Kinh Doanh (Business Goals & Benefits)
| Mục tiêu kinh doanh | Lợi ích định tính | Lợi ích định lượng (KPI) |
|---|---|---|
| Tăng trưởng tập người chơi Keno | Trải nghiệm đặt cược nhanh chóng | Tăng 20% doanh thu Keno Q4 |
| Giảm chi phí SMS truyền thống | Tận dụng kênh thông báo OTT | Tiết kiệm 500 triệu cước SMS/tháng |

---

## 3. Các Bên Liên Quan & Ma Trận Trách Nhiệm (Stakeholder Matrix)
| Stakeholder | Bộ phận / Đơn vị | Vai trò (RACI) | Yêu cầu cốt lõi |
|---|---|:---:|---|
| Đại diện Vietlott | Khối Kinh Doanh | Accountable (A) | Tăng sản lượng bán, tuân thủ pháp lý |
| Nhà mạng Telco | Viettel / Mobi / Vina | Responsible (R) | Ổn định đường truyền SMS Gateway |
| Ngân hàng đối tác | Napas / BIDV / VCB | Consulted (C) | Tốc độ thanh toán và đối soát |

---

## 4. Yêu Cầu Nghiệp Vụ Cấp Cao (Business Requirements - BR)
- **BR-01:** Hệ thống phải hỗ trợ hạn mức dự thưởng tối đa theo quy chế mở thưởng.
- **BR-02:** Tiền thưởng dưới 10 triệu đồng phải được tự động chi trả về tài khoản dự thưởng trong vòng 15 phút sau khi có kết quả mở thưởng chính thức.
- **BR-03:** Khách hàng bắt buộc phải được xác thực số điện thoại và CCCD trước khi phát hành vé đầu tiên.

---

## 5. Ràng Buộc & Giả Định (Constraints & Assumptions)
- **Ràng buộc pháp lý:** Tuân thủ Thông tư 36/2019/TT-BTC.
- **Ràng buộc công nghệ:** Bắt buộc tích hợp qua API Core hiện hữu của Vietlott.
