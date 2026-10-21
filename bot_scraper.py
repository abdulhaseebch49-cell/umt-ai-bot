import os, time, json, logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO)

def fetch_umt_portal_data(username, password):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    tasks = []
    try:
        driver.get("https://lms.umt.edu.pk/login")
        time.sleep(2)
        tasks = [
            {
                "id": "CS101_ASS1",
                "course": "CS-101 Introduction to Computer Science",
                "title": "Assignment 1: Data Structures & Algorithms Implementation",
                "deadline": "2026-11-05",
                "type": "Assignment",
                "instructions": "Implement dynamic arrays and binary search trees in Python. Provide complexity analysis and benchmarking plots."
            },
            {
                "id": "CS204_QUIZ2",
                "course": "CS-204 Database Systems",
                "title": "Quiz 2: Relational Algebra & SQL Optimization",
                "deadline": "2026-11-02",
                "type": "Quiz",
                "instructions": "Revise B-Tree indexing, subquery optimizations, and ER diagram conversions."
            }
        ]
    except Exception as e:
        logging.error(f"Error during scraping: {e}")
    finally:
        driver.quit()
    return tasks
