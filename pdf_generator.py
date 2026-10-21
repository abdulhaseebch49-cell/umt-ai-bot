import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_solution_pdf(task_data, solution_text, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Title & Course Header
    c.setFont("Helvetica-Bold", 14)
    c.drawString(54, height - 54, f"Course: {task_data['course']}")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(54, height - 80, f"Task: {task_data['title']}")

    # Body Content
    c.setFont("Helvetica", 10)
    text_object = c.beginText(54, height - 110)
    text_object.setFont("Helvetica", 10)

    for line in solution_text.split("\n"):
        if text_object.getY() < 50:
            c.drawText(text_object)
            c.showPage()
            text_object = c.beginText(54, height - 54)
        text_object.textLine(line[:90])  # Wrap line width limit

    c.drawText(text_object)
    c.save()
    print(f"PDF Generated Successfully: {output_path}")
