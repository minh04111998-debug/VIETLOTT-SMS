---
name: qa-automation
description: Kỹ năng automation test — Playwright setup, code generation, browser testing, API test automation
---

# Kỹ Năng: Test Automation

> **Nguồn gốc:** Tách từ QA monolith §5, §7-§8

---

## 1. Automation Strategy & Execution

> **Kích hoạt:** Cần setup hoặc mở rộng test automation.

**Test Automation Pyramid:**
```
         /  E2E  \        ← Ít nhất, chậm nhất, đắt nhất
        / Integration \
       /  Unit Tests   \   ← Nhiều nhất, nhanh nhất, rẻ nhất
```

**Framework Selection:** Playwright (browser) | Jest/Vitest (unit) | Postman/Newman (API) | k6/Artillery (performance)

## 2. Chạy Test Trực Tiếp Trên Browser

> **Kích hoạt:** Cần kiểm tra UI/UX trực tiếp, test responsive, visual regression.

**Quy trình:**
1. Mở browser dev tools → chạy scenario thủ công
2. Ghi lại steps + kết quả (screenshot/video)
3. Dùng browser recording tools nếu cần replay

## 3. Sinh Dữ Liệu Kiểm Thử (Test Data Generator)

> **Kích hoạt:** Cần tạo bulk test data tự động.

**Cách tiếp cận:**
- Script Python/JS sinh data theo schema
- Faker library cho realistic data
- Seed data cho database test environment

## 4. Playwright Automation (Chi tiết)

> **Kích hoạt:** `/playwright-test` hoặc cần setup Playwright từ đầu.

**Setup:** `npm init playwright@latest` → Chọn TypeScript → Config baseURL
**Page Object Model:** Mỗi page = 1 class, locators + actions tách biệt
**Best Practices:**
- Auto-wait (Playwright tự wait, không cần sleep)
- Trace on failure (`trace: 'on-first-retry'`)
- Parallel execution default
- Visual comparison: `expect(page).toHaveScreenshot()`
