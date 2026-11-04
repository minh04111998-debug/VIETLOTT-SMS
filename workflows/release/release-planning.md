---
description: Quy trình lập kế hoạch release và launch - Vai trò PO
---

# Workflow: Release Planning

> **Slash command**: `/release-planning`
> **Vai trò**: `[🔵 ROLE: PO]`
> **Khi nào dùng**: Chuẩn bị release feature/product, launch planning
> **Đầu ra**: Release Plan tại `artifacts/technical/releases/`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[🔵 ROLE: PO]`
- **Nạp Rules:** `po-rules.md` (§8: Release Strategy)
- **Nạp Skills:** `.agents/skills/po/SKILL.md` (POA-D5: Deliver Often)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

---

## Bước 1: Release Scope

AI hỏi:
```
1. Feature/stories nào nằm trong release này?
2. Target release date?
3. Release type: Big Bang / Incremental / Feature Toggle / Canary?
4. Target audience: All users / Segment / Beta?
5. Có breaking changes không? (API changes, UI overhaul, data migration)
6. Dependencies: Hệ thống khác cần coordinate?
```

🛑 **[DỪNG]** — Confirm scope

---

## Bước 2: Pre-Launch Checklist

AI tạo Release Plan với checklist (POA-D5.4):

```markdown
## Release Plan — [Feature/Version]

### Pre-Launch
- [ ] All stories Done (DoD met)
- [ ] UAT signed off
- [ ] Rollback plan documented
- [ ] Monitoring configured
- [ ] Docs updated
- [ ] Stakeholders notified
- [ ] Support team briefed
- [ ] Telemetry verified
```

🛑 **[DỪNG]** — Verify checklist items

---

## Bước 3: Metrics & MCS

```markdown
### Success Criteria
| Metric | Baseline | MCS (Minimum) | Stretch Target |
|--------|----------|---------------|----------------|

### Monitoring Plan (Week 1)
| Metric | Alert Threshold | Dashboard | Owner |
|--------|----------------|-----------|-------|
```

---

## Bước 4: Communication & Rollout

```markdown
### Release Communication
| Audience | Channel | Message | Timing | Owner |
|----------|---------|---------|--------|-------|
| Internal team | Slack | Release notes | D-1 | PM |
| Stakeholders | Email | Feature summary | D-0 | PO |
| End users | In-app | What's new | D+0 | Product |

### Rollout Plan
| Phase | Audience % | Duration | Proceed Criteria |
|-------|-----------|----------|-----------------|
```

---

## Bước 5: Post-Launch Review Template

```markdown
### Post-Launch Review (schedule at D+7 and D+30)

**D+7 Quick Check:**
- Error rate vs baseline: [OK / Elevated]
- Feature adoption: [X%]
- Critical bugs found: [N]
- Action needed: [Yes / No → details]

**D+30 Full Review:**
- MCS met: [Yes / No]
- User feedback themes: [List]
- Decision: Keep / Enhance / Pivot / Kill
- Lessons learned: [Key takeaways]
```

- Lưu tại `artifacts/technical/releases/release-[version]-[date].md`
