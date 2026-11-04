/**
 * @file login.page.ts
 * @description Page Object Model — Login Page
 *
 * Ví dụ POM cho QA Agent.
 * Tách toàn bộ UI selectors và actions ra khỏi test file.
 * AI sẽ dùng pattern này khi sinh POM cho các trang khác.
 *
 * Quy tắc POM:
 * 1. Dùng `data-testid` selectors — KHÔNG dùng XPath/CSS class
 * 2. Mỗi page/component = 1 file POM
 * 3. Chỉ chứa: selectors + actions + helpers
 * 4. KHÔNG chứa assertions (assertions thuộc về test file)
 * 5. Tên file: [tên-page].page.ts
 */

import { type Page, type Locator, expect } from '@playwright/test';

export class LoginPage {
  // ============================================================
  // Selectors — Khai báo tất cả UI elements
  // ============================================================
  readonly page: Page;
  readonly usernameInput: Locator;
  readonly passwordInput: Locator;
  readonly submitButton: Locator;
  readonly errorMessage: Locator;
  readonly rememberMeCheckbox: Locator;
  readonly forgotPasswordLink: Locator;
  readonly registerLink: Locator;
  readonly loadingSpinner: Locator;

  constructor(page: Page) {
    this.page = page;
    this.usernameInput = page.locator('[data-testid="username"]');
    this.passwordInput = page.locator('[data-testid="password"]');
    this.submitButton = page.locator('[data-testid="login-btn"]');
    this.errorMessage = page.locator('[data-testid="error-msg"]');
    this.rememberMeCheckbox = page.locator('[data-testid="remember-me"]');
    this.forgotPasswordLink = page.locator('[data-testid="forgot-password-link"]');
    this.registerLink = page.locator('[data-testid="register-link"]');
    this.loadingSpinner = page.locator('[data-testid="loading-spinner"]');
  }

  // ============================================================
  // Navigation
  // ============================================================

  /**
   * Mở trang đăng nhập
   */
  async goto() {
    await this.page.goto('/login');
    await this.page.waitForLoadState('networkidle');
  }

  // ============================================================
  // Actions — Các hành động người dùng
  // ============================================================

  /**
   * Đăng nhập với username và password
   * @param username - Tên đăng nhập
   * @param password - Mật khẩu
   */
  async login(username: string, password: string) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.submitButton.click();

    // Chờ navigation hoặc error message xuất hiện
    await Promise.race([
      this.page.waitForURL(/.*dashboard/, { timeout: 10_000 }).catch(() => {}),
      this.errorMessage.waitFor({ state: 'visible', timeout: 10_000 }).catch(() => {}),
    ]);
  }

  /**
   * Đăng nhập với option "Ghi nhớ đăng nhập"
   */
  async loginWithRememberMe(username: string, password: string) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.rememberMeCheckbox.check();
    await this.submitButton.click();
  }

  /**
   * Xóa toàn bộ fields
   */
  async clearFields() {
    await this.usernameInput.clear();
    await this.passwordInput.clear();
  }

  // ============================================================
  // Helpers — Tiện ích
  // ============================================================

  /**
   * Kiểm tra trang login đã load xong chưa
   */
  async isReady(): Promise<boolean> {
    try {
      await this.usernameInput.waitFor({ state: 'visible', timeout: 5_000 });
      await this.submitButton.waitFor({ state: 'visible', timeout: 5_000 });
      return true;
    } catch {
      return false;
    }
  }

  /**
   * Lấy text error message (nếu có)
   */
  async getErrorText(): Promise<string | null> {
    try {
      await this.errorMessage.waitFor({ state: 'visible', timeout: 3_000 });
      return await this.errorMessage.textContent();
    } catch {
      return null;
    }
  }

  /**
   * Kiểm tra loading spinner có đang hiển thị
   */
  async isLoading(): Promise<boolean> {
    return await this.loadingSpinner.isVisible();
  }
}
