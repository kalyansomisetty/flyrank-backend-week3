import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg.connect(DATABASE_URL)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title TEXT,
        done BOOLEAN
    )
""")

cursor.execute("SELECT COUNT(*) FROM tasks")
task_count = cursor.fetchone()[0]

if task_count == 0:
    example_tasks = [
        ("Buy milk", False),
        ("Study FastAPI", False),
        ("Exercise", False)
    ]

    cursor.executemany(
        "INSERT INTO tasks (title, done) VALUES (%s, %s)",
        example_tasks
    )

connection.commit()
