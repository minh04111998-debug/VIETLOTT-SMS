---
description: Lập kế hoạch refactoring code - Vai trò DEV
---

# Workflow: Refactoring Plan

> **Slash command**: `/refactoring-plan`
> **Vai trò**: `[💻 ROLE: DEV]`
> **Khi nào dùng**: Khi cần cải thiện code quality, reduce tech debt, prepare for scaling
> **Đầu ra**: Refactoring Plan + Risk Assessment + Test Coverage Check

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[💻 ROLE: DEV]`
- **Nạp Rules:** `.agents/rules/dev-rules.md` (đặc biệt §3 Code Standards)
  - Cross-ref: §8 (Software Maintenance — Tech Debt Quadrant)
- **Nạp Skills:** `.agents/skills/dev/SKILL.md` (Skill 4: Refactoring, Skill 8: Performance, Skill 11: Tech Debt Tracker)
- **Dừng cứng:** 🛑 = BẮT BUỘC DỪNG

> [!CAUTION]
> Rule #1 of refactoring: "Make it work, make it right, make it fast" — in that order.
> NEVER refactor without tests. Write tests FIRST if missing.

---

## Bước 1: Identify Refactoring Targets

Hỏi người dùng:
```
1. Code/module nào cần refactor?
2. Lý do refactor? (Performance / Readability / Tech debt / New feature prep)
3. Hiện tại có test coverage không? Bao nhiêu %?
4. Có feature mới nào phụ thuộc vào code này?
5. Timeline / Sprint capacity cho refactoring?
```

Hoặc AI tự scan code tìm:
- Functions > 30 dòng
- Classes > 300 dòng  
- Cyclomatic complexity > 10
- Duplicate code
- Anti-patterns (Skill 1: Anti-patterns list)

🛑 **[DỪNG]** — *"Tìm thấy [N] refactoring targets. Review?"*

---

## Bước 2: Risk Assessment

Cho mỗi refactoring target:
- **Blast radius:** Modules/functions nào depend on this code?
- **Test coverage:** Có đủ tests để verify sau refactor?
- **Breaking change risk:** API contracts có thay đổi?
- **Rollback plan:** Nếu refactor fail, revert như thế nào?

🛑 **[DỪNG]** — *"Risk assessment OK? Proceed?"*

---

## Bước 3: Refactoring Plan

AI tạo plan từng bước:
- Liệt kê refactoring techniques (Skill 4)
- Chia nhỏ thành commits (1 refactoring = 1 commit)
- Test plan: tests nào chạy sau mỗi step

```markdown
## Refactoring Plan — [Module/File]

| Step | What | Technique | Risk | Tests to Run |
|------|------|-----------|------|-------------|
| 1 | Write missing tests first | N/A | None | New tests pass |
| 2 | Extract method X from Y | Extract Method | Low | All unit tests |
| 3 | Rename class A to B | Rename | Low | All tests |
| 4 | Remove duplicate code | Extract + DRY | Medium | Unit + Integration |
| 5 | Verify performance | Benchmark | Low | Performance tests |
```

🛑 **[DỪNG]** — *"Refactoring plan OK? Start execution?"*

---

## Bước 4: Execute + Verify

AI thực hiện refactoring theo plan:
- Từng step, commit sau mỗi bước
- Chạy tests sau mỗi step
- Nếu test fail → revert step, investigate

🛑 **[DỪNG]** — *"Refactoring complete. All tests passing."*
