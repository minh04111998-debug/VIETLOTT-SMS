# Fintech Knowledge: Hệ Sinh Thái & Mô Hình Đại Lý

| Version | Ngày | Người thực hiện | Trạng thái |
|:---:|:---:|:---:|---|
| 1.0 | 2026-10-08 | BA / Fintech Knowledge Team | Approved |

> **Mã module:** `KB-FINTECH-01`  
> **Thuộc hệ thống:** Kiến trúc Tri thức Fintech Vietlott SMS  
> **Master Index:** [fintech-knowledge-base.md](file:///f:/VIETLOTT-SMS/knowledge/product/fintech-knowledge-base.md)

---

## 1. Tổng quan hệ sinh thái

### 1.1. Vietlott SMS là gì?

Vietlott SMS là **nền tảng trung gian phân phối vé số điện toán Vietlott** qua kênh số (digital channel). Thay vì mua vé tại điểm bán vật lý, người chơi có thể mua vé xổ số trực tuyến thông qua:

- **App di động** (iOS/Android) của Vietlott SMS
- **Web nhúng (Webview HTML5)** tích hợp trên các Super App (ZaloPay, MobiFone Money, PostPay)
- **Hệ thống CTV (Xổ Số+)** — Đại lý offline mua hộ vé

### 1.2. Các bên tham gia (Stakeholders)

| Vai trò | Tổ chức/Hệ thống | Chức năng |
|---------|-------------------|-----------|
| **Nhà phát hành xổ số** | Vietlott (BGT — Ban Giám Tốc/Ban Giám Trị) | Quản lý kỳ quay, xuất vé, xác nhận trúng thưởng |
| **Nhà vận hành nền tảng** | CTIN (Vietlott SMS) | Phát triển & vận hành hệ thống mua vé trực tuyến |
| **Ví điện tử / PSP** | ZaloPay, MobiFone Money, PostPay, VNPay, ViettelPay | Xử lý thanh toán, cung cấp API |
| **Nhà mạng viễn thông** | Viettel, MobiFone, VinaPhone | Cung cấp SMS Gateway, xác thực thuê bao |
| **Ngân hàng** | VPBank (VAN), VNPT Pay | Tài khoản ảo, thanh toán |
| **Người chơi** | Khách hàng cá nhân | Mua vé, nhận thưởng |
| **Đại lý** | CTV (Xổ Số+) | Mua vé hộ, phát triển khách hàng |

### 1.3. Kiến trúc phân hệ (System Landscape)

Dự án được chia làm 3 phân hệ (System) chính:
1. **Hệ thống 1: App Vietlott SMS (Mobile App)** — Giao diện dành cho Người chơi (Nạp/Rút, Mua vé, Lịch sử, Nhận thưởng) & Đại lý.
2. **Hệ thống 2: Trang Quản Trị (Web Admin)** — Giao diện dành cho Quản trị viên/Operator (Duyệt eKYC, Quản lý rủi ro, Đối soát, Trả thưởng giải lớn, Cấu hình Game).
3. **Hệ thống 3: Hệ thống Backend (Core System)** — Middleware xử lý nghiệp vụ lõi, quản lý tài chính bằng nguyên tắc Kế toán kép (Double-Entry Ledger), giao tiếp BGT.

### 1.4. Sản phẩm xổ số

| Sản phẩm | Loại | Tần suất quay | Đặc điểm nổi bật |
|----------|------|---------------|-------------------|
| **Mega 6/45** | Ma trận (Matrix) | 3 lần/tuần (T4, T6, CN) | 4 hạng giải, Jackpot tích lũy từ 12 tỷ |
| **Power 6/55** | Ma trận (Matrix) | 3 lần/tuần (T3, T5, T7) | 5 hạng giải, **2 Jackpot** (30 tỷ + 3 tỷ) |
| **Max 3D / 3D+ / 3D Pro** | Dãy số | 3 lần/tuần | Trúng nhiều giải **cộng gộp** (khác Matrix) |
| **Bingo18** | Quay nhanh (Fast Draw) | **6 phút/kỳ**, 159 kỳ/ngày | Độc quyền trên Vietlott SMS, áp lực TPS cao nhất |
| **Lotto 5/35** | Ma trận (Matrix) | **2 lần/ngày** (13h, 21h) | Sản phẩm mới nhất, có "Chia giải Độc Đắc" |

> [!TIP]
> **Insight kiến trúc:** Bingo18 với 159 kỳ/ngày × 50.000 lượt/kỳ tạo áp lực lớn nhất lên hệ thống xử lý giao dịch (TPS) và SMS Gateway. Đây là điểm cần ưu tiên khi thiết kế Message Queue.
>
> **Nguồn:** [bao-cao-san-pham-vietlott.md](file:///f:/artifacts/product/bao-cao-san-pham-vietlott.md)

---


---

## 8. Mô hình đại lý & Cộng tác viên (CTV)

### 8.1. Tổng quan mô hình Xổ Số+

**Xổ Số+** (Cộng tác viên) là hệ thống mở rộng bán vé offline thông qua mạng lưới đại lý cấp 2:

```
┌──────────────────────────────────┐
│         Vietlott SMS             │
│    ┌────────────────────────┐    │
│    │   Admin CMS (Tích hợp) │    │
│    └────────────────────────┘    │
│              │                   │
│    ┌─────────┴─────────┐        │
│    │   VPBank VAN       │        │
│    │  (Tài khoản ảo)   │        │
│    └───────────────────┘        │
└──────────────────────────────────┘
         │
    ┌────┴────┐
    │  CTV    │  ← Nạp tiền ứng trước vào TK VAN
    │  (App)  │  ← Mua vé hộ cho KH
    └─────────┘
         │
    ┌────┴────┐
    │  Khách  │  ← Nhận SMS xác nhận
    │  hàng   │  ← Click link → vé được xuất
    └─────────┘
```

### 8.2. Cơ chế xác nhận mua hộ (Mandatory Confirmation)

1. CTV chọn bộ số → Hệ thống **Hold tiền** từ TK VAN
2. Hệ thống sinh **URL chứa Random ID** (chống giả mạo) + TTL
3. Gửi SMS link cho KH → KH click link xác nhận
4. Hệ thống kiểm tra: còn cách giờ đóng kỳ > 30s? → Gọi BGT xuất vé

> [!WARNING]
> **Rủi ro bảo mật:** Link xác nhận hiện tại chỉ yêu cầu click, không yêu cầu đăng nhập → "bất cứ ai có link đều có thể xác nhận". Giải pháp: Random ID phải đủ entropy (UUIDv4 trở lên) để không thể đoán.

### 8.3. Quy tắc T-30s & SLA Timeout

| Quy tắc | Mô tả | Mục đích |
|---------|--------|----------|
| **T-30s** | Không gửi lệnh mua vé trong 30s trước khi đóng kỳ | Tránh rủi ro vé trôi sang kỳ sau |
| **SLA 60s** | BGT phải trả kết quả trong 60s, nếu không → BGT chịu trách nhiệm | Đảm bảo SLA, chia rủi ro |
| **Lưu kỳ** | Hệ thống lưu thêm kỳ theo thời điểm gửi yêu cầu (độc lập với kỳ BGT) | Căn cứ đối chiếu |

### 8.4. Cơ chế hoa hồng

| Loại hoa hồng | Công thức | Ghi chú |
|----------------|-----------|---------|
| **Phát triển KH mới** | x đồng/KH đăng ký thành công | Cấu hình trên Admin |
| **Bán vé** | y% × tổng tiền vé mua thành công trong ngày | Cấu hình trên Admin |
| **Tổng ngày** | Hoa hồng mua vé + Hoa hồng đăng ký | Hiển thị trên App CTV |

> **Nguồn:** [XosoPlus_extracted.txt](file:///f:/VIETLOTT-SMS/artifacts/requirements/XosoPlus_extracted.txt), [Master_Summary_4_Tasks.md §4](file:///f:/plans/completed/Master_Summary_4_Tasks.md)

---


---

## 11. Thuật ngữ chuyên ngành (Glossary)

| Thuật ngữ | Viết tắt | Định nghĩa |
|-----------|----------|-------------|
| **Tài khoản dự thưởng** | TKDT | Tài khoản chính của người chơi trên Vietlott SMS |
| **Tài khoản thanh toán** | TKTT | Tài khoản liên kết để thanh toán mua vé (ví, ngân hàng) |
| **Tài khoản nhận thưởng** | TKNT | Tài khoản liên kết để nhận tiền trả thưởng |
| **Hạn mức dự thưởng** | HMDT | Số dư khả dụng trong TKDT để mua vé |
| **Hạn mức bán hàng** | HMBH | Hạn mức cho phép Vietlott SMS bán vé (cấp bởi BGT) |
| **Ban Giám Trị** | BGT | Hệ thống trung tâm của Vietlott — xuất vé, quay thưởng |
| **PayByToken** | PBT | Thanh toán bằng token đã liên kết (không nhập lại thẻ/ví) |
| **Bypass OTP** | - | Giao dịch tự động không cần xác thực OTP |
| **Chi hộ / Disbursement** | - | Chuyển tiền từ Merchant sang ví/TK người nhận |
| **Thu hộ / Collection** | - | Thu tiền từ KH qua ví/TK về Merchant |
| **Đối soát / Reconciliation** | - | Đối chiếu dữ liệu GD giữa 2 hệ thống |
| **RRC** | - | Mã kết quả đối soát của MobiFone (Reconciliation Result Code) |
| **Virtual Account Number** | VAN | Tài khoản ngân hàng ảo (VPBank) — dùng cho CTV nạp tiền |
| **Cộng tác viên** | CTV | Đại lý cấp 2 mua vé hộ khách hàng |
| **eKYC** | - | Electronic Know Your Customer — Định danh điện tử |
| **OCR** | - | Optical Character Recognition — Nhận dạng ký tự quang học |
| **IPN** | - | Instant Payment Notification — Webhook thông báo thanh toán |
| **TTL** | - | Time To Live — Thời gian sống của link/token |
| **Pari-Mutuel** | - | Mô hình chia đều giải thưởng giữa những người thắng |
| **NĐ 2345** | - | Quyết định 2345/QĐ-NHNN về an toàn bảo mật thanh toán trực tuyến |
| **PGP RSA-3072** | - | Chuẩn mã hóa Pretty Good Privacy với RSA 3072-bit key |
| **FaceID / Face Matching** | - | Xác thực sinh trắc học bằng khuôn mặt |
| **T-30s** | - | Quy tắc chặn GD trong 30s cuối trước khi đóng kỳ quay |
| **MO/MT** | - | Mobile Originated / Mobile Terminated — Tin nhắn gửi đi / nhận |
| **Site** | - | Phiên bản web/app theo nhà mạng (site Viettel, site MobiFone, site VNPT) |
| **POS (Point of Sale)** | POS | Kênh phân phối vé số vật lý truyền thống qua đại lý |
| **Omnichannel** | - | Mô hình phân phối kết hợp đa kênh (POS và SMS/Digital) |
| **Ticket ID** | - | Mã vé điện tử định danh duy nhất cho một vé phát hành qua SMS |
| **Auto-payout** | - | Trả thưởng tự động (giải nhỏ) trừ thuế TNCN và cộng vào TKNT |
| **TPS** | TPS | Số lượng giao dịch xử lý mỗi giây (áp lực chính với Bingo18) |
| **Mã kênh** | - | Mã định danh kênh bán (CTV, ZaloPay, MobiFone) gắn trên mỗi vé |

---

> [!NOTE]
> **Phạm vi tài liệu:** Knowledge Base này được tổng hợp từ nội dung text đã extract (~64 tài liệu). Các file binary (.docx, .xlsx, .pdf) chưa được đọc nội dung chi tiết → độ bao phủ ước tính ~75-80%. Cần bổ sung khi có thêm thông tin từ các buổi họp nghiệp vụ.

> [!TIP]
> **Cách sử dụng tài liệu này:**
> - **BA mới onboard:** Đọc từ đầu đến cuối để hiểu toàn cảnh hệ sinh thái
> - **DEV:** Tập trung §2 (Payment), §4 (Reconciliation), §9 (Security), §10 (Patterns)
> - **QA:** Tập trung §2.3 (Refund), §3 (Kênh), §5 (Trả thưởng), §10.1 (Edge cases)
> - **SA:** Tập trung §10 (Patterns), §9 (Security), §4 (Reconciliation Architecture)

---

**Tham chiếu nguồn chính:**
- [BABOK® Guide v3](https://www.iiba.org/standards-and-resources/babok/) — IIBA
- [Quyết định 2345/QĐ-NHNN](https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Quyet-dinh-2345-QD-NHNN-2023-an-toan-bao-mat-thanh-toan-truc-tuyen-ngan-hang-dien-tu-572389.aspx) — NHNN
- [PGP Encryption Standard](https://www.openpgp.org/) — OpenPGP
- [OAuth 2.0 Authorization Code Grant](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1) — IETF RFC 6749
- [Pari-mutuel betting](https://en.wikipedia.org/wiki/Parimutuel_betting) — Wikipedia