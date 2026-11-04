# BÁO CÁO PHÂN TÍCH HIỆN TRẠNG (AS-IS), NGHỆU CẦU TƯƠNG LAI (TO-BE) VÀ GAP ANALYSIS
## CHỨC NĂNG: CẤU HÌNH & TỰ ĐỘNG PHÁT TẶNG VÉ CHO TÀI KHOẢN MỞ MỚI KÊNH BANK

---

- **Mã tài liệu:** `GAP-ANALYSIS-CAMPAIGN-BANK-V1.0`
- **Ngày lập:** 2026-07-29
- **Tác giả:** Business Analyst Agent (BA)
- **Trạng thái:** `Draft` (Báo cáo Phân tích Chuyên sâu - /goal mode)
- **Dữ liệu đầu vào:**
  - Yêu cầu từ Chị Hoài VDI (Group VIETLOTTSMS-BA) - Triển khai đầu tháng 8/2026
  - Rà soát đệ quy 4 thư mục tài liệu hệ thống `artifacts/requirements/` (`VIETLOTT SMS_ Tài liệu nghiệp vụ`, `VIETLOTT SMS_Tích hợp kênh bán`, `VIETLOTT_SMS`, `Xổ Số+_Tài liệu nghiệp vụ`)

---

## 1. TỔNG QUAN VÀ MỤC TIÊU PHÂN TÍCH

Báo cáo này tập trung phân tích toàn diện khoảng cách giữa **Hạ tầng / Chức năng hiện tại của Vietlott SMS (As-Is)** và **Nhu cầu nghiệp vụ mới từ Chị Hoài VDI (To-Be)** nhằm phục vụ chương trình tặng vé tự động cho khách hàng mở tài khoản từ các kênh Ngân hàng (Bank channels) triển khai từ đầu tháng 8/2026.

---

## 2. PHÂN TÍCH CHI TIẾT HIỆN TRẠNG HỆ THỐNG (AS-IS ANALYSIS)

Dựa trên kết quả rà soát đệ quy 4 thư mục tài liệu chuẩn tại `artifacts/requirements/`:

### 2.1. Phân hệ Admin - Quản lý Khuyến mại & Tặng quà hiện tại (`03.12.Affiliate_Gift` & `VIETLOTTSMS_ADMIN`)
1. **Tính năng Tặng Quà / Mã Code (`28.Tính năng tặng quà_tặng code.doc`, `28.3+Cấu hình tặng quà.doc`):**
   - System As-Is cho phép Admin tạo các Mã quà tặng (Voucher Code) đơn lẻ với số lượng mã cố định.
   - Khách hàng bắt buộc phải chủ động nhập mã trên App/Webview thì hệ thống mới tặng vé.
   - *Hạn chế:* Không có cơ chế tự động tặng vé dựa trên sự kiện kích hoạt tài khoản.
2. **Tính năng Import Tặng quà thủ công (`28.4+Import tặng quà.doc`):**
   - Admin phải chuẩn bị file Excel danh sách SĐT khách hàng + Loại vé/Mã quà, sau đó tải lên hệ thống để chạy batch job.
   - *Hạn chế:* Thao tác hoàn toàn thủ công, có độ trễ lớn (1-3 ngày), không thể đáp ứng thời gian thực (realtime) ngay khi KH vừa mở tài khoản thành công trên App Bank.
3. **Tính năng Giới thiệu bạn bè / Referral (`29.2+Thiết lập chương trình giới thiệu bạn bè.doc`):**
   - Tự động tặng quà/vé khi Khách hàng A (Người giới thiệu) gửi mã cho Khách hàng B đăng ký.
   - *Hạn chế:* Logic gắn cứng theo mô hình Người giới thiệu - Người được giới thiệu 1-1, không hỗ trợ mở rộng cấu hình theo Kênh Bank, Trạng thái TKNT, Daily Cap hay Total Budget.
4. **Tính năng Affiliate (`33.4+Thiết lập chương trình Affiliate.doc`):**
   - Hỗ trợ tracking lượt đăng ký theo link Affiliate của đại lý, chi hoa hồng theo kỳ.
   - *Hạn chế:* Chưa hỗ trợ cấp vé dự thưởng tự động realtime theo cụm điều kiện tài khoản active và điều kiện thanh toán.

### 2.2. Phân hệ Quản lý Tài khoản & Định danh (`03.1.DangKy_QLTK`)
1. **Trạng thái Tài khoản Dự thưởng - TKDT (`Sơ đồ trạng thái TKDT.doc`):**
   - Hệ thống đã có đầy đủ sơ đồ trạng thái TKDT: `NEW` $\rightarrow$ `CHO_PHE_DUYET` $\rightarrow$ `ACTIVE` $\rightarrow$ `HAU_KIEM` $\rightarrow$ `KHOA` / `HUY`.
   - Đã có Event Bus / Message Queue phát sự kiện `ACCOUNT_STATUS_CHANGED` khi hồ sơ eKYC được duyệt thành `ACTIVE`.
2. **Trạng thái Tài khoản Nhận thưởng - TKNT (`5.6.+Quản lý tài khoản nhận thưởng.doc`):**
   - Hệ thống đã phân định rõ TKNT (Tài khoản Ngân hàng/Ví điện tử dùng để nhận tiền thưởng Auto-payout) với các trạng thái: Chưa liên kết, Đã liên kết, Đã xác thực.

### 2.3. Phân hệ Tích hợp Kênh Bank (`VIETLOTT SMS_Tích hợp kênh bán`)
1. **Nhận diện Nguồn đăng ký (`Tích hợp bank ví/Tài liệu luồng tích hợp Vietlott SMS lên ứng dụng bank, ví.docx`):**
   - Khi KH truy cập từ App Ngân hàng (VPBank, SeABank, MBBank, BIDV...), hệ thống nhận diện được tham số `channel_code` / `partner_code` đại diện cho Kênh Bank.
2. **Tiền lệ Chiến dịch VPBank (`Tích hợp VPBank/VLT tặng vé KH mở thẻ tín dụng VPBank.xlsx`):**
   - Trước đây đã từng triển khai 1 chương trình tặng vé riêng lẻ cho VPBank, nhưng xử lý dưới dạng postback API riêng lẻ và đối soát file Excel thủ công, chưa được quy chuẩn thành Rule Engine động trên Admin.

---

## 3. PHÂN TÍCH NHU CẦU MỚI (TO-BE REQUIREMENTS)

Chương trình khuyến mại mở tài khoản kênh Bank từ đầu tháng 8/2026 đặt ra các yêu cầu mới:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              MÔ HÌNH TO-BE TỔNG THỂ                                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. ADMIN CONFIGURATION (Cấu hình cụm 7 tiêu chí linh hoạt):                            │
│    Kênh Bank ──► Trạng thái TKDT ──► Trạng thái TKNT ──► ĐK Thanh toán                     │
│    ──► Giá trị/Loại vé ──► Daily Cap (Người/ngày) ──► Total Budget (Trần tiền)          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. REALTIME RULE ENGINE (Xử lý tự động 100%):                                          │
│    Event: KH Active từ Bank ──► Validate 7 Điều kiện ──► Atomic Lock Quota/Budget      │
│    ──► Call Core Ticketing cấp vé ──► Push Notification/SMS cho KH                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. FAIL-SAFE & RECOVERY:                                                               │
│    Timeout API ──► Auto-Retry 3 lần ──► Pending Manual Queue cho Admin                  │
│    Daily Cap Reached ──► Queueing bảo lưu sang ngày sau (Option A đề xuất)              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. BẢNG MA TRẬN GAP ANALYSIS (KHOẢNG CÁCH GIỮA AS-IS VÀ TO-BE)

| STT | Trụ Nghiệp Vụ | Hiện Trạng (As-Is trong 04_Doc) | Yêu Cầu Mới (To-Be) | Khoảng Cách (GAP) & Công Việc Cần Xây Dựng | Mức Độ (Complexity) |
|---|---|---|---|---|---|
| **1** | **Cấu hình Chiến dịch Admin** | Chỉ cấu hình Mã quà tặng đơn lẻ (`28.3`) hoặc Import Excel (`28.4`). | Màn hình Admin cấu hình chiến dịch động với cụm 7 tiêu chí liên hoàn. | **GAP LỚN:** Cần xây dựng mới UI Admin + Data Model `campaign_config` lưu trữ 7 nhóm điều kiện. | 🔴 HIGH |
| **2** | **Cơ chế Kích hoạt Tặng vé** | KH nhập mã thủ công hoặc Admin chạy batch job import file. | Tự động 100% realtime khi KH active từ kênh Bank mà không cần nhập code. | **GAP LỚN:** Cần phát triển Event-driven Rule Engine lắng nghe event `ACCOUNT_ACTIVATED`. | 🔴 HIGH |
| **3** | **Kiểm soát Hạn mức & Ngân sách** | Giới hạn tổng số lượng mã phát ra (Voucher quantity). | Đa tầng (Dual-Limit): Quản lý đồng thời **Daily Cap** (người/ngày) & **Total Budget** (tổng tiền). | **GAP TRUNG BÌNH:** Cần phát triển thuật toán Atomic Lock (Redis Lock) tránh phát lố budget khi bùng nổ traffic. | 🟡 MEDIUM |
| **4** | **Kiểm tra Điều kiện TKNT & Thanh toán** | Chưa kết nối luồng check TKNT và ĐK thanh toán vào engine tặng quà. | Realtime validate trạng thái TKNT (`VERIFIED`/`LINKED`) và phát sinh giao dịch thanh toán đầu tiên. | **GAP TRUNG BÌNH:** Cần viết service kết nối API Check TKNT và API History Transaction. | 🟡 MEDIUM |
| **5** | **Xử lý Ngoại lệ & Treo luồng (Hung State)** | Chưa có cơ chế retry tự động cho luồng tặng vé khi API Core bận. | Auto-retry 3 lần khi Timeout/Fail + Màn hình Admin duyệt thủ công `PENDING_RETRY_MANUAL`. | **GAP TRUNG BÌNH:** Cần xây dựng Retry Queue & UI Admin Quản lý Giao dịch Tặng vé Lỗi. | 🟡 MEDIUM |
| **6** | **Chính sách Quá Hạn mức Ngày (Daily Cap Exceeded)** | Chưa hỗ trợ Daily Cap. | Khi vượt Daily Cap trong ngày, tự động đưa vào Hàng chờ (Queue) bảo lưu sang ngày hôm sau. | **GAP TRUNG BÌNH:** Cần xây dựng Midnight Scheduler Job quét Queue lúc 00:00:01 hằng ngày. | 🟡 MEDIUM |
| **7** | **Báo cáo & Đối soát** | Chỉ có Báo cáo lịch sử sử dụng Code (`28.6`). | Báo cáo tiến độ giải ngân Budget chiến dịch realtime theo từng Kênh Bank. | **GAP NHỎ:** Cần phát triển 01 Dashboard/Báo cáo thống kê giải ngân campaign. | 🟢 LOW |

---

## 5. CÁC CẢNH BÁO RỦI RO THỜI GIAN & ĐỀ XUẤT NGUYÊN TẮC THIẾT KẾ (RED FLAGS & RECOMMENDATIONS)

> [!WARNING]
> ### 🚨 CẢNH BÁO RỦI RO TIẾN ĐỘ & KỸ THUẬT:
> 1. **Áp lực Thời gian (Go-live đầu tháng 8/2026):** Thời gian còn lại chỉ còn 2-3 ngày làm việc. Nếu làm quá phức tạp luồng Rule Engine, dự án sẽ trễ deadline.
> 2. **Rủi ro Race Condition trên Ngân sách:** Khi chiến dịch mở rộng trên các kênh Bank như VPBank/VietinBank, lượng tài khoản mở mới có thể tăng hàng nghìn tài khoản/giờ. Nếu không dùng Redis Distributed Lock, nguy cơ phát vượt Total Budget là 100%.

### Đề xuất Kế hoạch Triển khai Theo Giai Đoạn (Phased Approach):

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          LỘ TRÌNH KỶ THUẬT NGHỆU VỤ GIAI ĐOẠN                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ PHASE 1 (Go-live Đúng Đầu Tháng 8 - MVP):                                             │
│ - Màn hình Admin Cấu hình Chiến dịch Kênh Bank (Cụm 7 tiêu chí).                      │
│ - Realtime Engine xử lý tặng vé tự động cho KH ACTIVE.                                │
│ - Atomic Lock cho Daily Cap & Total Budget.                                            │
│ - Tự động phát vé ngẫu nhiên (QuickPick) + Gửi SMS thông báo.                         │
│ - Xử lý Daily Cap theo Option A (Bảo lưu hàng chờ Queue sang ngày sau).                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ PHASE 2 (Nâng cấp sau Go-live 2 tuần):                                                 │
│ - Màn hình Admin Quản lý Retry Manual & Dashboard Báo cáo Phân tích Kênh Bank sâu.   │
│ - Hỗ trợ KH chọn số trên App khi nhận vé tặng.                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. HƯỚNG DẪN BÀN GIAO VÀ PHÊ DUYỆT

- **Báo cáo GAP Analysis:** `artifacts/analysis/gap-analysis-campaign-tang-ve-bank.md`
- **File Đặc tả SRS Nháp:** `artifacts/requirements/srs-campaign-tang-ve-bank.md`
- **Bước tiếp theo:**
  1. Trình báo cáo GAP Analysis và 5 câu hỏi chốt nghiệp vụ cho Chị Hoài VDI.
  2. Xin phê duyệt để baseline tài liệu sang `artifacts/requirements/`.
  3. Bàn giao kết quả phân tích GAP cho SA để thiết kế DB Schema & API Contracts.
