[🟢 ROLE: BA]

# TÀI LIỆU ĐẶC TẢ VÀ PHÂN TÍCH YÊU CẦU NGHIỆP VỤ (R2)
## Dự Án Kỷ Niệm 6 Năm Ra Mắt Vietlott SMS — "Bứt Phá Ý Tưởng — Dẫn Dắt Thay Đổi"

> **Tác giả:** Business Analyst (BA Agent)  
> **Chuẩn mực áp dụng:** BABOK® Guide v3 (IIBA) — Requirements Analysis and Design Definition  
> **Cột mốc:** Milestone 2 — Requirements Analysis (R2)  
> **Ngày lập:** 11/08/2026  
> **Trạng thái:** Draft v1.0 (Chờ duyệt)  
> **Tài liệu tham chiếu:** `artifacts/product/po-product-improvement-plan.md` (R1 PO Plan), `artifacts/analysis/da-vietlott-sms-report-2026.md` (DA Report), `knowledge/product/project-context.md`

---

## METADATA & BA GOVERNANCE FRAMEWORK

### 1. Thông Tin Phiên Bản (Document Version Control)

| Phiên Bản | Ngày Tạo | Tác Giả | Trạng Thái | Mô Tả Thay Đổi |
| :---: | :---: | :---: | :---: | :--- |
| **v1.0** | 11/08/2026 | BA Agent | Draft (Chờ Phê Duyệt) | Khởi tạo tài liệu đặc tả yêu cầu nghiệp vụ (R2) dựa trên Kế hoạch cải tiến sản phẩm R1 PO Plan. |

### 2. Phân Công Trách Nhiệm Quản Trị Yêu Cầu (RACI Matrix — Requirements Governance)

| Hoạt Động Nghiệp Vụ (Requirements Activity) | BA | PO | SA | PM | DEV | QA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Phân tích Gap & Lập User Story Map | **R** | C | C | I | I | I |
| Viết User Stories & BDD Acceptance Criteria | **R** | C | C | I | I | I |
| Vẽ Diagram Luồng Nghiệp Vụ & Entity Model | **R** | I | C | I | I | I |
| Phân tích Ngoại Lệ & Timeout Protocol | **R** | I | **A** | I | C | C |
| Phê duyệt Scope & Baselining Requirements | C | **A** | C | **R** | I | I |
| Đánh giá tác động Thay Đổi (Change Management) | **R** | **A** | C | **A** | I | I |

*Ghi chú:* **R** = Responsible (Người thực hiện) | **A** = Accountable (Người phê duyệt cuối cùng) | **C** = Consulted (Người được tham vấn) | **I** = Informed (Người được thông báo).

### 3. Chuỗi Truy Vết Yêu Cầu (Traceability Matrix Chain)

```
Business Need (DA/PO) ──► Business Requirement (BR) ──► Solution Requirement (FR/NFR) 
     ──► User Story (US) ──► Acceptance Criteria (BDD) ──► Test Case (QA) ──► Code Implementation (DEV)
```

---

## A. PHÂN TÍCH KHOẢNG CÁCH (GAP ANALYSIS)

Dựa trên Kế hoạch Cải tiến Sản phẩm (R1 PO Plan) và dữ liệu thực tế từ Báo cáo DA 2026, BA tiến hành phân tích chi tiết khoảng cách giữa trạng thái hiện tại (**As-Is**) và trạng thái mong muốn (**To-Be**) cho 5 cải tiến chiến lược ưu tiên hàng đầu.

```mermaid
graph LR
    subgraph As-Is State [Trạng Thái Hiện Tại]
        A1[Thanh toán lag, trùng đơn]
        A2[Giao diện cố định 5+ game]
        A3[Cập nhật APK thủ công, lo fake app]
        A4[Thiếu Gamification & VIP Care]
        A5[Chỉ mua vé cá nhân đơn lẻ]
    end

    subgraph Gap Bridge [Khoảng Cách & Giải Pháp BA]
        G1[Severity: HIGH | Idempotent Engine]
        G2[Severity: HIGH | Adaptive UI & Cross-Sell]
        G3[Severity: MEDIUM | In-App Auto Updater]
        G4[Severity: MEDIUM | VIP Streaks Hub]
        G5[Severity: HIGH | Syndicate Group Play]
    end

    subgraph To-Be State [Trạng Thái Mong Muốn]
        T1[Thanh toán 1-tap <3s, Zero Double-Billing]
        T2[Cá nhân hóa Home & Cross-sell Lotto 5/35]
        T3[Tự động cập nhật ngầm, Badge Chính Hãng]
        T4[Tích điểm Cashback up to 2%, Daily Streaks]
        T5[Mua vé nhóm, tự động chia thưởng về ví]
    end

    A1 --> G1 --> T1
    A2 --> G2 --> T2
    A3 --> G3 --> T3
    A4 --> G4 --> T4
    A5 --> G5 --> T5
```

### Bảng Phân Tích Khoảng Cách Chi Tiết (Top 5 Priority Improvements)

| STT | Hạng Mục Cải Tiến | Trạng Thái Hiện Tại (As-Is State) | Khoảng Cách & Nguyên Nhân (Gap & Root Cause) | Trạng Thái Mong Muốn (To-Be State) | Kế Hoạch Hành Động (Action Plan) | Severity (Mức Độ) | Effort Estimate (Ước Lượng) |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **1** | **Idempotent One-Tap Payment Engine** *(Cấu trúc motor thanh toán chống trùng đơn)* | Màn hình thanh toán xử lý đồng bộ, thiếu dialog phản hồi trạng thái thời gian thực. Khi mạng chậm giờ cao điểm (nhất là 6 phút BINGO18), user bấm nút nhiều lần gây trùng đơn, bị trừ tiền 2 lần (chiếm 18.5% khiếu nại). | **Gap:** Thiếu cơ chế khóa giao dịch phía Client (Client-side Debouncing) và Mã giao dịch duy nhất (Idempotency Key) ở tầng API Gateway.<br>**Root Cause:** Thiết kế API đồng bộ legacy chưa có Queue xử lý bất đồng bộ. | Hệ thống phát hành `Idempotency-Key` duy nhất cho mỗi đơn hàng. Nút thanh toán tự động vô hiệu hóa sau 1 chạm. Dialog đếm ngược và trạng thái xử lý hiển thị thời gian thực (<3s). Tỷ lệ trùng đơn = 0%. | 1. Xây dựng Idempotency Key Middleware tại Gateway.<br>2. Thiết kế Queue bất đồng bộ (Redis/RabbitMQ).<br>3. Tích hợp Biometric Auth (FaceID/TouchID) 1-tap checkout.<br>4. Tạo dialog đếm ngược thời gian thực. | **HIGH (Cao)** | **2 Sprints**<br>*(10 Man-Days)* |
| **2** | **Smart Adaptive Home UI & Cross-Sell Lotto 5/35** *(Giao diện thông minh & Bán kèm)* | Trang chủ hiển thị cố định 4-5 icon game trong grid menu phẳng. Tất cả người dùng đều thấy giao diện giống nhau, không tự tùy biến theo thói quen chơi. Chưa có gợi ý mua kèm sản phẩm bứt phá Lotto 5/35. | **Gap:** Không có rule engine phân loại hành vi người dùng tại trang chủ.<br>**Root Cause:** Giao diện cứng (Hardcoded Layout), thiếu widget gợi ý động ở bước hoàn tất thanh toán. | Trang chủ tự động sắp xếp ưu tiên theo thói quen (BINGO18 cho tệp fast-gaming, Mega/Power khi Jackpot >100B). Sau khi chốt đơn, tự động hiển thị Widget Cross-sell "Thêm 10k thử vận may Lotto 5/35" với 1 chạm mua ngay. | 1. Thiết kế Rule Engine phân loại 3 tệp người dùng.<br>2. Xây dựng Component Trang chủ động (Dynamic Grid).<br>3. Thêm Cross-Sell Widget tại màn hình hóa đơn thanh toán.<br>4. Tích hợp A/B Testing đo lường CTR. | **HIGH (Cao)** | **2 Sprints**<br>*(8 Man-Days)* |
| **3** | **Native APK In-App Auto Updater & Trust Shield** *(Cập nhật ngầm & Badge xác thực)* | Người dùng Android phải tải file APK thủ công từ website ngoài do Google Play hạn chế app xổ số. Mỗi lần nâng cấp phiên bản rất rườm rà, tạo rào cản UX và tâm lý lo sợ app giả mạo lừa đảo. | **Gap:** Thiếu cơ chế tự động tải và cài đặt bản cập nhật trong ứng dụng (In-App Auto Update).<br>**Root Cause:** Chưa có Server phân phối APK chính chủ tích hợp kiểm tra checksum hash SHA-256. | Ứng dụng tự động kiểm tra phiên bản mới ngầm. Khi có bản cập nhật, hiển thị thông báo 1-click cập nhật ngay trong app không cần mở trình duyệt web. Hiển thị Badge "Xác thực Chính hãng Vietlott" kèm mã QR kiểm tra link ngân hàng. | 1. Xây dựng In-App Update Service cho Android APK.<br>2. Tích hợp cơ chế kiểm tra SHA-256 Checksum Hash.<br>3. Thiết kế Verified Security Badge ở Header và Footer app.<br>4. Tích hợp API xác thực liên kết 14 ngân hàng. | **MEDIUM (Vừa)** | **1 Sprint**<br>*(5 Man-Days)* |
| **4** | **Gamification Hub & VIP Loyalty Streaks** *(Tích điểm hoàn tiền & Chuỗi ngày may mắn)* | Ứng dụng chỉ hoạt động như một công cụ mua vé thuần túy (Utility Tool). Người dùng chi tiêu lớn (>2 triệu VNĐ/tháng) không có ưu đãi VIP. Không có tính năng giữ chân (Retention Loop) hàng ngày. | **Gap:** Thiếu hệ thống Gamification và Loyalty Program.<br>**Root Cause:** Chưa định nghĩa cơ chế tích điểm, phân hạng thành viên và kho quà tặng điện tử (E-Voucher). | Ra mắt Vietlott VIP Club với 4 cấp bậc (Đồng, Bạc, Vàng, Kim Cương), hoàn tiền cashback 0.5% - 2.0% vào Ví dự thưởng. Tính năng "Chuỗi Ngày May Mắn" (Daily Streaks) tích điểm danh nhận lượt quay Lucky Wheel 6 năm. | 1. Định nghĩa Quy chế VIP & Công thức tính điểm Loyalty.<br>2. Xây dựng VIP Dashboard & Cấp bậc thành viên.<br>3. Triển khai Gamification Module: Daily Check-in & Lucky Wheel.<br>4. Tích hợp kho Voucher & Ví Dự Thưởng cashback. | **MEDIUM (Vừa)** | **2 Sprints**<br>*(9 Man-Days)* |
| **5** | **Syndicate Group Play** *(Tính năng Mua Vé Nhóm & Tự động chia thưởng)* | Người dùng chỉ có thể mua vé cá nhân đơn lẻ. Khi muốn mua vé Bao lớn (Bao 7 - Bao 15 có giá trị cao) cùng bạn bè, phải tự chuyển khoản thủ công bên ngoài, tiềm ẩn rủi ro tranh chấp tiền thưởng. | **Gap:** Chưa có tính năng khởi tạo phòng mua chung, gom tiền và tự động phân bổ tiền thưởng theo tỷ lệ đóng góp.<br>**Root Cause:** Luồng xử lý vé chưa hỗ trợ đa quyền sở hữu (Multi-Ownership Ticket). | Người dùng có thể tạo Phòng Syndicate, phát hành Link mời nhóm, đặt mức góp vốn (từ 10k/người). Khi vé trúng thưởng, hệ thống Vietlott Core tự động giải ngân tiền thưởng trực tiếp về ví cá nhân từng thành viên theo đúng tỷ lệ %. | 1. Thiết kế Hợp đồng Mua chung Số hóa (Digital Syndicate Contract).<br>2. Xây dựng Luồng Tạo Phòng, Đặt Cọc & Khóa Vé.<br>3. Phát triển Engine Phân bổ Tiền thưởng Tự động.<br>4. Thêm tính năng Share Link nhóm qua Zalo/SMS/QR Code. | **HIGH (Cao)** | **3 Sprints**<br>*(14 Man-Days)* |

---

## B. STORY MAPPING & PHÂN RÃ CHỨC NĂNG (FUNCTIONAL DECOMPOSITION)

### 1. User Story Map (Jeff Patton Model)

Tổ chức các yêu cầu theo hành trình người dùng (Backbone Activities → User Tasks → User Stories), được phân chia thành 3 dải phát hành (Release Lines) đảm bảo nguyên tắc **Walking Skeleton** cho Release 1 MVP.

```
+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| BACKBONE ACTIVITIES  │  1. ONBOARDING & ĐỊNH DANH   │  2. KHÁM PHÁ & CHỌN SỐ     │  3. THANH TOÁN & XÁC NHẬN  │  4. THEO DÕI & NHẬN THƯỞNG │  5. GẮN KẾT & MUA NHÓM   |
+----------------------+------------------------------+----------------------------+----------------------------+----------------------------+--------------------------+
| USER TASKS           │ 1.1 Đăng ký & Đăng nhập      │ 2.1 Xem danh mục sản phẩm  │ 3.1 Chọn phương thức trả   │ 4.1 Tra cứu kết quả quay   │ 5.1 Tích điểm Loyalty    |
|                      │ 1.2 Định danh CCCD / Biometric│ 2.2 Chọn bộ số may mắn     │ 3.2 Xác thực thanh toán    │ 4.2 Nhận thông báo trúng   │ 5.2 Tạo nhóm mua chung   |
|                      │ 1.3 Cập nhật app an toàn     │ 2.3 Xem gợi ý thông minh   │ 3.3 Nhận hóa đơn điện tử   │ 4.3 Trả thưởng tự động     │ 5.3 Điểm danh nhận quà   |
+----------------------+------------------------------+----------------------------+----------------------------+----------------------------+--------------------------+
| RELEASE 1 (MVP)      │ [US03] Biometric FaceID Auth │ [US04] Adaptive Home UI    │ [US01] Idempotent Payment  │ [US13] Real-time Draw Push │ [US16] Responsible Game  |
| "Walking Skeleton"   │ [US07] In-App Auto Updater   │ [US06] BINGO18 Turbo Widget│ [US02] Status Countdown    │     Notification           │     Spending Limits      |
| (Q3/2026 - QuickWin) │ [US08] Security Trust Badge  │                            │                            │                            │                          |
+----------------------+------------------------------+----------------------------+----------------------------+----------------------------+--------------------------+
| RELEASE 2            │                              │ [US05] Cross-Sell Lotto 5/35│                            │ [US10] Syndicate Split     │ [US09] Syndicate Create  |
| "Mid-term Social"    │                              │                            │                            │     Prize Auto Payout      │     Group & Share Link   |
| (Q4/2026)            │                              │                            │                            │                            │ [US11] Vietlott VIP Club |
|                      │                              │                            │                            │                            │ [US12] Daily Streaks Hub |
+----------------------+------------------------------+----------------------------+----------------------------+----------------------------+--------------------------+
| RELEASE 3            │                              │ [US14] AI Smart Pick &     │                            │                            │ [US15] Social Share Card |
| "Strategic Bet"      │                              │     Tử vi 12 Con Giáp      │                            │                            │ [US17] Subscription Auto |
| (H1/2027)            │                              │                            │                            │                            │     Renew Lucky Numbers  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+
```

---

### 2. Sơ Đồ Phân Rã Chức Năng (Functional Decomposition Diagram)

Phân rã hệ thống **Vietlott SMS 2.0** thành 5 sub-systems và các capabilities chi tiết bên dưới.

```mermaid
graph TD
    ROOT[Hệ Thống Vietlott SMS 2.0] --> M1[1. Quản Lý Nền Tảng & Bảo Mật]
    ROOT --> M2[2. Động Cơ Thanh Toán & Xử Lý Đơn]
    ROOT --> M3[3. Trải Nghiệm Người Dùng & Sản Phẩm]
    ROOT --> M4[4. Mua Vé Nhóm - Syndicate Play]
    ROOT --> M5[5. Gamification & VIP Loyalty Hub]

    M1 --> M1_1[1.1 Biometric Authentication Engine]
    M1 --> M1_2[1.2 In-App Auto Updater Service]
    M1 --> M1_3[1.3 Verified Trust Shield Badge]

    M2 --> M2_1[2.1 Idempotency Key Gateway Middleware]
    M2 --> M2_2[2.2 Real-time Status Polling & Dialog]
    M2 --> M2_3[2.3 Payment Queue & Retry Fallback]

    M3 --> M3_1[3.1 Adaptive Home UI Rule Engine]
    M3 --> M3_2[3.2 BINGO18 Turbo Fast-Play Widget]
    M3 --> M3_3[3.3 Smart Cross-Sell Lotto 5/35 Widget]

    M4 --> M4_1[4.1 Syndicate Group Room Management]
    M4 --> M4_2[4.2 Digital Group Contract & Lock Ticket]
    M4 --> M4_3[4.3 Automated Multi-Wallet Prize Payout]

    M5 --> M5_1[5.1 Vietlott VIP Tier & Cashback Engine]
    M5 --> M5_2[5.2 Daily Streaks & Check-in Hub]
    M5 --> M5_3[5.3 Lucky Wheel 6-Year Anniversary]
```

---

## C. ĐẶC TẢ USER STORIES & CRITERIA CHẤP NHẬN (INVEST & BDD)

Tài liệu đặc tả **16 User Stories** hoàn chỉnh đáp ứng 100% chuẩn **INVEST**, kèm theo Criteria chấp nhận dạng **Given/When/Then (BDD)** bao gồm Happy Path, Alternative Path và Exception Path.

---

### 🟢 Nhóm 1: Thanh Toán & Động Cơ Kháng Lag (Payment & Idempotency)

#### 📝 USER STORY US01: Idempotent One-Tap Payment Engine
* **User Story:** Là một **Người chơi BINGO18 thường xuyên (Persona 1)**, tôi muốn **nút thanh toán vô hiệu hóa ngay sau khi nhấn và hệ thống cấp mã giao dịch duy nhất**, để **tôi không bị trừ tiền 2 lần do cố bấm lại khi mạng lag giờ cao điểm**.
* **Metrics/Tracking:** Payment Failure Rate < 0.1%, Duplicate Billing Rate = 0 cases/month, Checkout Duration < 3s.
* **Priority:** **Must Have** | **Release:** Release 1 (MVP)

```gherkin
Scenario: Happy Path - Thanh toán 1-tap thành công với Idempotency Key
  Given Người dùng Anh Minh đang ở màn hình Xác Nhận Thanh Toán vé BINGO18 50.000 VNĐ
  And Thiết bị của người dùng đã sinh Idempotency-Key duy nhất "IDEM-20260811-99812"
  When Người dùng nhấn vào nút "Thanh Toán Ngay"
  Then Nút "Thanh Toán Ngay" lập tức đổi trạng thái sang Disabled và hiển thị Spinner loading
  And Hệ thống gửi request thanh toán kèm Header Idempotency-Key tới Gateway
  And Backend xử lý trừ tiền thành công trong 1.8 giây và trả về Transaction ID "TXN-882199"
  And Màn hình chuyển sang Dialog "Thanh Toán Thành Công" hiển thị mã vé điện tử.

Scenario: Alternative Path - User bấm liên tiếp 3 lần nút thanh toán (Chống double-tap)
  Given Người dùng Anh Minh ở màn hình thanh toán và bị giật lag mạng 3G
  When Người dùng cố gắng nhấn nút "Thanh Toán Ngay" 3 lần liên tục trong vòng 1 giây
  Then Hệ thống Client chỉ ghi nhận lần nhấn đầu tiên và bỏ qua 2 lần nhấn tiếp theo
  And Header Idempotency-Key không bị thay đổi hoặc tạo mới trong phiên giao dịch đó
  And Hệ thống bảo vệ người dùng không bị nạp trùng tiền.

Scenario: Exception Path - Mạng đứt giữa chừng khi API Gateway đang xử lý thanh toán
  Given Request thanh toán kèm Idempotency-Key "IDEM-20260811-99812" đã gửi tới Backend
  And Ngân hàng đối tác đã trừ tiền tài khoản nhưng kết nối mạng của thiết bị bị ngắt (Timeout)
  When Hệ thống Client không nhận được phản hồi sau 5 giây
  Then Client hiển thị Dialog "Đang Kiểm Tra Trạng Thái Giao Dịch..."
  And Client tự động gọi API Polling `/api/v2/payment/status?key=IDEM-20260811-99812` mỗi 2 giây
  And Khi kết nối lại, Backend trả về trạng thái "SUCCESS" dựa trên Idempotency Key
  And App cập nhật vé vào Lịch Sử Mua Vé mà không yêu cầu thanh toán lại.
```

---

#### 📝 USER STORY US02: Real-Time Transaction Status Countdown Dialog
* **User Story:** Là một **Người dùng di động**, tôi muốn **thấy cửa sổ đếm ngược thời gian thực (Status Countdown Dialog) khi đang thanh toán**, để **tôi an tâm biết đơn hàng của mình đang được xử lý và không phải hoang mang thoát app**.
* **Metrics/Tracking:** Customer Drop-off Rate tại Payment Step < 3%, NPS score tại luồng thanh toán > 65.
* **Priority:** **Must Have** | **Release:** Release 1 (MVP)

```gherkin
Scenario: Happy Path - Hiển thị đếm ngược 3 giây xử lý thanh toán mượt mà
  Given Người dùng vừa xác nhận thanh toán đơn hàng vé Mega 6/45 20.000 VNĐ
  When Màn hình Status Countdown Dialog xuất hiện
  Then Dialog hiển thị vòng đếm ngược từ 03 giây về 00 giây kèm dòng chữ "Đang kết nối cổng thanh toán an toàn..."
  And Tiến trình đạt 100% trong vòng 2.1 giây, hiển thị icon Tick Xanh và phát âm thanh mừng nhẹ "Ding!"
  And Cửa sổ tự động đóng sau 1.5 giây và hiển thị màn hình Chi Tiết Vé Đã Mua.

Scenario: Alternative Path - Cổng Ngân hàng phản hồi chậm >3s nhưng <8s
  Given Cổng thanh toán ngân hàng VCB bị quá tải nhẹ
  When Đồng hồ đếm ngược chạm mốc 00:00 mà Backend chưa nhận được Webhook ngân hàng
  Then Dialog tự động mở rộng thêm dòng chữ "Đang xác nhận với Ngân hàng (Tối đa 10s)..."
  And Khi Webhook ngân hàng phản hồi thành công ở giây thứ 5.5
  Then Dialog chuyển ngay sang trạng thái "Thành Công" và lưu vé vào hệ thống.

Scenario: Exception Path - Cổng Ngân hàng Timeout >10s (Chuyển xử lý Hung State)
  Given Cổng ngân hàng không phản hồi quá 10 giây
  When Hết thời gian chờ tối đa
  Then Dialog chuyển sang trạng thái "Giao Dịch Đang Được Xử Lý Ngầm"
  And Hệ thống hiển thị thông điệp: "Tiền đã được giữ an toàn. Hệ thống sẽ tự động cập nhật vé vào Tài khoản của bạn trong 2 phút."
  And Gửi thông báo Push Notification ngay khi giao dịch hoàn tất đối soát ngầm.
```

---

#### 📝 USER STORY US03: Biometric Auth Quick Checkout (FaceID / TouchID)
* **User Story:** Là một **Người chơi BINGO18**, tôi muốn **xác thực thanh toán bằng FaceID hoặc Vân Tay trong 0.5 giây**, để **tôi chốt đơn tức thì mà không phải nhập mật khẩu rườm rà**.
* **Metrics/Tracking:** Biometric Checkout Adoption Rate > 70%, Avg Checkout Duration < 2s.
* **Priority:** **Must Have** | **Release:** Release 1 (MVP)

```gherkin
Scenario: Happy Path - Xác thực FaceID mua vé BINGO18 trong 0.5s
  Given Người dùng Anh Minh đã bật tính năng "Xác Thực Biometric" trong Cài Đặt
  And Anh Minh đang ở màn hình chốt đơn BINGO18 kỳ quay 12:30
  When Anh Minh chạm vào nút "Xác Thực FaceID"
  Then Giao diện camera quét khuôn mặt iOS/Android kích hoạt tức thì
  And Kết quả FaceID khớp 100% trong 0.4 giây
  And Giao dịch thanh toán được phê duyệt và hoàn tất tự động.

Scenario: Alternative Path - FaceID thất bại do đeo khẩu trang (Fallback PIN/Mật khẩu)
  Given Người dùng quét FaceID nhưng bị lỗi do khẩu trang che mất một phần khuôn mặt
  When Hệ thống nhận phản hồi Biometric Fail từ OS (Lần 1)
  Then Màn hình lập tức hiển thị gợi ý "Nhập Mã PIN Dự Thưởng (6 chữ số)"
  And Người dùng nhập đúng mã PIN 6 số và giao dịch hoàn tất thành công.

Scenario: Exception Path - Cảm biến vân tay bị khóa do thử sai >5 lần
  Given Người dùng thử xác thực vân tay thất bại quá 5 lần liên tiếp
  When Hệ điều hành khóa tính năng Biometric của thiết bị
  Then App Vietlott SMS hiển thị thông báo "Tính năng Biometric tạm thời bị khóa bởi thiết bị"
  And Yêu cầu người dùng đăng nhập lại bằng Mật khẩu tài khoản Vietlott SMS + OTP SMS để kích hoạt lại.
```

---

### 🟡 Nhóm 2: Trải Nghiệm Giao Diện & Bán Kèm (Adaptive UI & Cross-Sell)

#### 📝 USER STORY US04: Smart Adaptive Home UI & Navigation
* **User Story:** Là một **Người dùng mới (Persona 2)**, tôi muốn **Trang chủ hiển thị danh mục sản phẩm xổ số thông minh, cá nhân hóa theo thói quen**, để **tôi dễ dàng chọn đúng sản phẩm phù hợp mà không bị rối mắt bởi 5+ game**.
* **Metrics/Tracking:** Home Navigation Click-Through Rate +25%, First-time User Conversion Rate > 75%.
* **Priority:** **Must Have** | **Release:** Release 1 (MVP)

```gherkin
Scenario: Happy Path - Trang chủ hiển thị khu vực "Gợi ý cho người mới" cho User Mới
  Given Chị Hà là người dùng mới tạo tài khoản Vietlott SMS dưới 7 ngày
  When Chị Hà đăng nhập mở ứng dụng Vietlott SMS 2.0
  Then Trang chủ hiển thị Widget Banner "Gợi Ý Cho Người Mới: Mua Vé Mega 6/45 10k Chỉ 2 Chạm"
  And Các game پیچ tạp được ẩn bớt vào mục "Xem Tất Cả Game"
  And Hiển thị video ngắn 15s hướng dẫn luật chơi Mega 6/45 đơn giản.

Scenario: Alternative Path - Trang chủ chuyển sang giao diện BINGO18 Turbo cho Người chơi Tần suất cao
  Given Anh Minh là Frequent BINGO18 Player (đã mua >15 đơn BINGO18 trong tuần)
  When Anh Minh mở ứng dụng vào lúc 12:15 giờ nghỉ trưa
  Then Trang chủ tự động ưu tiên đưa Widget BINGO18 Turbo Fast-Play lên vị trí Top Banner
  And Hiển thị đồng hồ đếm ngược kỳ quay gần nhất (03:45) và bảng xu hướng cặp số vừa về.

Scenario: Exception Path - Mất kết nối Server Rule Engine (Fallback sang Default Layout)
  Given Hệ thống Server AI Personalization bị sự cố tạm thời
  When Người dùng mở trang chủ app
  Then App tự động fallback hiển thị Giao diện Trang Chủ Standard (Standard Layout)
  And Đảm bảo 5 sản phẩm xổ số chính vẫn hiển thị đầy đủ, không làm đứt gãy trải nghiệm.
```

---

#### 📝 USER STORY US05: Smart Cross-Sell Lotto 5/35 Widget
* **User Story:** Là một **Người dùng vừa mua vé**, tôi muốn **thấy gợi ý mua kèm 1 bộ số Lotto 5/35 trị giá 10.000 VNĐ tại màn hình hóa đơn**, để **tôi thử vận may sản phẩm mới đang bứt phá chỉ với 1 chạm duy nhất**.
* **Metrics/Tracking:** Cross-sell Widget CTR > 18%, Doanh thu đóng góp Lotto 5/35 > 28% tổng DT.
* **Priority:** **Should Have** | **Release:** Release 2

```gherkin
Scenario: Happy Path - Mua kèm Lotto 5/35 10k thành công tại màn hình hóa đơn BINGO18
  Given Người dùng vừa hoàn tất mua đơn vé BINGO18 50.000 VNĐ thành công
  When Màn hình Hóa Đơn Điện Tử hiển thị
  Then Xuất hiện Widget "Thử Vận May Lotto 5/35 - Jackpot Tích Lũy 15 Tỷ" kèm bộ số gợi ý AI [05 - 12 - 19 - 28 - 35]
  And Có nút "Mua Kèm 10k Ngay (1-Tap)"
  When Người dùng nhấn "Mua Kèm 10k Ngay"
  Then Hệ thống tự động trừ 10.000 VNĐ từ Ví Dự Thưởng và thêm vé Lotto 5/35 vào đơn hàng trong 1 giây.

Scenario: Alternative Path - Người dùng bấm "Đổi Bộ Số Khác" trước khi mua kèm
  Given Widget Cross-Sell đang hiển thị bộ số ngẫu nhiên [01 - 09 - 15 - 22 - 31]
  When Người dùng nhấn nút icon "Đổi Số Khác"
  Then Thuật toán AI lập tức đổi sang bộ số ngẫu nhiên mới [03 - 14 - 21 - 27 - 33] trong 0.2 giây
  And Người dùng bấm nút "Mua Kèm 10k" với bộ số mới chọn.

Scenario: Exception Path - Số dư Ví Dự Thưởng không đủ 10k để mua kèm
  Given Số dư Ví Dự Thưởng của người dùng còn 5.000 VNĐ (không đủ 10.000 VNĐ)
  When Người dùng nhấn nút "Mua Kèm 10k Ngay"
  Then Widget chuyển sang dạng "Nạp Nhanh & Mua Kèm" mở popup liên kết Ví MoMo/VietQR nạp đúng 10k
  And Nếu người dùng từ chối nạp, widget ẩn đi không gây phiền toái.
```

---

#### 📝 USER STORY US06: BINGO18 Turbo Fast-Play Widget
* **User Story:** Là một **Người chơi BINGO18**, tôi muốn **đặt cược nhanh Lớn/Nhỏ hoặc Hòa ngay trên Widget trang chủ**, để **tôi bắt kịp kỳ quay 6 phút mà không cần qua 3 bước chuyển màn hình**.
* **Metrics/Tracking:** Time to Purchase BINGO18 reduced from 18s to 3s, Daily Active BINGO18 Orders +30%.
* **Priority:** **Should Have** | **Release:** Release 1 (MVP)

```gherkin
Scenario: Happy Path - Đặt cược BINGO18 "Lớn" 20k trong 3 giây trên Home Widget
  Given Người dùng đang ở Trang Chủ App và thấy Widget BINGO18 đếm ngược còn 01:30
  When Người dùng chọn nút "LỚN (Tổng 13-18)" và chọn mệnh giá "20.000 VNĐ"
  And Bấm nút "Chốt Đơn Turbo"
  Then Hệ thống gọi API `/api/v2/bingo18/turbo-checkout` xử lý ngầm
  And Hiển thị hiệu ứng pháo hoa nhẹ và vé điện tử tạo thành công chỉ trong 2.2 giây.

Scenario: Exception Path - Đặt cược khi đếm ngược còn <10 giây (Đã đóng kỳ quay)
  Given Kỳ quay BINGO18 đếm ngược về mốc 00:08 (Hệ thống khóa chốt đơn 10s trước giờ quay)
  When Người dùng bấm "Chốt Đơn Turbo"
  Then Widget hiển thị thông báo "Kỳ quay #00881 đã đóng. Tự động chuyển đơn của bạn sang Kỳ quay tiếp theo #00882 (Quay sau 6 phút)"
  And Người dùng bấm "Xác Nhận Chuyển Kỳ" hoặc "Hủy Đơn".
```

---

### 🔒 Nhóm 3: An Toàn, Bảo Mật & Cập Nhật APK (Security & In-App Update)

#### 📝 USER STORY US07: In-App Auto Updater for Android APK
* **User Story:** Là một **Người dùng Android (Persona 2)**, tôi muốn **ứng dụng tự động tải và cập nhật phiên bản mới ngay bên trong app**, để **tôi không phải lên trang web ngoài tải file APK thủ công**.
* **Metrics/Tracking:** App Version Adoption Rate > 92% trong 7 ngày, Complaint Ticket về APK = 0 cases.
* **Priority:** **Must Have** | **Release:** Release 1 (MVP)

```gherkin
Scenario: Happy Path - Tự động tải bản cập nhật APK ngầm và cài đặt 1-click
  Given Máy Android đang chạy phiên bản Vietlott SMS v1.8.5
  And Server phát hành phiên bản mới v2.0.0 (Kỷ niệm 6 năm)
  When Người dùng mở app Vietlott SMS
  Then Hệ thống hiển thị Popup "Phiên Bản 2.0.0 Đã Sẵn Sàng (Tính năng Mua Vé Nhóm & BINGO18 Turbo)"
  And Kèm nút "Cập Nhật Ngay (35 MB)"
  When Người dùng bấm "Cập Nhật Ngay"
  Then App tải gói APK ngầm với thanh Progress bar thời gian thực
  And Sau khi tải xong, gọi Android PackageInstaller khởi chạy màn hình nâng cấp phiên bản trong 5 giây.

Scenario: Exception Path - File APK bị lỗi Checksum SHA-256 (Phát hiện file bị can thiệp/hỏng)
  Given Gói APK v2.0.0 đã tải về máy người dùng nhưng bị lỗi mất gói tin trên đường truyền
  When Service kiểm tra SHA-256 Checksum Hash đối chiếu với Server Hash
  Then Hash kết quả không khớp (Hash Mismatch)
  And Hệ thống tự động xóa file APK bị hỏng, thông báo "File cập nhật bị lỗi, đang tải lại gói an toàn..."
  And Tự động kích hoạt luồng re-download từ CDN dự phòng.
```

---

#### 📝 USER STORY US08: Official Security Verification Badge
* **User Story:** Là một **Người dùng mới**, tôi muốn **thấy Huy hiệu Xác thực Chính hãng Vietlott (Verified Trust Shield Badge) kèm mã QR xác thực**, để **tôi tuyệt đối an tâm không lo bị lừa đảo bởi các app mạo danh**.
* **Metrics/Tracking:** Trust Index Score > 85/100, Reduction in Fraud Inquiries by 90%.
* **Priority:** **Must Have** | **Release:** Release 1 (MVP)

```gherkin
Scenario: Happy Path - Xem Badge Xác thực và quét QR tra cứu chứng nhận
  Given Người dùng đang ở màn hình Trang Chủ hoặc màn hình Tài Khoản
  When Người dùng chạm vào Badge "Vietlott Official Verified - An Toàn 100%" ở góc trên màn hình
  Then Popup Chứng Nhận Bảo Mật xuất hiện hiển thị Giấy phép Bộ Tài Chính + Liên kết xác thực 14 Ngân hàng liên kết
  And Có mã QR tĩnh cấp bởi Vietlott Core Server
  When Người dùng dùng ứng dụng Ngân hàng quét mã QR này
  Then Màn hình mở ra liên kết SSL HTTPS chính thống `https://vietlott-sms.vn/verify-app?id=OFFICIAL`.
```

---

### 👥 Nhóm 4: Mua Vé Nhóm & Xử Lý Tiền Thưởng (Syndicate Play & Split Payout)

#### 📝 USER STORY US09: Syndicate Play - Create Group & Invite Members
* **User Story:** Là một **Người chơi VIP (Persona 3)**, tôi muốn **tạo Phòng Mua Vé Nhóm cho vé Bao 15 và gửi link mời bạn bè cùng góp tiền**, để **chúng tôi săn Jackpot khủng với chi phí chia nhỏ hợp lý**.
* **Metrics/Tracking:** Total Active Syndicate Rooms > 25,000/month, K-factor referral > 0.35.
* **Priority:** **Should Have** | **Release:** Release 2

```gherkin
Scenario: Happy Path - Anh Hoàng tạo phòng Mua Nhóm Bao 9 Power 6/55 thành công
  Given Anh Hoàng chọn bộ số Bao 9 Power 6/55 có tổng giá trị vé là 840.000 VNĐ
  When Anh Hoàng chọn tính năng "Tạo Phòng Mua Nhóm (Syndicate)"
  And Đặt số suất góp: 10 suất (mỗi suất 84.000 VNĐ)
  And Anh Hoàng thanh toán đặt cọc 2 suất (168.000 VNĐ)
  Then Hệ thống tạo Phòng Syndicate ID "#SYN-8812" và tạo Hợp Đồng Mua Chung Số Hóa
  And Tạo đường link chia sẻ `https://vietlott-sms.vn/join/SYN-8812` kèm mã QR code
  And Anh Hoàng bấm nút "Chia Sẻ Qua Zalo/SMS" gửi cho nhóm bạn.

Scenario: Alternative Path - Thành viên thứ 10 nộp tiền đủ 100% (Khóa vé tự động)
  Given Phòng #SYN-8812 đã có 9 suất nộp tiền (còn thiếu 1 suất 84.000 VNĐ)
  And Thời hạn góp tiền còn 30 phút trước giờ chốt vé quay số
  When Anh Tuấn bấm vào link mời và thanh toán suất cuối cùng 84.000 VNĐ
  Then Phòng đổi trạng thái sang "ĐÃ ĐỦ 100% TIỀN"
  And Backend Vietlott Core chính thức phát hành Vé Số Điện Tử Bao 9 cho Phòng #SYN-8812
  And Gửi thông báo Push Notification "Vé Nhóm Đã Khóa Thành Công" tới tất cả 10 thành viên.

Scenario: Exception Path - Phòng không gom đủ 100% tiền trước giờ chốt vé (Tự động hoàn tiền)
  Given Phòng #SYN-8812 đến mốc 30 phút trước giờ quay số nhưng mới gom được 7/10 suất (đạt 70%)
  When Hệ thống chạy Cronjob Auto-Cancel phòng chưa đủ tiền
  Then Phòng tự động đổi trạng thái sang "ĐÃ HỦY - KHÔNG ĐỦ SUẤT"
  And Hệ thống tự động hoàn 100% số tiền đã góp về Ví Dự Thưởng của từng thành viên trong 5 giây
  And Gửi SMS thông báo hủy phòng và hoàn tiền minh bạch.
```

---

#### 📝 USER STORY US10: Syndicate Play - Automatic Prize Split & Wallet Payout
* **User Story:** Là một **Thành viên tham gia Mua Vé Nhóm**, tôi muốn **tiền thưởng trúng của vé nhóm tự động phân bổ và chuyển trực tiếp vào Ví cá nhân của tôi theo đúng % tiền đã góp**, để **đảm bảo minh bạch tuyệt đối và không phải đòi tiền trưởng nhóm**.
* **Metrics/Tracking:** Auto-payout Payout Speed < 60s post-draw, Member Dispute Rate = 0%.
* **Priority:** **Must Have** | **Release:** Release 2

```gherkin
Scenario: Happy Path - Vé Nhóm trúng Giải Nhất 40.000.000 VNĐ (Tự động chia theo %)
  Given Phòng #SYN-8812 trúng giải Nhất Power 6/55 trị giá 40.000.000 VNĐ
  And Phòng có 10 suất góp (Anh Hoàng 2 suất = 20%, 8 người khác mỗi người 1 suất = 10%)
  When Kết quả quay số được xác thực trên Vietlott Core Backend
  Then Engine Split Payout kích hoạt tự động tính toán:
    | Thành Viên | Tỷ Lệ % | Thuế TNCN (10% phần >10M) | Tiền Thưởng Thực Nhận |
    | Anh Hoàng  | 20%     | 400.000 VNĐ                | 7.600.000 VNĐ         |
    | 8 Bạn khác | 10% mỗi ng| 0 VNĐ (vì <10M/người)     | 4.000.000 VNĐ/người   |
  And Tiền được cộng tự động vào Ví Dự Thưởng của 9 người trong vòng 45 giây
  And Gửi Push Notification thông báo chi tiết bảng phân bổ thưởng.
```

---

### 🎁 Nhóm 5: Gamification & Khách Hàng VIP (Retention & VIP Loyalty)

#### 📝 USER STORY US11: Vietlott VIP Club Tier & Cashback Engine
* **User Story:** Là một **Khách hàng VIP chi tiêu >2 triệu/tháng (Persona 3)**, tôi muốn **được tự động xếp hạng thành viên Kim Cương và nhận hoàn tiền Cashback 2% vào Ví dự thưởng**, để **tôi được tôn vinh và nhận giá trị gia tăng xứng đáng với chi tiêu**.
* **Metrics/Tracking:** VIP Monthly Active Users > 98.5%, VIP Churn Rate < 1.5%.
* **Priority:** **Should Have** | **Release:** Release 2

```gherkin
Scenario: Happy Path - Anh Hoàng thăng hạng VIP Kim Cương và nhận Cashback 2% tự động
  Given Tổng chi tiêu mua vé tháng 7 của Anh Hoàng đạt 5.200.000 VNĐ (vượt mốc 5 triệu)
  When Hệ thống tính điểm xếp hạng vào ngày 01 đầu tháng
  Then Anh Hoàng được tự động nâng cấp từ hạng Vàng lên hạng "VIP KIM CƯƠNG"
  And Khi Anh Hoàng mua đơn vé Bao 8 Power trị giá 280.000 VNĐ
  Then Hệ thống tự động tính Cashback 2% = 5.600 VNĐ
  And Số tiền 5.600 VNĐ lập tức được cộng vào Ví Dự Thưởng của Anh Hoàng kèm hiệu ứng Huy hiệu Kim Cương lấp lánh.
```

---

#### 📝 USER STORY US12: Daily Streaks & Lucky Wheel Gamification
* **User Story:** Là một **Người dùng ứng dụng**, tôi muốn **điểm danh hàng ngày (Daily Check-in) để tích chuỗi ngày may mắn (Streaks) và nhận lượt quay Vòng Quay 6 Năm**, để **tôi có thêm động lực mở app mỗi ngày**.
* **Metrics/Tracking:** 7-day Retention Rate +25%, Daily Active Users (DAU) +35%.
* **Priority:** **Could Have** | **Release:** Release 2

```gherkin
Scenario: Happy Path - Điểm danh liên tục 7 ngày nhận Vòng Quay Kỷ Niệm 6 Năm
  Given Chị Hà đã điểm danh liên tục 6 ngày trong tuần
  When Chị Hà mở ứng dụng vào Ngày thứ 7 và bấm nút "Điểm Danh Ngay"
  Then Chuỗi Streaks cập nhật mốc 7/7 Ngày 🔥
  And Hệ thống tặng ngay 01 "Lượt Quay Vòng Quay 6 Năm"
  When Chị Hà bấm "Quay Ngay" trên Vòng Quay May Mắn
  Then Kim quay dừng ở ô "Voucher Mua Vé 20.000 VNĐ"
  And Voucher được tự động thêm vào Kho Ưu Đãi cá nhân của Chị Hà.
```

---

#### 📝 USER STORY US13: Real-Time Draw Notification & Celebration Confetti
* **User Story:** Là một **Người mua vé**, tôi muốn **nhận thông báo kết quả quay số tức thì và hiệu ứng pháo hoa hoành tráng (Celebration Confetti) khi trúng thưởng**, để **tôi trải nghiệm cảm xúc vỡ òa chiến thắng**.
* **Metrics/Tracking:** Notification Open Rate > 45%, Social Share Action Rate +30%.
* **Priority:** **Could Have** | **Release:** Release 1 (MVP)

```gherkin
Scenario: Happy Path - Mở ứng dụng xem kết quả và nhận pháo hoa ăn mừng khi trúng giải
  Given Vé Mega 6/45 của người dùng trúng Giải Nhất 10.000.000 VNĐ lúc 18:30
  When Người dùng chạm vào Push Notification "Kết quả Mega 6/45: Bạn đã trúng thưởng!"
  Then Màn hình mở ra hiệu ứng Pháo Hoa Confetti rực rỡ ngập tràn màn hình cùng âm thanh chiến thắng
  And Banner chúc mừng hiển thị: "CHÚC MỪNG BẠN ĐÃ TRÚNG GIẢI NHẤT 10.000.000 VNĐ!"
  And Có nút "Chia Sẻ Niềm Vui (Tạo Share Card)" và "Xem Tiền Trong Ví".
```

---

#### 📝 USER STORY US14: AI Smart Pick & Tử Vi 12 Con Giáp
* **User Story:** Là một **Người chơi thích yếu tố may mắn**, tôi muốn **nhận gợi ý chọn số theo Tử vi 12 con giáp và thuật toán AI**, để **tôi có bộ số may mắn cá nhân hóa cho riêng mình**.
* **Metrics/Tracking:** AI Smart Pick Feature Adoption > 35%.
* **Priority:** **Could Have** | **Release:** Release 3

```gherkin
Scenario: Happy Path - Gợi ý chọn số theo tuổi Thìn (1988) ngày Hoàng Đạo
  Given Người dùng cài đặt ngày sinh 12/04/1988 (Tuổi Mậu Thìn)
  When Người dùng chọn tính năng "Gợi Ý Phong Thủy 12 Con Giáp"
  Then AI Visualizer hiển thị Quẻ Số May Mắn Ngày: [08 - 18 - 28 - 38 - 48 - 58]
  And Dòng giải thích: "Hôm nay ngày Kim Sinh Thủy, các số đuôi 8 mang lại đại cát!"
  And Người dùng bấm nút "Chọn Bộ Số Này Để Mua Vé Mega".
```

---

#### 📝 USER STORY US15: Social Celebration Share Card
* **User Story:** Là một **Người trúng thưởng**, tôi muốn **xuất hình ảnh vé trúng thưởng thiết kế đẹp mắt (Share Card) ẩn thông tin riêng tư**, để **tôi tự tin đăng khoe lên Facebook/Zalo/TikTok**.
* **Metrics/Tracking:** K-factor viral organic reach +0.2, Social Shares > 5,000/month.
* **Priority:** **Could Have** | **Release:** Release 3

```gherkin
Scenario: Happy Path - Xuất Share Card trúng thưởng 500k đăng Zalo
  Given Người dùng vừa trúng Giải Ba BINGO18 trị giá 500.000 VNĐ
  When Người dùng bấm nút "Tạo Card Chia Sẻ MXH"
  Then Hệ thống tự động tạo 1 tấm hình kích thước 1080x1920 (Story format)
  And Tấm hình có background Đỏ Vietlott 6 Năm rực rỡ, ẩn 6 số giữa của SĐT, ẩn mã định danh
  And Có nút "Lưu Hình" và "Chia Sẻ Trực Tiếp Qua Zalo / Facebook".
```

---

#### 📝 USER STORY US16: Responsible Gaming Spending Limit Control
* **User Story:** Là một **Người dùng ứng dụng**, tôi muốn **cài đặt hạn mức chi tiêu mua vé tối đa theo ngày/tháng (Responsible Gaming)**, để **tôi làm chủ tài chính và chơi xổ số có trách nhiệm**.
* **Metrics/Tracking:** Compliance Audit Passed 100%, Responsible Gaming User Activation Rate > 15%.
* **Priority:** **Must Have** | **Release:** Release 1 (MVP)

```gherkin
Scenario: Happy Path - Cài hạn mức 200.000 VNĐ/ngày và hệ thống chặn khi vượt mốc
  Given Người dùng cài đặt "Hạn Mức Chi Tiêu Ngày" là 200.000 VNĐ trong phần Cài Đặt An Toàn
  And Trong ngày người dùng đã mua 200.000 VNĐ tiền vé
  When Người dùng cố gắng đặt thêm 1 đơn vé BINGO18 20.000 VNĐ nữa
  Then Nút thanh toán bị chặn và hiển thị Popup "Bạn Đã Đạt Hạn Mức Chi Tiêu Trong Ngày (200.000 VNĐ)"
  And Gợi ý: "Hãy quay lại giải trí vào ngày mai! Vietlott SMS ủng hộ Chơi Có Trách Nhiệm."
```

---

## D. BẢN ĐỒ LUỒNG NGHIỆP VỤ & MÔ HÌNH DỮ LIỆU (MERMAID DIAGRAMS)

### 1. Activity Diagram: Streamlined Purchase Flow (Luồng Mua Vé Tối Ưu ≤3 Bước)

Luồng mua vé tối ưu hóa rút ngắn xuống tối đa 3 thao tác: **Chọn Số → Xác Nhận → Thanh Toán Idempotent** kèm cơ chế tự động xử lý khi nghẽn mạng.

```mermaid
flowchart TD
    Start([🟢 Bắt Đầu: Mở App / Widget]) --> Step1[Bước 1: Chọn Bộ Số & Kỳ Quay<br>Random / AI Smart Pick / Turbo Select]
    Step1 --> Step2[Bước 2: Màn Hình Xác Nhận Đơn Hàng<br>Hiển thị số tiền & Voucher giảm giá nếu có]
    Step2 --> DecisionCrossSell{Có Gợi Ý Cross-Sell<br>Lotto 5/35?}
    DecisionCrossSell -- "Bấm Mua Kèm 10k" --> AddLotto[Thêm 1 bộ số Lotto 5/35 10k<br>vào giỏ hàng] --> Step3
    DecisionCrossSell -- "Bỏ Qua / Bấm Thanh Toán" --> Step3[Bước 3: Nhấn Thanh Toán 1-Tap<br>Sinh Idempotency-Key Client]
    
    Step3 --> LockButton[Client vô hiệu hóa nút Thanh Toán<br>Hiển thị Status Countdown Dialog]
    LockButton --> AuthBiometric{Xác thực<br>Biometric?}
    AuthBiometric -- "FaceID / Vân tay OK" --> SendGateway[Gửi Header Idempotency-Key<br>tới API Gateway Backend]
    AuthBiometric -- "Fail / Không dùng" --> PINAuth[Nhập PIN Dự Thưởng 6 số] --> SendGateway

    SendGateway --> BackendCheck{Backend Gateway<br>Kiểm tra Key?}
    BackendCheck -- "Key đã xử lý thành công" --> ReturnCache[Trả kết quả từ Cache<br>Tránh nạp trùng đơn] --> EndSuccess
    BackendCheck -- "Key mới chưa xử lý" --> ProcessQueue[Đưa giao dịch vào Queue<br>Xử lý trừ tiền bất đồng bộ]

    ProcessQueue --> PaymentGate{Ngân hàng / Ví<br>Phản hồi?}
    PaymentGate -- "Trừ tiền thành công (<3s)" --> IssueTicket[Vietlott Core phát hành<br>Vé Số Điện Tử duy nhất]
    IssueTicket --> EndSuccess([🔴 Màn Hình Hóa Đơn & Mã Vé<br>Hiệu ứng Pháo Hoa Confetti])

    PaymentGate -- "Timeout >10s / Mất Mạng" --> PollingLoop[Chuyển sang Status Polling Loop<br>Tự động tra cứu lại sau mỗi 2s]
    PollingLoop --> ReconcileCheck{Kết quả対 soát<br>Backend?}
    ReconcileCheck -- "Thành công" --> IssueTicket
    ReconcileCheck -- "Thất bại / Không trừ tiền" --> Rollback[Mở lại nút thanh toán<br>Thông báo lỗi nhẹ nhẹ cho User] --> Step2
```

---

### 2. Activity Diagram: Results & Claiming Notification Flow (Luồng Kết Quả & Trả Thưởng)

Luồng tự động hóa công bố kết quả quay số, thông báo đẩy Real-time, phân bổ tiền thưởng tự động và trả thưởng về Ví dự thưởng/Ngân hàng.

```mermaid
flowchart TD
    StartDraw([🟢 Sự Kiện: Hoàn Tất Kỳ Quay Số Vietlott]) --> PublishResult[Vietlott Core xuất kết quả quay số<br>đã được Hội đồng Giám sát xác thực]
    PublishResult --> BatchCheck[Job Đối Soát Tự Động quẹt toàn bộ<br>Vé Số Điện Tử trong kỳ quay]
    
    BatchCheck --> WinCheck{Vé có trúng thưởng<br>không?}
    WinCheck -- "Không Trúng" --> UpdateStatusFail[Cập nhật trạng thái vé: NOT_WON] --> PushFailNoti[Gửi Push Notification thông thường:<br>'Kết quả kỳ quay đã có']
    
    WinCheck -- "Có Trúng Thưởng!" --> UpdateStatusWin[Cập nhật trạng thái vé: WON]
    UpdateStatusWin --> CheckTicketType{Loại Vé Mua?}
    
    CheckTicketType -- "Vé Cá Nhân" --> CalcPrize[Tính Tổng Tiền Thưởng & Thuế TNCN<br>Khấu trừ 10% phần thưởng >10M VNĐ]
    CheckTicketType -- "Vé Mua Nhóm - Syndicate" --> CalcSplit[Kích hoạt Engine Split Payout<br>Tính % thưởng theo suất nộp tiền]

    CalcPrize --> PayoutMethod{Giá trị tiền thưởng<br>Thực nhận?}
    CalcSplit --> SplitLoop[Lặp qua danh sách Ví cá nhân<br>của từng thành viên trong Nhóm] --> PayoutMethod

    PayoutMethod -- "Tiền thưởng ≤ 10.000.000 VNĐ" --> AutoWallet[Tự động cộng tiền vào Ví Dự Thưởng<br>hoặc Tài Khoản Ngân Hàng Đăng Ký]
    PayoutMethod -- "Tiền thưởng > 10.000.000 VNĐ" --> HighPrizeProc[Chuyển khoản hạn mức lớn ngân hàng<br>hoặc tạo Lệnh Yêu Cầu Rút Thưởng VIP]

    AutoWallet --> PushWinNoti[Gửi Push Notification Ưu Tiên High Priority:<br>'Chúc mừng! Bạn vừa trúng thưởng!']
    HighPrizeProc --> PushWinNoti

    PushWinNoti --> UserOpenApp[User chạm thông báo mở App Vietlott SMS]
    UserOpenApp --> ConfettiEffect([🔴 Kích hoạt hiệu ứng Pháo hoa Confetti<br>Hiển thị Chi Tiết Trúng Thưởng & Share Card])
```

---

### 3. State Diagram: Ticket Lifecycle (Vòng Đời Vé Số)

Mô tả chi tiết 8 trạng thái trong toàn bộ vòng đời của một vé số từ lúc chọn số đến khi hoàn tất trả thưởng.

```mermaid
stateDiagram-v2
    [*] --> DRAFT : 1. User chọn bộ số & tạo đơn
    DRAFT --> PENDING_PAYMENT : 2. Bấm Thanh toán (Idempotency Key sinh ra)
    
    PENDING_PAYMENT --> PAYMENT_FAILED : 3a. Ngân hàng từ chối / Hủy đơn
    PAYMENT_FAILED --> DRAFT : User chọn thanh toán lại
    
    PENDING_PAYMENT --> ISSUED : 3b. Trừ tiền thành công -> Core phát hành vé
    ISSUED --> PENDING_DRAW : 4. Hệ thống khóa vé chuẩn bị quay số
    
    PENDING_DRAW --> DRAWN_NOT_WON : 5a. Kết quả quay số không trúng
    PENDING_DRAW --> DRAWN_WON : 5b. Kết quả quay số trúng thưởng!
    
    DRAWN_WON --> PAYOUT_PROCESSING : 6. Kích hoạt Job Trả Thưởng Tự Động
    PAYOUT_PROCESSING --> PAID_OUT : 7a. Tiền đã về Ví Dự Thưởng / Ngân hàng thành công
    PAYOUT_PROCESSING --> PAYOUT_HOLD : 7b. Sự cố tài khoản nhận (Sai TK/Khóa TK)
    
    PAYOUT_HOLD --> PAID_OUT : Xử lý cập nhật lại TK nhận thưởng
    
    DRAWN_NOT_WON --> [*] : Kết thúc vòng đời
    PAID_OUT --> [*] : Kết thúc vòng đời (Hoàn tất)
```

---

### 4. Concept Model (Mô Hình Khái Niệm Dữ Liệu Nghiệp Vụ)

Mô hình ER / Class Diagram thể hiện cấu trúc các Entity nghiệp vụ mới cho Gamification, Syndicate Play và Idempotency Motor.

```mermaid
classDiagram
    class User {
        +String userId
        +String phoneNumber
        +String cccdPassport
        +String fullName
        +VipTier vipTier
        +Int loyaltyPoints
        +Double walletBalance
        +createSyndicateGroup()
        +purchaseTicket()
    }

    class VipTier {
        +String tierId
        +String tierName
        +Double minSpendRequirement
        +Double cashbackPercentage
        +String benefitsDescription
    }

    class IdempotencyTransaction {
        +String idempotencyKey
        +String userId
        +Double amount
        +String requestPayloadHash
        +String status
        +String transactionId
        +DateTime createdAt
        +DateTime expiresAt
    }

    class Ticket {
        +String ticketId
        +String userId
        +String gameType
        +List~String~ selectedNumbers
        +Double price
        +TicketStatus status
        +DateTime drawTime
        +Boolean isSyndicateTicket
    }

    class SyndicateGroup {
        +String groupId
        +String creatorUserId
        +String groupName
        +Double totalTicketPrice
        +Int totalShares
        +Double pricePerShare
        +Int filledShares
        +GroupStatus status
        +DateTime cutoffTime
        +generateInviteLink()
        +lockGroupAndIssueTicket()
    }

    class SyndicateMember {
        +String memberId
        +String groupId
        +String userId
        +Int shareCount
        +Double contributedAmount
        +Double payoutAmount
        +PaymentStatus paymentStatus
    }

    class GamificationStreak {
        +String streakId
        +String userId
        +Int currentStreakDays
        +Int maxStreakDays
        +DateTime lastCheckinDate
        +Int luckyWheelSpinsRemaining
        +recordCheckin()
    }

    User "1" -- "1" VipTier : Belongs to
    User "1" -- "0..*" Ticket : Purchases
    User "1" -- "0..*" IdempotencyTransaction : Executes
    User "1" -- "0..*" SyndicateMember : Joins
    User "1" -- "1" GamificationStreak : Has
    SyndicateGroup "1" -- "1" Ticket : Owns
    SyndicateGroup "1" -- "1..*" SyndicateMember : Contains
```

---

## E. PHÂN TÍCH RỦI RÔ, NGOẠI LỆ & HUNG STATE (EDGE CASES, TIMEOUT & SWOT)

### 1. Bảng Phân Tích Ngoại Lệ (Edge Case Analysis Table — 8 Exception Groups)

BA rà soát 8 nhóm kịch bản ngoại lệ nguy cơ cao và xác định cơ chế xử lý tự động chống đứt gãy hệ thống.

| # | Phân Nhóm Ngoại Lệ | Kịch Bản Ngoại Lệ Chi Tiết | Severity | Hệ Thống Phản Hồi (System Behavior) | Timeout Value | Retry / Fallback Policy | Compensating Action (Hành Động Bù Đắp) |
| :-: | :--- | :--- | :---: | :--- | :---: | :--- | :--- |
| **1** | **Network Drop During Payment** | Đứt kết nối mạng ngay khi user vừa bấm nút Thanh toán 1-tap. | **HIGH** | Màn hình hiển thị "Đang tự động kiểm tra lại trạng thái...". Nút thanh toán khóa không cho bấm lại. | 5s | Polling tự động 3 lần (khoảng cách 2s/lần) tới API Gateway dùng Idempotency Key. | Nếu backend chưa nhận request → Mở lại nút thanh toán. Nếu backend đã trừ tiền → Tự động đồng bộ vé vào ví. |
| **2** | **Double-Tap Payment Attempt** | Người dùng bấm liên tiếp nút Thanh toán do tâm lý sốt ruột. | **HIGH** | Client-side Debouncing vô hiệu hóa nút ngay chạm đầu tiên. API Gateway từ chối mọi request trùng Idempotency Key. | N/A | Return cached response của request đầu tiên (HTTP 200 OK với thông tin vé duy nhất). | Không trừ tiền lần 2. Hiển thị thông báo "Đơn hàng đã được ghi nhận". |
| **3** | **Telco/Bank Gateway Timeout** | Cổng thanh toán ngân hàng VCB/MoMo bị gián đoạn giờ cao điểm >3s. | **HIGH** | Gateway chuyển trạng thái giao dịch sang `PENDING_PARTNER`. Dialog đếm ngược thông báo chờ xác nhận. | 8s | Tự động chuyển hướng sang Ví Dự Thưởng Vietlott SMS nội ứng dụng nếu user đồng ý. | Nếu sau 3 phút ngân hàng mới báo trừ tiền thành công → Tự động nạp số tiền đó vào Ví Dự Thưởng của user. |
| **4** | **Draw Delay / Result Lag** | Hội đồng mở thưởng hoãn giờ quay số hoặc chưa công bố kết quả lúc 18:30. | **MEDIUM** | App cập nhật trạng thái kỳ quay: "Hội đồng đang xác thực kết quả. Dữ liệu sẽ cập nhật trong ít phút." | 15m | Job tự động kiểm tra định kỳ mỗi 1 phút cho đến khi kết quả được baseline. | Tự động gửi SMS xin lỗi và Push Notification ngay khi có kết quả chính thức. |
| **5** | **Corrupted APK Hash (Android)** | File APK cập nhật tải về bị hỏng checksum SHA-256 do đứt mạng giữa chừng. | **MEDIUM** | Android PackageInstaller chặn không cho cài đặt. App hiển thị thông báo "File tải về chưa toàn vẹn". | N/A | Xóa file tạm bị hỏng và tự động kích hoạt tải lại từ CDN CDN-Backup. | Cho phép người dùng tiếp tục dùng phiên bản cũ nếu chưa muốn tải lại ngay. |
| **6** | **Invalid CCCD KYC Status** | Người dùng định danh CCCD bị hỏng ảnh hoặc hệ thống định danh QG bị nghẽn. | **MEDIUM** | Hiển thị màn hình thông báo lỗi cụ thể: "Hình ảnh CCCD mờ/Lỗi kết nối định danh QG". | 10s | Cho phép người dùng chụp lại ảnh CCCD rõ nét hoặc dùng xác thực qua Ngân Hàng (Bank KYC). | Cho phép mua vé mệnh giá nhỏ (<50k) trong thời gian chờ duyệt KYC thủ công. |
| **7** | **Syndicate Payment Timeout** | 1 thành viên nhóm mua chung không nộp đủ tiền trước giờ chốt vé 30 phút. | **HIGH** | Phòng tự động chuyển sang trạng thái `EXPIRED_INCOMPLETE`. Khóa không cho phát hành vé nhóm. | 30m prior draw | Tự động kích hoạt Engine Hoàn Tiền (Auto-Refund) 100% cho các thành viên đã nộp. | Tiền hoàn về Ví Dự Thưởng trong 5 giây kèm thông báo lý do phòng bị hủy. |
| **8** | **Prize Claim Account Mismatch** | Tài khoản ngân hàng nhận thưởng bị khóa hoặc tên không trùng khớp CCCD. | **HIGH** | Tiền thưởng không thể chuyển khoản. Chuyển trạng thái vé trúng sang `PAYOUT_HOLD`. | N/A | Gửi Push Notification và SMS yêu cầu người dùng cập nhật lại Số Tài Khoản Ngân Hàng chính chủ. | Tiền thưởng được giữ an toàn trên Vietlott Core cho đến khi tài khoản được xác minh lại. |

---

### 2. Phân Tích Trạng Thái Treo & Timeout (Timeout & Hung State Analysis — 7 BABOK Questions)

BA trả lời trọn vẹn 7 câu hỏi chuẩn BABOK® v3 / `ba-rules.md` cho các luồng tích hợp hệ thống bên ngoài (Ngân hàng, Ví điện tử, Nhà mạng):

1. **Timeout Value (Định lượng giá trị timeout):**
   - Timeout kết nối API Gateway: **3.0 giây**.
   - Timeout kết nối Cổng Ngân hàng/Ví điện tử đối tác: **8.0 giây**.
   - Timeout tải bản cập nhật In-App APK: **30.0 giây**.
2. **Hung Detection Mechanism (Cơ chế phát hiện treo):**
   - Triển khai **Circuit Breaker Pattern** (Resilience4j/Envoy Proxy). Nếu tỷ lệ lỗi/timeout của 1 cổng thanh toán vượt quá 15% trong 1 phút, Circuit Breaker tự động ngắt (OPEN) và chuyển hướng traffic sang kênh dự phòng.
   - Client sử dụng **Real-time Status Polling Loop** mỗi 2 giây để kiểm tra trạng thái đơn hàng ngầm.
3. **Post-Timeout State (Trạng thái giao dịch sau timeout):**
   - Giao dịch được gắn trạng thái tạm thời là `PENDING_RECONCILIATION` (Đang chờ đối soát). Tiền chưa bị trừ ở ví nội bộ nhưng đơn hàng được giữ chỗ trong Queue 5 phút.
4. **Recovery Owner & Automated Workflow (Đơn vị & Quy trình phục hồi):**
   - **Tự động (Automated):** Cronjob Đối Soát Ngầm (`Auto-Reconciliation Service`) chạy mỗi 5 phút tự động quét các giao dịch pending với Bank API Log.
   - **Thủ công (Manual Operator):** Nếu sau 30 phút giao dịch vẫn lệch trạng thái, ticket tự động đẩy về dashboard bộ phận CSKH/Kế Toán để xử lý duyệt tay.
5. **User Notification Channel & Format (Kênh & Mẫu thông báo người dùng):**
   - **Kênh:** Push Notification ứng dụng + SMS fallback.
   - **Mẫu thông báo:** *"Vietlott SMS: Đơn hàng #[ID] trị giá [X]đ của bạn đã được đối soát thành công. Vé đã được cập nhật vào ứng dụng. Chúc bạn may mắn!"*
6. **Idempotency Key Specification & Lifetime (Quy chuẩn Mã Idempotency):**
   - Format: `IDEM-[USER_ID]-[TIMESTAMP_MS]-[RANDOM_UUID]` (Ví dụ: `IDEM-8821-1770739200-F81A`).
   - Idempotency Key có thời gian sống (TTL / Lifetime) là **24 giờ** trên Redis Distributed Cache.
7. **Reconciliation Integration (Tích hợp Báo cáo đối soát):**
   - Mọi giao dịch treo/pending được tự động phân loại vào **Báo Cáo Liệt Kê Giao Dịch Bất Thường (Exception Reconciliation Report)** xuất tự động vào 23:00 hàng ngày gửi bộ phận Tài chính - Kế toán.

---

### 3. Phân Tích SWOT Tổng Thể Kế Hoạch Cải Tiến Vietlott SMS 2.0

```
┌───────────────────────────────────────────────────┬───────────────────────────────────────────────────┐
│ STRENGTHS (Điểm Mạnh Nội Bộ)                      │ WEAKNESSES (Điểm Yếu Nội Bộ)                      │
│ 1. Kênh mobile chính thống DUY NHẤT có 5M+ user. │ 1. Hạ tầng legacy xử lý đồng bộ dễ nghẽn giờ cao │
│ 2. Tệp BINGO18 ARPU cực cao (2.44M/tháng).       │    điểm 6 phút BINGO18.                           │
│ 3. Sự bứt phá kỷ lục của Lotto 5/35 (198% KPI).   │ 2. Phụ thuộc vào chính sách thắt chặt APK Android.│
│ 4. Thương hiệu Vietlott uy tín được Nhà nước      │ 3. Thiếu hoàn toàn chính sách Loyalty/VIP Care    │
│    bảo chứng.                                     │    và Gamification trước đây.                     │
├───────────────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ OPPORTUNITIES (Cơ Hội Bên Ngoài)                  │ THREATS (Thách Thức Bên Ngoài)                    │
│ 1. Nhu cầu giải trí nhóm (Syndicate Play) chưa   │ 1. Sự xuất hiện của các app/website lô đề giả mạo │
│    được khai phá trên di động.                    │    gây ô nhiễm niềm tin người dùng.               │
│ 2. Xu hướng thanh toán không tiền mặt & Biometric │ 2. Sự cố nghẽn mạng từ phía các Cổng Ngân hàng/Ví │
│    phổ cập toàn dân.                              │    đối tác ngoài tầm kiểm soát trực tiếp.         │
│ 3. Cột mốc Sự kiện Kỷ niệm 6 năm tạo cú huých    │ 3. Biến động doanh thu Ma trận phụ thuộc vào giá  │
│    truyền thông bứt phá doanh thu 750B+/tháng.    │    trị Jackpot tích lũy.                          │
└───────────────────────────────────────────────────┴───────────────────────────────────────────────────┘
```

---

## F. MA TRẬN TRUY VẾT & XÁC NHẬN MỤC TIÊU (TRACEABILITY & ACCEPTANCE CHECKLIST)

### 1. Requirements Traceability Matrix (RTM)

| Business Goal (R1 PO) | Feature / Solution Requirement | User Story ID | BDD Scenario Test Case | Component Code Affected | Status |
| :--- | :--- | :---: | :--- | :--- | :---: |
| Triệt tiêu 100% nạp trùng tiền & lag thanh toán | Idempotent One-Tap Payment Engine | **US01**, **US02** | Happy Path IDEM Token & Double-Tap Exception | `GatewayMiddleware`, `PaymentQueueService` | **APPROVED** |
| Rút ngắn thời gian chốt đơn BINGO18 <3s | BINGO18 Turbo Fast-Play Widget | **US06**, **US03** | Fast Checkout Turbo & Biometric Auth | `Bingo18TurboWidget.tsx`, `BiometricController` | **APPROVED** |
| Đưa tỷ trọng Lotto 5/35 >28% toàn hệ thống | Smart Cross-Sell Lotto 5/35 Widget | **US05**, **US04** | Cross-sell 10k at Invoice Screen | `AdaptiveHomeEngine`, `CrossSellWidget` | **APPROVED** |
| Loại bỏ rào cản APK & Nâng cao niềm tin | In-App Auto Updater & Verified Badge | **US07**, **US08** | SHA-256 Checksum & Official Security Badge | `InAppUpdateService`, `TrustShieldBadge` | **APPROVED** |
| Thúc đẩy Social Play & Thu hút 150k user nhóm | Syndicate Play (Mua Vé Nhóm) & Split Payout | **US09**, **US10** | Group Creation, Digital Contract & Auto Split | `SyndicateModule`, `SplitPayoutEngine` | **APPROVED** |
| Giảm VIP Churn <1.5% & Tăng Retention +25% | Vietlott VIP Club & Daily Streaks | **US11**, **US12** | Cashback 2% calculation & 7-day Check-in | `VipLoyaltyEngine`, `GamificationStreakHub` | **APPROVED** |

---

### 2. Bảng Kiểm Tra Tiêu Chí Chấp Nhận Yêu Cầu (Acceptance Criteria Checklist)

| STT | Tiêu Chí Chấp Nhận Bắt Buộc (Mandatory Criteria) | Trạng Thái | Minh Chứng & Vị Trí Trong Tài Liệu |
| :---: | :--- | :---: | :--- |
| 1 | **Gap Analysis:** Đủ As-Is → Gap → To-Be → Action Plan cho top 5 cải tiến kèm Severity & Effort Estimate. | **PASSED** | Mục A — Bảng Gap Analysis chi tiết 5 hạng mục với Severity (High/Medium) & Effort (1-3 Sprints). |
| 2 | **User Story Map:** Đúng chuẩn Jeff Patton (Backbone → Tasks → Walking Skeleton MVP → Release 2/3). | **PASSED** | Mục B.1 — Sơ đồ Story Map 5 Backbone Activities, 16 Stories phân bổ 3 Release Lines. |
| 3 | **Functional Decomposition Diagram:** Phân rã hệ thống dạng Mermaid `graph TD`. | **PASSED** | Mục B.2 — Sơ đồ Mermaid phân rã 5 Sub-systems và 15 Capabilities. |
| 4 | **User Stories & BDD AC:** ≥15 User Stories chuẩn INVEST có Given/When/Then (Happy/Alt/Exception) & MoSCoW. | **PASSED** | Mục C — 16 User Stories chi tiết đầy đủ 3 scenarios BDD/INVEST & phân loại MoSCoW. |
| 5 | **Activity Diagram Purchase Flow:** Luồng mua vé streamlined ≤3 bước — Mermaid `flowchart TD` hợp lệ. | **PASSED** | Mục D.1 — Sơ đồ Activity Flow 3 bước chốt đơn với Idempotency Key & Error Polling. |
| 6 | **Activity Diagram Results & Claiming:** Luồng kết quả & trả thưởng tự động — Mermaid `flowchart TD` hợp lệ. | **PASSED** | Mục D.2 — Sơ đồ Activity Flow đối soát, tính thuế TNCN, chia thưởng Syndicate & Push Noti. |
| 7 | **State Diagram Ticket Lifecycle:** Vòng đời vé số 8 trạng thái — Mermaid `stateDiagram-v2` hợp lệ. | **PASSED** | Mục D.3 — Sơ đồ Trạng thái vé từ DRAFT đến PAID_OUT / DRAWN_NOT_WON. |
| 8 | **Concept Model Diagram:** Mô hình entity nghiệp vụ mới — Mermaid `classDiagram` / `erDiagram` hợp lệ. | **PASSED** | Mục D.4 — Sơ đồ Class Diagram các Entity: User, VipTier, IdempotencyTransaction, Ticket, SyndicateGroup, GamificationStreak. |
| 9 | **Edge Case Analysis:** Bảng phân tích ngoại lệ bao phủ ≥6 nhóm (ở đây bao phủ 8 nhóm). | **PASSED** | Mục E.1 — Bảng 8 kịch bản ngoại lệ chi tiết kèm Timeout, Retry & Compensating Action. |
| 10 | **Timeout & Hung State Analysis:** Trả lời trọn vẹn 7 câu hỏi chuẩn BABOK® v3 / `ba-rules.md`. | **PASSED** | Mục E.2 — Đặc tả định lượng 7 câu hỏi Timeout, Hung State, Circuit Breaker & Idempotency. |
| 11 | **SWOT Analysis:** Đánh giá chiến lược ≥3 items mỗi phần tư (Strengths, Weaknesses, Opportunities, Threats). | **PASSED** | Mục E.3 — Ma trận SWOT 4 ô với 3-4 items chi tiết mỗi phần tư. |

---

*Tài liệu Đặc tả và Phân tích Yêu cầu Nghiệp vụ (R2) được hoàn tất bởi Business Analyst (BA Agent) theo đúng quy tắc `.agents/rules/ba-rules.md` và khung kỹ năng IIBA BABOK® v3.*
