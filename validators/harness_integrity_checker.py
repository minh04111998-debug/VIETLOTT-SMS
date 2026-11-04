#!/usr/bin/env python3
"""
Harness Integrity Checker — kiểm tra "bộ khung" của harness còn nguyên vẹn.

Thiết kế chuẩn (DEC-004 — 2026-10-07):
  - .agents/rules/<file>.md: Nguồn chân lý duy nhất (Single Source of Truth) cho toàn bộ rules.
  - .agents/skills/<skill>/: Nguồn chân lý duy nhất cho toàn bộ 26 skills (IDE auto-discovery).
  - .agents/hooks.json = cấu hình hook DUY NHẤT được IDE nạp (cwd khi chạy = .agents/)
  - AGENTS.md <= 120 dòng (Bản đồ Harness nạp vào context).

Bổ sung DEC-008 (2026-10-10):
  - HARNESS_MAP: mọi thư mục gốc phải được ánh xạ vào >= 1 trong 7 AI Harnesses
    (.agents/definitions/harness-map.json); evidence file phải tồn tại.
  - CONTEXT_SIZE: file tri thức trong knowledge/ > 15 KB -> WARN (bài học TD-004).
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
AGENTS_MD_MAX_LINES = 120  # AGENTS.md luôn được nạp vào context -> giữ ở dạng "bản đồ"
KNOWLEDGE_MAX_KB = 15      # TD-004: file 40 KB đã phải phân rã; ngưỡng cảnh báo sớm
HARNESS_KEYS = ("context", "tool", "orchestration", "evaluation", "security", "governance", "agentops")
IGNORED_TOP_DIRS = {".git", "__pycache__", "node_modules", ".vscode", ".idea"}

# Backticked path-like tokens: `rules/global/x.md`, `validators/`, `hooks/post-task.ps1`
RE_BACKTICK_PATH = re.compile(r"`([\w.\-]+(?:/[\w.\-]+)*/?)`")


def _result(check, status, message):
    return {"check": check, "status": status, "message": message}


def check_rule_links(root):
    out = []
    agents_rules = root / ".agents" / "rules"
    if not agents_rules.exists():
        return [_result("RULE_LINKS", "FAIL", ".agents/rules/ không tồn tại — thiếu thư mục rules của harness")]
    rule_files = sorted(agents_rules.glob("*.md"))
    if len(rule_files) == 0:
        return [_result("RULE_LINKS", "FAIL", ".agents/rules/ không có file .md nào")]
    for rf in rule_files:
        if rf.stat().st_size == 0:
            out.append(_result("RULE_LINKS", "FAIL", f".agents/rules/{rf.name}: file rỗng (0 bytes)"))
    if not out:
        out.append(_result("RULE_LINKS", "PASS", f"{len(rule_files)} rule file: .agents/rules/ là nguồn chân lý duy nhất (Single Source of Truth)"))
    return out


def _read_frontmatter(skill_md):
    try:
        text = skill_md.read_text(encoding="utf-8")
    except Exception:
        return None
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def check_skill_junctions(root):
    out = []
    canon = root / ".agents" / "skills"
    if not canon.exists():
        return [_result("SKILL_LINKS", "FAIL", ".agents/skills/ không tồn tại — thiếu thư mục skills của harness")]
    canon_skills = sorted(d for d in canon.iterdir() if d.is_dir())
    for d in canon_skills:
        skill_md = d / "SKILL.md"
        fm = _read_frontmatter(skill_md) if skill_md.exists() else None
        if fm is None:
            out.append(_result("SKILL_META", "FAIL", f".agents/skills/{d.name}: thiếu SKILL.md"))
        elif not fm.get("name") or not fm.get("description"):
            out.append(_result("SKILL_META", "FAIL", f".agents/skills/{d.name}/SKILL.md: frontmatter thiếu 'name' hoặc 'description' -> IDE không hiển thị được skill"))
        elif fm.get("name") != d.name:
            out.append(_result("SKILL_META", "WARN", f".agents/skills/{d.name}/SKILL.md: name='{fm.get('name')}' khác tên thư mục"))

    # Đảm bảo không còn thư mục skills/ thừa tại root
    views = root / "skills"
    if views.exists():
        out.append(_result("SKILL_LINKS", "WARN", "skills/ vẫn tồn tại ở thư mục gốc — nên xóa để đảm bảo .agents/skills/ là nguồn duy nhất"))

    if not any(r["status"] == "FAIL" for r in out):
        out.append(_result("SKILL_LINKS", "PASS", f"{len(canon_skills)} skill: .agents/skills/ hợp lệ, SKILL.md có frontmatter đầy đủ (Single Source of Truth)"))
    return out


def check_hooks(root):
    out = []
    cfg = root / ".agents" / "hooks.json"
    if not cfg.exists():
        return [_result("HOOKS", "WARN", ".agents/hooks.json không tồn tại — harness không có lifecycle hook nào")]
    try:
        data = json.loads(cfg.read_text(encoding="utf-8"))
    except Exception as e:
        return [_result("HOOKS", "FAIL", f".agents/hooks.json không phải JSON hợp lệ: {e}")]

    commands = []

    def walk(node):
        if isinstance(node, dict):
            if "command" in node and isinstance(node["command"], str):
                commands.append(node["command"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(data)
    hook_cwd = cfg.parent  # theo docs: cwd = thư mục chứa hooks.json
    for cmd in commands:
        for tok in re.findall(r"[\w.\-/\\]+\.(?:py|ps1|sh)\b", cmd):
            if not (hook_cwd / tok).resolve().exists():
                out.append(_result("HOOKS", "FAIL", f"Hook command '{cmd}': script '{tok}' không tồn tại (resolve từ .agents/)"))
    for stray in root.rglob("hooks.json"):
        if stray.resolve() != cfg.resolve() and ".agents" not in stray.relative_to(root).parts[:1]:
            rel = stray.relative_to(root).as_posix()
            if not any(part in ("node_modules", ".git") for part in stray.parts):
                out.append(_result("HOOKS", "WARN", f"{rel}: IDE KHÔNG nạp file này (chỉ nạp .agents/hooks.json) — dễ gây hiểu nhầm, nên xóa"))
    if not any(r["status"] == "FAIL" for r in out):
        out.append(_result("HOOKS", "PASS", f".agents/hooks.json hợp lệ, {len(commands)} command, script tồn tại"))
    return out


# Domain/URL và các mẫu không phải đường dẫn hệ thống để tránh false positive
IGNORED_DOMAIN_SUFFIXES = (".com/", ".io/", ".org/", ".net/", ".design/", ".vn/", ".edu/", ".gov/")
IGNORED_BRANCH_PREFIXES = ("feat/", "fix/", "chore/", "refactor/", "hotfix/")
IGNORED_DEV_DIRS = ("controller/", "dto/", "entity/", "service/", "modules/", "repository/", "__tests__/", "test/", "components/", "migrations/", "bingo18/", "home/", "lottie/", "wallet/")
IGNORED_TEXT_SLASHES = ("Given/When/Then", "Approve/Reject", "Yes/No", "Keep/Drop/Modify", "DEV/QA", "PO/PM", "BA/PO", "BA/PM", "H/M/L")
IGNORED_PLAYWRIGHT_RUNTIME = (
    "fixtures/", "test-results/", "tests/fixtures/", "tests/pages/",
    ".github/workflows/e2e-tests.yml", ".github/workflows/"
)
IGNORED_ASSET_EXTENSIONS = (".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif", ".ico", ".ttf", ".woff", ".woff2")


RE_LEGACY_PATTERNS = re.compile(
    r"\b(00_Draft|01_Requirements|02_Design|03_Development|03_Workspace|04_Document|05_Release|05_Meetings|06_Testing|07_Scripts|08_Template|harness/(context|guardrails|verification|loop)|rules/global|rules/quality)[/\\]"
)
RE_DATE_TOKEN = re.compile(r"^\d{1,2}/\d{1,2}(/\d{2,4})?$")
RE_ID_PAIR = re.compile(r"^[A-Za-z0-9\-]+/\d+$")


def _check_paths_in(md_file, root, check_name, level):
    out = []
    try:
        text = md_file.read_text(encoding="utf-8")
    except Exception:
        return out
    rel_file = md_file.relative_to(root).as_posix()
    missing = []
    for m in RE_BACKTICK_PATH.finditer(text):
        tok = m.group(1).strip()
        # Chỉ xét token có '/' (đường dẫn thật). Tên file trần thường là ví dụ đặt tên -> bỏ qua.
        if "/" not in tok:
            continue
        if tok.startswith(("http", "www.")) or tok.count(".") > 3:
            continue
        if any(tok.endswith(s) or (s in tok) for s in IGNORED_DOMAIN_SUFFIXES):
            continue
        if tok.startswith(IGNORED_BRANCH_PREFIXES):
            continue
        if any(tok.startswith(d) for d in IGNORED_DEV_DIRS) or tok in IGNORED_TEXT_SLASHES or tok in IGNORED_PLAYWRIGHT_RUNTIME:
            continue
        if any(tok.endswith(ext) for ext in IGNORED_ASSET_EXTENSIONS):
            continue
        if "xxx" in tok or "NNN" in tok or "[" in tok or "]" in tok or tok.startswith("Timeout/"):
            continue
        if tok.endswith(("-", "_")):
            continue
        if RE_DATE_TOKEN.match(tok) or RE_ID_PAIR.match(tok):
            continue
        # Bỏ qua nhắc lại lịch sử trong decisions-log hoặc README regression về việc xóa rules/ skills/
        if rel_file in ("observability/decisions-log.md", "evaluations/regression/README.md") and tok in ("rules/", "skills/"):
            continue
        cand_root = root / tok
        cand_local = md_file.parent / tok
        if cand_root.exists() or cand_local.exists():
            continue
        missing.append(tok)
    missing = sorted(set(missing))
    if missing:
        out.append(_result(check_name, level,

                           f"{rel_file}: {len(missing)} đường dẫn không tồn tại: " + ", ".join(f"`{t}`" for t in missing)))
    return out


def check_agents_md(root):
    out = []
    f = root / "AGENTS.md"
    lines = f.read_text(encoding="utf-8").splitlines()
    if len(lines) > AGENTS_MD_MAX_LINES:
        out.append(_result("AGENTS_MD", "FAIL",
                           f"AGENTS.md dài {len(lines)} dòng > {AGENTS_MD_MAX_LINES} (luôn được nạp vào context). "
                           f"Chuyển chi tiết sang rules/ và để lại con trỏ"))
    out += _check_paths_in(f, root, "AGENTS_MD", "FAIL")
    if not out:
        out.append(_result("AGENTS_MD", "PASS", f"AGENTS.md {len(lines)} dòng, mọi đường dẫn tham chiếu đều tồn tại"))
    return out


def check_legacy_patterns(root):
    """FAIL-level: Cấm hoàn toàn mọi tàn dư của các thư mục cũ đã bị xóa (00_Draft, 04_Document, 06_Testing...)."""
    out = []
    hits = []
    for p in root.rglob("*.md"):
        if any(x in p.parts for x in [".git", "node_modules", "__pycache__", "Dulieudoanhthu", "brain"]):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        for idx, line in enumerate(text.splitlines(), 1):
            m = RE_LEGACY_PATTERNS.search(line)
            if m:
                rel = p.relative_to(root).as_posix()
                hits.append(f"{rel}:{idx} (tìm thấy `{m.group(0)}`)")
    if hits:
        out.append(_result("LEGACY_PATTERNS", "FAIL",
                           f"Phát hiện {len(hits)} tàn dư đường dẫn cũ cấm kỵ: " + "; ".join(hits[:5]) +
                           (f" ... và {len(hits)-5} vị trí khác" if len(hits) > 5 else "")))
    else:
        out.append(_result("LEGACY_PATTERNS", "PASS", "Không còn tàn dư đường dẫn cũ (00_Draft, 04_Document, 06_Testing, harness/...)"))
    return out


def check_stale_paths(root):
    """WARN-level: đường dẫn chết trong toàn bộ hệ thống harness (rules, personas, workflows, evaluations, definitions...)."""
    out = []
    scan_dirs = [
        root / ".agents" / "rules",
        root / ".agents" / "personas",
        root / ".agents" / "definitions",
        root / ".agents" / "skills",
        root / "workflows",
        root / "evaluations",
        root / "observability",
        root / "templates",
        root / "knowledge",
        root / "references",
        root / "tools",
        root / "scripts",
        root / "plans",
        root / "artifacts"
    ]
    targets = []
    for sd in scan_dirs:
        if sd.exists():
            targets.extend(sd.rglob("*.md"))
    for md in sorted(set(targets)):
        out += _check_paths_in(md, root, "STALE_PATHS", "WARN")
    if not out:
        out.append(_result("STALE_PATHS", "PASS", f"Không có đường dẫn chết trong toàn bộ {len(targets)} tài liệu harness & workflows"))
    return out


def check_harness_map(root):
    """FAIL-level: mọi thư mục gốc (và mọi thư mục con của .agents/) phải thuộc >= 1 harness."""
    cfg = root / ".agents" / "definitions" / "harness-map.json"
    if not cfg.exists():
        return [_result("HARNESS_MAP", "FAIL", ".agents/definitions/harness-map.json không tồn tại (DEC-008)")]
    try:
        data = json.loads(cfg.read_text(encoding="utf-8"))
        harnesses = data["harnesses"]
    except Exception as e:
        return [_result("HARNESS_MAP", "FAIL", f"harness-map.json không hợp lệ: {e!r}")]

    out = []
    keys = set(harnesses)
    if keys != set(HARNESS_KEYS):
        out.append(_result("HARNESS_MAP", "FAIL",
                           f"harness-map.json phải có đúng 7 harness {list(HARNESS_KEYS)}; "
                           f"thiếu {sorted(set(HARNESS_KEYS) - keys)}, thừa {sorted(keys - set(HARNESS_KEYS))}"))
    mapped = set()
    for key, h in harnesses.items():
        paths = h.get("paths") or []
        if not paths:
            out.append(_result("HARNESS_MAP", "FAIL", f"Harness '{key}' không có thư mục nào"))
        for p in paths:
            if not (root / p).exists():
                out.append(_result("HARNESS_MAP", "FAIL", f"Harness '{key}': thư mục `{p}` không tồn tại"))
            mapped.add(p.strip("/"))
        for ev in h.get("evidence") or []:
            if not (root / ev).exists():
                out.append(_result("HARNESS_MAP", "FAIL", f"Harness '{key}': evidence `{ev}` không tồn tại"))

    unmapped = []
    for d in sorted(p for p in root.iterdir() if p.is_dir() and p.name not in IGNORED_TOP_DIRS):
        if d.name == ".agents":
            for sub in sorted(s for s in d.iterdir() if s.is_dir() and s.name not in IGNORED_TOP_DIRS):
                rel = f".agents/{sub.name}"
                if rel not in mapped and ".agents" not in mapped:
                    unmapped.append(rel)
        elif d.name.startswith("."):
            continue  # thư mục ẩn khác (cấu hình IDE/VCS) không thuộc harness
        elif d.name not in mapped:
            unmapped.append(d.name)
    if unmapped:
        out.append(_result("HARNESS_MAP", "FAIL",
                           f"{len(unmapped)} thư mục chưa ánh xạ vào harness nào: " + ", ".join(f"`{u}`" for u in unmapped)
                           + " -> khai báo trong .agents/definitions/harness-map.json"))
    if not out:
        out.append(_result("HARNESS_MAP", "PASS",
                           f"7 harness ánh xạ đủ {len(mapped)} thư mục, mọi evidence tồn tại (DEC-008)"))
    return out


def check_context_size(root):
    """WARN-level: file tri thức quá lớn làm tốn context budget khi agent nạp."""
    kdir = root / "knowledge"
    if not kdir.exists():
        return [_result("CONTEXT_SIZE", "WARN", "knowledge/ không tồn tại")]
    files = list(kdir.rglob("*.md"))
    big = [(f, f.stat().st_size / 1024) for f in files if f.stat().st_size / 1024 > KNOWLEDGE_MAX_KB]
    if big:
        return [_result("CONTEXT_SIZE", "WARN",
                        f"{f.relative_to(root).as_posix()}: {kb:.1f} KB > {KNOWLEDGE_MAX_KB} KB — phân rã thành module + index gateway (xem TD-004)")
                for f, kb in big]
    return [_result("CONTEXT_SIZE", "PASS", f"{len(files)} file tri thức đều ≤ {KNOWLEDGE_MAX_KB} KB")]


def run_checks(root=ROOT):
    results = []
    for fn in (check_rule_links, check_skill_junctions, check_hooks, check_agents_md, check_legacy_patterns,
               check_stale_paths, check_harness_map, check_context_size):
        try:
            results += fn(root)
        except Exception as e:  # một check lỗi không được làm sập cả bộ
            results.append(_result(fn.__name__.upper(), "FAIL", f"Checker crash: {e!r}"))
    return results


def main():
    ap = argparse.ArgumentParser(description="Harness integrity checker")
    ap.add_argument("--json", action="store_true", help="Xuất JSON")
    ap.add_argument("--root", default=str(ROOT))
    args = ap.parse_args()

    results = run_checks(Path(args.root))
    fails = [r for r in results if r["status"] == "FAIL"]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        icon = {"PASS": "✅", "WARN": "⚠️ ", "FAIL": "❌"}
        for r in results:
            print(f"{icon[r['status']]} [{r['check']}] {r['message']}")
        warns = sum(r["status"] == "WARN" for r in results)
        print("-" * 60)
        print(f"Tổng: {len(fails)} FAIL, {warns} WARN")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

