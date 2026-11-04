# Designer Examples — Practical References

---

## Example 1: Design System Tokens

```css
/* design-tokens.css — VIETLOTT-SMS Design System */

:root {
  /* === COLORS === */
  --color-brand-50: #EFF6FF;
  --color-brand-100: #DBEAFE;
  --color-brand-500: #3B82F6;
  --color-brand-600: #2563EB;
  --color-brand-700: #1D4ED8;
  
  /* Semantic */
  --color-success: #16A34A;
  --color-warning: #F59E0B;
  --color-error: #DC2626;
  --color-info: #0EA5E9;
  
  /* Neutral */
  --color-gray-50: #F9FAFB;
  --color-gray-100: #F3F4F6;
  --color-gray-200: #E5E7EB;
  --color-gray-500: #6B7280;
  --color-gray-700: #374151;
  --color-gray-900: #111827;
  
  /* === SPACING (8px grid) === */
  --space-1: 4px;
  --space-2: 8px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
  
  /* === TYPOGRAPHY === */
  --font-family: 'Inter', sans-serif;
  --font-h1: 700 32px/1.2 var(--font-family);
  --font-h2: 600 24px/1.3 var(--font-family);
  --font-body: 400 16px/1.5 var(--font-family);
  --font-small: 400 14px/1.5 var(--font-family);
  
  /* === BORDERS === */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
  
  /* === SHADOWS === */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  
  /* === MOTION === */
  --duration-fast: 200ms;
  --duration-normal: 300ms;
  --duration-slow: 500ms;
  --easing-standard: cubic-bezier(0.4, 0, 0.2, 1);
}

[data-theme="dark"] {
  --color-bg-primary: #0F172A;
  --color-bg-secondary: #1E293B;
  --color-text-primary: #F1F5F9;
  --color-text-secondary: #94A3B8;
}
```

---

## Example 2: UX Audit Report Summary

```markdown
## UX Audit — VIETLOTT-SMS Admin Dashboard
**Date:** 10/06/2025

### Scores
| # | Heuristic | Score |
|---|-----------|-------|
| 1 | Visibility of system status | 2/5 🔴 |
| 2 | Match real world | 4/5 🟢 |
| 3 | User control | 3/5 🟡 |
| 4 | Consistency | 3/5 🟡 |
| 5 | Error prevention | 2/5 🔴 |
| **Average** | | **3.0/5** |

### Quick Wins
1. 🔴 Add loading spinners (Sev 3, Low effort)
2. 🔴 Add inline validation (Sev 3, Low effort)
3. 🟡 Add empty state illustrations (Sev 2, Low effort)
```
