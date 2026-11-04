/**
 * @file api-users.spec.ts
 * @description API Test Suite — Users Endpoint
 * @ref TC-API-001 → TC-API-010
 *
 * Ví dụ API test dùng Playwright request context.
 * Không cần browser — chạy nhanh hơn E2E.
 * AI sẽ dùng file này làm mẫu khi sinh API automation test.
 *
 * Chạy:
 *   npx playwright test tests/api/api-users.spec.ts --project=api
 */

import { test, expect } from '@playwright/test';

// ============================================================
// Config
// ============================================================
const BASE_URL = process.env.API_URL || 'http://localhost:3000/api/v1';

// ============================================================
// Test Data
// ============================================================
const TEST_USER = {
  name: 'Nguyễn Văn Test',
  email: 'test@example.com',
  phone: '0912345678',
  password: 'Test@123',
};

const ADMIN_CREDENTIALS = {
  username: 'admin',
  password: 'Admin@123',
};

// ============================================================
// Helpers
// ============================================================
let authToken: string;
let createdUserId: number;

// ============================================================
// Test Suite: Users API
// ============================================================
test.describe('Users API', () => {

  // Setup: Lấy auth token trước tất cả tests
  test.beforeAll(async ({ request }) => {
    const res = await request.post(`${BASE_URL}/auth/login`, {
      data: ADMIN_CREDENTIALS,
    });
    expect(res.status()).toBe(200);

    const body = await res.json();
    authToken = body.data.token;
    expect(authToken).toBeTruthy();
  });

  // ----------------------------------------------------------
  // CREATE (POST)
  // ----------------------------------------------------------

  // TC-API-001: Tạo user mới — Happy Path
  test('TC-API-001: POST /users — should create user with valid data', async ({ request }) => {
    const res = await request.post(`${BASE_URL}/users`, {
      headers: { Authorization: `Bearer ${authToken}` },
      data: TEST_USER,
    });

    expect(res.status()).toBe(201);

    const body = await res.json();
    expect(body.data).toHaveProperty('id');
    expect(body.data.name).toBe(TEST_USER.name);
    expect(body.data.email).toBe(TEST_USER.email);

    // Lưu ID để dùng cho tests sau
    createdUserId = body.data.id;
  });

  // TC-API-002: Tạo user — Email không hợp lệ
  test('TC-API-002: POST /users — should reject invalid email', async ({ request }) => {
    const res = await request.post(`${BASE_URL}/users`, {
      headers: { Authorization: `Bearer ${authToken}` },
      data: { ...TEST_USER, email: 'invalid-email' },
    });

    expect(res.status()).toBe(422);

    const body = await res.json();
    expect(body.error).toBeDefined();
    expect(body.error.code).toBe('VALIDATION_ERROR');
  });

  // TC-API-003: Tạo user — Email đã tồn tại
  test('TC-API-003: POST /users — should reject duplicate email', async ({ request }) => {
    const res = await request.post(`${BASE_URL}/users`, {
      headers: { Authorization: `Bearer ${authToken}` },
      data: TEST_USER, // same email as TC-API-001
    });

    expect(res.status()).toBe(409);
  });

  // TC-API-004: Tạo user — Thiếu required fields
  test('TC-API-004: POST /users — should reject missing required fields', async ({ request }) => {
    const res = await request.post(`${BASE_URL}/users`, {
      headers: { Authorization: `Bearer ${authToken}` },
      data: { name: 'Only Name' }, // thiếu email, password
    });

    expect(res.status()).toBe(422);
  });

  // ----------------------------------------------------------
  // READ (GET)
  // ----------------------------------------------------------

  // TC-API-005: Lấy danh sách users
  test('TC-API-005: GET /users — should return user list', async ({ request }) => {
    const res = await request.get(`${BASE_URL}/users`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });

    expect(res.status()).toBe(200);

    const body = await res.json();
    expect(body.data).toBeInstanceOf(Array);
    expect(body.data.length).toBeGreaterThan(0);

    // Verify pagination metadata
    expect(body.meta).toBeDefined();
    expect(body.meta).toHaveProperty('total');
    expect(body.meta).toHaveProperty('page');
  });

  // TC-API-006: Lấy user theo ID
  test('TC-API-006: GET /users/:id — should return single user', async ({ request }) => {
    const res = await request.get(`${BASE_URL}/users/${createdUserId}`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });

    expect(res.status()).toBe(200);

    const body = await res.json();
    expect(body.data.id).toBe(createdUserId);
    expect(body.data.name).toBe(TEST_USER.name);

    // Verify: password KHÔNG được trả về
    expect(body.data).not.toHaveProperty('password');
    expect(body.data).not.toHaveProperty('passwordHash');
  });

  // TC-API-007: Lấy user không tồn tại
  test('TC-API-007: GET /users/999999 — should return 404', async ({ request }) => {
    const res = await request.get(`${BASE_URL}/users/999999`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });

    expect(res.status()).toBe(404);
  });

  // ----------------------------------------------------------
  // AUTHORIZATION
  // ----------------------------------------------------------

  // TC-API-008: Truy cập không có token
  test('TC-API-008: GET /users — should return 401 without token', async ({ request }) => {
    const res = await request.get(`${BASE_URL}/users`);
    // Không gửi Authorization header

    expect(res.status()).toBe(401);
  });

  // TC-API-009: Truy cập với token hết hạn / sai
  test('TC-API-009: GET /users — should return 401 with invalid token', async ({ request }) => {
    const res = await request.get(`${BASE_URL}/users`, {
      headers: { Authorization: 'Bearer invalid-token-12345' },
    });

    expect(res.status()).toBe(401);
  });

  // ----------------------------------------------------------
  // SECURITY
  // ----------------------------------------------------------

  // TC-API-010: SQL Injection qua query param
  test('TC-API-010: GET /users?search — should reject SQL injection', async ({ request }) => {
    const res = await request.get(
      `${BASE_URL}/users?search=' OR '1'='1`,
      {
        headers: { Authorization: `Bearer ${authToken}` },
      }
    );

    // Phải trả về kết quả bình thường (rỗng) hoặc 400 — KHÔNG trả về tất cả users
    if (res.status() === 200) {
      const body = await res.json();
      // Nếu 200, data phải rỗng (không leak data)
      expect(body.data.length).toBe(0);
    } else {
      expect(res.status()).toBe(400);
    }
  });

  // ----------------------------------------------------------
  // CLEANUP
  // ----------------------------------------------------------

  // TC-API-011: Xóa user (cleanup)
  test('TC-API-011: DELETE /users/:id — should delete created user', async ({ request }) => {
    const res = await request.delete(`${BASE_URL}/users/${createdUserId}`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });

    expect(res.status()).toBe(200);

    // Verify: user đã bị xóa
    const verifyRes = await request.get(`${BASE_URL}/users/${createdUserId}`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });
    expect(verifyRes.status()).toBe(404);
  });
});

// ============================================================
// API Contract Tests
// ============================================================
test.describe('API Contract Validation', () => {

  test.beforeAll(async ({ request }) => {
    const res = await request.post(`${BASE_URL}/auth/login`, {
      data: ADMIN_CREDENTIALS,
    });
    authToken = (await res.json()).data.token;
  });

  // TC-API-012: Response format nhất quán
  test('TC-API-012: API responses should follow standard format', async ({ request }) => {
    // Success response
    const successRes = await request.get(`${BASE_URL}/users`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });
    const successBody = await successRes.json();
    expect(successBody).toHaveProperty('data');

    // Error response
    const errorRes = await request.get(`${BASE_URL}/users/999999`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });
    if (errorRes.status() === 404) {
      const errorBody = await errorRes.json();
      expect(errorBody).toHaveProperty('error');
    }
  });

  // TC-API-013: Response time < 500ms
  test('TC-API-013: API response time should be under 500ms', async ({ request }) => {
    const start = Date.now();
    await request.get(`${BASE_URL}/users`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });
    const duration = Date.now() - start;

    expect(duration).toBeLessThan(500);
  });

  // TC-API-014: Error messages không leak sensitive data
  test('TC-API-014: Error messages should not expose internal details', async ({ request }) => {
    const res = await request.get(`${BASE_URL}/users/invalid-id`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });

    const body = await res.json();
    const responseText = JSON.stringify(body);

    // Không chứa stack trace
    expect(responseText).not.toContain('node_modules');
    expect(responseText).not.toContain('at Object');
    expect(responseText).not.toContain('Error:');

    // Không chứa SQL
    expect(responseText).not.toContain('SELECT');
    expect(responseText).not.toContain('FROM');
  });
});
