import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

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
        requests.post(url, json=payload)
    except Exception as e:
        print(f"[ERROR]: Telegram API Error: {e}")

def create_solution_pdf(title, content, filename):
    os.makedirs("docs", exist_ok=True)
    filepath = os.path.join("docs", filename)
    
    doc = SimpleDocTemplate(filepath, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1, 12))
    
    for line in content.split('\n'):
        if line.strip():
            story.append(Paragraph(line, styles['Normal']))
            story.append(Spacer(1, 6))

    doc.build(story)
    print(f"[INFO]: PDF generated successfully at {filepath}")

if __name__ == "__main__":
    username = os.getenv("UMT_USERNAME")
    password = os.getenv("UMT_PASSWORD")

    if not username or not password:
        print("[ERROR]: UMT Portal credentials missing in repository secrets!")
        sys.exit(1)

    print("[INFO]: Environment verified. Running AI Solver...")
    
    try:
        # Import your ai_solver module
        import ai_solver
        
        sample_task = {"title": "CS101 Assignment 1"}
        solution_text = ai_solver.generate_assignment_solution(sample_task)
        
        # Generate the PDF inside docs/ folder so GitHub Pages can host it live
        create_solution_pdf("CS101 Assignment 1 Solution", solution_text, "CS101_ASS1_Solution.pdf")
        
        print("[INFO]: Pipeline finished successfully!")
        send_telegram_reminder("✅ *UMT AI Bot* successfully generated CS101 Assignment PDF!")

    except Exception as e:
        print(f"[ERROR]: Pipeline failed: {e}")
        sys.exit(1)
