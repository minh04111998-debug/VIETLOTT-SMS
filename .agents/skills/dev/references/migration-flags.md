# Database Migration & Feature Flags (DEV)

> Tham chiếu từ: `.agents/skills/dev/SKILL.md` — Sections 9, 10

---

## 1. Database Migration Checklist (Section 9)

> **Trigger:** Khi cần thay đổi database schema (thêm/sửa/xóa bảng/cột)
> **Nguyên tắc:** Every schema change = migration file. Không bao giờ ALTER trực tiếp production.

### Migration Safety Checklist
```
PRE-MIGRATION:
□ Migration file tạo bằng CLI tool (typeorm, prisma, knex), KHÔNG viết tay
□ File có cả UP (apply) và DOWN (rollback)
□ Test migration trên staging với data volume tương tự production
□ Backup database trước khi chạy production migration
□ Estimate thời gian chạy (large table ALTER có thể mất hàng giờ)
□ Schedule maintenance window nếu migration > 5 phút

DURING MIGRATION:
□ Chạy migration 1 file tại 1 thời điểm
□ Monitor DB performance (connections, locks, CPU)
□ Sẵn sàng rollback command

POST-MIGRATION:
□ Verify data integrity (row counts, key constraints)
□ Application functions correctly with new schema
□ Update TypeORM/Prisma entities to match new schema
□ Commit migration file to git
□ Document breaking changes (nếu có)
```

### Dangerous Operations — Cần Special Care
```
🔴 DROP TABLE / DROP COLUMN → Không thể undo! Backup trước.
🔴 RENAME COLUMN → Application code phải update TRƯỚC hoặc CÙNG LÚC
🟡 ADD NOT NULL column → Phải có DEFAULT value, hoặc backfill first
🟡 ADD UNIQUE constraint → Verify không có duplicates trước
🟡 Change column type → Data conversion có thể fail
🟢 ADD NULLABLE column → Safe, no downtime
🟢 ADD INDEX → Safe nhưng slow trên large table (consider CONCURRENTLY)
```

---

## 2. Feature Flag Strategy (Section 10)

> **Trigger:** Deploy feature chưa hoàn thiện, A/B testing, hoặc gradual rollout
> **Nguyên tắc:** Deploy ≠ Release. Feature flags decouple deployment from release.

### Feature Flag Types
```
1. RELEASE FLAG — Toggle new feature on/off
   - Lifecycle: Short (remove after feature stable, < 2 sprints)
   - Example: ENABLE_NEW_CHECKOUT_FLOW

2. EXPERIMENT FLAG — A/B testing
   - Lifecycle: Medium (duration of experiment)
   - Example: EXPERIMENT_PRICING_PAGE_V2
   - Needs: User segmentation, analytics tracking

3. OPS FLAG — Operational control
   - Lifecycle: Long-term (permanent or until deprecated)
   - Example: ENABLE_MAINTENANCE_MODE, RATE_LIMIT_AGGRESSIVE

4. PERMISSION FLAG — Feature access control
   - Lifecycle: Long-term
   - Example: ENABLE_ADMIN_ANALYTICS
```

### Implementation Pattern
```typescript
// ❌ BAD — scattered if/else
if (featureFlags.newCheckout) {
  // 200 lines of new code
} else {
  // 200 lines of old code
}

// ✅ GOOD — strategy pattern
const checkoutStrategy = featureFlags.newCheckout
  ? new NewCheckoutFlow()
  : new LegacyCheckoutFlow();
await checkoutStrategy.execute(cart);
```

### Feature Flag Hygiene
```
□ Flag có tên descriptive (ENABLE_X, EXPERIMENT_Y)
□ Flag có owner + expiry date
□ Remove flag code khi feature stable (debt cleanup)
□ Dashboard: list tất cả active flags + status
□ KHÔNG nest flags (if flag1 && flag2 → too complex)
□ Flag defaults: OFF for new features, ON for kill switches
```
