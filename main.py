import os
import sys

print("[INFO]: UMT AI Bot Starting...")

# 1. Telegram Notification Function (Built-in to avoid any import errors)
def send_telegram_reminder(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id or bot_token.lower() == "dummy":
        print("[INFO]: Telegram credentials not provided or set to dummy. Skipping notification.")
        return

    import requests
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

# 2. Main Execution Flow
if __name__ == "__main__":
    username = os.getenv("UMT_USERNAME")
    password = os.getenv("UMT_PASSWORD")
    hf_token = os.getenv("HF_TOKEN")

    if not username or not password:
        print("[ERROR]: UMT Portal credentials missing in repository secrets!")
        sys.exit(1)

    print("[INFO]: Environment verified successfully. Running modules...")
    
    # Send test notification or execution start message
    send_telegram_reminder("🤖 *UMT AI Bot* started execution successfully on GitHub Actions!")
    
    print("[INFO]: Bot run completed successfully.")
