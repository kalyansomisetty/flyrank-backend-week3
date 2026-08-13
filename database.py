import sqlite3

connection = sqlite3.connect('tasks.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
            )''')

cursor.execute("SELECT COUNT(*) FROM tasks")
task_count = cursor.fetchone()[0]

if task_count == 0:
    example_tasks = [
        ("Buy milk",),
        ("Study FastAPI",),
        ("Exercise",)
    ]
    cursor.executemany("INSERT INTO tasks (title) VALUES (?)", example_tasks)

connection.commit() 