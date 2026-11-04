import mammoth
import os

test_file = r"F:\VIETLOTT-SMS\04_Document\VIETLOTT_SMS\VIETLOTT_SMS\03.Business_Analysis\03.1.DangKy_QLTK\VietlottSMS_ChucNangDangNhap-Web_v1.0_20251128.docx.doc"

# Check file signature
with open(test_file, 'rb') as f:
    header = f.read(4)

is_zip = (header == b'PK\x03\x04')
print(f"File size: {os.path.getsize(test_file)} bytes")
print(f"Is ZIP (docx): {is_zip}")

if is_zip:
    with open(test_file, 'rb') as f:
        result = mammoth.convert_to_html(f)
    print("=== HTML OUTPUT (first 3000 chars) ===")
    print(result.value[:3000])
    print(f"\n=== Total HTML length: {len(result.value)} ===")
    if result.messages:
        print(f"=== Messages ({len(result.messages)}): ===")
        for msg in result.messages[:10]:
            print(f"  - {msg}")
    
    # Also test mammoth markdown conversion
    with open(test_file, 'rb') as f:
        result_md = mammoth.convert_to_markdown(f)
    print("\n=== MARKDOWN OUTPUT (first 3000 chars) ===")
    print(result_md.value[:3000])
    print(f"\n=== Total MD length: {len(result_md.value)} ===")
else:
    print("Not a ZIP-based docx file - this is MHTML format")
    print("Need different approach for this file type")

# Also test a .docx file (true docx)
test_docx = r"F:\VIETLOTT-SMS\04_Document\VIETLOTT_SMS\VIETLOTT_SMS\03.Business_Analysis\03.1.DangKy_QLTK\VietlottSMS_BRD_DieuChinhLuongDangNhap_20241112.docx"
if os.path.exists(test_docx):
    with open(test_docx, 'rb') as f:
        hdr = f.read(4)
    print(f"\n\n=== Testing .docx file ===")
    print(f"File: {os.path.basename(test_docx)}")
    print(f"Is ZIP: {hdr == b'PK' + bytes([3, 4])}")
    
    with open(test_docx, 'rb') as f:
        result2 = mammoth.convert_to_markdown(f)
    print(f"MD length: {len(result2.value)}")
    print("=== MARKDOWN (first 3000 chars) ===")
    print(result2.value[:3000])
