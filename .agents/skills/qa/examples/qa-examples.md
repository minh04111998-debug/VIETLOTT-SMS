# Ví Dụ QA: Test Cases + Bug Report

## Ví dụ Test Case: Đăng nhập

### TC-AUTH-001: Đăng nhập thành công với thông tin hợp lệ

| Thuộc tính | Giá trị |
|-----------|---------|
| **TC ID** | TC-AUTH-001 |
| **Module** | Authentication |
| **Độ ưu tiên** | Cao |
| **Yêu cầu liên quan** | UC-01 / US-001 |
| **Điều kiện tiên quyết** | Có tài khoản test_user / Test@123 đã được tạo |

### Các Bước Thực Hiện
| Bước | Hành động | Dữ liệu test | Kết quả mong đợi | Kết quả thực tế | Pass/Fail |
|------|-----------|---------------|-------------------|------------------|-----------|
| 1 | Mở trang đăng nhập | URL: /login | Hiển thị form đăng nhập | | |
| 2 | Nhập username | test_user | Ô username hiển thị "test_user" | | |
| 3 | Nhập password | Test@123 | Ô password hiển thị dấu *** | | |
| 4 | Click "Đăng nhập" | — | Chuyển sang Dashboard, hiển thị "Xin chào, Test User" | | |

---

### TC-AUTH-005: Đăng nhập với SQL Injection

| Thuộc tính | Giá trị |
|-----------|---------|
| **TC ID** | TC-AUTH-005 |
| **Module** | Authentication — Security |
| **Độ ưu tiên** | Cao |
| **Yêu cầu liên quan** | NFR-SEC-001 |

### Các Bước Thực Hiện
| Bước | Hành động | Dữ liệu test | Kết quả mong đợi | Kết quả thực tế | Pass/Fail |
|------|-----------|---------------|-------------------|------------------|-----------|
| 1 | Nhập username | `' OR '1'='1` | Ô username chấp nhận input | | |
| 2 | Nhập password | `' OR '1'='1` | Ô password chấp nhận input | | |
| 3 | Click "Đăng nhập" | — | Hiển thị lỗi "Sai thông tin đăng nhập". KHÔNG được đăng nhập thành công | | |

---

## Ví dụ Bug Report

### 🐛 [BUG] Hệ thống cho phép đăng nhập bằng SQL Injection

- **Mức độ (Severity):** 🔴 Critical
- **Các bước tái hiện (Steps to Reproduce):**
  1. Mở trang /login
  2. Nhập username: `' OR '1'='1`
  3. Nhập password: `' OR '1'='1`
  4. Click "Đăng nhập"
- **Kết quả thực tế trong Code (Actual):**
  - Đăng nhập thành công, hiển thị Dashboard với quyền admin
  - Nguyên nhân: File `auth.controller.js` dòng 45 dùng string concatenation thay vị parameterized query:
    ```javascript
    // ❌ Sai
    const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
    ```
- **Kết quả mong đợi (Expected):** Hiển thị lỗi "Sai thông tin đăng nhập", không cho truy cập
- **Gợi ý nguyên nhân (Root Cause Guess):** Thiếu parameterized query. Sửa:
  ```javascript
  // ✅ Đúng
  const query = `SELECT * FROM users WHERE username = ? AND password = ?`;
  db.query(query, [username, hashedPassword]);
  ```
- **Bằng chứng:** Screenshot đính kèm

---

## Ví dụ Test Data: Trường "Số điện thoại"

| Loại | Giá trị | Kết quả mong đợi |
|------|---------|-------------------|
| ✅ Valid | 0912345678 | Chấp nhận |
| ✅ Valid | 0398765432 | Chấp nhận |
| ❌ Invalid format | 091234567 | Từ chối (9 số) |
| ❌ Invalid format | 09123456789 | Từ chối (11 số) |
| ❌ Invalid chars | 091abc5678 | Từ chối (chứa chữ) |
| 📏 Boundary | 0000000000 | Từ chối (không hợp lệ) |
| 🔐 Security | `<script>alert(1)</script>` | Từ chối + sanitize |
| 🔲 Empty | _(để trống)_ | Hiển thị "Số điện thoại là bắt buộc" |
| 🔲 Null | _(chỉ khoảng trắng)_ | Hiển thị "Số điện thoại là bắt buộc" |
