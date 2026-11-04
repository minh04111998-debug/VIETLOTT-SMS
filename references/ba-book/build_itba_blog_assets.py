#!/usr/bin/env python3
"""
Generate all 100 ITBA Mentor Cover Cards (1200x675 16:9 PNG matching media_1793500827171_0a768a6e.png)
+ Blog-formatted Notion-Flavored Markdown bodies matching 1e7d4f15f66e8069ada9e2380c21c5c3
while preserving 100% verbatim book text.
"""
import concurrent.futures
import datetime
import html
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(r"f:\VIETLOTT-SMS\references\ba-book")
ARTICLES_JSON = BASE_DIR / "extracted" / "articles_100.json"
COVERS_DIR = BASE_DIR / "itba_covers"
HTML_DIR = COVERS_DIR / "html"
CHUNKS_V2_DIR = BASE_DIR / "extracted" / "blog_update_chunks"

COVERS_DIR.mkdir(parents=True, exist_ok=True)
HTML_DIR.mkdir(parents=True, exist_ok=True)
CHUNKS_V2_DIR.mkdir(parents=True, exist_ok=True)

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
EDGE = next(p for p in EDGE_PATHS if Path(p).exists())

STEPS_323 = Path(r"C:\Users\MyLaptop\.gemini\antigravity\brain\8ea8e18e-a26f-4bc4-909c-659e5ff0e34c\.system_generated\steps\323\output.txt")

ACRONYMS = {
    "ba": "BA",
    "babok": "BABOK",
    "srs": "SRS",
    "brd": "BRD",
    "prd": "PRD",
    "frd": "FRD",
    "uat": "UAT",
    "sit": "SIT",
    "ui": "UI",
    "ux": "UX",
    "ui/ux": "UI/UX",
    "dev": "DEV",
    "qa": "QA",
    "qc": "QC",
    "po": "PO",
    "pm": "PM",
    "sa": "SA",
    "da": "DA",
    "api": "API",
    "sql": "SQL",
    "ddd": "DDD",
    "bpmn": "BPMN",
    "uml": "UML",
    "erd": "ERD",
    "kpi": "KPI",
    "kpis": "KPIs",
    "okr": "OKR",
    "okrs": "OKRs",
    "ci/cd": "CI/CD",
    "cr": "CR",
    "uc": "UC",
    "hrm": "HRM",
    "erp": "ERP",
    "crm": "CRM",
    "cms": "CMS",
    "wms": "WMS",
    "oms": "OMS",
    "ai": "AI",
    "bi": "BI",
    "ot": "OT",
    "mvp": "MVP",
    "roi": "ROI",
    "sla": "SLA",
    "rbac": "RBAC",
    "crud": "CRUD",
    "json": "JSON",
    "scrum": "Scrum",
    "agile": "Agile",
    "sprint": "Sprint",
    "retro": "Retro",
    "backlog": "Backlog",
    "roadmap": "Roadmap",
    "production": "Production",
    "release": "release",
    "stakeholder": "Stakeholder",
    "stakeholders": "Stakeholders",
    "senior": "Senior",
    "junior": "Junior",
    "middle": "Middle",
    "lead": "Lead",
    "manager": "Manager",
    "mentor": "Mentor",
    "startup": "Startup",
    "product": "Product",
    "outsource": "Outsource",
    "domain-driven": "Domain-Driven",
    "domain": "Domain",
    "driven": "Driven",
    "design": "Design",
    "thinking": "Thinking",
    "data": "Data",
    "object": "Object",
    "hidden": "Hidden",
    "requirement": "Requirement",
    "requirements": "Requirements",
    "use": "Use",
    "case": "Case",
    "user": "User",
    "story": "Story",
    "stories": "Stories",
    "flow": "flow",
    "checklist": "Checklist",
    "template": "Template",
    "framework": "Framework",
    "excel": "Excel",
    "figma": "Figma",
    "jira": "Jira",
    "notion": "Notion",
    "cskh": "CSKH",
    "ceo": "CEO",
    "cto": "CTO",
    "hr": "HR",
    "it": "IT",
    "p.o.l.c": "P.O.L.C",
    "polc": "P.O.L.C",
    "raci": "RACI",
    "swot": "SWOT",
    "smart": "SMART",
    "invest": "INVEST",
    "moscow": "MoSCoW",
    "done": "DONE",
}


def smart_vietnamese_title(raw_upper: str) -> str:
    s = raw_upper.strip()
    s = re.sub(r"\s+-\s+", " – ", s)
    lower = s.lower()

    def repl_word(m):
        w = m.group(0)
        if w in ACRONYMS:
            return ACRONYMS[w]
        return w

    tokens_re = re.compile(r"[a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ0-9]+(?:[./-][a-z0-9]+)*")
    res = tokens_re.sub(repl_word, lower)

    chars = list(res)
    cap_next = True
    for idx, ch in enumerate(chars):
        if cap_next and ch.isalpha():
            chars[idx] = ch.upper()
            cap_next = False
        elif ch in "?!:":
            cap_next = True
        elif ch == "." and idx + 1 < len(chars) and chars[idx + 1] == " ":
            cap_next = True
        elif idx >= 1 and "".join(chars[max(0, idx - 1) : idx + 1]) in ("– ", "— ", "= "):
            cap_next = True
    return "".join(chars)


def classify_article(day: int, raw_title: str, body: str):
    text = (raw_title + " " + body).lower()
    # Match Mr. Phú's exact Tags style in screenshot: ["BA100", "BABOK"] (plus 1 specific tag when not BABOK)
    tags = ["BA100"]
    if "babok" in text:
        tags.append("BABOK")
    else:
        if any(k in text for k in ["ba lead", "ba manager", "p.o.l.c", "khung năng lực", "mentor", "coaching", "giao kpi"]):
            tags.append("Leadership")
        elif any(k in text for k in ["phỏng vấn", "lương", "cv", "nhảy việc", "startup", "hr", "nghỉ việc", "senior ba"]):
            tags.append("HR")
        elif any(k in text for k in ["hệ thống", "system", "data object", "ddd", "api", "database", "ci/cd", "kiến trúc"]):
            tags.append("System Thinking")
        elif any(k in text for k in ["họp", "stakeholder", "khách", "quay xe", "chia bè", "retro", "sprint", "deadline", "release"]):
            tags.append("Work")
        else:
            tags.append("Skill")

    t_low = raw_title.lower()
    if any(k in t_low for k in ["hidden", "ngầm", "gốc", "soi", "rủi ro", "giả định", "assumption", "check", "review", "bẫy"]):
        scene = "magnifier"
        prop_label = "HIDDEN REQ" if ("hidden" in t_low or "ngầm" in t_low) else "DEEP CHECK"
    elif any(k in t_low for k in ["chia bè", "đổ lỗi", "quay xe", "ngại hỏi", "gật đầu", "comment", "cãi", "ép", "họp"]):
        scene = "crossfire"
        prop_label = "STAKEHOLDER"
    elif any(k in t_low for k in ["tốn 3 team", "1 dòng", "khóc", "toang", "bug oan", "vỡ tiến độ", "nợ", "mệt", "rời đi"]):
        scene = "stressed_ba"
        prop_label = "SCOPE CREEP"
    elif any(k in t_low for k in ["lỗi", "bug", "phá", "test", "production", "ci/cd", "exception", "lọt case"]):
        scene = "tester_laptop"
        prop_label = "EDGE CASE"
    elif any(k in t_low for k in ["senior", "level", "lên", "sự nghiệp", "học gì", "startup", "lương", "phỏng vấn", "nâng tầm"]):
        scene = "stairs"
        prop_label = "SENIOR BA"
    elif any(k in t_low for k in ["hệ thống", "bản vẽ", "data object", "ddd", "domain", "kiến trúc", "luồng", "mở rộng", "database", "api"]):
        scene = "blueprint"
        prop_label = "SYSTEM DESIGN"
    elif any(k in t_low for k in ["release", "đo lường", "kpi", "hiệu quả", "data", "chỉ số", "giá trị"]):
        scene = "metrics_rocket"
        prop_label = "POST-RELEASE"
    elif any(k in t_low for k in ["lead", "manager", "p.o.l.c", "team", "khung năng lực", "quản lý", "retro"]):
        scene = "team_compass"
        prop_label = "BA LEAD"
    else:
        scene = ("magnifier", "blueprint", "babok_desk", "crossfire")[day % 4]
        prop_label = "BABOK" if "babok" in text else f"DAY {day}/100"

    return tags, scene, prop_label


def extract_summary(body_md: str) -> str:
    lines = []
    for raw in body_md.splitlines():
        s = raw.strip()
        if not s or s.startswith("#") or s.startswith("> **Nguồn:**"):
            continue
        s = re.sub(r"^[✦■✖▲▼◆●✎👤💊🔧📌👉💡🔍💬🗣⚠️✅❌]+\s*", "", s)
        s = re.sub(r"^>\s*", "", s)
        s = s.replace("**", "").replace("*", "")
        if len(s) > 15:
            lines.append(s)
        if len(" ".join(lines)) >= 110:
            break
    summary = " ".join(lines)
    if len(summary) > 180:
        summary = summary[:177].rsplit(" ", 1)[0] + "..."
    return summary


def get_scene_svg(scene: str, prop_label: str, day: int) -> str:
    lbl = html.escape(prop_label)
    ba_head = """
      <path d="M195 118 C185 68, 240 42, 295 48 C345 52, 372 86, 362 135 C358 152, 348 162, 342 168 L206 168 Z" fill="#5A3E2B" stroke="#3B2618" stroke-width="3.5" stroke-linejoin="round"/>
      <ellipse cx="204" cy="152" rx="13" ry="17" fill="#FAD7BA" stroke="#4A3222" stroke-width="3"/>
      <ellipse cx="348" cy="152" rx="13" ry="17" fill="#FAD7BA" stroke="#4A3222" stroke-width="3"/>
      <path d="M210 112 C210 82, 342 82, 342 112 L342 158 C342 198, 310 216, 276 216 C242 216, 210 198, 210 158 Z" fill="#FCE2C9" stroke="#4A3222" stroke-width="3.5"/>
      <ellipse cx="232" cy="172" rx="13" ry="7" fill="#F4B393" opacity="0.55"/>
      <ellipse cx="320" cy="172" rx="13" ry="7" fill="#F4B393" opacity="0.55"/>
      <path d="M202 124 C212 88, 256 76, 305 84 C326 88, 344 100, 350 120 C332 104, 300 98, 262 102 C234 105, 216 114, 202 124 Z" fill="#6B4B35" stroke="#3B2618" stroke-width="3.2" stroke-linejoin="round"/>
      <path d="M232 126 Q248 119 262 125" fill="none" stroke="#4A3222" stroke-width="4" stroke-linecap="round"/>
      <path d="M290 125 Q304 119 320 126" fill="none" stroke="#4A3222" stroke-width="4" stroke-linecap="round"/>
      <rect x="223" y="134" width="46" height="32" rx="9" fill="#FFFFFF" fill-opacity="0.45" stroke="#2D231E" stroke-width="4.5"/>
      <rect x="283" y="134" width="46" height="32" rx="9" fill="#FFFFFF" fill-opacity="0.45" stroke="#2D231E" stroke-width="4.5"/>
      <line x1="269" y1="148" x2="283" y2="148" stroke="#2D231E" stroke-width="4.5"/>
      <line x1="210" y1="146" x2="223" y2="148" stroke="#2D231E" stroke-width="4"/>
      <line x1="329" y1="148" x2="342" y2="146" stroke="#2D231E" stroke-width="4"/>
      <path d="M236 151 Q246 157 256 151" fill="none" stroke="#3B2618" stroke-width="3.6" stroke-linecap="round"/>
      <path d="M296 151 Q306 157 316 151" fill="none" stroke="#3B2618" stroke-width="3.6" stroke-linecap="round"/>
      <path d="M275 160 Q271 169 277 172" fill="none" stroke="#8C5E3C" stroke-width="2.8" stroke-linecap="round"/>
      <path d="M260 185 Q276 196 292 185" fill="none" stroke="#6E4427" stroke-width="3.4" stroke-linecap="round"/>
    """
    ba_suit_torso = """
      <path d="M188 360 L204 232 C210 218, 232 212, 252 212 L300 212 C320 212, 342 218, 348 232 L364 360 Z" fill="#635852" stroke="#3B2618" stroke-width="3.5" stroke-linejoin="round"/>
      <polygon points="252,212 300,212 276,296" fill="#EDEBE6" stroke="#3B2618" stroke-width="3"/>
      <polygon points="252,212 276,236 260,248 242,222" fill="#F7F5F0" stroke="#3B2618" stroke-width="2.8"/>
      <polygon points="300,212 276,236 292,248 310,222" fill="#F7F5F0" stroke="#3B2618" stroke-width="2.8"/>
      <polygon points="270,236 282,236 287,316 276,332 265,316" fill="#C9643B" stroke="#4A3222" stroke-width="2.8" stroke-linejoin="round"/>
      <polyline points="242,220 228,262 256,308" fill="none" stroke="#3B2618" stroke-width="3" stroke-linejoin="round"/>
      <polyline points="310,220 324,262 296,308" fill="none" stroke="#3B2618" stroke-width="3" stroke-linejoin="round"/>
    """

    if scene == "magnifier":
        return f"""
        <svg viewBox="80 35 420 295" xmlns="http://www.w3.org/2000/svg">
          {ba_suit_torso}
          {ba_head}
          <rect x="166" y="218" width="12" height="58" rx="5" transform="rotate(-12 172 247)" fill="#5A3E2B" stroke="#2D231E" stroke-width="3"/>
          <circle cx="158" cy="176" r="44" fill="#FDF8EE" fill-opacity="0.76" stroke="#5A3E2B" stroke-width="7"/>
          <circle cx="158" cy="176" r="36" fill="none" stroke="#9C7A54" stroke-width="2"/>
          <path d="M138 156 Q148 144 164 148" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
          <circle cx="174" cy="252" r="18" fill="#FCE2C9" stroke="#4A3222" stroke-width="3.2"/>
          <g transform="rotate(6 382 280)">
            <rect x="322" y="220" width="126" height="118" rx="8" fill="#F2E2BE" stroke="#6E5236" stroke-width="3.5"/>
            <line x1="338" y1="246" x2="432" y2="246" stroke="#B89F74" stroke-width="3"/>
            <text x="385" y="280" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-weight="800" font-size="16" fill="#3E3228">{lbl}</text>
            <text x="385" y="305" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-weight="800" font-size="14" fill="#004AAD">DAY {day}/100</text>
          </g>
          <circle cx="444" cy="292" r="17" fill="#FCE2C9" stroke="#4A3222" stroke-width="3.2"/>
        </svg>"""

    if scene == "crossfire":
        # Like Card 2 in user's screenshot (BA between two opposing team silhouettes!)
        return f"""
        <svg viewBox="70 35 440 295" xmlns="http://www.w3.org/2000/svg">
          <!-- Left Stakeholder Silhouette (Warm Ochre) -->
          <g opacity="0.72" transform="translate(-18, 12)">
            <circle cx="165" cy="135" r="44" fill="#CFA072" stroke="#8C6239" stroke-width="3"/>
            <path d="M108 320 C114 235, 140 205, 198 205 L220 320 Z" fill="#C98A5B" stroke="#8C6239" stroke-width="3"/>
          </g>
          <!-- Right Stakeholder Silhouette (Cool Slate) -->
          <g opacity="0.72" transform="translate(18, 12)">
            <circle cx="385" cy="135" r="44" fill="#8EA2B4" stroke="#536878" stroke-width="3"/>
            <path d="M330 320 L352 205 C410 205, 436 235, 442 320 Z" fill="#768D9E" stroke="#536878" stroke-width="3"/>
          </g>
          <!-- Central BA Character with worried/focused eyebrows (just like Card 2!) -->
          {ba_suit_torso}
          <path d="M195 118 C185 68, 240 42, 295 48 C345 52, 372 86, 362 135 C358 152, 348 162, 342 168 L206 168 Z" fill="#2D2926" stroke="#1E1B18" stroke-width="3.5"/>
          <ellipse cx="204" cy="152" rx="13" ry="17" fill="#FAD7BA" stroke="#4A3222" stroke-width="3"/>
          <ellipse cx="348" cy="152" rx="13" ry="17" fill="#FAD7BA" stroke="#4A3222" stroke-width="3"/>
          <path d="M210 112 C210 82, 342 82, 342 112 L342 158 C342 198, 310 216, 276 216 C242 216, 210 198, 210 158 Z" fill="#FCE2C9" stroke="#4A3222" stroke-width="3.5"/>
          <path d="M202 124 C212 88, 256 76, 305 84 C326 88, 344 100, 350 120 C332 104, 300 98, 262 102 C234 105, 216 114, 202 124 Z" fill="#3B3531" stroke="#1E1B18" stroke-width="3.2"/>
          <path d="M232 128 Q248 120 262 122" fill="none" stroke="#2D231E" stroke-width="4" stroke-linecap="round"/>
          <path d="M290 122 Q304 120 320 128" fill="none" stroke="#2D231E" stroke-width="4" stroke-linecap="round"/>
          <circle cx="246" cy="152" r="22" fill="#FFFFFF" fill-opacity="0.45" stroke="#5A4638" stroke-width="3.8"/>
          <circle cx="306" cy="152" r="22" fill="#FFFFFF" fill-opacity="0.45" stroke="#5A4638" stroke-width="3.8"/>
          <line x1="268" y1="152" x2="284" y2="152" stroke="#5A4638" stroke-width="3.8"/>
          <circle cx="246" cy="153" r="4.8" fill="#2D231E"/>
          <circle cx="306" cy="153" r="4.8" fill="#2D231E"/>
          <path d="M264 190 Q276 184 288 190" fill="none" stroke="#6E4427" stroke-width="3.2" stroke-linecap="round"/>
        </svg>"""

    if scene == "stressed_ba":
        # Like Card 4 in user's screenshot (humorous crying/sweating BA when "chỉ thêm 1 dòng thôi mà"!)
        return f"""
        <svg viewBox="80 35 420 295" xmlns="http://www.w3.org/2000/svg">
          {ba_suit_torso}
          <path d="M195 118 C185 68, 240 42, 295 48 C345 52, 372 86, 362 135 L206 168 Z" fill="#4A3728" stroke="#2D231E" stroke-width="3.5"/>
          <ellipse cx="204" cy="152" rx="13" ry="17" fill="#F5C9A6" stroke="#4A3222" stroke-width="3"/>
          <ellipse cx="348" cy="152" rx="13" ry="17" fill="#F5C9A6" stroke="#4A3222" stroke-width="3"/>
          <path d="M210 112 C210 82, 342 82, 342 112 L342 158 C342 198, 310 216, 276 216 C242 216, 210 198, 210 158 Z" fill="#F7CFAF" stroke="#4A3222" stroke-width="3.5"/>
          <path d="M202 124 C212 88, 256 76, 305 84 C326 88, 344 100, 350 120 C332 104, 300 98, 262 102 Z" fill="#5A4230" stroke="#2D231E" stroke-width="3.2"/>
          <!-- Worried slanted brows -->
          <path d="M230 130 Q248 122 262 118" fill="none" stroke="#3B2618" stroke-width="4.2" stroke-linecap="round"/>
          <path d="M290 118 Q304 122 322 130" fill="none" stroke="#3B2618" stroke-width="4.2" stroke-linecap="round"/>
          <rect x="223" y="134" width="46" height="30" rx="7" fill="#FFFFFF" fill-opacity="0.4" stroke="#2D231E" stroke-width="4"/>
          <rect x="283" y="134" width="46" height="30" rx="7" fill="#FFFFFF" fill-opacity="0.4" stroke="#2D231E" stroke-width="4"/>
          <line x1="269" y1="148" x2="283" y2="148" stroke="#2D231E" stroke-width="4"/>
          <path d="M236 150 Q246 144 256 150" fill="none" stroke="#3B2618" stroke-width="3.5" stroke-linecap="round"/>
          <path d="M296 150 Q306 144 316 150" fill="none" stroke="#3B2618" stroke-width="3.5" stroke-linecap="round"/>
          <!-- Comic tear streams -->
          <path d="M238 164 Q232 188 236 206" fill="none" stroke="#7CC0EE" stroke-width="6" stroke-linecap="round"/>
          <path d="M314 164 Q320 188 316 206" fill="none" stroke="#7CC0EE" stroke-width="6" stroke-linecap="round"/>
          <path d="M258 192 Q276 180 294 192" fill="none" stroke="#6E4427" stroke-width="3.8" stroke-linecap="round"/>
        </svg>"""

    if scene == "tester_laptop":
        return f"""
        <svg viewBox="85 45 430 295" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(-75, -10)">
            <path d="M210 250 C205 168, 232 115, 272 115 C312 115, 338 168, 334 250 Z" fill="#46423F" stroke="#2D231E" stroke-width="3.5"/>
            <ellipse cx="272" cy="186" rx="34" ry="36" fill="#231F1D"/>
            <path d="M248 178 Q258 186 266 178" fill="#EFE6D5"/>
            <path d="M278 178 Q286 186 296 178" fill="#EFE6D5"/>
            <path d="M254 198 Q272 212 290 198" fill="none" stroke="#EFE6D5" stroke-width="3.5" stroke-linecap="round"/>
            <text x="272" y="145" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="14" fill="#E6DEC8">TESTER</text>
          </g>
          <g transform="translate(65, 8)">
            {ba_suit_torso}
            {ba_head}
          </g>
          <polygon points="210,252 356,252 374,340 228,340" fill="#C9C3B8" stroke="#3B2618" stroke-width="3.5" stroke-linejoin="round"/>
          <rect x="274" y="268" width="32" height="14" rx="3" fill="#EDE7DA" stroke="#4A3222" stroke-width="2.2"/>
          <polygon points="292,290 306,300 292,310 278,300" fill="#EDE7DA" stroke="#4A3222" stroke-width="2.2"/>
          <line x1="291" y1="282" x2="292" y2="290" stroke="#4A3222" stroke-width="2.2"/>
        </svg>"""

    if scene == "stairs":
        return f"""
        <svg viewBox="80 40 440 295" xmlns="http://www.w3.org/2000/svg">
          <polyline points="95,335 95,285 190,285 190,230 285,230 285,175 385,175 385,120 480,120" fill="none" stroke="#4A3222" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
          <line x1="445" y1="120" x2="445" y2="48" stroke="#4A3222" stroke-width="4.5" stroke-linecap="round"/>
          <path d="M445 50 L525 68 L445 86 Z" fill="#C9643B" stroke="#4A3222" stroke-width="3.2" stroke-linejoin="round"/>
          <text x="476" y="73" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="11" fill="#FFF8EC">{lbl}</text>
          <g transform="translate(-38, 2) scale(0.95)">
            {ba_suit_torso}
            {ba_head}
          </g>
        </svg>"""

    if scene == "blueprint":
        return f"""
        <svg viewBox="75 40 455 295" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(-58, 6) scale(0.96)">
            {ba_suit_torso}
            {ba_head}
          </g>
          <rect x="292" y="132" width="224" height="178" rx="12" fill="#1E4B85" stroke="#3B2618" stroke-width="4"/>
          <rect x="304" y="144" width="200" height="154" rx="6" fill="none" stroke="#7FB3EB" stroke-width="1.8" stroke-dasharray="5,4"/>
          <text x="404" y="168" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="13" fill="#FCE8B2">{lbl}</text>
          <rect x="320" y="186" width="66" height="32" rx="6" fill="#F9F1DC" stroke="#0052B4" stroke-width="2.5"/>
          <text x="353" y="207" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="11" fill="#0052B4">DOMAIN</text>
          <rect x="422" y="186" width="66" height="32" rx="6" fill="#F9F1DC" stroke="#0052B4" stroke-width="2.5"/>
          <text x="455" y="207" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="11" fill="#0052B4">FLOW</text>
          <rect x="366" y="246" width="76" height="32" rx="6" fill="#FCE2C9" stroke="#C9643B" stroke-width="2.5"/>
          <text x="404" y="267" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="11" fill="#8C3B1A">SYSTEM</text>
          <line x1="386" y1="202" x2="422" y2="202" stroke="#FCE8B2" stroke-width="3"/>
          <line x1="353" y1="218" x2="392" y2="246" stroke="#FCE8B2" stroke-width="3"/>
          <line x1="455" y1="218" x2="416" y2="246" stroke="#FCE8B2" stroke-width="3"/>
        </svg>"""

    if scene == "metrics_rocket":
        return f"""
        <svg viewBox="75 40 455 295" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(-55, 6) scale(0.96)">
            {ba_suit_torso}
            {ba_head}
          </g>
          <rect x="300" y="142" width="214" height="172" rx="12" fill="#FDF8EE" stroke="#4A3222" stroke-width="3.8"/>
          <rect x="300" y="142" width="214" height="36" rx="10" fill="#004AAD" stroke="#4A3222" stroke-width="3.5"/>
          <text x="407" y="165" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="13" fill="#FFFFFF">{lbl}</text>
          <rect x="328" y="252" width="26" height="40" rx="4" fill="#9BC2F0" stroke="#4A3222" stroke-width="2.4"/>
          <rect x="368" y="228" width="26" height="64" rx="4" fill="#5B9AE6" stroke="#4A3222" stroke-width="2.4"/>
          <rect x="408" y="206" width="26" height="86" rx="4" fill="#004AAD" stroke="#4A3222" stroke-width="2.4"/>
          <rect x="448" y="190" width="26" height="102" rx="4" fill="#C9643B" stroke="#4A3222" stroke-width="2.4"/>
          <polyline points="341,240 381,216 421,194 461,180" fill="none" stroke="#2D7A4F" stroke-width="4" stroke-linecap="round"/>
        </svg>"""

    if scene == "team_compass":
        return f"""
        <svg viewBox="75 40 455 295" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(-48, 6) scale(0.96)">
            {ba_suit_torso}
            {ba_head}
          </g>
          <circle cx="412" cy="232" r="80" fill="#F2E2BE" stroke="#4A3222" stroke-width="4"/>
          <circle cx="412" cy="232" r="64" fill="#FDF9EE" stroke="#8C6D46" stroke-width="2.2"/>
          <polygon points="412,178 426,232 412,222 398,232" fill="#C9643B" stroke="#3B2618" stroke-width="2.2"/>
          <polygon points="412,286 426,232 412,242 398,232" fill="#004AAD" stroke="#3B2618" stroke-width="2.2"/>
          <circle cx="412" cy="232" r="9" fill="#F2E2BE" stroke="#3B2618" stroke-width="3"/>
          <text x="412" y="140" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="14" fill="#004AAD">{lbl}</text>
        </svg>"""

    return f"""
    <svg viewBox="80 40 440 295" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(-42, 6) scale(0.96)">
        {ba_suit_torso}
        {ba_head}
      </g>
      <rect x="322" y="152" width="152" height="172" rx="10" fill="#F2E2BE" stroke="#4A3222" stroke-width="3.8"/>
      <rect x="368" y="140" width="60" height="22" rx="6" fill="#635852" stroke="#3B2618" stroke-width="3"/>
      <text x="398" y="186" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="14" fill="#004AAD">{lbl}</text>
      <polyline points="344,212 351,220 364,204" fill="none" stroke="#2D7A4F" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      <line x1="374" y1="213" x2="452" y2="213" stroke="#5A3E2B" stroke-width="4" stroke-linecap="round"/>
      <polyline points="344,248 351,256 364,240" fill="none" stroke="#2D7A4F" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      <line x1="374" y1="249" x2="452" y2="249" stroke="#5A3E2B" stroke-width="4" stroke-linecap="round"/>
      <polyline points="344,284 351,292 364,276" fill="none" stroke="#C9643B" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      <line x1="374" y1="285" x2="440" y2="285" stroke="#5A3E2B" stroke-width="4" stroke-linecap="round"/>
    </svg>"""


def build_cover_html(day: int, smart_title: str, scene: str, prop_label: str) -> str:
    """Exact 1200x675 (16:9) layout matching media_1793500827171_0a768a6e.png!"""
    title_escaped = html.escape(smart_title)
    tlen = len(smart_title)
    if tlen <= 38:
        fsize = "48px"
    elif tlen <= 58:
        fsize = "42px"
    elif tlen <= 85:
        fsize = "36px"
    else:
        fsize = "31px"

    svg_markup = get_scene_svg(scene, prop_label, day)

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{
  width: 1200px;
  height: 675px;
  overflow: hidden;
  background: #F6EED9;
  font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Tahoma, sans-serif;
  -webkit-font-smoothing: antialiased;
}}
.canvas {{
  width: 1200px;
  height: 675px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 26px 48px 0 48px;
  background:
    radial-gradient(circle at 20% 22%, rgba(255,255,255,0.45) 0%, rgba(255,255,255,0) 48%),
    radial-gradient(circle at 82% 76%, rgba(226,208,170,0.38) 0%, rgba(226,208,170,0) 52%),
    linear-gradient(180deg, #F8F0DC 0%, #F4E9CE 100%);
}}
.topbar {{
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}}
.logo {{
  font-size: 27px;
  font-weight: 900;
  color: #141414;
  letter-spacing: -0.6px;
  line-height: 1;
}}
.title-wrap {{
  width: 100%;
  max-width: 1060px;
  text-align: center;
  margin-top: 8px;
  min-height: 118px;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
}}
h1 {{
  color: #004AAD;
  font-size: {fsize};
  font-weight: 900;
  line-height: 1.24;
  letter-spacing: -0.3px;
}}
.art-wrap {{
  display: flex;
  align-items: flex-end;
  justify-content: center;
  width: 100%;
  flex-grow: 1;
  overflow: hidden;
}}
.art-wrap svg {{
  width: 620px;
  height: 430px;
}}
</style>
</head>
<body>
  <div class="canvas">
    <div class="topbar">
      <div class="logo">iTBA M<span style="position:relative; display:inline-block;">e<svg style="position:absolute; top:-8px; left:0px;" width="18" height="11" viewBox="0 0 20 12"><path d="M4 10 Q2 2 8 3 M13 10 Q17 2 11 3" fill="none" stroke="#141414" stroke-width="2.1" stroke-linecap="round"/></svg></span>ntor</div>
    </div>
    <div class="title-wrap">
      <h1>{title_escaped}</h1>
    </div>
    <div class="art-wrap">
      {svg_markup}
    </div>
  </div>
</body>
</html>"""


def render_one_cover(args):
    day, html_str = args
    html_p = HTML_DIR / f"day_{day:03d}.html"
    png_p = COVERS_DIR / f"day_{day:03d}_cover.png"
    html_p.write_text(html_str, encoding="utf-8")
    cmd = [
        EDGE,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1200,675",
        "--force-device-scale-factor=1",
        f"--screenshot={png_p}",
        html_p.as_uri(),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return day, png_p


NUM_EMOJIS = {
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "4": "4️⃣",
    "5": "5️⃣",
    "6": "6️⃣",
    "7": "7️⃣",
    "8": "8️⃣",
    "9": "9️⃣",
    "10": "🔟",
}


def escape_angle_brackets_outside_code(line: str) -> str:
    parts = line.split("`")
    for idx in range(0, len(parts), 2):
        prefix = ""
        chunk = parts[idx]
        if idx == 0 and chunk.startswith("> "):
            prefix = "> "
            chunk = chunk[2:]
        chunk = chunk.replace("<", r"\<").replace(">", r"\>")
        parts[idx] = prefix + chunk
    return "`".join(parts)


def format_blog_markdown(day: int, smart_title: str, body_md: str, page_label: str) -> str:
    """
    Exact form of Mr. Phú's `1e7d4f15f66e8069ada9e2380c21c5c3` ([Day 24/100] Hidden Requirement):
    - Starts directly with Hook Heading (`### 🌟 ...` or bold lead) — no duplicate title since page header already shows `🗓️ [Day X/100] ...`
    - `> Quote` blocks for dialogue, hidden rules, & takeaways
    - `---` dividers between sections & numbered points
    - `## 📚 / 🎯 / 💡` major section headers
    - `### 1️⃣ / 2️⃣ / 3️⃣` & `### ❌ / ✅` sub-headers
    - Clean `- ...` bullets
    - 100% verbatim author text preserved!
    """
    raw_lines = body_md.splitlines()
    blocks = []
    prev_was_divider = False
    seen_first_content = False

    def add_divider():
        nonlocal prev_was_divider
        if blocks and not prev_was_divider and blocks[-1] != "---":
            blocks.append("---")
            prev_was_divider = True

    def add_block(b: str):
        nonlocal prev_was_divider, seen_first_content
        blocks.append(b)
        prev_was_divider = (b == "---")
        if b != "---":
            seen_first_content = True

    for line in raw_lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("# DAY ") or s.startswith("> **Nguồn:**"):
            continue

        if s.startswith("## "):
            add_divider()
            txt = escape_angle_brackets_outside_code(s[3:].strip())
            add_block(f"## 🎯 {txt}")
            continue
        if s.startswith("### "):
            txt = escape_angle_brackets_outside_code(s[4:].strip())
            add_block(f"### {txt}")
            continue

        if s.startswith("> "):
            qtxt = escape_angle_brackets_outside_code(s[2:].strip())
            add_block(f"> {qtxt}")
            continue

        # Numbered major items
        m_num = re.match(r"^(?:[-◆▲✦■●]\s*)?(\*\*)?(\d{1,2})[.)]\s+(.+)$", s)
        if m_num and len(s) <= 140:
            lead_bold, num_str, rest = m_num.group(1) or "", m_num.group(2), m_num.group(3).strip()
            add_divider()
            emo = NUM_EMOJIS.get(num_str, f"{num_str}.")
            rest_clean = escape_angle_brackets_outside_code(lead_bold + rest)
            add_block(f"### {emo} {rest_clean}")
            continue

        if s.startswith(("✖ ", "▼ ")):
            rest = escape_angle_brackets_outside_code(s[2:].strip())
            if len(rest) <= 110:
                add_block(f"### ❌ {rest}")
            else:
                add_block(f"❌ {rest}")
            continue

        if s.startswith("▲ "):
            rest = escape_angle_brackets_outside_code(s[2:].strip())
            add_divider()
            if len(rest) <= 125:
                add_block(f"## 🎯 {rest}")
            else:
                add_block(f"⚠️ {rest}")
            continue

        if s.startswith("✦ "):
            rest = escape_angle_brackets_outside_code(s[2:].strip())
            if seen_first_content:
                add_divider()
            if len(rest) <= 125:
                add_block(f"### 🌟 {rest}")
            else:
                add_block(f"🌟 {rest}")
            continue

        if s.startswith("💡 "):
            rest = escape_angle_brackets_outside_code(s[2:].strip())
            if len(rest) <= 115 and (rest.startswith("**") or "kỹ thuật" in rest.lower() or "nguyên tắc" in rest.lower() or "cách" in rest.lower()):
                add_divider()
                add_block(f"## 🎯 {rest}")
            else:
                add_block(f"💡 {rest}")
            continue

        if s.startswith("✎ "):
            rest = escape_angle_brackets_outside_code(s[2:].strip())
            if len(rest) <= 95 and (":" in rest or rest.startswith("**")):
                add_divider()
                add_block(f"## 📚 {rest}")
            else:
                add_block(f"- 📝 {rest}")
            continue

        if re.match(r"^(?:🔍\s*|📍\s*)?(?:\*\*)?(?:Tóm lại|Tổng kết|Kết luận|Bài học xương máu)", s, re.IGNORECASE):
            add_divider()
            rest = escape_angle_brackets_outside_code(re.sub(r"^(?:🔍|📍)\s*", "", s))
            if len(rest) <= 90:
                add_block(f"## 💡 {rest}")
            elif ":" in rest:
                head, tail = rest.split(":", 1)
                add_block(f"## 💡 {head.strip()}:")
                if tail.strip():
                    add_block(f"> {tail.strip()}")
            else:
                add_block(f"> 💡 {rest}")
            continue

        if s.startswith("💬 "):
            add_divider()
            rest = escape_angle_brackets_outside_code(s[2:].strip())
            if len(rest) <= 110:
                add_block(f"## 💬 {rest}")
            else:
                add_block(f"💬 {rest}")
            continue

        if s.startswith("🔥 "):
            rest = escape_angle_brackets_outside_code(s[2:].strip())
            add_block(f"> 🔥 {rest}")
            continue

        if s.startswith(("■ ", "◆ ")):
            rest = escape_angle_brackets_outside_code(s[2:].strip())
            low = rest.lower()
            if any(low.startswith(k) for k in ["cách làm đúng", "đúng:", "đúng ", "**đúng", "mà là", "giải pháp", "nên làm", "checklist"]):
                add_block(f"### ✅ {rest}")
            elif any(low.startswith(k) for k in ["một bài học", "**một bài học", "ví dụ thực tế", "**ví dụ", "chuyện thật"]):
                add_divider()
                add_block(f"## 📚 {rest}")
            elif (rest.endswith(":") or rest.endswith("?") or rest.startswith("**")) and len(rest) <= 105:
                add_block(f"### 📌 {rest}")
            else:
                add_block(f"- {rest}")
            continue

        if s.startswith(("● ", "▸ ", "• ")):
            rest = escape_angle_brackets_outside_code(s[2:].strip())
            if rest.endswith(":") and len(rest) <= 90:
                add_block(f"### 📌 {rest}")
            else:
                add_block(f"- {rest}")
            continue

        if s.startswith("- "):
            rest = escape_angle_brackets_outside_code(s[2:].strip())
            add_block(f"- {rest}")
            continue

        if (s.startswith("“") and s.endswith("”")) or (s.startswith('"') and s.endswith('"')):
            qtxt = escape_angle_brackets_outside_code(s)
            add_block(f"> {qtxt}")
            continue

        add_block(escape_angle_brackets_outside_code(s))

    add_divider()
    add_block(f"*📖 Chuỗi **100 ngày làm BA** — **ITBA Mentor** ({escape_angle_brackets_outside_code(page_label)})*")
    return "\n\n".join(blocks)


if __name__ == "__main__":
    articles = json.loads(ARTICLES_JSON.read_text(encoding="utf-8"))
    step_data = json.loads(STEPS_323.read_text(encoding="utf-8"))
    day_to_url = {int(row["Ngày"]): row["url"] for row in step_data["results"]}

    base_date = datetime.date(2025, 4, 8)
    jobs = []
    enriched = []
    for art in articles:
        d = art["day"]
        st = smart_vietnamese_title(art["raw_title"])
        tags, scene, prop_lbl = classify_article(d, art["raw_title"], art["body_markdown"])
        summary = extract_summary(art["body_markdown"])
        blog_md = format_blog_markdown(d, st, art["body_markdown"], art["page_label"])
        cover_png = str(COVERS_DIR / f"day_{d:03d}_cover.png")
        purl = day_to_url[d]
        pid = purl.rstrip("/").split("/")[-1].split("?")[0]
        pub_date = (base_date + datetime.timedelta(days=d - 1)).isoformat()
        jobs.append((d, build_cover_html(d, st, scene, prop_lbl)))
        enriched.append({
            "day": d,
            "page_url": purl,
            "page_id": pid,
            "notion_title": f"[Day {d}/100] {st}",
            "tags": tags,
            "summary": summary,
            "published": pub_date,
            "cover_png": cover_png,
            "blog_markdown": blog_md,
        })

    print("Rendering 100 16:9 (1200x675) ITBA Mentor covers...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        cnt = 0
        for d, p in ex.map(render_one_cover, jobs):
            cnt += 1
            if cnt % 25 == 0 or cnt == 100:
                print(f"  Rendered {cnt}/100 covers (latest: {p.name})")

    out_master = BASE_DIR / "extracted" / "articles_100_itba_blog.json"
    out_master.write_text(json.dumps(enriched, ensure_ascii=False, indent=2), encoding="utf-8")
    chunk_size = 5
    for idx in range(0, 100, chunk_size):
        cnum = (idx // chunk_size) + 1
        cpath = CHUNKS_V2_DIR / f"blog_chunk_{cnum:02d}.json"
        cpath.write_text(json.dumps(enriched[idx : idx + chunk_size], ensure_ascii=False, indent=2), encoding="utf-8")
    print("DONE generating 100 covers and 20 chunks!")
