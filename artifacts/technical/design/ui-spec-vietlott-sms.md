# Vietlott SMS App - Design Specification (UI Markdown)

| Version | Ngày | Người thực hiện | Mô tả |
|:---:|:---:|:---:|---|
| 1.0 | 2026-06-22 | UI/UX Designer | Đặc tả thiết kế giao diện ứng dụng Vietlott SMS |

---

## 1. Global Design System (Tokens)

### 1.1 Colors
- **Primary:** `#ED1C24` (Đỏ Vietlott) - Dùng cho nút chính, nền banner chính, tab active.
- **Background (App):** `#F5F5F5` (Xám nhạt) hoặc `#FFFFFF` (Trắng) tùy màn hình.
- **Text Primary:** `#333333` (Đen đậm) - Tiêu đề, nội dung chính.
- **Text Secondary:** `#888888` (Xám) - Placeholder, ghi chú.
- **Accent/Secondary:** `#0056A6` (Xanh dương) - Dùng cho liên kết (link), text nhấn mạnh.
- **Card Background:** `#FFFFFF` (Trắng) - Nền của các danh sách, khung chức năng.
- **Border:** `#E0E0E0` (Xám rất nhạt) - Viền thẻ, form nhập liệu.

### 1.2 Typography
- **Font Family:** `Roboto` (Default System Font).
- **Headings (H1):** 24px, Bold.
- **Titles (H2):** 18px, Bold / Semi-bold.
- **Body Text:** 14px, Regular.
- **Caption / Small Text:** 12px, Regular.

### 1.3 Bottom Navigation (Global Component)
Hiển thị ở dưới cùng của tất cả các màn hình chính (trừ Đăng nhập). Nền trắng, viền trên mỏng hoặc shadow lật lên. **Thứ tự các nút từ trái sang phải như sau:**
1. **Kết quả:** Icon hai vòng tròn lồng nhau.
2. **Lịch sử:** Icon đồng hồ có mũi tên quay vòng.
3. **Trang chủ:** Icon quả bóng xổ số (hoặc logo Vietlott). Nằm ở chính giữa.
4. **Tiện ích:** Icon hộp quà/cửa sổ.
5. **Cá nhân:** Icon user hình người.
*Trạng thái Active:* Text và Icon chuyển sang màu Đỏ (`#ED1C24`).
*Trạng thái Inactive:* Text và Icon màu Xám (`#888888`).

---

## 2. Screens Breakdown

### Screen 1: Màn hình mở App (Trang chủ chưa Đăng nhập)
- **Tham chiếu:** `Login 1.jpg`
- **Background Header:** Đỏ đậm `#ED1C24` kèm pattern cành hoa đào (chủ đề Tết/Xuân).
- **Top Section (User Greeting):**
  - Góc trái: Logo Vietlott màu trắng. Góc phải: Dropdown `Viettel` (nền mờ) và Icon Chuông thông báo.
  - Text: `Chào buổi sáng!` và `NGUYỄN VĂN MINH` (in đậm, chữ trắng).
  - Text mô tả: `Đăng nhập để sử dụng đầy đủ các tính năng` (chữ trắng).
  - Nút `Đăng nhập` to nền trắng chữ đỏ `#ED1C24` và nút `Vân tay` (outline viền mờ) nằm cạnh nhau.
  - Text link: `Quên mật khẩu?` (trắng gạch chân).
  - Mascot: Ông Thần Tài đứng bên phải dang hai tay.
- **Main Menu (Grid Card):** Nền đỏ đô `#B01018` (bo góc 16px). Gồm 3 cột:
  1. Icon Nhà (Trang chủ) màu xanh dương -> Text `Trang chủ`
  2. Icon Quả bóng đỏ Mega 6/45 -> Text `Chọn số Mega 6/45`
  3. Icon Quả bóng vàng Power 6/55 -> Text `Chọn số Power 6/55`
- **Banner Carousel:** Dưới thẻ Menu là các banner trượt ngang (hiển thị banner Bingo nền xanh dương đậm, bóng số 3, 0). Có 2 dấu chấm chuyển slide.
- **Footer (Thông tin liên hệ):** Nền đỏ tối, text trắng. "Tổng đài 1900 599 822 (1.500đ/phút)". Các logo đối tác: Viettel, VDI "là đại lý chính thức của Vietlott". "Phiên bản hiện tại 4.4.18".

### Screen 2: Form Đăng nhập (Login Form)
- **Tham chiếu:** `Login 2.jpg`
- **Background:** `#FFFFFF`
- **Header:** Nút Back (mũi tên trái) ở góc trên cùng bên trái. Góc trên phải có nút `Đăng ký` (nền trắng viền nhạt bo góc, chữ xanh dương). Dòng chữ "Chưa có tài khoản?" nằm cạnh mũi tên lượn sóng trỏ vào nút Đăng ký.
- **Body:**
  - **Logo:** Logo Vietlott SMS hình tròn (màu đỏ) bên trái chữ `Đăng nhập` (size 24px, Bold).
  - **Provider Selector:** Dropdown chọn nhà mạng `Viettel` (chữ xanh dương, gạch chân xanh dương mỏng).
  - **User Info:** Tên `NGUYỄN VĂN MINH` (chữ đỏ in hoa, in đậm), số điện thoại bị che `0394***975`.
  - **Form Input:** Ô `Nhập mật khẩu`. Placeholder màu xám, góc phải có icon `Con mắt` (ẩn/hiện mật khẩu).
  - **Action Row:** Nút `Đăng nhập` lớn, màu nền `#ED1C24`, chữ trắng, bo góc. Kế bên phải là nút `Vân tay` nền xám nhạt bo góc, icon đỏ.
  - **Footer Links:** Hàng dưới cùng có 2 text links: `Bạn quên mật khẩu?` (Trái, chữ đen gạch chân) và `Tài khoản khác` (Phải, chữ xanh).

### Screen 3: Trang chủ (Authenticated Home)
- **Tham chiếu:** `Trang chủ.jpg`
- **Header:** Background màu vàng đồng gradient, có hoa văn lồng đèn mờ.
  - Trái: Avatar `M` nền vàng nhạt. Chữ trắng `NGUYỄN VĂN MINH`, số dư `0đ`.
  - Phải: Các icon trắng liên tiếp: Icon Hộp quà, Icon Chuông, Icon Danh sách menu.
  - Action Row: Nút outline `Rút tiền` (icon xoắn ốc đỏ), Nút outline `Nạp tiền` (icon xoắn ốc đỏ). Góc phải có Box chữ nhật trắng viền bóng `Tải QR nạp` kèm icon mã QR màu xanh.
- **Body (Scrollable):**
  - **Banner Khuyến mãi:** Banner ngang "Giới thiệu hăng say NHẬN NGAY QUÀ KHỦNG", "THAM GIA NGAY". (Nền xanh đậm, rương vàng).
  - **Card Lotto 5/35 (Màu xanh lá):** Góc trái trên "Xổ 2 lần/ngày". Kỳ #00622. Quỹ "15.000.000.000đ". Đồng hồ đếm ngược "01:16:40". Góc phải là túi lộc đỏ "ĐẠT MỨC CHIA", nút vàng "Chơi ngay".
  - **Card Bingo 18 (Nền da cam nhạt):** Góc trái "Xổ 10 phút/kỳ". KQ kỳ #0059237. Bóng xổ 3 quả màu cam "1", "1", "3". Kế tiếp "Kỳ tiếp 00:00". Góc phải có mascot Thần tài, nút đỏ "Chơi ngay".
  - **Card Power 6/55 (Nền kem nhạt):** Có badge "Mai xổ". "Giá trị Jackpot 2", "30.000.000.000đ", Đồng hồ đếm ngược "30:16:40", Kỳ #00517 Thứ 3 23/06/2026. Nút "Chơi ngay" màu vàng nâu.
  - **Card Mega 6/45 (Nền hồng đào - Cắt nửa ở dưới cùng):** "Giá trị Jackpot", Kỳ #00556 Thứ 4.

### Screen 4: Kết quả (Results)
- **Tham chiếu:** `Kết quả.jpg`
- **Header:** Nền trắng. Chữ `Kết quả` to góc trái trên kèm icon cặp giấy nhỏ màu đỏ vàng.
- **Body (List of Results):** Mỗi kết quả là một khối nằm ngang chia cách bằng viền mờ.
  - **Block 1 (Lotto 5/35):** Text thời gian 'Thứ 4, 03/06/2026 - Kỳ #00593 - 21:00', dãy 5 bóng tròn xanh lá '01, 02, 03, 04, 05' và 1 bóng cam '10'. Trạng thái 'Đang cập nhật' màu xanh lá đậm. Dưới cùng: '15988 Vé trúng thưởng' (số đỏ) - 'Xem thêm >' (chữ xanh).
  - **Block 2 (Bingo 18):** Text 'Kết quả kỳ #0059237', bóng cam '1', '1', '3'. Trạng thái 'Cập nhật liên tục' màu đỏ nhạt. Dưới cùng: '0 Vé trúng thưởng' - 'Xem thêm >'.
  - **Block 3 (Max 3D Pro):** Text 'Thứ 5, 07/05/2026 - Kỳ #00316'. 6 bóng tím than đánh số '1 1 1', đường kẻ dọc, '2 2 2'. 'Giải đặc biệt: 2 tỷ' (chữ tím đỏ). Dưới cùng: '2334 Vé trúng thưởng' - 'Xem thêm >'.
  - **Block 4 (Max 3D):** Text 'Thứ 2, 11/05/2026 - Kỳ #00465'. 6 bóng hồng đậm '1 4 5 | 3 4 7'. 'Giải đặc biệt max 3D+: 1 tỷ' (chữ hồng). Dưới cùng: '122 Vé trúng thưởng' - 'Xem thêm >'.

### Screen 5: Lịch sử (History)
- **Tham chiếu:** `Lịch sử.jpg`
- **Background:** `#FFFFFF`
- **Header:** Text `Lịch sử` góc trái trên, icon đồng hồ nhỏ nền đỏ.
- **Top Tabs:** 3 tab tròn:
  1. **Dự thưởng:** Icon vé số đỏ chấm bi, active đỏ.
  2. **Thanh toán:** Icon thẻ tín dụng đỏ, mờ.
  3. **Trúng thưởng:** Icon cúp vàng, mờ.
- **Filters Row:** Dropdown `7 ngày gần nhất`, Text xanh `Tất cả`, Icon Settings (Bộ lọc) bo tròn viền nhạt.
- **Empty State Body:** 
  - Hình ảnh Mascot Ông Thần Tài giơ ngón tay chỉ vào bóng thoại lớn chữ đỏ/xanh thẫm: `MUA VÉ NGAY, VẬN MAY ĐANG CHỜ!`.
  - Text màu xám nhạt: `Bạn chưa có vé dự thưởng`.
  - CTA Button: Nút `Mua vé ngay` hình chữ nhật bo góc, nền đỏ `#ED1C24`, chữ trắng.

### Screen 6: Tiện ích (Utilities)
- **Tham chiếu:** `Tiện ích.jpg`
- **Header:** Text `Tiện ích` góc trái trên, icon quà nhỏ đỏ.
- **Body (Grid Layout):** Lưới thẻ dạng lưới bất đối xứng, lề 16px. Các thẻ bo góc rất lớn.
  - **Card 1 (Full width top):** Background mùa xuân vàng ươm rực rỡ, hình ảnh Mascot cưỡi bạch mã cầm điện thoại. Text mờ `Hội xuân`. Nút trắng `Thử ngay`.
  - **Card 2 (Vuông - Left):** `12 Cung hoàng đạo` (Nền tím galaxy), vòng tròn hoàng đạo Horoscope.
  - **Card 3 (Vuông - Right):** `Tử vi 12 con giáp` (Nền cam gradient sáng), hình bát quái Âm Dương.
  - **Card 4 (Vuông - Left):** `Khai xuân đón lộc` (Nền hồng nhạt hoa đào, chữ uốn lượn thư pháp), có đèn lồng.
  - **Card 5 (Vuông - Right):** `Trao may mắn` (Nền cam đỏ gradient), hộp quà nổ tung xổ ra các quả bóng số. Text nhỏ mô tả cơ hội trúng thưởng.
  - **Card 6 (Chữ nhật ngang - Left):** `Thống kê` (Nền đỏ đậm). Text nhỏ 'Thống kê các con số'.
  - **Card 7 (Chữ nhật ngang - Right):** `Tiện ích chat` (Nền đỏ rực). Text nhỏ 'Buôn chuyện cùng chúng tôi!'.

### Screen 7: Cá nhân (Profile)
- **Tham chiếu:** `Cá nhân.jpg`
- **Header:** Text `Cá nhân` góc trái trên (icon user đỏ vàng).
- **Top Card (Profile Info):** Thẻ lớn nền Gradient Đỏ rực rỡ, hoa văn tròn mờ, bo góc 16px.
  - Góc trái trên: Logo Vietlott trắng, chữ 'Cơ hội để tốt hơn'. Góc phải trên: Huy hiệu tròn viền trắng logo SMS.
  - Hàng giữa: Avatar `M` (vòng tròn vàng), chữ `NGUYỄN VĂN MINH` (trắng), số dư `0đ`. Góc phải có cụm 3 icon outline trắng: Hộp quà (tặng), Chuông, Danh sách.
  - Hàng dưới: Hai nút viền mờ nền trắng trong suốt: `Rút tiền` (icon xoắn đồng hồ), `Nạp tiền` (icon xoắn đồng hồ). Góc phải có box vàng/đỏ: `TẢI QR ĐỂ NẠP TIỀN` kèm mã QR nhỏ trắng.
- **Promo Banner:** Dưới thẻ Profile là thẻ màu hồng nhạt `Vui là Sẻ chia` (chữ cách điệu). Text "Với mỗi 10.000đ mua vé, bạn đã đóng góp gần 3.000đ vào Ngân sách TP Hà Nội".
- **Menu List:** Dạng List, chữ đen, icon mũi tên xám bên phải. Mỗi mục có icon tròn màu ở đầu:
  1. `Thông tin cá nhân` (Icon người + tick xanh).
  2. `Tài khoản nhận thưởng` (Icon thẻ ngân hàng + huy chương vàng).
  3. `Tài khoản thanh toán` (Icon thẻ ngân hàng + mũi tên xanh biển).
  4. `Tài khoản hoàn tiền` (Icon thẻ ngân hàng + đồng xu cam).
  5. `Nơi đăng ký tham gia dự thưởng` (Icon map pin đỏ).
  6. `Cài đặt` (Icon bánh răng xanh đậm).
  7. `Trợ giúp` (Icon dấu hỏi chấm nền xanh đen).
