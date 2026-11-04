# -*- coding: utf-8 -*-
"""
Definitions for 100 unique themed cards for "100 ngày làm BA".
Each day defines:
- badge: Topic tag (e.g. "POST-RELEASE", "GIT & DEV", "SYSTEM ARCHITECTURE")
- theme: Color theme ('blueprint', 'terminal', 'amber', 'crimson', 'executive', 'creative', 'emerald', 'sapphire', 'hazard')
- headline: Main punchy title
- subheadline: Core takeaway / intriguing quote
- graphic_svg: Dedicated vector diagram / illustration for that concept
"""

THEMES = {
    "blueprint": {
        "bg": "radial-gradient(circle at 15% 20%, #1e293b 0%, #0f172a 100%)",
        "badge_border": "#38bdf8",
        "badge_bg": "rgba(56, 189, 248, 0.15)",
        "badge_color": "#38bdf8",
        "headline_color": "#38bdf8",
        "sub_color": "#cbd5e1",
        "accent": "#0284c7"
    },
    "terminal": {
        "bg": "radial-gradient(circle at 20% 25%, #27272a 0%, #18181b 100%)",
        "badge_border": "#4ade80",
        "badge_bg": "rgba(74, 222, 128, 0.15)",
        "badge_color": "#4ade80",
        "headline_color": "#4ade80",
        "sub_color": "#e4e4e7",
        "accent": "#16a34a"
    },
    "amber": {
        "bg": "radial-gradient(circle at 20% 20%, #312e81 0%, #1e1b4b 100%)",
        "badge_border": "#f59e0b",
        "badge_bg": "rgba(245, 158, 11, 0.15)",
        "badge_color": "#f59e0b",
        "headline_color": "#fbbf24",
        "sub_color": "#e0e7ff",
        "accent": "#d97706"
    },
    "crimson": {
        "bg": "radial-gradient(circle at 15% 20%, #450a0a 0%, #1c1917 100%)",
        "badge_border": "#f87171",
        "badge_bg": "rgba(248, 113, 113, 0.15)",
        "badge_color": "#f87171",
        "headline_color": "#fca5a5",
        "sub_color": "#fecdd3",
        "accent": "#dc2626"
    },
    "executive": {
        "bg": "radial-gradient(circle at 20% 25%, #292524 0%, #1c1917 100%)",
        "badge_border": "#eab308",
        "badge_bg": "rgba(234, 179, 8, 0.15)",
        "badge_color": "#eab308",
        "headline_color": "#fef08a",
        "sub_color": "#f5f5f4",
        "accent": "#ca8a04"
    },
    "creative": {
        "bg": "radial-gradient(circle at 15% 25%, #3b0764 0%, #1e1b4b 100%)",
        "badge_border": "#c084fc",
        "badge_bg": "rgba(192, 132, 252, 0.15)",
        "badge_color": "#c084fc",
        "headline_color": "#e9d5ff",
        "sub_color": "#fae8ff",
        "accent": "#9333ea"
    },
    "emerald": {
        "bg": "radial-gradient(circle at 20% 20%, #064e3b 0%, #022c22 100%)",
        "badge_border": "#34d399",
        "badge_bg": "rgba(52, 211, 153, 0.15)",
        "badge_color": "#34d399",
        "headline_color": "#6ee7b7",
        "sub_color": "#ecfdf5",
        "accent": "#059669"
    },
    "sapphire": {
        "bg": "radial-gradient(circle at 15% 25%, #1e3a8a 0%, #0f172a 100%)",
        "badge_border": "#60a5fa",
        "badge_bg": "rgba(96, 165, 250, 0.15)",
        "badge_color": "#60a5fa",
        "headline_color": "#93c5fd",
        "sub_color": "#eff6ff",
        "accent": "#2563eb"
    },
    "hazard": {
        "bg": "radial-gradient(circle at 20% 20%, #431407 0%, #1c1917 100%)",
        "badge_border": "#fb923c",
        "badge_bg": "rgba(251, 146, 60, 0.15)",
        "badge_color": "#fb923c",
        "headline_color": "#fed7aa",
        "sub_color": "#ffedd5",
        "accent": "#ea580c"
    }
}
