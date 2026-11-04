# Production-Grade Code Scaffolding Patterns (DEV)

> Tham chiếu từ: `.agents/skills/dev/SKILL.md` — Section 7: Scaffolding

---

## 1. Module Structure Template (Scaffold-01)

Khi tạo module mới, PHẢI tạo đủ các thành phần:

```
/modules/[tên-module]/
├── controller/          # Nhận request, validate input, gọi service
├── service/             # Business logic THUẦN — không biết HTTP/DB
├── repository/          # Data access — chỉ nói chuyện với DB
├── dto/                 # Data Transfer Objects — input/output shapes
├── entity/              # Database entity/model
├── __tests__/           # Tests cho module này
├── [module].module.*    # Module registration (nếu dùng DI framework)
└── [module].constants.* # Constants, enums cho module
```

**Quy tắc Dependency Direction:**
```
Controller → Service → Repository → Database
     ↓            ↓           ↓
  (validate)  (business)   (data access)
     ↓            ↓           ↓
  Biết HTTP   Không biết   Không biết
              HTTP/Framework  business logic
```

---

## 2. Service Layer Template (Scaffold-02)

```
// Service là NƠI DUY NHẤT chứa business logic
class OrderService {
  // Dependencies inject qua constructor — KHÔNG new trong service
  constructor(orderRepo, paymentGateway, logger) { ... }

  async createOrder(input) {
    // 1. Validate business rules (không phải input format — đó là controller)
    this.validateBusinessRules(input)

    // 2. Execute business logic
    const order = this.buildOrder(input)

    // 3. Persist
    const saved = await this.orderRepo.save(order)

    // 4. Side effects (event, notification, logging)
    this.logger.info('Order created', { orderId: saved.id })

    // 5. Return plain object (không trả entity/model)
    return this.toResponse(saved)
  }
}

Nguyên tắc:
□ Service KHÔNG import framework-specific modules
□ Service KHÔNG gọi req/res — chỉ nhận/trả plain objects
□ Service throw custom errors (OrderNotFoundError, InsufficientBalanceError)
□ Controller bắt error và chuyển thành HTTP response
□ Test service bằng cách mock repository — không cần HTTP server
```

---

## 3. Error Handling Architecture (Scaffold-03)

```
Thiết kế error handling TRƯỚC khi code, không phải sau.

LAYER 1 — Custom Business Errors:
  AppError(code, message, httpStatus, details)
  Ví dụ:
    - OrderNotFoundError    → 404
    - InsufficientBalanceError → 422
    - UnauthorizedError     → 401

LAYER 2 — Service throws business errors:
  if (!order) throw new AppError('ORDER_NOT_FOUND', '...', 404)
  if (balance < amount) throw new AppError('INSUFFICIENT_BALANCE', '...', 422)

LAYER 3 — Global Error Handler (1 NƠI DUY NHẤT):
  if (err instanceof AppError) {
    // Business error → trả về client với code + message
    return response(err.httpStatus, { error: { code, message } })
  }
  // Unexpected error → log chi tiết, trả generic cho client
  logger.error('Unexpected', { error, requestId })
  return response(500, { error: { code: 'INTERNAL_ERROR' } })

Nguyên tắc:
□ KHÔNG try-catch ở mỗi function — chỉ catch khi CÓ THỂ xử lý
□ Để error bubble up đến Global Handler
□ Business error ≠ System error — phân biệt rõ
□ Client KHÔNG BAO GIỜ thấy stack trace
□ Error có correlation ID để trace
```
