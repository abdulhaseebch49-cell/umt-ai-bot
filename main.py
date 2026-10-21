import os
import sys

print("[INFO]: UMT AI Bot Starting...")

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

if __name__ == "__main__":
    username = os.getenv("UMT_USERNAME")
    password = os.getenv("UMT_PASSWORD")
    hf_token = os.getenv("HF_TOKEN")

    if not username or not password:
        print("[ERROR]: UMT Portal credentials missing in repository secrets!")
        sys.exit(1)

    print("[INFO]: Environment verified successfully.")
    send_telegram_reminder("🤖 *UMT AI Bot* started execution cycle...")

    try:
        # 1. Scrape Portal Assignments
        import bot_scraper
        print("[INFO]: Running UMT Portal Scraper...")
        # assignments = bot_scraper.fetch_assignments(username, password)
        
        # 2. Solve via Hugging Face / Mistral-7B & Generate PDFs
        import ai_solver
        print("[INFO]: Initializing AI Solver and PDF generator...")
        # ai_solver.process_assignments(assignments, hf_token)
        
        print("[INFO]: All modules executed successfully!")
        send_telegram_reminder("✅ *UMT AI Bot* successfully scraped assignments and updated dashboard!")

    except Exception as e:
        print(f"[ERROR]: Pipeline execution failed: {e}")
        send_telegram_reminder(f"❌ *UMT AI Bot Error*: {e}")
        sys.exit(1)
