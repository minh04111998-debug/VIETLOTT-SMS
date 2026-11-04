# SWEBOK v4 — Knowledge Area Mapping

> Reference file cho DEV role. Lazy load khi cần.
> Nguồn: [SWEBOK v4](https://www.computer.org/education/bodies-of-knowledge/software-engineering)

## 11 Applicable Knowledge Areas

| # | Knowledge Area | Agent Coverage | Files |
|---|---------------|----------------|-------|
| KA1 | Software Requirements | ✅ 80% | dev-rules.md §2, AC reading |
| KA2 | Software Design | ✅ 85% | SKILL.md §6, ADR template, scaffolding |
| KA3 | Software Construction | ✅ 90% | dev-rules.md §1-§3, code standards |
| KA4 | Software Testing | ✅ 80% | dev-rules.md §10, TDD cycle |
| KA5 | Software Maintenance | ✅ 85% | dev-rules.md §8, Strangler Fig, Boy Scout |
| KA6 | Software Config Mgmt | ✅ 85% | dev-rules.md §9, branching, commits |
| KA7 | SE Management | ⚠️ 70% | dev-rules.md §11, estimation |
| KA8 | SE Process | ⚠️ 65% | dev-workflow.md, CI/CD awareness |
| KA9 | SE Models & Methods | ⚠️ 70% | refactoring, DDD concepts |
| KA10 | Software Quality | ✅ 85% | Production-Ready Gate (8 gates) |
| KA11 | SE Professional Practice | ⚠️ 60% | Code review etiquette, escalation |

## Excluded KAs (Not applicable for AI agent context)
- KA12: SE Economics
- KA13: Computing Foundations
- KA14: Mathematical Foundations
- KA15: Engineering Foundations

## Cross-References
- Role: `.agents/personas/dev/persona.md`
- Rules: `.agents/rules/dev-rules.md` (§1-§11)
- Skills: `.agents/skills/dev/SKILL.md`
- Patterns: `.agents/skills/dev/references/dev-patterns.md`
- Performance: `.agents/skills/dev/references/performance-scalability.md`
- Migration: `.agents/skills/dev/references/migration-flags.md`
