# Try importing telegram notifier safely, fallback if missing
try:
    from notifier import send_telegram_reminder
except ImportError:
    def send_telegram_reminder(msg):
        print(f"[LOG]: Telegram notification skipped: {msg}")
