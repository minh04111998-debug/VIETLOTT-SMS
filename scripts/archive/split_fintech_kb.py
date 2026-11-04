import os
import re
from pathlib import Path

source_file = Path("knowledge/product/fintech-knowledge-base.md")
dest_dir = Path("knowledge/product/fintech")
dest_dir.mkdir(parents=True, exist_ok=True)

with open(source_file, "r", encoding="utf-8") as f:
    text = f.read()
lines = text.splitlines()

# Section line markers (0-indexed)
# 28: Section 1 (idx 27)
# 74: Section 2 (idx 73)
# 161: Section 3 (idx 160)
# 280: Section 4 (idx 279)
# 336: Section 5 (idx 335)
# 390: Section 6 (idx 389)
# 433: Section 7 (idx 432)
# 470: Section 8 (idx 469)
# 530: Section 9 (idx 529)
# 563: Section 10 (idx 562)
# 644: Section 11 (idx 643)

header_template = """# {title}

| Version | Ngày | Người thực hiện | Trạng thái |
|:---:|:---:|:---:|---|
| 1.0 | 2026-10-08 | BA / Fintech Knowledge Team | Approved |

> **Mã module:** `{code}`  
> **Thuộc hệ thống:** Kiến trúc Tri thức Fintech Vietlott SMS  
> **Master Index:** [fintech-knowledge-base.md](file:///f:/VIETLOTT-SMS/knowledge/product/fintech-knowledge-base.md)

---

"""

# Module 1: Ecosystem & Agency Model
m1_content = header_template.format(title="Fintech Knowledge: Hệ Sinh Thái & Mô Hình Đại Lý", code="KB-FINTECH-01")
m1_content += "\n".join(lines[27:73]) + "\n\n---\n\n" + "\n".join(lines[469:529]) + "\n\n---\n\n" + "\n".join(lines[643:])
(dest_dir / "01-ecosystem-overview.md").write_text(m1_content, encoding="utf-8")

# Module 2: Payment Methods & Integrated Channels
m2_content = header_template.format(title="Fintech Knowledge: Mô Hình & Kênh Thanh Toán Tích Hợp", code="KB-FINTECH-02")
m2_content += "\n".join(lines[73:279])
(dest_dir / "02-payment-methods.md").write_text(m2_content, encoding="utf-8")

# Module 3: Reconciliation & Settlement
m3_content = header_template.format(title="Fintech Knowledge: Đối Soát Giao Dịch & Quyết Toán (Reconciliation)", code="KB-FINTECH-03")
m3_content += "\n".join(lines[279:335])
(dest_dir / "03-reconciliation-settlement.md").write_text(m3_content, encoding="utf-8")

# Module 4: Disbursement & Prize Payout
m4_content = header_template.format(title="Fintech Knowledge: Trả Thưởng & Chi Hộ (Disbursement)", code="KB-FINTECH-04")
m4_content += "\n".join(lines[335:389])
(dest_dir / "04-disbursement-rules.md").write_text(m4_content, encoding="utf-8")

# Module 5: eKYC, Compliance & Technical Patterns
m5_content = header_template.format(title="Fintech Knowledge: eKYC, Tuân Thủ Pháp Luật & Architecture Patterns", code="KB-FINTECH-05")
m5_content += "\n".join(lines[389:469]) + "\n\n---\n\n" + "\n".join(lines[529:643])
(dest_dir / "05-ekyc-compliance.md").write_text(m5_content, encoding="utf-8")

print("Created 5 modular knowledge documents in knowledge/product/fintech/")
