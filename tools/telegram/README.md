# Telegram Integration Scripts

Script gửi **thông báo một chiều** từ AI qua Telegram. Script không chờ phản hồi và không có chức năng phê duyệt.

> **Lưu ý (DEC-008):** Luồng phê duyệt từ xa (`tele_gateway.py`) đã được gỡ bỏ. Mọi Hard Stop do Human quyết định trực tiếp trong phiên làm việc với agent.

## Setup (Lần đầu)

1. Copy `.env.example` thành `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```

2. Điền thông tin vào `.env`:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```

3. Cài dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Cách Dùng

```powershell
# NOTIFY (không block, exit 0 = gửi thành công, 1 = lỗi)
$env:PYTHONIOENCODING="utf-8"; python "tools/telegram/tele_notify.py" "Nội dung"
```

**Nơi gọi tự động:** `validators/gate_runner.py` gửi cảnh báo escalation khi agent vượt quá 2 vòng sửa tại Quality Gate (DEC-002).

## Lưu Ý Bảo Mật
- File `.env` **KHÔNG** được commit vào git (đã khai báo trong `.gitignore` ở thư mục gốc).
- Chỉ commit `.env.example` làm template.
