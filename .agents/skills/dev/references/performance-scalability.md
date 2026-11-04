# Performance & Scalability Patterns (DEV)

> Tham chiếu từ: `.agents/skills/dev/SKILL.md` — Section 8: Performance & Scalability

---

## 1. Database Performance Checklist (Perf-01)

| # | Kiểm tra | Tại sao |
|---|---------|---------| 
| 1 | Query có dùng index? (EXPLAIN) | Không index = full table scan = chậm khi data lớn |
| 2 | Có N+1 query? | 100 orders → 100 query lấy user = 101 queries. Dùng JOIN/eager load |
| 3 | SELECT đúng field cần? | SELECT * lấy 50 columns khi chỉ cần 3 → lãng phí |
| 4 | Pagination cursor-based? | OFFSET lớn = chậm (OFFSET 10000 skip 10000 rows) |
| 5 | Batch insert cho write-heavy? | 1000 INSERT riêng lẻ vs 1 batch → 10-100x nhanh hơn |
| 6 | Connection pool configured? | Mỗi request tạo connection mới = chậm + exhaust connections |
| 7 | Transaction scope nhỏ nhất? | Transaction dài = lock rows lâu = deadlock risk |

---

## 2. API Performance Checklist (Perf-02)

| # | Kiểm tra | Target |
|---|---------|--------|
| 1 | Response time P95 | < 500ms read, < 1s write |
| 2 | Payload size | < 100KB ideal, < 1MB max |
| 3 | Compression (gzip/brotli) | Giảm 60-80% payload |
| 4 | Pagination bắt buộc cho list | Default page size ≤ 50 |
| 5 | Rate limiting | Protect khỏi abuse |
| 6 | Async cho heavy operations | Email, PDF, report → queue |
| 7 | Cache headers cho semi-static data | Cache-Control, ETag |

---

## 3. Caching Strategy Decision Matrix (Perf-03)

| Data | Cache ở đâu | TTL | Invalidation |
|------|------------|-----|-------------|
| User session | Redis/Memory | 15-60 min | On update |
| Config/Settings | App memory | 5-15 min | On deploy |
| DB query results | Redis | 1-5 min | On write |
| API response | CDN | 1-24h | Purge on change |
| Static assets | Browser + CDN | 1 year | Filename hash |

```
Nguyên tắc:
□ App phải chạy đúng KHI KHÔNG CÓ cache — cache là optimization
□ Prefer TTL-based invalidation (đơn giản, ít bug)
□ Đo trước, cache sau — không cache nếu chưa chứng minh bottleneck
```

---

## 4. Scalability Red Flags — AI PHẢI Cảnh Báo (Perf-04)

```
🚩 Code KHÔNG SCALE — Cảnh báo ngay nếu phát hiện:

1. Global mutable state (biến global thay đổi được)
   → Nhiều instance = state không đồng bộ

2. File lưu trên local disk (upload, temp files)
   → Nhiều instance = file chỉ có trên 1 server

3. In-memory session
   → Request đến server khác = mất session

4. Synchronous heavy processing trong request handler
   → 1 request chậm = block thread = chậm tất cả

5. Hardcoded single database connection
   → Không connection pooling, không read replica

6. Không có idempotency cho write operations
   → Retry = duplicate data

7. Tight coupling giữa modules
   → Không thể tách service khi cần scale riêng
```

> **Nguồn tham chiếu:**
> - [12-Factor App](https://12factor.net/)
> - [Martin Fowler — Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/)
> - [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
> - [System Design Primer](https://github.com/donnemartin/system-design-primer)
