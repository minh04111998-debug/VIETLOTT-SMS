# Developer Patterns & Best Practices Reference

> **Nguồn:** Clean Code, Pragmatic Programmer, OWASP, Google Eng Practices
> **Mục đích:** Tài liệu tham chiếu chi tiết cho DEV. Lazy-load khi workflow hoặc SKILL.md gọi.

---

## Clean Code Patterns

### Error Handling — Expert Level
```
❌ Catching tất cả exceptions im lặng:
   try { ... } catch (e) { console.log(e) }

✅ Error handling có ý nghĩa:
   - Happy path và error path cùng được thiết kế
   - Error message có đủ context để debug (không leak sensitive data)
   - Distinguish: expected errors (validation) vs unexpected (system failure)
   - Retry chỉ khi idempotent — không retry payment mutation
   - Circuit breaker cho external dependencies
```

### API Design
```
RESTful:
- Resource names: noun, plural: /users, /orders
- HTTP verb đúng nghĩa: GET, POST, PUT, PATCH, DELETE
- Status code: 200, 201, 400, 401, 403, 404, 422, 500
- Pagination cho list endpoints
- Versioning: /api/v1/

Response format thống nhất:
{
  "data": {...} | [...],
  "error": null | {"code": "VALIDATION_ERROR", "message": "...", "details": [...]},
  "meta": {"page": 1, "total": 100}
}
```

### Database Interaction
```
- Không raw query — dùng ORM/query builder
- Transaction cho multi-step operations (đặc biệt financial)
- Index trước khi query production large dataset
- Không SELECT *
- Soft delete cho data quan trọng
- Migration có rollback plan
```

### Project Structure
```
Tổ chức theo FEATURE/DOMAIN:
✅ /modules/order/ (controller, service, repo, test cùng nhau)
❌ /controllers/ + /services/ + /repositories/ (tách theo layer)

Dependency direction: 1 chiều
Controller → Service → Repository → Database

Service Layer Pattern (bắt buộc):
□ Service = NƠI DUY NHẤT chứa business logic
□ Service KHÔNG biết HTTP (không access req/res)
□ Controller chỉ validate input + gọi Service + trả response
□ Repository chỉ data access
```

---

## Logging & Observability

### Structured Logging
```json
{
  "timestamp": "ISO-8601",
  "level": "ERROR|WARN|INFO|DEBUG",
  "service": "order-service",
  "correlationId": "uuid",
  "action": "createOrder",
  "message": "Payment gateway timeout",
  "duration_ms": 30000,
  "metadata": { "orderId": "...", "userId": "..." }
}
```

### PHẢI LOG:
```
□ Request vào/ra (method, path, status, duration)
□ Business events (đặt hàng, thanh toán, phê duyệt)
□ Error + stack trace + context
□ External API call (URL, status, duration)
□ Auth events (login success/fail)
```

### KHÔNG ĐƯỢC LOG:
```
□ Password, token, secret key
□ PII (CMND, số thẻ) — mask nếu bắt buộc
□ Debug level trên production
```

### Health Check
```
□ Endpoint /health → 200 nếu healthy
□ Check: DB connection, cache, disk space
□ Correlation ID xuyên suốt call chain (X-Correlation-Id header)
```

---

## Configuration & Environment
```
KHÔNG HARDCODE — externalize mọi giá trị thay đổi theo environment.

□ DB connection → env var
□ API keys, secrets → secret manager (KHÔNG commit git)
□ Timeout values → config file
□ Feature flags → config hoặc feature flag service
□ .env KHÔNG commit → .gitignore
□ .env.example với giá trị mẫu
□ Validate required env vars khi app start → fail fast
```

---

## Testing Strategy

### Test Pyramid
```
        /  E2E Tests (ít, chậm, fragile)         \
       /   Integration Tests (medium)              \
      /    Unit Tests (nhiều, nhanh, isolated)      \
```

### Test Priority — Theo Risk
```
🔴 LUÔN TEST:
   - Business logic core (tính toán, validation, rules)
   - Authentication & authorization
   - Payment & financial transactions
   - Data transformation (import/export, ETL)

🟡 TEST KHI CÓ TIME:
   - Utility functions, API adapters, complex UI

🟢 SKIP OK:
   - Pure getters/setters, framework boilerplate, DTOs
```

### Test Quality
```
Mỗi test phải có:
□ Tên mô tả behavior: "should_return_error_when_email_exists"
□ Arrange-Act-Assert structure
□ Test 1 behavior per test case
□ Independent — không phụ thuộc thứ tự
□ Fast — unit test < 100ms/test
```

---

## Dependency Management
```
TRƯỚC KHI THÊM DEPENDENCY MỚI:
□ Maintained? (commit gần nhất < 6 tháng)
□ Known CVE? (npm audit / snyk)
□ License compatible? (GPL ≠ commercial friendly)
□ Tự viết được trong < 50 dòng? → tự viết
□ Bundle size impact?

BẮT BUỘC:
□ Lock file committed
□ Pin version cụ thể cho production
□ Security audit trước mỗi release
□ Update dependencies ≥ 1 lần/tháng
```
