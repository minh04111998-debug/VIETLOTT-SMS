# ISTQB® CTFL v4.0 — Syllabus Mapping

> Reference file cho QA role. Lazy load khi cần.
> Nguồn: [ISTQB CTFL v4.0](https://www.istqb.org/certifications/certified-tester-foundation-level)

## 7 Testing Principles

| # | Principle | Tóm Tắt | Agent Coverage |
|---|-----------|---------|----------------|
| 1 | Testing shows presence of defects | Chứng minh có bug, KHÔNG chứng minh không có | qa.md Mindset #6 |
| 2 | Exhaustive testing is impossible | Ưu tiên bằng risk + kỹ thuật | qa.md Mindset #7 |
| 3 | Early testing saves time & money | Shift-left: review req trước code | qa-rules.md §2 |
| 4 | Defect clustering | 80% bugs ở 20% modules | qa.md Mindset #8 |
| 5 | Pesticide paradox | Rotate test techniques | qa.md Mindset #9 |
| 6 | Testing is context dependent | Mỗi dự án cần chiến lược khác | qa.md Mindset #10 |
| 7 | Absence of errors is a fallacy | Bug-free ≠ useful | qa-rules.md §1.5 |

## 6 Chapters Mapping

| Chapter | Topic | Agent Files |
|---------|-------|-------------|
| CH1 | Fundamentals of Testing | qa-rules.md §1, qa.md Mindset |
| CH2 | Testing Throughout SDLC | qa.md Quadrants, qa-rules.md §2 |
| CH3 | Static Testing | qa-rules.md §7 |
| CH4 | Test Analysis & Design | SKILL.md techniques, qa-rules.md §10 |
| CH5 | Managing Test Activities | qa-rules.md §8-§9, qa-workflow.md |
| CH6 | Test Tools | SKILL.md Playwright, qa-workflow.md |

## Advanced Level — Test Analyst

| Area | Agent Coverage |
|------|----------------|
| Test Process | qa-workflow.md (8 steps) |
| Test Monitoring & Control | qa-rules.md §8 |
| Reviews | qa-rules.md §7 |
| Test Environment | create-test-plan.md Mode D |

## Cross-References
- Role: `.agents/personas/qa/persona.md`
- Rules: `.agents/rules/qa-rules.md` (§1-§10)
- Skills: `.agents/skills/qa/SKILL.md`
- Playwright: `.agents/skills/qa/examples/`
