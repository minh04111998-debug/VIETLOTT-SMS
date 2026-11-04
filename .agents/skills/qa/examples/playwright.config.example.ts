/**
 * @file playwright.config.example.ts
 * @description Config mẫu Playwright cho dự án
 *
 * AI sẽ copy file này → playwright.config.ts tại root project
 * và điều chỉnh baseURL, testDir theo dự án thực tế.
 *
 * Ref: https://playwright.dev/docs/test-configuration
 *
 * Sử dụng:
 *   1. Copy file này → root project, đổi tên thành playwright.config.ts
 *   2. Sửa baseURL theo môi trường dev/staging
 *   3. Chạy: npx playwright test
 */

import { defineConfig, devices } from '@playwright/test';

/**
 * Đọc biến môi trường từ .env (nếu có)
 * Ref: https://github.com/motdotla/dotenv
 */
// import dotenv from 'dotenv';
// dotenv.config({ path: '.env.test' });

export default defineConfig({
  // ============================================================
  // Thư mục chứa test files
  // ============================================================
  testDir: './tests',

  // ============================================================
  // Parallel & Timeout
  // ============================================================

  /** Chạy tests song song giữa các files */
  fullyParallel: true,

  /** Timeout cho mỗi test (ms) */
  timeout: 30_000,

  /** Timeout cho mỗi expect/assertion (ms) */
  expect: {
    timeout: 5_000,
  },

  /**
   * Fail CI nếu có test.only() trong code
   * Tránh commit test chạy isolated lên main
   */
  forbidOnly: !!process.env.CI,

  /**
   * Retry failed tests
   * - CI: retry 2 lần (flaky test protection)
   * - Local: không retry (debug nhanh hơn)
   */
  retries: process.env.CI ? 2 : 0,

  /**
   * Số workers chạy song song
   * - CI: 1 worker (ổn định hơn)
   * - Local: auto-detect (nhanh hơn)
   */
  workers: process.env.CI ? 1 : undefined,

  // ============================================================
  // Reporters — Định dạng output
  // ============================================================
  reporter: [
    /** Console output — hiển thị realtime */
    ['list'],

    /** HTML Report — mở bằng browser */
    ['html', {
      open: 'never', // 'always' | 'never' | 'on-failure'
      outputFolder: 'playwright-report',
    }],

    /** JUnit XML — cho CI/CD integration */
    ['junit', {
      outputFile: 'test-results/junit.xml',
    }],
  ],

  // ============================================================
  // Shared Settings — Áp dụng cho tất cả projects
  // ============================================================
  use: {
    /**
     * Base URL cho navigation
     * Dùng: await page.goto('/login') thay vì full URL
     */
    baseURL: process.env.BASE_URL || 'http://localhost:3000',

    /**
     * Chụp screenshot
     * - 'only-on-failure': chỉ khi test fail (tiết kiệm storage)
     * - 'on': luôn chụp
     * - 'off': không chụp
     */
    screenshot: 'only-on-failure',

    /**
     * Quay video
     * - 'retain-on-failure': giữ video chỉ khi fail
     * - 'on': luôn quay
     * - 'off': không quay
     */
    video: 'retain-on-failure',

    /**
     * Trace viewer — debug tool mạnh nhất
     * - 'on-first-retry': thu trace khi retry lần đầu
     * - 'on': luôn thu
     * - 'off': không thu
     * Xem trace: npx playwright show-trace trace.zip
     */
    trace: 'on-first-retry',

    /** Extra HTTP headers (nếu cần) */
    // extraHTTPHeaders: {
    //   'X-Custom-Header': 'value',
    // },

    /** Locale & Timezone (Vietnam) */
    locale: 'vi-VN',
    timezoneId: 'Asia/Ho_Chi_Minh',
  },

  // ============================================================
  // Projects — Cấu hình cho từng loại test
  // ============================================================
  projects: [
    // ----------------------------------------------------------
    // E2E Tests — Chạy trên browser Chromium
    // ----------------------------------------------------------
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
        // Viewport mặc định
        viewport: { width: 1280, height: 720 },
      },
      // Chỉ chạy file .spec.ts (không phải .api.spec.ts)
      testIgnore: /\.api\.spec\.ts/,
    },

    // ----------------------------------------------------------
    // Mobile Tests (Optional) — Uncomment nếu cần
    // ----------------------------------------------------------
    // {
    //   name: 'mobile-chrome',
    //   use: {
    //     ...devices['Pixel 5'],
    //   },
    //   testIgnore: /\.api\.spec\.ts/,
    // },

    // ----------------------------------------------------------
    // API Tests — Không cần browser
    // ----------------------------------------------------------
    {
      name: 'api',
      use: {
        // API tests không cần browser, chỉ cần request context
        baseURL: process.env.API_URL || 'http://localhost:3000/api/v1',
      },
      // Chỉ chạy file .api.spec.ts
      testMatch: /\.api\.spec\.ts/,
    },
  ],

  // ============================================================
  // Web Server — Tự động start server trước khi test
  // ============================================================
  // Uncomment nếu cần tự động chạy dev server
  // webServer: {
  //   command: 'npm run dev',
  //   url: 'http://localhost:3000',
  //   reuseExistingServer: !process.env.CI,
  //   timeout: 120_000,
  // },
});
