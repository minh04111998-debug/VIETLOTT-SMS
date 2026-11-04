# [🟢 ROLE: BA] PHÂN TÍCH NGHIỆP VỤ (FUNCTIONAL SPEC) - 4 TÁC VỤ TÍCH HỢP

> **Mục tiêu:** Tài liệu tổng hợp toàn diện (E2E) cho 4 nền tảng tích hợp (ZaloPay, MobiFone Money, Xổ số+, PostPay). Kết hợp giữa **Luồng tổng quan**, **Đặc tả chi tiết từng bước** và **Các ràng buộc nghiệp vụ (Business Rules)**.

---

## BẢNG TỔNG QUAN DANH SÁCH QUY TRÌNH NGHIỆP VỤ

| STT | Tên công việc (Hệ thống) | Tên quy trình chi tiết |
|---|---|---|
| 1 | **TÍCH HỢP VIETLOTT SMS x ZALOPAY** | 1. Quy trình Đăng nhập Onboarding<br>2. Quy trình Liên kết tài khoản thanh toán<br>3. Quy trình Hủy liên kết<br>4. Quy trình Mua vé (PayByToken)<br>5. Quy trình Trả thưởng<br>6. Thêm & Đặt mặc định TKNT ZaloPay |
| 2 | **TÍCH HỢP VIETLOTT SMS x MOBIFONE MONEY** | 1. Luồng truy cập dịch vụ<br>2. Luồng thêm TKTT<br>3. Luồng Liên kết tài khoản<br>4. Luồng Thanh toán mua vé (Bypass Threshold)<br>5. Luồng Hủy liên kết<br>6. Luồng Đối soát tự động (Batch sFTP) |
| 3 | **TÍCH HỢP VIETLOTT SMS x POSTPAY (VNPOST)** | 1. Quy trình Liên kết TK Merchant<br>2. Quy trình Thanh toán<br>3. Quy trình Hoàn trả<br>4. Quy trình Hủy liên kết |
| 4 | **SẢN PHẨM XỔ SỐ+ (CỘNG TÁC VIÊN)** | 1. Luồng Đăng ký TK CTV<br>2. Luồng CTV Đăng ký TK Khách Hàng<br>3. Luồng Mua hộ vé (Mandatory Confirmation)<br>4. Luồng Hoàn tiền Mua hộ<br>5. Luồng Thống kê Hoa hồng |

---

## 1. TÍCH HỢP VIETLOTT SMS x ZALOPAY

### 1.1. TỔNG QUAN & TƯƠNG TÁC HỆ THỐNG
- **Mục tiêu:** Mở rộng kênh bán vé qua ứng dụng ZaloPay, mang lại trải nghiệm thanh toán không gián đoạn.
- **Hệ thống tham gia:** ZaloPay App, ZaloPay API System, Vietlott SMS Backend.
- **Giao diện:** Webview HTML5 nhúng trên ZaloPay.
- **Bảo mật API:** Xác thực người dùng bằng **OAuth 2.0**.
- **Payout:** Gọi API "Chi Hộ" (Disbursement) của ZaloPay để trả thưởng tự động.

### 1.2. QUY TRÌNH CHI TIẾT (STEP-BY-STEP)

#### 1.2.1. Quy trình Đăng nhập Onboarding
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Mở ứng dụng | Khách hàng | Khách hàng mở ứng dụng ZaloPay. |
| 2 | Chọn dịch vụ | Khách hàng | Khách hàng chọn dịch vụ Vietlott SMS. |
| 3 | Mở Webview | ZaloPay | ZaloPay gọi URL Webview truyền tham số `telco_code`. |
| 4 | Kiểm tra nhà mạng | Hệ thống Vietlott | Hệ thống Vietlott kiểm tra `telco_code`. Nếu không thuộc Viettel, MobiFone, VinaPhone -> Hiển thị lỗi chặn truy cập và dừng luồng. |
| 5 | Kiểm tra đăng nhập | Hệ thống Vietlott | Hệ thống Vietlott kiểm tra trạng thái Webview đã từng đăng nhập SĐT chưa. |
| 6 | Yêu cầu chia sẻ TT | ZaloPay | Nếu chưa đăng nhập, ZaloPay hiển thị màn hình yêu cầu Khách hàng xác nhận chia sẻ thông tin. |
| 7 | Xác nhận chia sẻ | Khách hàng | Khách hàng bấm nút [Đồng ý] trên màn hình ZaloPay. |
| 8 | Chuyển hướng | ZaloPay | ZaloPay chuyển hướng về Vietlott kèm theo `Authorization code`. |
| 9 | Gọi API xác thực | Hệ thống Vietlott | Hệ thống Vietlott gọi API ZaloPay truyền `Authorization code`. |
| 10 | Trả Token | ZaloPay API | ZaloPay trả về `Access token` và `Refresh token` cho Vietlott. |
| 11 | Lấy thông tin cơ bản | Hệ thống Vietlott | Hệ thống Vietlott dùng `Access token` gọi API lấy SĐT và Họ tên từ ZaloPay. |
| 12 | Trả dữ liệu KH | ZaloPay API | ZaloPay trả dữ liệu SĐT và Họ tên về cho Vietlott. |
| 13 | Kiểm tra TKDT | Hệ thống Vietlott | Hệ thống Vietlott kiểm tra SĐT đã tồn tại Tài khoản dự thưởng (TKDT) chưa. |
| 14 | Lấy thông tin eKYC | Hệ thống Vietlott | Hệ thống Vietlott gọi API ZaloPay để lấy thông tin eKYC chi tiết (nếu cần). |
| 15 | Trả dữ liệu eKYC | ZaloPay API | ZaloPay trả về toàn bộ dữ liệu eKYC (Giấy tờ, Ngày cấp, Nơi cấp...). |
| 16 | Lưu trữ eKYC | Hệ thống Vietlott | Hệ thống Vietlott lưu trữ thông tin eKYC để đối chiếu. |
| 17 | Chuyển luồng | Hệ thống Vietlott | Nếu SĐT chưa có TKDT, hệ thống chuyển sang luồng Đăng ký mới. |
| 18 | Điền sẵn thông tin | Hệ thống Vietlott | Hệ thống điền sẵn thông tin nhà mạng, SĐT (block không cho sửa) và Bypass luồng gửi OTP xác thực SĐT. |
| 19 | Hiển thị Đăng nhập | Hệ thống Vietlott | Nếu SĐT đã có TKDT, hiển thị màn hình Đăng nhập. |
| 20 | Điền sẵn thông tin | Hệ thống Vietlott | Hệ thống điền sẵn mạng và SĐT trên màn hình Đăng nhập. |
| 21 | Nhập mật khẩu | Khách hàng | Khách hàng nhập Mật khẩu TKDT. |
| 22 | Xác thực | Hệ thống Vietlott | Hệ thống xác thực mật khẩu và lưu trạng thái phiên đăng nhập. |
| 23 | Kiểm tra TKTT | Hệ thống Vietlott | Hệ thống kiểm tra Khách hàng đã liên kết Tài khoản thanh toán (TKTT) là ví ZaloPay chưa. |
| 24 | Tự động liên kết | Hệ thống Vietlott | Nếu chưa có TKTT, tự động tạo mới liên kết TKTT ZaloPay với số tài khoản là SĐT vừa đăng nhập. |
| 25 | Kiểm tra TK mặc định | Hệ thống Vietlott | Nếu đã liên kết TKTT, hệ thống kiểm tra trạng thái Tài khoản mặc định. |
| 26 | Đề xuất mặc định | Hệ thống Vietlott | Nếu ZaloPay chưa phải TKTT mặc định, hiển thị Popup đề xuất đổi TKTT mặc định thành ZaloPay. |
| 27 | Xác nhận mặc định | Khách hàng | Khách hàng bấm [Đồng ý] trên Popup. |
| 28 | Cập nhật mặc định | Hệ thống Vietlott | Hệ thống cập nhật ZaloPay làm TKTT mặc định. |
| 29 | Kiểm tra TKNT | Hệ thống Vietlott | Hệ thống tiếp tục kiểm tra Khách hàng đã có Tài khoản nhận thưởng (TKNT) là ZaloPay chưa. |
| 30 | Đề xuất nhận thưởng | Hệ thống Vietlott | Nếu chưa có TKNT ZaloPay, hiển thị Popup thông báo tính năng nhận thưởng ZaloPay miễn phí. |
| 31 | Xác nhận TKNT | Khách hàng | Khách hàng bấm [Đồng ý] thiết lập TKNT. |
| 32 | Chuyển hướng Trang chủ | Hệ thống Vietlott | Hệ thống chuyển hướng Khách hàng vào trang chủ Vietlott SMS. Quá trình Onboarding kết thúc. |

#### 1.2.2. Quy trình Liên kết tài khoản thanh toán
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Truy cập Quản lý TK | Khách hàng | Khách hàng truy cập trang Quản lý Tài khoản thanh toán trên Vietlott SMS. |
| 2 | Chọn Liên kết | Khách hàng | Khách hàng bấm nút [Liên kết] tại logo ZaloPay. |
| 3 | Yêu cầu URL liên kết | Hệ thống Vietlott | Hệ thống Vietlott gọi API yêu cầu ZaloPay sinh đường dẫn web liên kết. |
| 4 | Kiểm tra Merchant | ZaloPay API | ZaloPay kiểm tra tính hợp lệ của Merchant. Nếu không hợp lệ -> Trả về lỗi, Vietlott hiển thị lỗi và dừng. |
| 5 | Trả URL | ZaloPay API | ZaloPay trả về URL liên kết cho Vietlott. |
| 6 | Mở URL | Hệ thống Vietlott | Hệ thống Vietlott mở URL hiển thị màn hình xác nhận của ZaloPay. |
| 7 | Yêu cầu mật khẩu | ZaloPay | ZaloPay yêu cầu Khách hàng nhập mật khẩu thanh toán (hoặc sinh trắc học). |
| 8 | Xác nhận | Khách hàng | Khách hàng xác nhận mật khẩu hợp lệ. |
| 9 | Trả kết quả | ZaloPay API | ZaloPay trả kết quả liên kết thành công về cho Hệ thống Vietlott qua Callback/Redirect. |
| 10 | Ghi nhận liên kết | Hệ thống Vietlott | Hệ thống Vietlott ghi nhận trạng thái đã liên kết TKTT ZaloPay và hiển thị thông báo thành công cho Khách hàng. |

#### 1.2.3. Quy trình Hủy liên kết
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Truy cập Quản lý TK | Khách hàng | Khách hàng vào mục Quản lý Tài khoản thanh toán. |
| 2 | Yêu cầu hủy | Khách hàng | Khách hàng chọn ZaloPay và bấm nút [Hủy liên kết]. |
| 3 | Gửi API hủy | Hệ thống Vietlott | Hệ thống Vietlott gửi API yêu cầu hủy token liên kết sang ZaloPay. |
| 4 | Cập nhật trạng thái | ZaloPay API / Hệ thống Vietlott | ZaloPay xử lý hủy phía Ví, trả về phản hồi thành công. Hệ thống Vietlott cập nhật trạng thái "Chưa liên kết" trên giao diện. |

#### 1.2.4. Quy trình Mua vé (PayByToken)
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Chốt giỏ hàng | Khách hàng | Khách hàng chọn bộ số và chốt giỏ hàng trên Vietlott SMS. |
| 2 | Chọn thanh toán | Khách hàng | Khách hàng chuyển sang màn hình Thanh toán, chọn nguồn tiền ZaloPay. |
| 3 | Hiển thị chi tiết tiền | Hệ thống Vietlott | Hệ thống Vietlott hiển thị chi tiết 3 dòng: Giá vé gốc, Phí xử lý giao dịch, Tổng tiền thanh toán. |
| 4 | Xác nhận đặt vé | Khách hàng | Khách hàng bấm xác nhận [SMS Đặt vé]. |
| 5 | Gửi API thanh toán | Hệ thống Vietlott | Hệ thống Vietlott gửi yêu cầu thanh toán PayByToken sang API ZaloPay. |
| 6 | Xử lý trừ tiền | ZaloPay API | ZaloPay kiểm tra số dư và trừ tiền trong ví Khách hàng. |
| 7 | Xử lý lỗi trừ tiền | ZaloPay API / Hệ thống Vietlott | Nếu trừ tiền thất bại (không đủ số dư/lỗi ví), ZaloPay trả mã lỗi -> Vietlott hiển thị thông báo lỗi cho Khách hàng và dừng luồng. |
| 8 | Xác nhận trừ tiền | ZaloPay API | Nếu trừ tiền thành công, ZaloPay trả kết quả thành công cho Vietlott. |
| 9 | Gửi lệnh BGT | Hệ thống Vietlott | Hệ thống Vietlott sinh lệnh mua vé và gửi sang hệ thống BGT. |
| 10 | Xử lý xuất vé | Hệ thống BGT | Hệ thống BGT tiếp nhận và xử lý yêu cầu xuất vé. |
| 11 | Nhận lỗi xuất vé | Hệ thống Vietlott | Nếu hệ thống BGT phản hồi hết vé hoặc lỗi xuất vé -> Vietlott ghi nhận trạng thái lỗi. |
| 12 | Yêu cầu hoàn tiền | Hệ thống Vietlott | Vietlott gọi API Hoàn tiền (Refund) của ZaloPay để trả lại Tiền gốc + Phí cho Khách hàng (trường hợp hoàn về Ví ZaloPay) hoặc ghi tăng Hạn mức dự thưởng (HMDT - chỉ hoàn tiền gốc, phí = 0đ). |
| 13 | Thực hiện hoàn tiền | ZaloPay API | ZaloPay thực hiện hoàn tiền. |
| 14 | Ghi nhận vé hợp lệ | Hệ thống Vietlott | Nếu BGT phản hồi xuất vé thành công -> Vietlott ghi nhận trạng thái vé hợp lệ. |
| 15 | Gửi SMS thông báo | Hệ thống Vietlott | Vietlott gửi tin nhắn SMS thông báo mua vé thành công cho Khách hàng. |
| 16 | Hiển thị thành công | Hệ thống Vietlott | Màn hình Khách hàng chuyển sang trạng thái Đặt vé thành công. |

#### 1.2.5. Quy trình Trả thưởng
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Quét vé trúng thưởng | Hệ thống Vietlott | Hệ thống Vietlott tự động quét danh sách vé trúng thưởng. |
| 2 | Chốt danh sách | Web Admin | Web Admin / Hệ thống chốt danh sách khách hàng có TKNT là ZaloPay để lập lô trả thưởng. |
| 3 | Gọi API Chi hộ | Hệ thống Vietlott | Hệ thống Vietlott gọi API Chi hộ (Disbursement) của ZaloPay cho từng giao dịch (hoặc theo lô). |
| 4 | Kiểm tra hợp lệ | ZaloPay API | ZaloPay tiếp nhận yêu cầu và kiểm tra tính hợp lệ của tài khoản ví đích. |
| 5 | Cộng tiền vào ví | ZaloPay API | ZaloPay thực hiện cộng tiền vào ví Khách hàng. |
| 6 | Trả kết quả | ZaloPay API | ZaloPay trả về kết quả trạng thái "Thành công" cho Vietlott. |
| 7 | Cập nhật trạng thái | Hệ thống Vietlott | Hệ thống Vietlott cập nhật trạng thái đã trả thưởng cho vé. |
| 8 | Gửi SMS chúc mừng | Hệ thống Vietlott | Hệ thống Vietlott gửi SMS chúc mừng và thông báo đã trả thưởng thành công. |
| 9 | Nhận thông báo ví | Khách hàng | Khách hàng nhận được biến động số dư trên ZaloPay. |
| 10 | Yêu cầu tăng HMBH | Kế toán Vietlott | Kế toán Vietlott thực hiện thủ tục yêu cầu tăng Hạn mức bán hàng (HMBH) sang BGT định kỳ. |
| 11 | Phê duyệt HMBH | Hệ thống BGT | Hệ thống BGT phê duyệt và phản hồi. |
| 12 | Tăng HMBH nội bộ | Hệ thống Vietlott | Hệ thống Vietlott tự động ghi tăng HMBH nội bộ. |
| 13 | Bù trừ dòng tiền | Kế toán Vietlott | Kế toán thực hiện bù trừ dòng tiền Tiền gốc + 0.2% Phí ủy quyền. |

#### 1.2.6. Thêm & Đặt mặc định TKNT ZaloPay
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Truy cập Quản lý TKNT | Khách hàng | Khách hàng truy cập Quản lý Tài khoản nhận thưởng. |
| 2 | Chọn Thêm mới | Khách hàng | Khách hàng chọn Thêm mới TKNT. |
| 3 | Điền sẵn thông tin | Hệ thống Vietlott | Hệ thống tự động điền sẵn Data ZaloPay của Khách hàng, ẩn toàn bộ các tùy chọn Ngân hàng/Ví khác. |
| 4 | Đặt mặc định | Khách hàng | Khách hàng bấm nút [Đặt mặc định]. |
| 5 | Kiểm tra vé chờ | Hệ thống Vietlott | Hệ thống kiểm tra xem Khách hàng có vé chờ trả thưởng nào đang dùng TKNT cũ không. Nếu có, thực hiện theo rule hiện hành. |
| 6 | Cập nhật trạng thái | Hệ thống Vietlott | Hệ thống đồng bộ thông tin TKNT sang BGT, lưu trạng thái ZaloPay là TKNT mặc định và hiển thị thông báo thành công cho Khách hàng. |

### 1.3. QUY TẮC NGHIỆP VỤ & RÀNG BUỘC (Business Rules)
- **Giới hạn mạng:** Yêu cầu người dùng đăng nhập bằng SĐT thuộc Viettel, MobiFone, VinaPhone (Nếu khác: Chặn truy cập).
- **Cấu trúc phí:** Giao dịch qua ZaloPay bị tính `Phí xử lý (% trên giá vé)`. Total = Giá vé + Phí.
- **Tuân thủ NĐ 2345:** Để thực hiện luồng Rút/Chuyển tiền ví, Merchant bắt buộc phải upload **Public Key** và dùng **Private Key** để ký số xác thực (Digital Signature).

### 1.4. KỊCH BẢN GIAO DỊCH (Use Cases)
- **✅ Happy Case:** Khách chọn số -> PayByToken trừ tiền (kèm phí) -> Gửi BGT xuất vé -> Trả thưởng (API Chi Hộ) thành công.
- **⚠️ Edge Case 1 (Lỗi xuất vé):** Trừ tiền ZaloPay thành công, nhưng BGT báo hết vé -> API kích hoạt hoàn tiền Real-time ngay lập tức kèm theo phí giao dịch.

---

## 2. TÍCH HỢP VIETLOTT SMS x MOBIFONE MONEY

### 2.1. TỔNG QUAN & TƯƠNG TÁC HỆ THỐNG
- **Mục tiêu:** Nhúng Vietlott SMS lên app MobiFone Money, tận dụng cả nguồn tiền Ví và Tiền di động (Mobile Money).
- **Giao diện:** Webview HTML5.
- **Đối soát dữ liệu:** Giao tiếp qua kết nối SFTP/FTP. Bắt buộc dùng chuẩn mã hóa **PGP RSA-3072** để mã hóa file đối soát.

### 2.2. QUY TRÌNH CHI TIẾT (STEP-BY-STEP)

#### 2.2.1. Luồng truy cập dịch vụ
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Mở ứng dụng | Khách hàng | Khách hàng mở ứng dụng MobiFone Money, bấm chọn icon Vietlott SMS. |
| 2 | Truyền Token | MobiFone | Ứng dụng MobiFone gọi Webview tải lên kèm theo Token định danh của Khách hàng, hệ thống Vietlott tự động nhận diện và đăng nhập khách hàng. |

#### 2.2.2. Luồng thêm TKTT
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Truy cập Quản lý TK | Khách hàng | Khách hàng truy cập màn hình Quản lý Tài khoản thanh toán trên Webview Vietlott. |
| 2 | Nhận diện phiên | Hệ thống Vietlott | Hệ thống Vietlott nhận diện phiên đăng nhập từ MobiFone, tự động chỉ hiển thị các tùy chọn thanh toán của MobiFone Money (ẩn tất cả các ngân hàng khác). |

#### 2.2.3. Luồng Liên kết tài khoản
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Yêu cầu Liên kết | Khách hàng | Khách hàng bấm chọn [Liên kết] dịch vụ MobiFone Money. |
| 2 | Chọn nguồn tiền | Khách hàng | Hệ thống yêu cầu Khách hàng lựa chọn một trong hai nguồn tiền: Ví điện tử hoặc Mobile Money. |
| 3 | Xác thực OTP | Khách hàng / MobiFone API | Hệ thống MobiFone gửi OTP về SĐT, Khách hàng nhập OTP xác thực. Nếu thành công, Vietlott lưu Token thanh toán. |

#### 2.2.4. Luồng Thanh toán mua vé (Bypass Threshold)
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Chốt giỏ hàng | Khách hàng | Khách hàng chốt giỏ hàng và chọn thanh toán bằng MobiFone Money. |
| 2 | Kiểm tra Hạn mức | Hệ thống Vietlott | Hệ thống Vietlott kiểm tra giá trị của đơn hàng so với `Hạn mức Bypass OTP` (ngưỡng giao dịch cấu hình trước). |
| 3 | Thanh toán <= Hạn mức | Hệ thống Vietlott | Nếu giá trị đơn hàng <= Hạn mức Bypass OTP: Vietlott gọi API PayByToken yêu cầu MobiFone Money trừ tiền tự động không cần xác thực OTP. |
| 4 | Thanh toán > Hạn mức | Hệ thống Vietlott | Nếu giá trị đơn hàng > Hạn mức Bypass OTP: Vietlott thông báo yêu cầu Khách hàng phải nhập mã OTP do MobiFone gửi tới để xác thực. |
| 5 | Trừ tiền | MobiFone API | MobiFone tiến hành trừ tiền. Trong quá trình trừ tiền, nếu Ví của khách hàng bị khóa, API sẽ trả về Exception (các mã lỗi từ VLT-252 đến VLT-255). |
| 6 | Xử lý Exception | Hệ thống Vietlott | Hệ thống Vietlott bắt lỗi Exception, hiển thị thông báo Ví không khả dụng và dừng luồng. |
| 7 | Xuất vé | Hệ thống Vietlott / Hệ thống BGT | Nếu trừ tiền thành công, Vietlott tiến hành xuất vé qua hệ thống BGT. |

#### 2.2.5. Luồng Hủy liên kết
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Yêu cầu hủy | Khách hàng | Khách hàng chọn TKTT MobiFone Money đã liên kết và bấm nút [Hủy liên kết]. |
| 2 | Xử lý hủy | Hệ thống Vietlott | Hệ thống Vietlott gọi API sang MobiFone yêu cầu xóa Token liên kết, đồng thời cập nhật trạng thái hủy ở phía Vietlott. |

#### 2.2.6. Luồng Đối soát tự động (Batch sFTP)
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Xuất file đối soát | Hệ thống Vietlott | Cuối ngày, hệ thống Vietlott tổng hợp giao dịch, xuất file đối soát có định dạng `MPOAPI_VLSMS...txt`. |
| 2 | Mã hóa và Tải lên | Hệ thống Vietlott | Hệ thống Vietlott tiến hành mã hóa chuẩn PGP RSA-3072 cho file này và tự động upload lên server SFTP của MobiFone. |
| 3 | Trả kết quả | MobiFone | Hệ thống MobiFone tiếp nhận file, giải mã, thực hiện đối soát tự động và trả lại 2 file kết quả: file Matched (các giao dịch khớp) và file RRC (các giao dịch sai lệch). |
| 4 | Giải mã và Import | Hệ thống Vietlott | Hệ thống Vietlott tự động tải file từ SFTP, giải mã và import vào trang Admin để Kế toán xử lý. |

### 2.3. QUY TẮC NGHIỆP VỤ & RÀNG BUỘC (Business Rules)
- **Ngưỡng thanh toán (PayByToken Conditional):** Cấu hình `Ngưỡng giao dịch bypass OTP`.
- **Chặn Trả thưởng:** **Không** hỗ trợ trả thưởng vào TK MobiFone Money.
- **Hoàn tiền:** Chỉ hoàn tiền về ví MobiFone Money, không hoàn về HMDT.
- **Chia sẻ rủi ro (RRC):** Lệch đối soát do lỗi gián đoạn hệ thống khách quan, chịu rủi ro **50:50**.

### 2.4. KỊCH BẢN GIAO DỊCH (Use Cases)
- **✅ Happy Case:** Đơn 20k (Dưới Threshold) -> Tự động trừ tiền không cần OTP -> Xuất vé.
- **⚠️ Edge Case 1 (Vượt hạn mức):** Đơn 500k (Vượt Threshold) -> Trả về lỗi -> Yêu cầu khách nhập OTP.
- **⚠️ Edge Case 2 (Mã lỗi VLT):** Khách bị khóa ví -> Hệ thống bắt mã lỗi `VLT-254/255` và nhả Pop-up báo ví không khả dụng.

---

## 3. TÍCH HỢP VIETLOTT SMS x POSTPAY (VNPOST)

### 3.1. TỔNG QUAN & TƯƠNG TÁC HỆ THỐNG
- **Mục tiêu:** Mở kênh bán vé trên ứng dụng thanh toán PostPay của mạng lưới bưu điện VNPOST.
- **Bảo mật API:** Mọi Request giao tiếp API yêu cầu băm chữ ký (Signature Hash) bằng thuật toán **SHA256** kèm Secret Key riêng.
- **Quản lý liên kết:** Hỗ trợ đồng bộ trạng thái hủy liên kết 2 chiều qua webhook.

### 3.2. QUY TRÌNH CHI TIẾT (STEP-BY-STEP)

#### 3.2.1. Quy trình Liên kết TK Merchant
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Chọn liên kết | Khách hàng | Khách hàng chọn liên kết PostPay trên ứng dụng Vietlott SMS. |
| 2 | Gọi API auth | Hệ thống Vietlott | Hệ thống Vietlott gọi API `/auth` sang PostPay để lấy `app_token`. |
| 3 | Gọi API request | Hệ thống Vietlott | Hệ thống Vietlott gọi tiếp API `/request-v3` kèm số điện thoại Khách hàng. |
| 4 | Gửi OTP | PostPay API | PostPay xác nhận và gửi SMS chứa mã OTP cho Khách hàng. |
| 5 | Nhập OTP | Khách hàng | Khách hàng nhập mã OTP lên màn hình ứng dụng. |
| 6 | Xác thực OTP | Hệ thống Vietlott | Hệ thống Vietlott băm dữ liệu theo thuật toán SHA256 và gọi API `/confirm-v3` sang PostPay. |
| 7 | Trả Token | PostPay API | PostPay xác thực OTP và trả về `user_token` (Token liên kết dài hạn). |

#### 3.2.2. Quy trình Thanh toán
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Xác nhận đơn hàng | Khách hàng | Khách hàng xác nhận thanh toán đơn hàng. |
| 2 | Gọi API request | Hệ thống Vietlott | Hệ thống Vietlott lấy `user_token` của Khách hàng, băm SHA256 và gọi API `/request-v2` sang PostPay. |
| 3 | Xử lý sinh trắc học | PostPay API | PostPay xử lý yêu cầu. Nếu hệ thống PostPay yêu cầu sinh trắc học (Trả về mã lỗi 101/102), hệ thống Vietlott sẽ Hold đơn hàng. |
| 4 | Mở ứng dụng PostPay | Hệ thống Vietlott | Hệ thống Vietlott gọi Redirect/Deeplink để mở ứng dụng PostPay, yêu cầu Khách hàng quét FaceID. |
| 5 | Gọi Webhook FaceID | PostPay API | Sau khi quét FaceID thành công, PostPay gọi webhook (IPN Callback) báo cho Vietlott. |
| 6 | Xác thực thanh toán | PostPay API | PostPay yêu cầu xác thực thanh toán (qua OTP hoặc PayByToken tự động). |
| 7 | Chốt giao dịch | Hệ thống Vietlott | Hệ thống Vietlott gọi API `/confirm-v2` để chốt giao dịch. |
| 8 | Xử lý Timeout | Hệ thống Vietlott | Nếu gặp Timeout không nhận được phản hồi, hệ thống Vietlott kích hoạt Job tự động (Poll check status) gọi lại sau mỗi 30 giây để kiểm tra. |
| 9 | Xuất vé | Hệ thống Vietlott | Sau khi trạng thái thanh toán thành công, Vietlott gọi BGT xuất vé cho Khách hàng. |

#### 3.2.3. Quy trình Hoàn trả
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Yêu cầu hoàn trả | Khách hàng / Hệ thống Vietlott | Khách hàng hoặc Hệ thống phát sinh yêu cầu hoàn trả (do vé lỗi, BGT từ chối). |
| 2 | Gọi API refund | Hệ thống Vietlott | Hệ thống Vietlott lấy `user_token`, băm SHA256 và gọi API `/refund-v2` sang PostPay. |
| 3 | Duyệt hoàn trả | Kế toán Vietlott | Giao dịch đưa vào hàng chờ, kế toán kiểm tra và gọi API `/confirm-v2` (tái sử dụng API confirm cho luồng hoàn trả) để duyệt. |
| 4 | Poll trạng thái | Hệ thống Vietlott | Hệ thống Vietlott tự động gọi API `/check-state` để poll trạng thái hoàn trả cho đến khi thành công. |

#### 3.2.4. Quy trình Hủy liên kết
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Yêu cầu hủy | Khách hàng / PostPay | Khách hàng hoặc PostPay yêu cầu hủy liên kết. |
| 2 | Hủy trên Vietlott | Hệ thống Vietlott | (Trường hợp KH hủy trên Vietlott): Hệ thống gọi API `/cancel` sang PostPay. |
| 3 | Vô hiệu hóa Token | PostPay API | PostPay tiếp nhận, đánh dấu vô hiệu hóa `user_token`. |
| 4 | Hủy trên PostPay | PostPay API / Hệ thống Vietlott | (Trường hợp KH hủy trên app PostPay): PostPay gọi webhook sang Vietlott thông báo hủy. Hệ thống Vietlott cập nhật trạng thái vô hiệu hóa. |

### 3.3. QUY TẮC NGHIỆP VỤ & RÀNG BUỘC (Business Rules)
- **Cấu hình Trả thưởng:** Chỉ cho phép thêm TKNT và thực hiện Chi hộ qua kênh thủ công (MANUAL BANK).
- **Báo cáo:** MT trả về máy khách hàng phải đính kèm nhãn mác Kênh bán "PostPay".

### 3.4. KỊCH BẢN GIAO DỊCH (Use Cases)
- **✅ Happy Case:** Khách thanh toán -> Token hợp lệ -> Trừ tiền thành công.
- **⚠️ Edge Case 1 (Sinh trắc học):** API trả mã lỗi `101/102` (Rủi ro cao) -> Redirect Deeplink quét FaceID -> IPN callback.
- **⚠️ Edge Case 2 (Sai lệch Đối soát):** Giao diện Admin tự động lọc ra các giao dịch `Sai lệch` hoặc `PostPay có - VLT không có` để Ops đối soát tay.

---

## 4. SẢN PHẨM XỔ SỐ+ (CỘNG TÁC VIÊN)

### 4.1. TỔNG QUAN & TƯƠNG TÁC HỆ THỐNG
- **Mục tiêu:** Mở rộng bán vé qua Cộng tác viên (CTV). CTV nạp tiền (ứng trước) và lập lệnh mua hộ vé.
- **Hệ thống tham gia:** Admin CMS, VPBank VAN (Virtual Account), SMS Gateway, BGT.

### 4.2. QUY TRÌNH CHI TIẾT (STEP-BY-STEP)

#### 4.2.1. Luồng Đăng ký TK CTV
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Đăng ký tài khoản | Người dùng | Người dùng tải ứng dụng, đăng ký với vai trò Cộng tác viên (CTV). |
| 2 | Xác thực hồ sơ | Hệ thống Vietlott | Hệ thống xác thực hồ sơ CTV. |
| 3 | Cấp TK VAN | Hệ thống Vietlott | Hệ thống tạo và cấp tài khoản ngân hàng ảo **VPBank VAN (Virtual Account)** làm tài khoản chuyên dụng để CTV nạp tiền ứng trước (Hệ thống không tạo TKDT thông thường cho luồng này). |

#### 4.2.2. Luồng CTV Đăng ký TK Khách Hàng
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Thu thập thông tin | Cộng tác viên | CTV thu thập thông tin của Khách hàng mới. |
| 2 | Nhập dữ liệu | Cộng tác viên | CTV nhập dữ liệu (Họ tên, SĐT, Giấy tờ) lên hệ thống để tạo tài khoản cho Khách hàng. |
| 3 | Duyệt hồ sơ | Hệ thống Vietlott / Bộ phận NV | Hệ thống tiếp nhận hồ sơ, đánh cờ ưu tiên (Flag) và chuyển sang luồng Duyệt Manual (Duyệt thủ công) bởi bộ phận nghiệp vụ. |

#### 4.2.3. Luồng Mua hộ vé (Mandatory Confirmation)
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Chọn số mua hộ | Cộng tác viên | CTV chọn bộ số cho Khách hàng trên ứng dụng. |
| 2 | Tạm giữ tiền | Hệ thống Vietlott | Hệ thống kiểm tra số dư TK VAN của CTV và tiến hành Hold (tạm giữ) số tiền tương ứng. |
| 3 | Sinh link URL | Hệ thống Vietlott | Hệ thống sinh ra một đường link URL chứa mã Random ID chống giả mạo và thiết lập thời gian hết hạn (TTL - Time To Live). |
| 4 | Gửi SMS | SMS Gateway | Hệ thống gọi SMS Gateway để gửi tin nhắn chứa link URL đến số điện thoại của Khách hàng. |
| 5 | Bấm link xác nhận | Khách hàng | Khách hàng nhận được SMS, click vào đường link URL để xác nhận đồng ý mua vé. |
| 6 | Tiếp nhận yêu cầu | Hệ thống Vietlott | Hệ thống nhận được yêu cầu từ URL, kiểm tra thời gian hiện tại so với giờ đóng kỳ quay số. |
| 7 | Chặn T-30s | Hệ thống Vietlott | Nếu thời gian hiện tại nằm trong khoảng sát giờ đóng kỳ (Khoảng cách <= 30 giây - T-30s), hệ thống tự động chặn giao dịch, hủy lệnh để tránh rủi ro trôi vé qua kỳ sau. |
| 8 | Đẩy lệnh xuất vé | Hệ thống Vietlott | Nếu khoảng cách thời gian an toàn (> 30 giây), hệ thống đẩy lệnh mua sang BGT. |
| 9 | Theo dõi Timeout | Hệ thống Vietlott | Hệ thống theo dõi phản hồi từ BGT. Nếu BGT phản hồi chậm quá 60 giây (Timeout), ghi nhận SLA Violation, BGT sẽ chịu trách nhiệm đền bù. |

#### 4.2.4. Luồng Hoàn tiền Mua hộ
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Giao dịch thất bại | Khách hàng / Hệ thống Vietlott | Giao dịch mua hộ thất bại do các nguyên nhân: Khách hàng không click link khi hết TTL, BGT báo hết vé, hoặc bị chặn bởi rule T-30s. |
| 2 | Cập nhật trạng thái | Hệ thống Vietlott | Hệ thống cập nhật trạng thái hủy giao dịch mua hộ. |
| 3 | Nhả tiền (Unlock) | Hệ thống Vietlott | Hệ thống thực hiện lệnh Unlock (Nhả tiền) vào lại TK VAN của CTV. (Lưu ý: Nếu vé đã xuất thành công nhưng sau đó gặp lỗi hệ thống cần hoàn tiền, tiền sẽ được hoàn thẳng về Tài khoản của Khách hàng, CTV không được hưởng). |

#### 4.2.5. Luồng Thống kê Hoa hồng
| STT | Tên bước | Người / Hệ thống thực hiện | Mô tả |
|---|---|---|---|
| 1 | Quét giao dịch | Hệ thống Vietlott | Hệ thống chạy Job định kỳ (cuối ngày/cuối tháng) quét danh sách các giao dịch mua hộ thành công (Khách hàng KYC thành công và mua vé hợp lệ). |
| 2 | Tính toán hoa hồng | Hệ thống Vietlott | Hệ thống tính toán % hoa hồng doanh thu cho CTV. |
| 3 | Tăng Hạn mức | Hệ thống Vietlott / Kế toán | Hệ thống ghi tăng Hạn mức hoa hồng của CTV. Kế toán tiến hành duyệt để CTV có thể rút tiền hoa hồng về ngân hàng cá nhân. |

### 4.3. QUY TẮC NGHIỆP VỤ & RÀNG BUỘC (Business Rules)
- **Xác thực mua hộ (Bắt buộc):** Khách hàng phải bấm link xác nhận. Link có mã Random ID chống giả mạo và có thời gian hiệu lực (TTL).
- **Bảo vệ quyền lợi:** Tiền hoàn khi vé lỗi/hết sẽ được trả thẳng về tài khoản của **Khách hàng**.
- **Quy tắc T-30s:** Chặn không gửi lệnh mua vé sang BGT nếu thời gian sát giờ đóng kỳ chỉ còn dưới 30 giây.
- **SLA Timeout:** Giới hạn BGT phản hồi là **60 giây**. Quá thời gian, BGT chịu trách nhiệm đền bù.

### 4.4. KỊCH BẢN GIAO DỊCH (Use Cases)
- **✅ Happy Case:** CTV chọn số -> KH click link ngay -> Gọi API BGT -> Vé xuất, CTV nhận hoa hồng.
- **⚠️ Edge Case 1 (Hết TTL):** KH bận, 15 phút sau mới click link -> Báo hết hạn -> Nhả lại tiền ứng trước cho CTV.
- **⚠️ Edge Case 2 (Sát giờ đóng kỳ):** KH bấm link lúc T-31s, API gọi sang BGT mất 2s (chạm vạch T-29s) -> Cảnh báo rủi ro trôi kỳ vé.
