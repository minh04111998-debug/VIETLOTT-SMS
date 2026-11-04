# Hướng Dẫn Kết Nối & Phân Tích Ứng Dụng Vietlott SMS Trên Điện Thoại Với Antigravity

> **Tài liệu thuộc dự án:** Vietlott SMS Multi-Role Framework  
> **Phiên bản:** v1.0.0 | **Ngày cập nhật:** 2026-08-08  
> **Ứng dụng mục tiêu:** Vietlott SMS (`vn.vietlott.vietlottsms1`) — Version 4.4.18 (Build 276)

---

## 1. Môi Trường & Kiến Trúc Kết Nối (4-Layer Integration Architecture)

Để AI Agent **Antigravity** có thể liên kết, điều khiển, và phân tích dữ liệu ứng dụng Vietlott SMS đang chạy trên điện thoại thực tế, hệ thống đã được xây dựng theo mô hình **4 Lớp Kết Nối Đa Tầng**:

```
+-----------------------------------------------------------------------------------+
|                            ANTIGRAVITY AI AGENT (PC)                              |
+-----------------------------------------------------------------------------------+
       |                        |                         |                         |
[1. ADB & UI Control]  [2. Network Traffic Proxy] [3. APK Static Bridge]   [4. Visual Vision Agent]
   - USB / Wireless ADB   - HTTP/HTTPS Intercept  - Androguard / Dex       - Screencap analysis
   - UI XML Tree Dump     - API Payload Log       - Flutter / Android      - Bounding box tap
   - Touch & Text Input   - Proxy Logger Server   - Deep link mapping      - Screenshot diff
       |                        |                         |                         |
+-----------------------------------------------------------------------------------+
|                        VIETLOTT SMS MOBILE APP (PHONE)                            |
|                          Package: vn.vietlott.vietlottsms1                        |
+-----------------------------------------------------------------------------------+
```

---

## 2. Kết Quả Phân Tích Cấu Trúc APK (APK Static Analysis Summary)

Qua việc giải mã file `app-release-4.4.18.276.apk` bằng script `scripts/apk_runtime_analyzer.py`, Antigravity đã xác định các thông số nền tảng của ứng dụng Vietlott SMS:

| Thông số | Chi tiết |
|---|---|
| **Package Name** | `vn.vietlott.vietlottsms1` |
| **Version** | 4.4.18 (Version Code: 276) |
| **Main Activity** | `vn.vietlott.vietlottsms.MainActivity` |
| **Framework Nền Tảng** | **Flutter** (`io.flutter.plugins...`, `flutter_inappwebview_android`) |
| **Tích hợp Native SDK** | VPBank eKYC (`com.vpbank.ekyc.android.EKycActivity`), Barcode Scanner (`com.journeyapps.barcodescanner.CaptureActivity`), Firebase Messaging |
| **Quyền Hạn (Permissions)** | 41 quyền (Bao gồm: `SEND_SMS`, `INTERNET`, `USE_BIOMETRIC`, `CAMERA`, `READ_CONTACTS`...) |

---

## 3. Hướng Dẫn Kích Hoạt Kết Nối Điện Thoại (Step-by-Step Phone Setup)

### 3.1. Chuẩn bị trên Điện thoại Android
1. Mở **Cài đặt (Settings)** -> **Thông tin điện thoại (About Phone)** -> Chạm 7 lần liên tục vào **Số hiệu bản dựng (Build Number)** để mở khóa *Tùy chọn nhà phát triển*.
2. Truy cập **Hệ thống (System)** -> **Tùy chọn nhà phát triển (Developer Options)**.
3. Bật **Sửa lỗi USB (USB Debugging)** và **Sửa lỗi không dây (Wireless Debugging)** (nếu muốn nối qua Wi-Fi).
4. Cắm cáp USB nối điện thoại với PC. Khi điện thoại hiển thị thông báo *"Cho phép sửa lỗi USB?"*, chọn **Luôn cho phép từ máy tính này (Always allow)** và nhấn **Đồng ý**.

### 3.2. Chạy Script Kiểm Tra Môi Trường Trên PC
Mở PowerShell tại máy tính và chạy script:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/setup_adb_environment.ps1
```

Script sẽ kiểm tra sự tồn tại của `adb.exe`, quét các thiết bị điện thoại đang kết nối, và hiển thị trạng thái ứng dụng `vn.vietlott.vietlottsms1`.

---

## 4. Các Lệnh Điều Khiển Của Antigravity (Bridge Commands)

Antigravity sử dụng module `scripts/vietlott_sms_bridge.py` để gửi lệnh trực tiếp tới điện thoại:

### 4.1. Kiểm tra trạng thái ứng dụng đang mở trên màn hình:
```bash
python scripts/vietlott_sms_bridge.py --check
```

### 4.2. Khởi chạy tự động ứng dụng Vietlott SMS:
```bash
python scripts/vietlott_sms_bridge.py --launch
```

### 4.3. Chụp ảnh màn hình điện thoại về PC:
```bash
python scripts/vietlott_sms_bridge.py --screenshot
```
*Ảnh sẽ được lưu tự động tại thư mục `scripts/screenshots/`.*

### 4.4. Trích xuất cây UI XML Hierarchy (UI Dump):
```bash
python scripts/vietlott_sms_bridge.py --dump-ui
```
*Trích xuất các node ID, text, bounds của tất cả thành phần giao diện trên màn hình app.*

### 4.5. Gửi thao tác chạm (Tap) và nhập liệu (Input):
```bash
# Chạm vào tọa độ X Y trên màn hình
python scripts/vietlott_sms_bridge.py --tap 540 1200

# Nhập văn bản vào ô tìm kiếm/nhập liệu
python scripts/vietlott_sms_bridge.py --input "Mega645"
```

---

## 5. Bắt Luồng Traffic Mạng & Payload API (Network Proxy Logger)

Để Antigravity ghi nhận các request/response API giữa Vietlott SMS và server backend:

1. Khởi chạy Proxy Logger trên máy tính:
   ```bash
   python scripts/vietlott_proxy_logger.py --port 8080
   ```
2. Trên điện thoại: Vào **Cài đặt Wi-Fi** -> Chọn Wi-Fi đang kết nối -> Chỉnh sửa -> **Proxy** chọn **Thủ công (Manual)**:
   - **Tên máy chủ Proxy (Host):** Đã hiển thị trên màn hình console script (VD: `192.168.1.15`)
   - **Cổng (Port):** `8080`
3. Mọi dữ liệu API phát sinh từ app sẽ được lưu tại file [vietlott_api_traffic.json](file:///f:/VIETLOTT-SMS/artifacts/requirements/vietlott_api_traffic.json).

---

## 6. Quy Tắc An Toàn & Bảo Mật (Safety & Risk Guidelines)

> [!WARNING]
> 1. **Tuyệt đối không tự động hóa mã PIN & OTP:** Antigravity sẽ không tự động nhập mật khẩu tài khoản ngân hàng, mã PIN ví điện tử hoặc OTP SMS mua vé thật mà không có xác nhận thủ công từ người dùng.
> 2. **Kiểm tra tọa độ trước khi Tap:** Luôn chụp ảnh màn hình (`--screenshot`) hoặc kiểm tra UI Dump (`--dump-ui`) trước khi gửi lệnh tap để tránh bấm nhầm nút xác nhận thanh toán.
> 3. **Bảo mật file Traffic Log:** File `vietlott_api_traffic.json` có thể chứa token phiên làm việc tạm thời, cần xóa bỏ thông tin nhạy cảm trước khi đưa vào tài liệu dùng chung.
