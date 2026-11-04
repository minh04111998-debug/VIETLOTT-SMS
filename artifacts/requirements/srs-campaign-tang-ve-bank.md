# ĐẶC TẢ YÊU CẦU NGHIỆP VỤ (SRS)
## CHỨC NĂNG: CẤU HÌNH & TỰ ĐỘNG PHÁT TẶNG VÉ CHO TÀI KHOẢN MỞ MỚI KÊNH BANK

---

- **Mã tài liệu:** `SRS-CAMPAIGN-BANK-V1.0`
- **Ngày cập nhật:** 2026-07-29
- **Tác giả:** Business Analyst Agent (BA)
- **Trạng thái:** `Draft` (Chờ Phê Duyệt)
- **Tham chiếu YC:** Yêu cầu từ Chị Hoài VDI (Group VIETLOTTSMS-BA) - Triển khai đầu tháng 8/2026

---

## 1. TỔNG QUAN VÀ MỤC TIÊU NGHIỆP VỤ (BUSINESS GOALS)

### 1.1. Bối cảnh
Nhằm kích thích tăng trưởng người dùng mới mở tài khoản Vietlott SMS qua các kênh Ngân hàng (Bank channels như VPBank, VietinBank, MBBank, BIDV, SeABank...) từ đầu tháng 8/2026, Vietlott SMS triển khai chương trình khuyến mại tặng vé dự thưởng tự động cho khách hàng mở tài khoản mới và đạt điều kiện Active.

### 1.2. Mục tiêu
- **Tự động hóa 100%:** Luồng tặng vé được kích hoạt và trả kết quả tự động ngay khi tài khoản khách hàng đáp ứng đầy đủ cụm điều kiện cấu hình.
- **Khả năng Tự Cấu hình (Admin):** Cho phép Quản trị viên (Admin) tự thiết lập, điều chỉnh các tiêu chí chiến dịch (kênh bank, trạng thái TK, điều kiện thanh toán, ngân sách, giới hạn ngày) qua giao diện Web Admin mà không cần can thiệp code.
- **Quản lý Ngân sách Chặt chẽ:** Đảm bảo hệ thống không phát lố Tổng budget chiến dịch hoặc Hạn mức tặng vé mỗi ngày (Daily Cap).

---

## 2. PHẠM VI NGHIỆP VỤ (SCOPE)

### 2.1. In-Scope
1. **Module Admin - Cấu hình Chiến dịch Tặng vé:**
   - Tạo mới / Chỉnh sửa / Kích hoạt / Tạm dừng chiến dịch.
   - Thêm cụm điều kiện áp dụng: Kênh Bank, Trạng thái TK dự thưởng, Trạng thái TKNT, Điều kiện thanh toán, Giá trị/Loại vé tặng, Số lần tặng/KH, Limit người/ngày, Tổng budget.
2. **Engine Xử lý Tặng vé Tự động (Background Job / Event Driven):**
   - Lắng nghe event tài khoản active / giao dịch thỏa điều kiện từ các Kênh Bank.
   - Validate cụm điều kiện chiến dịch realtime.
   - Kiểm tra Hạn mức Ngày (Daily Limit) & Ngân sách Tổng (Total Budget).
   - Gọi hệ thống Core Ticketing để tạo vé & gửi tặng vé cho khách hàng.
3. **Luồng Thông báo (Notification Engine):**
   - Gửi SMS / Push Notification thông báo tặng vé thành công, bảo lưu lượt hoặc thông báo lỗi cho KH.
   - Ghi nhận lịch sử gửi tin.
4. **Luồng Báo cáo & Đối soát (Reporting & Reconciliation):**
   - Báo cáo tiến độ giải ngân budget chiến dịch, số lượng vé đã phát theo ngày/kênh bank.
   - Xuất file đối soát dữ liệu tặng vé với các Ngân hàng đối tác và Core Ticketing.

### 2.2. Out-of-Scope (Phiên bản 1.0)
- Các chương trình tặng vé thủ công (đã có tính năng riêng).
- Tặng tiền trực tiếp vào tài khoản dự thưởng (Chương trình chỉ tập trung vào tặng vé sản phẩm Vietlott).

---

## 3. ĐẶC TẢ CHI TIẾT CỤM ĐIỀU KIỆN CẤU HÌNH (ADMIN CONFIGURATION)

| STT | Trụ Điều Kiện | Chi Tiết Cấu Hình | Mô Tả Nghiệp Vụ & Ràng Buộc |
| --- | --- | --- | --- |
| 1 | **Kênh đăng ký** | Multi-select dropdown (VPBank, VietinBank, MBBank, BIDV, SeABank, ALL...) | Chiến dịch chỉ áp dụng cho KH đăng ký mở tài khoản qua các kênh Bank được tick chọn. |
| 2 | **Trạng thái TK Dự thưởng** | Checklist (NEW, ACTIVE, HAU_KIEM...) | Trạng thái TK Vietlott SMS bắt buộc để được xét thưởng. (Chỉ tặng khi TK chuyển sang `ACTIVE`). |
| 3 | **Trạng thái TKNT** | Dropdown/Checklist (Đã liên kết, Đã xác thực, Ready...) | Trạng thái Tài khoản Nhận thưởng (TK Ngân hàng/Ví liên kết nhận tiền thưởng Auto-payout). |
| 4 | **Điều kiện thanh toán** | Radios / Checkbox + Input | - Không yêu cầu GD thanh toán.<br>- Hoặc Nạp tiền tối thiểu `X` VNĐ.<br>- Hoặc Phát sinh GD mua vé đầu tiên tối thiểu `Y` VNĐ. |
| 5 | **Vé tặng & Tần suất** | Dynamic inputs | - Loại vé (Power 6/55, Mega 6/45, Max 3D...).<br>- Giá trị vé (10,000 VNĐ, 20,000 VNĐ...).<br>- Hình thức số: Ngẫu nhiên (QuickPick) / KH tự chọn.<br>- Số lần tặng tối đa / KH (Mặc định: 1 lần/KH trong cả chiến dịch). |
| 6 | **Hạn mức người/ngày (Daily Cap)** | Numeric Input (VD: 500 người/ngày) | Số lượng KH đủ điều kiện nhận vé tối đa trong 1 ngày (00:00:00 - 23:59:59). Khi chạm mốc -> Dừng tặng trong ngày. |
| 7 | **Tổng Budget chiến dịch** | Currency Input (VD: 100,000,000 VNĐ) | Tổng ngân sách tối đa cấp cho chiến dịch. Hệ thống tự động DỪNG chiến dịch khi tổng giá trị vé phát đạt trần budget. |

---

## 4. QUY TRÌNH LUỒNG XỬ LÝ (SWIMLANE ACTIVITY DIAGRAM & BẢNG MÔ TẢ TỪNG BƯỚC)

### 4.1. Sơ đồ Activity Diagram dạng Swimlane (Draw.io Native XML & Codebase File)

> [!TIP]
> **Hướng dẫn Import & Chỉnh sửa trực tiếp trên Draw.io (app.diagrams.net / Draw.io Desktop):**
> 1. Truy cập [app.diagrams.net](https://app.diagrams.net) hoặc mở ứng dụng **Draw.io**.
> 2. Chọn **File** &rarr; **Open From** &rarr; **Device...** (hoặc chọn **Import from** &rarr; **Device...**).
> 3. Chọn file `activity_diagram_swimlane.drawio` (hoặc `activity_diagram_swimlane.xml`) được tạo sẵn trong thư mục `artifacts/requirements/`.
> 4. Sơ đồ sẽ hiển thị đầy đủ 3 làn Swimlane, 23 bước xử lý, nút Start/End, hình thoi điều kiện với các đường nối tự động căn chỉnh đẹp mắt.

- 🔗 **File Draw.io (.drawio):** [artifacts/requirements/activity_diagram_swimlane.drawio](file:///f:/VIETLOTT-SMS/artifacts/requirements/activity_diagram_swimlane.drawio)
- 🔗 **File Draw.io XML (.xml):** [artifacts/requirements/activity_diagram_swimlane.xml](file:///f:/VIETLOTT-SMS/artifacts/requirements/activity_diagram_swimlane.xml)
- 🖼️ **File Vector SVG:** [artifacts/requirements/activity_diagram_swimlane.svg](file:///f:/VIETLOTT-SMS/artifacts/requirements/activity_diagram_swimlane.svg)

---

### 4.2. Bảng Mô Tả Chi Tiết Từng Bước Nghiệp Vụ (Detailed Step-by-Step Business Description Table)

| Bước (#) | Tên Bước / Hành Động | Phân Hệ / Tác Nhân (Swimlane) | Đầu Vào (Input) / Điều Kiện | Nội Dung Xử Lý Nghiệp Vụ Chi Tiết | Đầu Ra (Output) / Dữ Liệu | Ngoại Lệ / Edge Cases |
| --- | --- | --- | --- | --- | --- | --- |
| **Bước 1** | Đăng ký mở TK mới | Khách hàng & Kênh Bank | SĐT, Giấy tờ cá nhân, Kênh Bank | Khách hàng truy cập ứng dụng Ngân hàng (VPBank, VietinBank...) thực hiện đăng ký tài khoản Vietlott SMS mới. | Hồ sơ đăng ký mới gửi về Vietlott SMS kèm `channel_code`. | Lỗi ngắt kết nối mạng Bank $\rightarrow$ Thông báo KH thử lại. |
| **Bước 2** | eKYC / Active / Thanh toán | Khách hàng & Kênh Bank | Kết quả duyệt eKYC, GD nạp/mua vé | KH hoàn tất xác thực eKYC. Trạng thái TKDT chuyển sang `ACTIVE` và thực hiện GD thanh toán (nếu có yêu cầu). | Event `ACCOUNT_ACTIVATED` được phát ra trên hệ thống. | TK bị chuyển sang `HAU_KIEM` $\rightarrow$ Tạm hoãn xét thưởng. |
| **Bước 3** | Thiết lập cụm 7 ĐK | Web Admin Vietlott SMS | Thông tin cấu hình từ Admin | Admin nhập Tên chiến dịch, chọn Kênh Bank, Trạng thái TK, TKNT, ĐK Thanh toán, Vé tặng, Daily Cap, Total Budget. | Dữ liệu nháp form cấu hình chiến dịch trên Web Admin. | Nhập thiếu thông tin bắt buộc $\rightarrow$ Highlight trường thiếu. |
| **Bước 4** | Lưu & Kích hoạt | Web Admin Vietlott SMS | Nút `Lưu & Kích hoạt` | Admin kiểm tra và xác nhận kích hoạt chiến dịch chạy tự động. | Yêu cầu Validate gửi về Backend Admin. | Mất session Admin $\rightarrow$ Yêu cầu đăng nhập lại. |
| **Bước 5** | Kiểm tra cấu hình | Web Admin Backend | Data form cấu hình | System kiểm tra Total Budget $\ge$ Giá trị 1 vé, Daily Cap $> 0$, thời gian hợp lệ. | Kết quả kiểm tra (Valid / Invalid). | - |
| **Bước 6** | Báo lỗi cấu hình | Web Admin UI | Kết quả Invalid từ Bước 5 | Hiển thị thông báo lỗi chi tiết trên màn hình (VD: *"Budget không đủ phát 1 vé"*). | Popup thông báo lỗi cho Admin. | Admin điều chỉnh lại số liệu tại Bước 3. |
| **Bước 7** | Chuyển `DANG_CHAY` | Web Admin Backend | Cấu hình Valid | Cập nhật trạng thái chiến dịch = `DANG_CHAY`, phát thông báo cho Event Bus kích hoạt Rule Engine. | Status chiến dịch = `DANG_CHAY`. | Đã có chiến dịch trùng kênh đang chạy $\rightarrow$ Cảnh báo ghi đè. |
| **Bước 8** | Lắng nghe Event | Realtime Rule Engine | Event `ACCOUNT_ACTIVATED` | Rule Engine nhận tín hiệu có KH vừa active tài khoản từ Kênh Bank. | Payload chứa `phone_number`, `channel_code`, `status`. | Event đến chậm $\rightarrow$ Queueing chờ xử lý theo sequence. |
| **Bước 9** | Validate TK & Kênh | Realtime Rule Engine | Payload Event + Config | Kiểm tra `channel_code` KH thuộc Kênh Bank cấu hình, TKDT = `ACTIVE`, TKNT đã liên kết/xác thực. | Valid (Đủ ĐK) hoặc Invalid (Không đủ). | KH mở qua kênh khác $\rightarrow$ Bỏ qua không tặng vé. |
| **Bước 10** | Log không đủ ĐK | Realtime Rule Engine | Kết quả Invalid từ Bước 9 | Ghi log nhật ký lý do từ chối (VD: `REJECTED_CHANNEL_NOT_MATCH` hoặc `TKNT_NOT_VERIFIED`). | Audit log record. | Không gửi SMS phiền khách hàng. |
| **Bước 11** | Kiểm tra Total Budget | Realtime Rule Engine | Total Budget & Spent Budget | Kiểm tra Ngân sách còn lại của chiến dịch: `Total_Budget - Total_Spent >= Ticket_Value`. | Đủ Budget hoặc Hết Budget. | - |
| **Bước 12** | Chuyển `DA_HET_BUDGET` | Realtime Rule Engine | Kết quả Hết Budget từ Bước 11 | Hệ thống tự động chuyển trạng thái chiến dịch = `DA_HET_BUDGET`, ngừng nhận yêu cầu mới, gửi email báo Admin. | Campaign Status = `DA_HET_BUDGET`. | Gửi email alert cho PM/Admin. |
| **Bước 13** | Kiểm tra Daily Cap | Realtime Rule Engine | Daily Cap & Issued Today | Kiểm tra số vé đã cấp trong ngày (00:00 - 23:59): `Issued_Today < Daily_Cap`. | Còn Quota Ngày hoặc Vượt Cap. | - |
| **Bước 14** | Kiểm tra Chính sách | Realtime Rule Engine | Cấu hình Policy Bảo lưu | Kiểm tra tham số `Is_Queue_Enabled` trong chiến dịch. | Option A (Bảo lưu) hoặc Option B (Mất lượt). | - |
| **Bước 15** | Log Exceeded Limit | Realtime Rule Engine | Option B (Không bảo lưu) | Ghi log từ chối cấp vé do hết hạn mức trong ngày. Không bảo lưu suất. | Audit log: `REJECTED_DAILY_CAP_EXCEEDED`. | Khách hàng không nhận được vé. |
| **Bước 16** | Đưa vào Queue chờ | Realtime Rule Engine | Option A (Có bảo lưu) | Lưu thông tin KH đủ điều kiện vào `daily_cap_pending_queue`. Chờ Midnight Job quét lúc 00:00:01 hôm sau. | Record trong Queue bảng tạm. | Chuyển sang Bước 16b (Thông báo bảo lưu). |
| **Bước 16b** | Nhận thông báo bảo lưu | Khách hàng & Kênh Bank | Event từ Queue Bước 16 | KH nhận tin nhắn SMS / Push Noti thông báo suất tặng vé được bảo lưu sang 00:00:01 ngày hôm sau. | SMS/Push Sent. | - |
| **Bước 17** | Atomic Lock Trừ Quota | Realtime Rule Engine | Redis Distributed Lock | Thực hiện khóa phân tán (Redis Lock) và trừ đồng thời `Total_Spent += 10,000` và `Issued_Today += 1`. | Transaction Lock thành công. | Race condition đồng thời $\rightarrow$ Lock thất bại, thử lại sau 100ms. |
| **Bước 18** | Gọi API Core Issue | Realtime Rule Engine | Ticket Payload | Gọi API `POST /core/ticketing/issue-promo-ticket` để Core sinh vé dự thưởng Vietlott. | Request API Core. | Core bận $\rightarrow$ Trigger Retry Protocol. |
| **Bước 19** | Kiểm tra kết quả Core | Realtime Rule Engine | API Response | Kiểm tra Response Code từ Core Ticketing (Success / Timeout / Failure). | Success hoặc Error. | - |
| **Bước 20** | Retry Queue / Pending | Realtime Rule Engine | Response Error / Timeout | Đưa bản tin vào `retry_ticket_queue`, thử lại tự động 3 lần (5m, 15m, 30m). Nếu thất bại $\rightarrow$ Ghi log `PENDING_RETRY_MANUAL`. | Log trạng thái lỗi & Retry Queue. | Hoàn trả Quota/Budget nếu thất bại vĩnh viễn. |
| **Bước 21** | Ghi Log & Cập nhật | Realtime Rule Engine | Response Success | Cập nhật bảng `gift_ticket_history`, tăng số tiền giải ngân realtime trên Dashboard Web Admin. | Record History & Dashboard updated. | - |
| **Bước 22** | Gửi lệnh Thông báo | Notification Engine | Ticket Details từ Core | Biên soạn tin nhắn chứa bộ số, loại vé, kỳ quay và gửi SMS Brandname / Push Notification cho KH. | SMS/Push Sent. | SMS lỗi $\rightarrow$ Tự động fallback sang Push App. |
| **Bước 23** | Nhận SMS/Push & Tra cứu | Khách hàng & Kênh Bank | SMS/Push từ Bước 22 | Khách hàng nhận SMS Brandname / Push Notification thông báo vé tặng thành công và vào App Vietlott SMS tra cứu bộ số dự thưởng. | Vé hiển thị trên App KH. | End Process ◉. |

---

## 5. PHÂN TÍCH PHẢN BIỆN, EDGE CASES & NGUY CƠ RỦI RO (RED FLAGS)

> [!WARNING]
>
> ### 🚨 CẢNH BÁO ĐỎ BA & NGUY CƠ TRỄ DEADLINE (Giao từ C.Hoài ngày 29/7, Triển khai đầu tháng 8)
>
> Thời gian triển khai chỉ còn 2-3 ngày làm việc. Luồng tặng vé tự động tiềm ẩn 2 rủi ro kỹ thuật trọng yếu: Concurrency (bùng nổ lượt mở TK từ Bank) và Race Condition trên Budget. BA kiến nghị chốt gấp các điểm mơ hồ dưới đây trong hôm nay.

### 5.1. Bảng Phân Tích Ngoại Lệ & Timeout (Exception Analysis & Hung State)

| # | Luồng/Bước | Sự Cố Tiềm Ẩn | Loại Rủi Ro | Giải Pháp Nghiệp Vụ Đề Xuất (BA Recommendation) |
| --- | --- | --- | --- | --- |
| 1 | Phát vé tự động | API Core Ticketing bị Timeout (>30s) hoặc bận | External Failure | **Retry Protocol:** Hệ thống thử lại tự động 3 lần (chu kỳ giãn cách 5m, 15m, 30m). Nếu vẫn lỗi, chuyển trạng thái `PENDING_RETRY_MANUAL` để Admin xem soát. **KHÔNG** phát trùng vé. |
| 2 | Trừ Budget / Daily Cap | 100 KH active đồng thời tại millisecond cuối cùng của Budget | Concurrency / Race Condition | **Atomic Lock / Redis Distributed Lock:** Đảm bảo kiểm tra và trừ Quota/Budget là 1 giao dịch nguyên tố (Atomic Transaction). Không để phát vượt quá 1 vé so với budget. |
| 3 | Hạn mức Ngày (Daily Cap) | KH active lúc 20:00 nhưng ngày hôm đó đã HẾT suất tặng (chạm Cap) | Logic Policy | **Cần chốt Policy:**<br>- *Option A (Bảo lưu):* Tự động chuyển suất của KH này sang 00:00:01 ngày hôm sau.<br>- *Option B (Mất quyền lợi):* Khách hàng không được tặng nữa.<br>=> **BA đề xuất Option A** để đảm bảo trải nghiệm khách hàng. |
| 4 | Trạng thái "Hậu kiểm" | TK bị đưa vào luồng Hậu kiểm do nghi ngờ gian lận/trùng thông tin | Risk/Fraud | Khi TK ở trạng thái `HAU_KIEM` -> **TẠM HOÃN** tặng vé. Sau khi Admin duyệt Hậu kiểm thành `ACTIVE` -> Hệ thống mới quét để tặng vé. |
| 5 | Hủy/Hoàn tiền giao dịch thanh toán | KH nạp tiền đủ điều kiện nhận vé, sau đó rút/hủy giao dịch | Fraud Loop | Vé tặng là **Vé không thể hoàn tiền/quy đổi cash**. Một khi vé đã tạo thành công trong Core thì không thu hồi vé đã tặng (trừ khi khóa tài khoản). |

---

## 6. CÂU HỎI LÀM RÕ DÀNH CHO STAKEHOLDER (ASK DON'T ASSUME)

Để hoàn thiện SRS chính thức trình duyệt, BA cần Chị Hoài & Team xác nhận 5 câu hỏi then chốt:

> [!IMPORTANT]
>
> 1. **Khái niệm TKNT:** `Trạng thái TKNT` trong tin nhắn của chị Hoài chính xác là **Tài khoản Ngân hàng liên kết** (xác thực liên kết thành công) hay là **Tài khoản Nhận thưởng** trên Vietlott SMS?
> 2. **Chính sách khi hết Quota Ngày (Daily Cap):** Khi số lượng mở mới trong ngày vượt Daily Cap, KH đủ điều kiện phát sinh sau đó sẽ **được bảo lưu chờ phát vào ngày hôm sau** hay **bị mất lượt tặng vé**?
> 3. **Hình thức Vé Tặng:** Vé tặng cho KH là loại vé gì (Power 6/55, Mega 6/45, Max 3D...)? Số trên vé là **Ngẫu nhiên (QuickPick do hệ thống sinh)** hay **Cho phép KH chọn số**?
> 4. **Trạng thái Hậu Kiểm:** Khách hàng thuộc diện Hậu kiểm sau khi được duyệt thành công (Active) thì có được tặng vé bổ sung bù không?
> 5. **Điều kiện thanh toán:** Cụ thể điều kiện thanh toán áp dụng cho chiến dịch đầu tháng 8 này là gì (VD: Chỉ cần liên kết Bank, hay phải nạp tối thiểu 10k/50k)?

---

## 7. USER STORIES & ACCEPTANCE CRITERIA (BDD FORMAT)

### User Story 1: Admin cấu hình chiến dịch tặng vé mở mới từ Kênh Bank

**As a** Quản trị viên hệ thống (Admin Vietlott SMS),  
**I want to** thiết lập chiến dịch tặng vé tự động với các tiêu chí (Kênh bank, Trạng thái TK, Điều kiện thanh toán, Giá trị vé, Daily Cap, Total Budget),  
**So that** hệ thống tự động chạy khuyến mại đúng đối tượng và kiểm soát chặt chẽ ngân sách.

#### Acceptance Criteria (AC):

- **Scenario 1 (Happy Path - Tạo mới thành công):**
  - **Given** Admin đang ở màn hình Cấu hình Chiến dịch Khuyến mại,
  - **When** Admin nhập đầy đủ thông tin: Tên chiến dịch, Chọn Kênh Bank (`VPBank`, `VietinBank`), Trạng thái TK (`ACTIVE`), Trạng thái TKNT (`Đã xác thực`), Giá trị vé (`10,000 VNĐ`), Daily Cap (`500 người/ngày`), Total Budget (`50,000,000 VNĐ`),
  - **And** nhấn nút `Lưu & Kích hoạt`,
  - **Then** Hệ thống chuyển trạng thái chiến dịch thành `DANG_CHAY`, bắt đầu kích hoạt job quét tặng vé tự động.

- **Scenario 2 (Validation Error - Budget không hợp lệ):**
  - **Given** Admin đang cấu hình chiến dịch,
  - **When** Admin nhập Total Budget nhỏ hơn Giá trị 1 vé tặng (hoặc nhập số âm/chữ),
  - **Then** Hệ thống hiển thị thông báo lỗi: *"Tổng ngân sách phải lớn hơn hoặc bằng giá trị 1 vé tặng (tối thiểu 10,000 VNĐ)"* và không cho phép lưu.

---

### User Story 2: Hệ thống tự động xét duyệt và tặng vé cho KH active mới

**As a** Khách hàng mở tài khoản mới qua kênh Bank,  
**I want to** nhận được vé dự thưởng tặng tự động ngay khi hoàn tất kích hoạt tài khoản và đủ điều kiện,  
**So that** tôi có trải nghiệm liền mạch và trải nghiệm sản phẩm Vietlott.

#### Acceptance Criteria (AC):

- **Scenario 1 (Happy Path - Tặng vé tự động thành công):**
  - **Given** Chiến dịch tặng vé Kênh Bank đang ở trạng thái `DANG_CHAY` và còn Budget/Daily Cap,
  - **When** Khách hàng A mở tài khoản từ kênh VPBank và hoàn tất chuyển trạng thái sang `ACTIVE` + thỏa điều kiện thanh toán,
  - **Then** Hệ thống tự động cấp 01 vé dự thưởng 10,000 VNĐ cho Khách hàng A,
  - **And** Gửi tin nhắn SMS/Push: *"Chao muong ban den voi Vietlott SMS! Ban da duoc tang 01 ve du thuong [Loai ve] tri gia 10k..."*,
  - **And** Tự động cộng 1 vào lượt tặng trong ngày và trừ 10,000 VNĐ vào Total Budget.

- **Scenario 2 (Edge Case - Chạm trần Total Budget):**
  - **Given** Total Budget còn lại của chiến dịch chỉ đủ cho 1 vé (10,000 VNĐ),
  - **When** Có 2 khách hàng B và C đồng thời active tài khoản,
  - **Then** Hệ thống chỉ cấp vé thành công cho 1 khách hàng (bằng Atomic Lock),
  - **And** Khách hàng còn lại không được cấp vé, hệ thống tự động chuyển trạng thái chiến dịch sang `DA_HET_BUDGET` và dừng phát vé.

---

### User Story 3: Luồng Gửi Thông báo Tặng vé (SMS / Push Notification)

**As a** Khách hàng đủ điều kiện nhận vé tặng từ kênh Bank,  
**I want to** nhận được tin nhắn SMS / Push Notification tức thì chứa thông tin chi tiết vé tặng (loại vé, bộ số, kỳ quay),  
**So that** tôi biết mình đã được tặng vé thành công và có thể theo dõi kết quả quay số mở thưởng.

#### Acceptance Criteria (AC):

- **Scenario 1 (Happy Path - Gửi SMS / Push Notification tặng vé thành công):**
  - **Given** Hệ thống Core Ticketing vừa tạo vé dự thưởng thành công cho Khách hàng A,
  - **When** Event `TICKET_ISSUED_SUCCESS` được phát ra,
  - **Then** Notification Engine tự động biên soạn tin nhắn chứa các biến: `@LOAI_VE@`, `@MANG_SO@`, `@KY_QUAY@`,
  - **And** Gửi tin nhắn SMS qua Brandname Vietlott SMS (hoặc Push Noti trên App): *"Vietlott SMS: Chúc mừng Quý khách nhận được 01 vé [LoaiVe] bộ số [BoSo] kỳ quay [KyQuay]. Chúc Quý khách may mắn!"*,
  - **And** Ghi nhận trạng thái gửi thành công vào nhật ký `sms_noti_history`.

- **Scenario 2 (Alternative Path - Thông báo hàng chờ khi vượt Daily Cap):**
  - **Given** Khách hàng B đủ điều kiện nhưng ngày hôm đó đã HẾT lượt Daily Cap (Option A - Bảo lưu),
  - **When** Hệ thống đưa yêu cầu tặng vé của Khách hàng B vào Queue ngày hôm sau,
  - **Then** Notification Engine gửi Push Noti/SMS thông báo: *"Vietlott SMS: Quý khách đã đủ điều kiện nhận vé tặng. Suất tặng vé của Quý khách sẽ được gửi tặng tự động vào ngày mai do số lượng tặng trong ngày đã hết. Trân trọng!"*.

- **Scenario 3 (Exception Path - SMS Gateway bị ngắt kết nối / Lỗi đối tác):**
  - **Given** SMS Gateway của nhà mạng bị ngắt kết nối khi đang gửi tin nhắn tặng vé,
  - **When** Notification Engine nhận mã lỗi Timeout / Fail từ SMS Brandname,
  - **Then** Hệ thống tự động chuyển luồng dự phòng sang gửi In-App Push Notification (nếu KH đã tải App),
  - **And** Đưa bản tin SMS lỗi vào Hàng chờ Retry gửi lại sau 15 phút.

---

### User Story 4: Luồng Báo cáo Tiến độ Giải ngân & Đối soát Kênh Bank

- **As a** Quản trị viên hệ thống / Chuyên viên Kế toán Vietlott SMS,
- **I want to** xem báo cáo thống kê tiến độ giải ngân ngân sách chiến dịch, số lượng vé phát theo từng Kênh Bank và xuất file đối soát,
- **So that** tôi kiểm soát chính xác số lượng vé giải ngân và thực hiện đối soát tài chính định kỳ với các Ngân hàng đối tác.

#### Acceptance Criteria (AC)

- **Scenario 1 (Happy Path - Xem Dashboard Báo cáo Giải ngân Realtime):**
  - **Given** Admin / Kế toán đăng nhập vào Web Admin và truy cập menu `Báo cáo Chiến dịch Kênh Bank`,
  - **When** Chọn chiến dịch "Tặng vé Mở tài khoản VPBank/VietinBank Tháng 8/2026",
  - **Then** Hệ thống hiển thị Dashboard với các chỉ số realtime:
    - **Tổng Ngân sách:** `$50.000.000$ VNĐ` | **Đã giải ngân:** `$32.400.000$ VNĐ` ($64.8\%$) | **Còn lại:** `$17.600.000$ VNĐ`.
    - **Hạn mức hôm nay (Daily Cap):** $500$ vé | **Đã phát hôm nay:** $342$ vé.
    - **Bảng phân rã theo Kênh Bank:** Tỷ lệ số người nhận vé của từng Bank (VPBank: $40\%$, VietinBank: $35\%$, MBBank: $25\%$).

- **Scenario 2 (Happy Path - Xuất File Báo cáo Đối soát với Kênh Bank):**
  - **Given** Chuyên viên Kế toán cần đối soát số liệu tặng vé với VPBank cuối tháng,
  - **When** Chọn khung thời gian từ `01/08/2026` đến `31/08/2026`, lọc kênh `VPBank` và nhấn `Xuất Excel Đối Soát`,
  - **Then** Hệ thống xuất file Excel chuẩn gồm các trường: `STT`, `Mã GD Tặng`, `SĐT KH (Masking)`, `Mã KH Bank`, `Ngày Active`, `Mã Vé Dự Thưởng`, `Giá Trị Vé`, `Trạng Thái Phát Vé`, `Thời Gian SMS Sent`.

- **Scenario 3 (Validation & Warning - Cảnh báo ngưỡng Ngân sách 80% & 95%):**
  - **Given** Chiến dịch đang chạy và Tổng budget đã sử dụng đạt $80\%$ (và $95\%$),
  - **When** Realtime Engine trừ tiền ngân sách chạm mốc $80\%$ ($40.000.000$ VNĐ),
  - **Then** Hệ thống tự động gửi Email & Push Notification cảnh báo cho Admin/PM: *"CANH BAO: Chiet dich Tang ve Kenh Bank [TenCampaign] da giai ngan dat 80% tong budget (40/50 trieu). Vui long xem xet gia han budget hoac chuan bi dong chiet dich."*.

---

## 7. YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL REQUIREMENTS - NFR)

- **NFR-01 (Hiệu năng):** Thời gian xử lý kiểm tra điều kiện và phát vé tự động từ khi nhận event tài khoản Active không quá 3 giây.
- **NFR-02 (Tải hệ thống):** Engine tặng vé chịu tải tối thiểu 500 sự kiện/giây trong các khung giờ cao điểm đăng ký mở tài khoản.
- **NFR-03 (Bảo mật & PII):** Toàn bộ thông tin số điện thoại khách hàng và tài khoản ngân hàng phải được che giấu (masking) theo Nghị định 13/2023/NĐ-CP trên toàn bộ giao diện Admin và file đối soát xuất ra.
- **NFR-04 (Tính toàn vẹn ngân sách):** Cơ chế trừ ngân sách chiến dịch phải đảm bảo tính nguyên tử (Atomicity) và chống trùng đơn (Idempotency), tuyệt đối không để phát vượt hạn mức Daily Cap và Total Budget đã thiết lập.

---

## 8. HƯỚNG DẪN BÀN GIAO VÀ BƯỚC TIẾP THEO

- **File tài liệu:** `artifacts/requirements/srs-campaign-tang-ve-bank.md` (Trạng thái: `Draft`)
- **Bước tiếp theo:**
  1. Trình duyệt file nháp với Chị Hoài & Team để chốt 5 câu hỏi làm rõ (§6).
  2. Phê duyệt tài liệu để chuyển sang trạng thái `Approved` hoặc `Baseline` sau khi Quality Gate PASS.
  3. Chuyển giao cho Designer thiết kế màn hình Admin & SA thiết kế API/DB schema.
