/**
 * @file login.spec.ts
 * @description E2E Test Suite — Authentication Module
 * @ref TC-AUTH-001 → TC-AUTH-007
 *
 * Ví dụ Playwright test thực tế cho QA Agent.
 * AI sẽ dùng file này làm mẫu khi sinh automation test code.
 *
 * Hướng dẫn:
 * - Chạy: npx playwright test tests/auth/login.spec.ts
 * - Debug: npx playwright test tests/auth/login.spec.ts --debug
 * - Report: npx playwright test tests/auth/login.spec.ts --reporter=html
 */

import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/login.page';

// ============================================================
// Test Data — Tách riêng để dễ maintain
// ============================================================
const VALID_USER = {
  username: 'test_user',
  password: 'Test@123',
  displayName: 'Test User',
};

const ADMIN_USER = {
  username: 'test_admin',
  password: 'Admin@123',
  displayName: 'Admin User',
};

// ============================================================
// Test Suite: Authentication
// ============================================================
test.describe('Authentication — Login', () => {
  let loginPage: LoginPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    await loginPage.goto();
  });

  // ----------------------------------------------------------
  // POSITIVE TESTS (Happy Path)
  // ----------------------------------------------------------

  // TC-AUTH-001: Đăng nhập thành công với user thường
  test('TC-AUTH-001: should login with valid user credentials', async ({ page }) => {
    await loginPage.login(VALID_USER.username, VALID_USER.password);

    // Verify: chuyển sang Dashboard
    await expect(page).toHaveURL(/.*dashboard/);

    // Verify: hiển thị tên user
    await expect(page.locator('[data-testid="welcome-msg"]'))
      .toContainText(`Xin chào, ${VALID_USER.displayName}`);
  });

  // TC-AUTH-002: Đăng nhập thành công với admin
  test('TC-AUTH-002: should login with admin credentials', async ({ page }) => {
    await loginPage.login(ADMIN_USER.username, ADMIN_USER.password);

    await expect(page).toHaveURL(/.*dashboard/);
    await expect(page.locator('[data-testid="user-role"]'))
      .toContainText('Admin');
  });

  // ----------------------------------------------------------
  // NEGATIVE TESTS
  // ----------------------------------------------------------

  // TC-AUTH-003: Đăng nhập với mật khẩu sai
  test('TC-AUTH-003: should show error with wrong password', async ({ page }) => {
    await loginPage.login(VALID_USER.username, 'WrongPassword123');

    // Verify: vẫn ở trang login
    await expect(page).toHaveURL(/.*login/);

    // Verify: hiển thị error message
    await expect(loginPage.errorMessage).toBeVisible();
    await expect(loginPage.errorMessage)
      .toContainText('Sai thông tin đăng nhập');
  });

  // TC-AUTH-004: Đăng nhập với username không tồn tại
  test('TC-AUTH-004: should show error with non-existent username', async ({ page }) => {
    await loginPage.login('nonexistent_user', 'SomePassword');

    await expect(page).toHaveURL(/.*login/);
    await expect(loginPage.errorMessage).toBeVisible();
  });

  // TC-AUTH-005: Đăng nhập với fields rỗng
  test('TC-AUTH-005: should show validation error when fields are empty', async ({ page }) => {
    // Click submit mà không điền gì
    await loginPage.submitButton.click();

    // Verify: validation messages hiển thị
    await expect(page.locator('[data-testid="username-error"]'))
      .toBeVisible();
    await expect(page.locator('[data-testid="password-error"]'))
      .toBeVisible();
  });

  // ----------------------------------------------------------
  // SECURITY TESTS
  // ----------------------------------------------------------

  // TC-AUTH-006: SQL Injection
  test('TC-AUTH-006: should reject SQL injection attempt', async ({ page }) => {
    await loginPage.login("' OR '1'='1", "' OR '1'='1");

    // Verify: KHÔNG được đăng nhập thành công
    await expect(page).not.toHaveURL(/.*dashboard/);
    await expect(loginPage.errorMessage).toBeVisible();
  });

  // TC-AUTH-007: XSS Injection
  test('TC-AUTH-007: should sanitize XSS in username field', async ({ page }) => {
    await loginPage.login('<script>alert("xss")</script>', 'password');

    // Verify: không có alert, error hiển thị bình thường
    await expect(page).not.toHaveURL(/.*dashboard/);
    await expect(loginPage.errorMessage).toBeVisible();

    // Verify: input đã được sanitize (không render HTML)
    const usernameValue = await loginPage.usernameInput.inputValue();
    expect(usernameValue).not.toContain('<script>');
  });

  // ----------------------------------------------------------
  // EDGE CASE TESTS
  // ----------------------------------------------------------

  // TC-AUTH-008: Đăng nhập với password có ký tự đặc biệt
  test('TC-AUTH-008: should handle special characters in password', async ({ page }) => {
    // Giả sử user có password chứa ký tự đặc biệt
    await loginPage.login('special_user', 'P@$$w0rd!#%&');

    // Test chỉ verify không crash — kết quả tùy thuộc user có tồn tại
    await expect(page.locator('body')).toBeVisible();
  });
});

// ============================================================
// Test Suite: Logout
// ============================================================
test.describe('Authentication — Logout', () => {
  let loginPage: LoginPage;

  // Login trước mỗi test
  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login(VALID_USER.username, VALID_USER.password);
    await expect(page).toHaveURL(/.*dashboard/);
  });

  // TC-AUTH-009: Logout thành công
  test('TC-AUTH-009: should logout and redirect to login', async ({ page }) => {
    await page.locator('[data-testid="logout-btn"]').click();

    // Verify: chuyển về trang login
    await expect(page).toHaveURL(/.*login/);
  });

  // TC-AUTH-010: Sau khi logout, không thể truy cập dashboard bằng back button
  test('TC-AUTH-010: should not access dashboard after logout via back button', async ({ page }) => {
    await page.locator('[data-testid="logout-btn"]').click();
    await expect(page).toHaveURL(/.*login/);

    // Try go back
    await page.goBack();

    // Verify: vẫn ở login hoặc redirect về login
    await expect(page).toHaveURL(/.*login/);
  });
});
