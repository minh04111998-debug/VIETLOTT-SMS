#!/usr/bin/env python3
import argparse
import sys
import os
import json
import subprocess
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

# Mapping role to their automated scripts based on quality-gate-runner.md
COMMON_SAFETY = ["pii_scanner.py", "secret_scanner.py", "banned_words_validator.py"]

ROLE_SCRIPTS = {
    "BA": COMMON_SAFETY + ["ambiguity_scanner.py", "traceability_checker.py"],
    "PO": COMMON_SAFETY + ["ambiguity_scanner.py", "doc_structure_validator.py"],
    "PM": COMMON_SAFETY + ["doc_structure_validator.py"],
    "DEV": COMMON_SAFETY + ["doc_structure_validator.py"],
    "QA": COMMON_SAFETY + ["doc_structure_validator.py"],
    "DA": COMMON_SAFETY + ["doc_structure_validator.py"],
    "Designer": COMMON_SAFETY + ["doc_structure_validator.py"]
}

DEFAULT_PROJECT_ROOT = str(Path(__file__).resolve().parents[1])

STATE_FILE = Path(__file__).parent / ".gate_state.json"
MAX_RETRY = 2

def load_state():
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_state(state):
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2)

def run_script(script_name, target_file, project_path):
    script_path = Path(__file__).parent / script_name
    if not script_path.exists():
        return False, f"Script not found: {script_name}"
    
    cmd = [sys.executable, str(script_path)]
    
    if script_name == "traceability_checker.py":
        cmd.extend(["--project-path", str(project_path)])
    else:
        cmd.extend(["--file", str(target_file)])
        
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', check=False)
        # We assume if script outputs "❌" or "⚠️", there are issues
        output = result.stdout + result.stderr
        if "❌" in output or "⚠️" in output:
            return False, output
        return True, output
    except Exception as e:
        return False, str(e)

def main():
    parser = argparse.ArgumentParser(description="Quality Gate Runner Orchestrator")
    parser.add_argument("--role", required=True, choices=ROLE_SCRIPTS.keys(), help="The role of the agent")
    parser.add_argument("--file", required=True, help="The draft file to check")
    parser.add_argument("--project", default=DEFAULT_PROJECT_ROOT, help="Project root path")
    parser.add_argument("--reset", action="store_true", help="Reset the loop counter for this file")
    parser.add_argument("--budget-limit", type=int, default=50000, help="Token budget limit (approx)")
    
    args = parser.parse_args()
    file_key = str(Path(args.file).resolve())
    
    state = load_state()
    
    if args.reset:
        if file_key in state:
            del state[file_key]
            save_state(state)
            print(f"✅ Reset loop counter for {args.file}")
        sys.exit(0)
        
    # Get current loop count
    current_loop = state.get(file_key, 0) + 1
    
    # Token counting estimation (word count * 1.3)
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
            word_count = len(content.split())
            estimated_tokens = int(word_count * 1.3)
            if estimated_tokens > args.budget_limit * 0.8:
                print(f"> [!WARNING] Context Budget 80% — recommend Drop Context (Estimated: {estimated_tokens} tokens)")
    except Exception as e:
        pass
        
    if current_loop > MAX_RETRY:
        msg = f"🔴 CẢNH BÁO ESCALATION\nAgent bị kẹt tại Quality Gate sau {MAX_RETRY} vòng lặp.\nFile: {args.file}\nRole: {args.role}\nCần sự can thiệp của Human."
        print(f"> [!CAUTION] Cảnh Báo Vòng Lặp Vô Hạn")
        print(f"🛑 ESCALATION: Đã vượt quá {MAX_RETRY} vòng lặp cho file {args.file}.")
        print("Agent MUST STOP and request human intervention.")
        
        # Trigger Telegram Notify
        tele_script = Path(__file__).resolve().parents[1] / "tools" / "telegram" / "tele_notify.py"
        if tele_script.exists():
            subprocess.run([sys.executable, str(tele_script), msg], check=False)
            
        sys.exit(1) # Hard stop

    scripts_to_run = ROLE_SCRIPTS.get(args.role, [])
    if not scripts_to_run:
        print(json.dumps({
            "status": "PASS",
            "loop_count": current_loop,
            "message": "No automated scripts for this role. Please perform manual checklist review."
        }, ensure_ascii=False))
        sys.exit(0)
        
    failures = []
    logs = []
    
    for script in scripts_to_run:
        passed, output = run_script(script, args.file, args.project)
        logs.append(f"--- Output of {script} ---\n{output}")
        if not passed:
            failures.append(script)
            
    if failures:
        # Save incremented loop count
        state[file_key] = current_loop
        save_state(state)
        
        print(f"❌ QUALITY GATE FAILED (Loop {current_loop}/{MAX_RETRY})")
        print(f"Failed scripts: {', '.join(failures)}")
        print("\n".join(logs))
        print(f"\nAI ACTION REQUIRED: Please fix the issues and run this gate again.")
        sys.exit(2) # Return non-zero to indicate failure but not escalation yet
    else:
        # Passed, reset loop count
        if file_key in state:
            del state[file_key]
            save_state(state)
            
        print(json.dumps({
            "status": "PASS",
            "loop_count": current_loop,
            "message": "All quality gate scripts passed."
        }, ensure_ascii=False))
        sys.exit(0)

if __name__ == "__main__":
    main()
