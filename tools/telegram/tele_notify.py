"""
Telegram Notify Script
Chỉ dùng để AI gửi thông báo (completion, answer) cho Sếp qua Telegram.
Không chờ phản hồi, chạy xong thoát luôn (Exit 0).
"""
import os
import sys
import telebot
from dotenv import load_dotenv
from pathlib import Path

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure') and sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure') and sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def send_notification(message: str):
    load_dotenv()
    _script_dir = Path(__file__).resolve().parent
    _project_root = _script_dir.parents[1]
    load_dotenv(_script_dir / ".env")
    load_dotenv(_project_root / ".env")

    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    AUTHORIZED_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

    if not BOT_TOKEN or not AUTHORIZED_CHAT_ID:
        print("❌ LỖI: Thiếu cấu hình BOT_TOKEN hoặc CHAT_ID trong file .env")
        sys.exit(1)

    bot = telebot.TeleBot(BOT_TOKEN)
    
    # Prefix để Sếp dễ nhận biết
    msg = f"📣 **THÔNG BÁO TỪ AI:**\n\n{message}"
    
    try:
        bot.send_message(AUTHORIZED_CHAT_ID, msg, parse_mode='Markdown')
        print("✅ Đã gửi thông báo qua Telegram thành công!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Lỗi khi gửi Telegram: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Sử dụng: python tele_notify.py \"Nội dung thông báo\"")
        sys.exit(1)
        
    thong_bao = sys.argv[1]
    send_notification(thong_bao)
