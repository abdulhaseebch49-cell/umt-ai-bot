import os
import requests

def send_telegram_reminder(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    # Agar tokens set nahi hain ya dummy hain, toh crash karne ke bajaye skip kar do
    if not bot_token or not chat_id or bot_token.lower() == "dummy":
        print("[INFO]: Telegram credentials not provided or set to dummy. Skipping notification.")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("[INFO]: Telegram notification sent successfully!")
        else:
            print(f"[WARNING]: Failed to send Telegram message: {response.text}")
    except Exception as e:
        print(f"[ERROR]: Telegram API Error: {e}")
