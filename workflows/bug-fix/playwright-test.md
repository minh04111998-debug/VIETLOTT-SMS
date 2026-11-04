---
description: Quy trình Playwright Testing — Setup, sinh code, chạy test, báo cáo. Gọi `/playwright-test` hoặc `/qa automation`.
---

# 🔴 Workflow: Playwright Testing

> **Slash command**: `/playwright-test` hoặc `/qa automation`
> **Vai trò**: `[🔴 ROLE: QA]`
> **Đầu vào**: Test Cases (markdown) + Link Dev (optional)
> **Đầu ra**: Automation test code + Test results + Bug Reports (nếu fail)
> **Ref:** [Playwright Docs](https://playwright.dev/docs/intro) | SKILL.md §5.3-5.5

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🔴 ROLE: QA]`
- **Nạp Rules:** `.agents/rules/qa-rules.md`
- **Nạp Skills:** `.agents/skills/qa/SKILL.md` §5 (Automation Testing)
- **Examples:** `.agents/skills/qa/examples/` (login.spec.ts, login.page.ts, api-users.spec.ts)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG, chờ user quyết định

---

## BƯỚC 1: Setup Playwright Project

### 1.1 Kiểm tra môi trường

AI chạy lần lượt:
```bash
# Check Node.js
node --version

# Check nếu Playwright đã cài
npx playwright --version
```

### 1.2 Quyết định setup

| Tình huống | Hành động |
|-----------|---------|
| ✅ Node.js + Playwright có sẵn | Bỏ qua setup → Bước 2 |
| ⚠️ Node.js có, Playwright chưa | Chạy script init → `.agents/skills/qa/scripts/playwright-init.ps1` |
| ❌ Node.js chưa có | 🛑 DỪNG — Yêu cầu user cài Node.js |

### 1.3 Chạy init script (nếu cần)

```powershell
# AI chạy script init
powershell -ExecutionPolicy Bypass -File .agents/skills/qa/scripts/playwright-init.ps1
```

Script sẽ:
1. Tạo `package.json` (nếu chưa có)
2. Cài `@playwright/test`
3. Cài browser Chromium
4. Tạo cấu trúc thư mục `tests/pages/`, `tests/fixtures/`
5. Copy config mẫu → `playwright.config.ts`
6. Verify: `npx playwright test --list`

🛑 **[DỪNG]** — *"Playwright đã setup xong. Tiếp tục sinh test code?"*

---

## BƯỚC 2: Sinh Automation Test Code

### 2.1 Xác định nguồn Test Cases

AI hỏi người dùng (nếu chưa rõ):
```
1. Test cases nằm ở file nào? (VD: artifacts/testing/test-cases-auth.md)
2. Modules nào cần automation? (VD: Auth, Order, Payment)
3. Loại test: E2E (UI) hay API hay cả hai?
4. Base URL của hệ thống? (VD: http://localhost:3000)
```

### 2.2 Sinh code theo pattern

**Với mỗi module, AI tạo 2 file:**

| File | Pattern | Ref |
|------|---------|-----|
| `tests/pages/[module].page.ts` | Page Object Model | [login.page.ts example](../../skills/qa/examples/login.page.ts) |
| `tests/[module]/[feature].spec.ts` | Test Suite | [login.spec.ts example](../../.agents/skills/qa-automation/SKILL.md) |

**Với API tests:**

| File | Pattern | Ref |
|------|---------|-----|
| `tests/api/[resource].api.spec.ts` | API Test Suite | [api-users.spec.ts example](../../skills/qa/examples/api-users.spec.ts) |

### 2.3 Quy tắc sinh code BẮT BUỘC

1. **Mỗi test case markdown → 1 test block** trong `.spec.ts`
2. **Test name = TC ID + mô tả tiếng Anh**: `'TC-AUTH-001: should login with valid credentials'`
3. **Dùng `data-testid` selectors** — KHÔNG dùng XPath hoặc CSS class
4. **Mỗi test block phải có `await expect()`** — KHÔNG có test "rỗng"
5. **Group tests bằng `test.describe()`** — theo module/feature
6. **Tách logic UI → POM** — test file KHÔNG chứa selectors trực tiếp
7. **Test data tách ra `fixtures/`** — nếu > 3 bộ data
8. **Comment TC ID** trước mỗi test block để traceability

### 2.4 Output

```
tests/
├── pages/
│   ├── login.page.ts        ← AI sinh
│   └── order.page.ts        ← AI sinh
├── auth/
│   └── login.spec.ts        ← AI sinh
├── order/
│   └── create-order.spec.ts ← AI sinh
├── api/
│   └── users.api.spec.ts    ← AI sinh
├── fixtures/
│   └── test-data.ts         ← AI sinh (nếu cần)
└── playwright.config.ts     ← Đã có từ Bước 1
```

🛑 **[DỪNG]** — *"Đã sinh [N] file test. Review code trước khi chạy?"*

---

## BƯỚC 3: Chạy Tests

### 3.1 Chạy automation

AI chạy bằng `run_command`:

```bash
# Chạy toàn bộ
npx playwright test

# Hoặc chạy theo module cụ thể
npx playwright test tests/auth/

# Hoặc theo TC ID pattern
npx playwright test --grep "TC-AUTH"

# Chỉ API tests
npx playwright test --project=api
```

### 3.2 Xử lý kết quả

| Output | Hành động |
|--------|---------|
| ✅ All passed | → Bước 4 (Report) |
| ❌ Có test fail | → Bước 4 (Report + Bug Reports) |
| 💥 Setup error | → Quay lại Bước 1, fix config |
| ⏱️ Timeout | → Tăng timeout trong config hoặc check hệ thống |

### 3.3 Retry failed tests (optional)

```bash
# Chạy lại chỉ các tests đã fail
npx playwright test --last-failed

# Chạy với retries
npx playwright test --retries=2
```

🛑 **[DỪNG]** — *"Tests chạy xong. Xem báo cáo chi tiết?"*

---

## BƯỚC 4: Parse Kết Quả & Báo Cáo

### 4.1 Tạo Test Summary

AI đọc output từ Bước 3 và tạo báo cáo:

```markdown
## 🧪 Playwright Test Results — [YYYY-MM-DD]

### Environment
- **URL**: [Base URL]
- **Browser**: Chromium [version]
- **OS**: Windows
- **Node**: [version]

### Summary
| Metric | Value |
|--------|-------|
| Total Tests | [N] |
| ✅ Passed | [N] ([%]) |
| ❌ Failed | [N] ([%]) |
| ⏭️ Skipped | [N] ([%]) |
| ⏱️ Duration | [N]s |

### ❌ Failed Tests
| # | Test | File:Line | Error | Severity |
|---|------|-----------|-------|----------|
| 1 | TC-AUTH-005: SQL injection | login.spec.ts:45 | Expected 401, got 200 | Critical |
| 2 | TC-ORDER-003: Timeout | order.spec.ts:78 | Timeout 30s | High |

### 📸 Screenshots (Failures)
- Lưu tại: `test-results/` (auto-captured on failure)

### Traceability
| TC ID | Test File | Status |
|-------|-----------|--------|
| TC-AUTH-001 | login.spec.ts | ✅ |
| TC-AUTH-002 | login.spec.ts | ✅ |
| TC-AUTH-005 | login.spec.ts | ❌ → BUG-AUTH-XXX |
```

### 4.2 Auto Bug Reports

**Với mỗi test FAIL**, AI tự động gọi kỹ năng **Tạo Bug Report** (SKILL.md §6):
- **Phát hiện bởi:** Automation Test (Playwright)
- **Bằng chứng:** Screenshot + video từ `test-results/`
- **Test Case liên quan:** TC ID từ test name

### 4.3 Lưu trữ

- Report: `artifacts/testing/automation-results/playwright-[YYYY-MM-DD].md`
- Bug Reports: `artifacts/testing/bug-automation-[date].md`

🛑 **[DỪNG]** — *"Báo cáo đã tạo. [N] bugs mới. Chuyển cho Dev sửa?"*

---

## BƯỚC 5: CI/CD Integration (Optional)

> **Bỏ qua** nếu user không cần. Chỉ chạy khi user yêu cầu.

### 5.1 Hỏi user

```
1. CI/CD platform: GitHub Actions / GitLab CI / Azure DevOps?
2. Trigger: push to main? pull request? manual?
3. Environment: Staging URL? Secrets cần set?
```

### 5.2 Sinh config file

AI tạo config dựa trên platform:
- **GitHub Actions**: `.github/workflows/e2e-tests.yml` (ref: SKILL.md §5.5)
- **GitLab CI**: `.gitlab-ci.yml`
- **Azure DevOps**: `azure-pipelines.yml`

### 5.3 Verify

```bash
# Dry-run check syntax
# GitHub: dùng act (optional)
# GitLab: gitlab-ci-local (optional)
```

🛑 **🎉 PLAYWRIGHT FLOW HOÀN TẤT.**

---

## Tổng Hợp

| Bước | Slash shortcut | Output |
|------|----------------|--------|
| 1. Setup | `/playwright-test setup` | Playwright project ready |
| 2. Generate | `/playwright-test generate` | .spec.ts + .page.ts files |
| 3. Run | `/playwright-test run` | Test execution output |
| 4. Report | `/playwright-test report` | Summary + Bug Reports |
| 5. CI/CD | `/playwright-test ci` | CI config file |

## Hướng Dẫn

| Lệnh | Hành vi |
|-------|---------|
| `/playwright-test` | Full flow 5 bước |
| `/playwright-test setup` | Bước 1 only |
| `/playwright-test generate` | Bước 2 only |
| `/playwright-test run` | Bước 3 + 4 (chạy + report) |
| `/qa automation` | Alias → `/playwright-test` |
| Điều khiển | `NEXT` / `SKIP` / `STOP` / `BACK` |

## Giới Hạn

- ❌ Không xử lý OTP, Captcha, 2FA (cần mock/bypass)
- ❌ Không chạy đa browser cùng lúc (mặc định Chromium only)
- ❌ Performance test → Dùng K6/JMeter, không phải Playwright
- ✅ Phù hợp: Functional E2E, API Testing, Regression, Smoke Test
