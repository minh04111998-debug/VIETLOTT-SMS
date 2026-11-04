# Architecture Decision Record (ADR)

## ADR-001: Lựa chọn giải pháp thay thế Stitch để phục dựng và kiểm thử 100% giao diện Vietlott SMS

- **Status:** Draft (Đang chờ duyệt)
- **Role:** Solution Architect (SA)
- **Date:** 2026-06-22

| Version | Ngày | Người đề xuất | Mô tả thay đổi |
|:---:|:---:|:---:|---|
| 1.0 | 2026-06-22 | Solution Architect | Lựa chọn giải pháp thay thế Stitch để phục dựng UI |

---

## 1. Context (Bối cảnh)

1. Hệ thống sinh UI tự động (Stitch MCP) bị ngắt kết nối và không cho phép gọi API tự động trong phiên làm việc.
2. Công cụ text-to-UI như Stitch khó có thể đạt độ chính xác 100% (pixel-perfect) so với các ảnh chụp màn hình gốc của ứng dụng Vietlott SMS do những hạn chế của mô hình AI tạo hình ảnh/layout từ văn bản.
3. Dự án cần phục dựng 7 giao diện gốc bao gồm:
   - Screen 1: Mở App (Trang chủ chưa Đăng nhập) - `Login 1.jpg`
   - Screen 2: Form Đăng nhập - `Login 2.jpg`
   - Screen 3: Trang chủ (Đã đăng nhập) - `Trang chủ.jpg`
   - Screen 4: Kết quả xổ số - `Kết quả.jpg`
   - Screen 5: Lịch sử dự thưởng - `Lịch sử.jpg`
   - Screen 6: Tiện ích - `Tiện ích.jpg`
   - Screen 7: Cá nhân - `Cá nhân.jpg`
4. Cần một cơ chế trực quan giúp đối chiếu độ chính xác của giao diện được dựng (Code UI) so với ảnh chụp màn hình gốc (Original Image) để đảm bảo khớp 100%.

---

## 2. Proposed Solution (Giải pháp đề xuất)

Xây dựng một ứng dụng **Interactive Web Prototype (Single Page Application)** chạy trực tiếp trên trình duyệt bằng **HTML5, CSS3 (Vanilla CSS) và JavaScript**. 

### Các tính năng cốt lõi của Prototype:
1. **Thiết kế Mobile Simulator**: Dựng một khung giả lập điện thoại di động (iPhone/Android frame) đẹp mắt ở trung tâm để chứa giao diện chạy thử.
2. **Tích hợp đầy đủ 7 màn hình**: Cho phép chuyển đổi giữa các màn hình qua thanh Bottom Navigation (đúng thứ tự: Kết quả, Lịch sử, Trang chủ, Tiện ích, Cá nhân) và qua các luồng tương tác (ví dụ: click "Đăng nhập" ở màn hình mở app -> chuyển sang Form đăng nhập -> nhập mật khẩu -> chuyển sang Trang chủ đã đăng nhập).
3. **Cơ chế so sánh Đối chiếu 1:1 (Side-by-Side & Overlay)**:
   - **Side-by-Side Mode**: Hiển thị khung Code UI và khung Ảnh gốc của màn hình đó song song với nhau.
   - **Overlay Mode**: Đè mờ ảnh gốc lên trên giao diện Code UI với một thanh trượt thay đổi độ trong suốt (opacity slider). Điều này giúp phát hiện sai lệch vị trí (misalignment) của từng pixel, text, icon hay độ dãn cách (spacing).
4. **Rich Aesthetics & Premium Design**: Sử dụng CSS variables đồng bộ theo hệ thống màu đã khai báo trong [DESIGN.md](file:///f:/VIETLOTT-SMS/artifacts/technical/design/DESIGN.md), kết hợp Google Font `Roboto`, `Be Vietnam Pro` và biểu tượng `Material Icons`. Thêm các hiệu ứng hover, active, gradient và micro-animations phản hồi 200ms để đảm bảo trải nghiệm người dùng.

---

## 3. Five-Dimensional Analysis (Phân tích 5 chiều)

### 3.1 Scale (Khả năng mở rộng)
- **Đánh giá:** Tốt. Mã nguồn HTML/CSS/JS thuần dễ dàng chuyển đổi sang UI của các framework di động như Flutter (Sử dụng các component tương đương như Container, Row, Column, Stack) hoặc React Native. Dễ dàng triển khai lên Web tĩnh (GitHub Pages, Vercel) để chia sẻ cho Stakeholders.

### 3.2 Cost (Chi phí)
- **Đánh giá:** 0 USD. Sử dụng hoàn toàn tài nguyên mã nguồn mở, không cần mua tài khoản hay sử dụng các công cụ Cloud sinh UI tốn phí.

### 3.3 Team (Nhân sự)
- **Đánh giá:** Khả thi với 1 DEV phụ trách. Do DEV (AI) thực hiện toàn bộ việc code và cấu trúc, người dùng chỉ cần mở file HTML trên trình duyệt để nghiệm thu, không yêu cầu kiến thức kỹ thuật phức tạp hoặc cài đặt môi trường build.

### 3.4 Time (Thời gian)
- **Đánh giá:** Thời gian thực hiện: Hoàn thành toàn bộ prototype tương tác và tính năng so sánh đối chiếu trong 2 ngày làm việc.

### 3.5 Risk (Rủi ro)
- **Đánh giá:** Thấp. Chạy local hoàn toàn nên không lo ngại rủi ro về rò rỉ dữ liệu hoặc gián đoạn kết nối internet như Stitch.

---

## 4. Trade-offs (Sự đánh đổi)

- **Ưu điểm (Pros):**
  - Đạt độ chính xác 100% nhờ khả năng căn chỉnh CSS thủ công theo ảnh gốc.
  - Có sẵn công cụ so sánh trực quan (Overlay/Side-by-side) giúp QA và người dùng nghiệm thu dễ dàng.
  - Tương tác thật (nhập liệu, ẩn/hiện mật khẩu, chuyển màn hình).
  - Không phụ thuộc vào Stitch MCP server.
- **Nhược điểm (Cons):**
  - Code được tạo ra là HTML/CSS chứ không phải Flutter trực tiếp. Tuy nhiên, việc convert từ HTML/CSS sang Flutter UI thực hiện trong vòng 2 ngày làm việc vì cấu trúc layout (flexbox) tương đương với Row/Column của Flutter.

---

## 5. Decision (Quyết định)

Lựa chọn xây dựng **Interactive Web Prototype** tại `artifacts/technical/design/mockup/`. Sau khi được người dùng duyệt thiết kế nháp này, tài liệu ADR sẽ được chuyển sang `artifacts/decisions/`.

---

## 6. Consequences (Hệ quả & Đánh giá tác động)
- **Tác động tích cực:** Đạt độ chính xác giao diện cao nhờ khả năng căn chỉnh CSS trực quan, hỗ trợ chế độ Overlay và Side-by-side phục vụ nghiệm thu.
- **Tác động kỹ thuật:** Cần chuyển đổi các component CSS sang mã nguồn ứng dụng di động ở giai đoạn sản xuất.

---

## 7. Review & Verification (Kế Hoạch Đánh Giá Lại)
- Rà soát lại khi hoàn tất vòng phản hồi người dùng về bản prototype hoặc khi khởi động sprint phát triển ứng dụng di động chính thức.
