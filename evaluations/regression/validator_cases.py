"""
Golden cases cho validators (PII, từ cấm, mơ hồ).

QUY TẮC PII: file này KHÔNG chứa chuỗi PII hoàn chỉnh. Dữ liệu giả được GHÉP lúc chạy
(vd "09" + "12" + "345678") để chính bộ test không vi phạm NĐ 13/2023 và không bị
pii_scanner bắt nhầm khi quét repo. Tất cả số là dữ liệu tổng hợp, không thuộc người thật.

Trường của mỗi case:
  id        : mã duy nhất (giữ ổn định để so lịch sử)
  validator : "pii" | "banned" | "ambiguity" | "secret"
  text      : nội dung file markdown dùng để test
  expect    : "detect" (phải bắt) | "clean" (không được bắt)
  xfail     : (tùy chọn) lý do — đây là LỖ HỔNG ĐÃ BIẾT của validator. Case vẫn chạy;
              nếu validator được sửa và case bắt đầu PASS -> runner báo XPASS để gỡ xfail.
"""

# ---- Dữ liệu tổng hợp, ghép lúc chạy ----
_PHONE = "09" + "12" + "345" + "678"            # định dạng di động VN 10 số
_PHONE_84 = "84" + _PHONE[1:]                   # dạng 84xxxxxxxxx
_PHONE_SPACED = " ".join([_PHONE[:4], _PHONE[4:7], _PHONE[7:]])
_CCCD = "0010" + "99" + "123" + "456"           # 12 số
_OTP = "48" + "39" + "20"
_CARD = " ".join(["9704", "12" + "34", "56" + "78", "90" + "12"])
_FENCE = "`" * 3

# ---- Secret giả (DEC-008), ghép lúc chạy để chính repo không chứa token hoàn chỉnh ----
_TG_TOKEN = "1234567890" + ":" + "AAH" + "k9" * 16           # 10 số : 35 ký tự
_GOOGLE_KEY = "AI" + "za" + "Sy" + "B1c2" * 8 + "x"             # AIza + 35 ký tự
_JIRA_TOKEN = "q7Lm2Xv9" + "Rt4Kp8Wz" + "3Nb6"                 # 20 ký tự trộn chữ số
_PEM_HEADER = "-----BEGIN " + "RSA " + "PRIVATE KEY-----"

CASES = [
    # ---------------- PII ----------------
    {"id": "PII-01", "validator": "pii", "expect": "detect",
     "text": f"Liên hệ khách hàng qua số {_PHONE} để xác nhận."},
    {"id": "PII-02", "validator": "pii", "expect": "clean",
     "text": "Liên hệ khách hàng qua số 091" + "****" + "888 để xác nhận."},
    {"id": "PII-03", "validator": "pii", "expect": "detect",
     "text": f"- **SĐT khách hàng:** {_PHONE}"},
    {"id": "PII-04", "validator": "pii", "expect": "detect",
     "text": f"MSISDN thuê bao: {_PHONE_84}"},
    {"id": "PII-05", "validator": "pii", "expect": "detect",
     "text": f"Số CCCD người chơi: {_CCCD}"},
    {"id": "PII-06", "validator": "pii", "expect": "clean",
     "text": "Số CCCD người chơi: 001099" + "*" * 6},
    {"id": "PII-07", "validator": "pii", "expect": "detect",
     "text": f"Mã OTP: {_OTP}"},
    {"id": "PII-08", "validator": "pii", "expect": "detect",
     "text": f"Số thẻ thanh toán: {_CARD}"},
    {"id": "PII-09", "validator": "pii", "expect": "detect",
     "text": f"Hotline khách: {_PHONE_SPACED}"},

    # ---------------- Từ cấm (banned_words_validator) ----------------
    {"id": "BW-01", "validator": "banned", "expect": "detect",
     "text": "Hệ thống phản hồi nhanh khi người chơi mua vé."},
    {"id": "BW-02", "validator": "banned", "expect": "clean",
     "text": "Hệ thống phản hồi trong vòng 2 giây (p95) khi người chơi mua vé."},
    {"id": "BW-03", "validator": "banned", "expect": "clean",
     "text": f"{_FENCE}text\nlog: phản hồi nhanh\n{_FENCE}\nPhản hồi trong vòng 2 giây."},
    {"id": "BW-04", "validator": "banned", "expect": "detect",
     "text": "Ngưỡng giải lớn: TBD"},
    {"id": "BW-05", "validator": "banned", "expect": "detect",
     "text": "Giao diện thân thiện với người dùng."},
    {"id": "BW-06", "validator": "banned", "expect": "clean",
     "text": "Sơ đồ phân nhánh luồng xử lý đối soát."},
    {"id": "BW-07", "validator": "banned", "expect": "clean",
     "text": "Người chơi phải nhập sai mã PIN ít nhất 3 lần thì tài khoản mới bị khóa."},

    # ---------------- Mơ hồ (ambiguity_scanner) ----------------
    {"id": "AMB-01", "validator": "ambiguity", "expect": "detect",
     "text": "TODO: bổ sung luồng hoàn tiền."},
    {"id": "AMB-02", "validator": "ambiguity", "expect": "clean",
     "text": "Hệ thống hoàn tiền trong vòng 24 giờ kể từ khi nhận mã lỗi 408 từ cổng thanh toán."},
    {"id": "AMB-03", "validator": "ambiguity", "expect": "detect",
     "text": "Chọn cấu hình phù hợp cho máy chủ."},
    {"id": "AMB-04", "validator": "ambiguity", "expect": "clean",
     "text": f"{_FENCE}python\n# TODO trong code mẫu\n{_FENCE}\nHoàn tiền trong vòng 24 giờ."},

    # ---------------- Secret (secret_scanner, DEC-008) ----------------
    {"id": "SEC-01", "validator": "secret", "expect": "detect",
     "text": f"Bot cảnh báo dùng token {_TG_TOKEN} để gửi tin."},
    {"id": "SEC-02", "validator": "secret", "expect": "detect",
     "text": f"Gọi Gemini với key {_GOOGLE_KEY}"},
    {"id": "SEC-03", "validator": "secret", "expect": "clean",
     "text": "TELEGRAM_BOT_TOKEN=your_bot_token\nTELEGRAM_CHAT_ID=your_chat_id"},
    {"id": "SEC-04", "validator": "secret", "expect": "detect",
     "text": f"JIRA_API_TOKEN={_JIRA_TOKEN}"},
    {"id": "SEC-05", "validator": "secret", "expect": "clean",
     "text": "BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')"},
    {"id": "SEC-06", "validator": "secret", "expect": "detect",
     "text": f"{_PEM_HEADER}\nMIIEow..."},
    {"id": "SEC-07", "validator": "secret", "expect": "clean",
     "text": "Token Telegram có dạng <bot_id>:<hash>; key Google bắt đầu bằng AIza********."},
]
