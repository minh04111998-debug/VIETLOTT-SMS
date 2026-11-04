#!/usr/bin/env python3
"""Backward-compatible wrapper forwarding to scripts/extractors/extract_docx.py"""
import subprocess
import sys
from pathlib import Path

target = Path(__file__).parent / "extractors" / "extract_docx.py"
sys.exit(subprocess.call([sys.executable, str(target)] + sys.argv[1:]))
