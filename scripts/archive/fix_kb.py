import sys
lines = open(r"f:\VIETLOTT-SMS\04_Document\fintech-knowledge-base.md", "r", encoding="utf-8").readlines()
s6 = next(i for i, l in enumerate(lines) if "## 6. eKYC" in l)
clean = lines[:388] + ["\n"] + lines[s6:]
open(r"f:\VIETLOTT-SMS\04_Document\fintech-knowledge-base.md", "w", encoding="utf-8").writelines(clean)
print(f"Done! {len(lines)} -> {len(clean)} lines (removed {len(lines)-len(clean)})")
