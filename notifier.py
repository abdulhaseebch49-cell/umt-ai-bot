import os, requests

def send_telegram_reminder(message):
    bot_token, chat_id = os.getenv("TELEGRAM_BOT_TOKEN"), os.getenv("TELEGRAM_CHAT_ID")
    if bot_token and chat_id:
        requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", json={"chat_id": chat_id, "text": message})
    else:
        print(f"[REMINDER]: {message}")
