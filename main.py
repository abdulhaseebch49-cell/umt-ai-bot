import os, json, logging
from bot_scraper import fetch_umt_portal_data
from ai_solver import generate_assignment_solution
from pdf_generator import create_solution_pdf
from notifier import send_telegram_reminder
logging.basicConfig(level=logging.INFO)
def run_automation():
    tasks = fetch_umt_portal_data(os.getenv("UMT_USERNAME", "id"), os.getenv("UMT_PASSWORD", "pass"))
    os.makedirs("docs", exist_ok=True)
    dashboard_tasks = []
    for task in tasks:
        send_telegram_reminder(f"🔔 *UMT Alert* - {task['course']} : {task['title']}")
        pdf_path = f"docs/{task['id']}_Solution.pdf"
        if task['type'] == "Assignment":
            create_solution_pdf(task, generate_assignment_solution(task), pdf_path)
        dashboard_tasks.append({**task, "status": "Processed", "pdf_link": f"{task['id']}_Solution.pdf"})
    json.dump(dashboard_tasks, open("docs/tasks.json", "w"), indent=2)
if __name__ == "__main__": run_automation()
