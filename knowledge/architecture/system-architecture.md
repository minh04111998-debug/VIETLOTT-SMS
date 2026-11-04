# Vietlott SMS — System Architecture & Integration Map

> **Kiến trúc tổng thể:** Mô hình phân tán tích hợp đa kênh (Omni-channel Lottery Distribution Engine)

---

## 1. Sơ Đồ Khối Kiến Trúc Hệ Thống (Context Diagram)

```mermaid
graph TB
    subgraph Users["📱 Người Dùng Cuối"]
        APP["App Vietlott SMS (iOS / Android)"]
        BANK_APP["App Ngân Hàng / Ví (BIDV, Vietcombank, ZaloPay, MoMo)"]
        SMS_DIRECT["SMS Truyền Thống (Cú pháp nhắn tin)"]
    end

    subgraph ChannelGateway["🌐 Lớp Cổng Phân Phối (Channel Layer)"]
        API_GW["API Gateway & Reverse Proxy"]
        AUTH_SVC["Authentication & eKYC Service (CCCD/NFC)"]
        SMS_GW["Telco SMS Gateway (Viettel, Vina, Mobi)"]
    end

    subgraph CoreEngine["⚙️ Lớp Xử Lý Trung Tâm (Core Lottery Platform)"]
        ORDER_SVC["Order & Ticket Management Service"]
        ACCOUNT_SVC["Tài Khoản Dự Thưởng (TKDT) Service"]
        PAYMENT_ROUTER["Payment & Settlement Router"]
        DRAW_RECON_SVC["Draw Results & Reconciliation Engine"]
    end

    subgraph IntegrationLayer["🏦 Lớp Tích Hợp Ngoại Vi"]
        VIETLOTT_CORE["Core Engine Vietlott Trung Tâm"]
        BANK_NAPAS["Cổng Thanh Toán Napas / Ngân Hàng"]
        TELCO_BILLING["Hệ Thống Trừ Cước Viễn Thông"]
    end

    APP --> API_GW
    BANK_APP --> API_GW
    SMS_DIRECT --> SMS_GW

    API_GW --> AUTH_SVC
    API_GW --> ORDER_SVC
    SMS_GW --> ORDER_SVC

    ORDER_SVC --> ACCOUNT_SVC
    ORDER_SVC --> PAYMENT_ROUTER
    ORDER_SVC --> VIETLOTT_CORE

    PAYMENT_ROUTER --> BANK_NAPAS
    PAYMENT_ROUTER --> TELCO_BILLING

    DRAW_RECON_SVC --> VIETLOTT_CORE
    DRAW_RECON_SVC --> ACCOUNT_SVC
```

---

## 2. Các Luồng Dữ Liệu Trọng Yếu (Critical Data Flows)

1. **Luồng Mua Vé (Ticket Purchase Flow):**
   - Client gửi lệnh đặt vé -> API Gateway xác thực Token/Session -> Kiểm tra số dư TKDT hoặc gửi yêu cầu trừ tiền qua Bank -> Gọi Core Vietlott phát hành vé -> Nhận Ticket ID -> Sinh mã tin nhắn SMS xác nhận vé về máy người dùng.
2. **Luồng Đối Soát & Trả Thưởng (Reconciliation & Payout):**
   - Core Vietlott chốt kết quả kỳ quay -> Engine đối soát quét toàn bộ vé đã phát hành trong kỳ -> Lập danh sách vé trúng -> Tự động ghi có vào TKDT của khách hàng (với giải < 10 tỷ) -> Gửi thông báo OTT/SMS chúc mừng trúng thưởng.
