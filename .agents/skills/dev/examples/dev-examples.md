# Ví Dụ DEV: Code Review + API Design

## Ví Dụ Code Review Feedback

### 🔴 PHẢI SỬA - auth.controller.js:45
**Vấn đề**: SQL Injection vulnerability — sử dụng string concatenation cho query
**Lý do**: Vi phạm OWASP Top 10 A03:Injection. Kẻ tấn công có thể bypass authentication hoặc trích xuất toàn bộ database
**Đề xuất**:
```javascript
// ❌ Hiện tại (Dòng 45)
const query = `SELECT * FROM users WHERE email = '${email}'`;

// ✅ Đề xuất sửa
const query = `SELECT * FROM users WHERE email = ?`;
const [rows] = await db.execute(query, [email]);
```

### 🟡 NÊN SỬA - user.service.js:120
**Vấn đề**: God function — hàm `processUser()` dài 85 dòng, xử lý cả validate + transform + save + notify
**Lý do**: Vi phạm Single Responsibility Principle. Khó test, khó maintain
**Đề xuất**: Tách thành 4 hàm riêng:
```javascript
async function processUser(userData) {
    const validated = validateUserData(userData);     // 1. Validate
    const transformed = transformUserData(validated); // 2. Transform
    const saved = await saveUser(transformed);        // 3. Save
    await notifyUserCreated(saved);                   // 4. Notify
    return saved;
}
```

### 🟢 GỢI Ý - order.model.js:10
**Vấn đề**: Magic number `30` không rõ ý nghĩa
**Lý do**: Người đọc không biết 30 là gì — 30 ngày? 30 items? 30%?
**Đề xuất**:
```javascript
// ❌ Hiện tại
if (daysSinceCreated > 30) { ... }

// ✅ Đề xuất
const ORDER_EXPIRY_DAYS = 30;
if (daysSinceCreated > ORDER_EXPIRY_DAYS) { ... }
```

---

## Ví Dụ API Design

### POST /api/v1/auth/login

**Request:**
```json
{
    "email": "user@example.com",
    "password": "SecurePass123!"
}
```

**Response (200 OK):**
```json
{
    "success": true,
    "data": {
        "accessToken": "eyJhbGciOiJIUzI1NiIs...",
        "refreshToken": "dGhpcyBpcyBhIHJlZnJl...",
        "expiresIn": 3600,
        "user": {
            "id": 1,
            "email": "user@example.com",
            "fullName": "Nguyễn Văn A",
            "role": "agent"
        }
    },
    "message": "Đăng nhập thành công"
}
```

**Response (401 Unauthorized):**
```json
{
    "success": false,
    "error": {
        "code": "INVALID_CREDENTIALS",
        "message": "Email hoặc mật khẩu không đúng"
    }
}
```

**Response (429 Too Many Requests):**
```json
{
    "success": false,
    "error": {
        "code": "ACCOUNT_LOCKED",
        "message": "Tài khoản bị khóa do nhập sai mật khẩu 5 lần. Vui lòng thử lại sau 30 phút.",
        "retryAfter": 1800
    }
}
```
