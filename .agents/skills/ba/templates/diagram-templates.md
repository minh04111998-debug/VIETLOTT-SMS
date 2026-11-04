# Mẫu Diagram Mermaid (BA)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — Sections 3, 7, 16, 17, 18, 21

---

## 1. Activity Diagram (Section 3)

```mermaid
flowchart TD
    Start([Bắt đầu]) --> A[Người dùng nhập thông tin]
    A --> B{Dữ liệu hợp lệ?}
    B -->|Có| C[Xử lý yêu cầu]
    B -->|Không| D[Hiển thị lỗi]
    D --> A
    C --> E{Thành công?}
    E -->|Có| F[Hiển thị kết quả]
    E -->|Không| G[Ghi log lỗi]
    G --> H[Thông báo người dùng]
    F --> End([Kết thúc])
    H --> End
```

---

## 2. Use Case Diagram (Section 2)

```mermaid
graph LR
    Actor1((Người dùng)) --> UC1[Đăng nhập]
    Actor1 --> UC2[Xem danh sách]
    Actor1 --> UC3[Tạo mới]
    Actor2((Quản trị viên)) --> UC4[Quản lý người dùng]
    Actor2 --> UC5[Xem báo cáo]
    UC1 -.-> UC6[Quên mật khẩu]
```

---

## 3. Flowchart — Quy Tắc Vẽ (Section 7)

**Quy tắc:**
- Prefer dùng `flowchart TD` (Từ trên xuống)
- Sử dụng hình thoi `{}` cho các điểm quyết định (Decision points / If-Else). Ví dụ: `A{Email hợp lệ?} -->|Có| B`
- Bắt buộc phải có text (label) trên các mũi tên rẽ nhánh
- Sử dụng hình viên thuốc `([ ])` cho điểm Bắt đầu và Kết thúc
- Trả về đoạn code Mermaid sạch, kèm theo 2-3 gạch đầu dòng giải thích tóm tắt luồng bên dưới

---

## 4. Decision Table & Decision Tree (Section 16)

### Decision Table Template
```markdown
## Business Rule: [Tên quy tắc]

| # | Điều kiện A | Điều kiện B | Điều kiện C | → Hành động |
|---|------------|------------|------------|------------|
| 1 | Có | Có | Có | Hành động X |
| 2 | Có | Có | Không | Hành động Y |
| 3 | Có | Không | * | Hành động Z |
| 4 | Không | * | * | Từ chối |

* = Không quan trọng (don't care)
```

### Decision Tree (Mermaid)
```mermaid
graph TD
    A{Khách hàng VIP?} -->|Có| B{Đơn hàng > 10M?}
    A -->|Không| C{Đơn hàng > 5M?}
    B -->|Có| D[Giảm 15% + Free ship]
    B -->|Không| E[Giảm 10%]
    C -->|Có| F[Giảm 5%]
    C -->|Không| G[Không giảm]
```

**Khi nào dùng:**
- **Decision Table:** Nhiều điều kiện kết hợp, tất cả conditions đều quan trọng ngang nhau
- **Decision Tree:** Logic có tính phân cấp, điều kiện trước quyết định điều kiện sau

**Self-check sau khi vẽ:**
- Tất cả combinations đã cover chưa? (2^n cho n conditions)
- Có rule nào mâu thuẫn không? (cùng input → khác output)
- Có case "else" / default chưa?

---

## 5. State Diagram (Section 17)

### Template Mermaid
```mermaid
stateDiagram-v2
    [*] --> Draft : Tạo mới
    Draft --> Submitted : User submit
    Draft --> Cancelled : User hủy
    Submitted --> InReview : Reviewer pick up
    InReview --> Approved : Reviewer duyệt
    InReview --> Rejected : Reviewer từ chối
    Rejected --> Draft : User sửa & resubmit
    Approved --> InProgress : Dev bắt đầu
    InProgress --> Done : Dev hoàn thành
    InProgress --> Blocked : Gặp blocker
    Blocked --> InProgress : Blocker resolved
    Done --> [*]
    Cancelled --> [*]
```

### State Matrix (Output kèm theo)
```markdown
## State Matrix: [Tên đối tượng]

| State | Mô tả | Ai có quyền? | Transition đến | Trigger |
|-------|--------|-------------|---------------|---------|
| Draft | Bản nháp | Creator | Submitted, Cancelled | Submit / Cancel button |
| Submitted | Chờ review | System | InReview | Auto-assign reviewer |
```

**Self-check:**
- Có dead-end state nào không mong muốn không?
- Từ mọi state (trừ terminal), có path đến end state không?
- Concurrent states có cần không? (parallel region)

---

## 6. BPMN Process Modeling — Swimlane (Section 18)

```mermaid
flowchart TD
    subgraph Customer["👤 Khách hàng"]
        A([Bắt đầu]) --> B[Gửi đơn hàng]
    end
    subgraph Sales["👔 Bộ phận bán hàng"]
        B --> C{Kiểm tra tồn kho}
        C -->|Đủ| D[Xác nhận đơn]
        C -->|Hết| E[Thông báo hết hàng]
    end
    subgraph Warehouse["📦 Kho"]
        D --> F[Đóng gói]
        F --> G[Xuất kho]
    end
    subgraph Shipping["🚚 Vận chuyển"]
        G --> H[Giao hàng]
        H --> I([Kết thúc])
    end
    E --> A
```

**Quy tắc:**
- Mỗi subgraph = 1 department/role (swimlane)
- Flow phải chạy từ trái sang phải hoặc trên xuống dưới
- Mọi decision point phải có label trên mũi tên
- Ghi rõ exception flows (timeout, error, escalation)

---

## 7. Context Diagram (Section 21)

```mermaid
flowchart LR
    User((👤 End User)) -->|Nhập đơn hàng| System[🖥️ Hệ thống XYZ]
    Admin((👤 Admin)) -->|Quản lý cấu hình| System
    System -->|Gửi email| Email[📧 Email Service]
    System -->|Thanh toán| Payment[💳 Payment Gateway]
    System -->|Tra cứu| CRM[📊 CRM System]
    Cron((⏰ Scheduler)) -->|Trigger batch job| System
```

---

## 8. Sequence Diagram (BABOK Technique #42)

> Sử dụng khi cần mô tả tương tác giữa các thành phần theo thứ tự thời gian.

```mermaid
sequenceDiagram
    actor User as 👤 User
    participant FE as 🖥️ Frontend
    participant API as ⚙️ API Gateway
    participant Service as 📦 Service
    participant DB as 🗄️ Database
    participant External as 🌐 External API

    User->>FE: 1. Thao tác
    FE->>API: 2. HTTP Request
    API->>Service: 3. Internal call
    Service->>DB: 4. Query data
    DB-->>Service: 5. Result
    Service->>External: 6. Call external API
    External-->>Service: 7. Response
    Service-->>API: 8. Business result
    API-->>FE: 9. HTTP Response
    FE-->>User: 10. Hiển thị kết quả

    Note over Service,External: Timeout: 5s<br/>Retry: 2 lần
    Note over DB: Transaction scope
```

**Quy tắc:**
- Mỗi message có **số thứ tự** rõ ràng
- Ghi chú **timeout**, **retry**, **transaction scope** khi có external call
- Luồng `-->>` (dashed) cho response, `->>`(solid) cho request

---

## 9. Functional Decomposition Diagram (BABOK Technique #22)

> Sử dụng khi cần phân rã hệ thống lớn thành sub-functions.

```mermaid
graph TD
    A["🖥️ Hệ Thống"] --> B["📦 Module A"]
    A --> C["📦 Module B"]
    A --> D["📦 Module C"]

    B --> B1["Feature A.1"]
    B --> B2["Feature A.2"]
    B --> B3["Feature A.3"]

    C --> C1["Feature B.1"]
    C --> C2["Feature B.2"]

    D --> D1["Feature C.1"]
    D --> D2["Feature C.2"]
    D --> D3["Feature C.3"]

    style A fill:#1a73e8,color:white
    style B fill:#34a853,color:white
    style C fill:#fbbc04,color:black
    style D fill:#ea4335,color:white
```

**Quy tắc:**
- Tối đa **3-4 cấp** (sâu hơn → quá chi tiết)
- Mỗi **leaf node** = 1 potential User Story hoặc Use Case
- Dùng **màu** để phân biệt modules

