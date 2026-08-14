from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import database

app = FastAPI()

#Request body model
class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    done: bool

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Study FastAPI", "done": True},
    {"id": 3, "title": "Exercise", "done": False}
]


@app.get("/", summary="API Home", description="Returns basic information about the API")
def home():
    return {"name": "Task API",
            "Version": "1.0",
            "endpoints": ["tasks"]}

@app.get("/health")
def health():
    return {"status": "ok"}

#GET all tasks
@app.get("/tasks", summary="Get all tasks", description="Returns a list of all tasks")
def get_tasks():
    database.cursor.execute("SELECT * FROM tasks")
    tasks = database.cursor.fetchall()

    task_list = []
    for row in tasks:
        task_list.append({"id": row[0],"title": row[1], "done": bool(row[2])} )
    return task_list

#GET single task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    database.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = database.cursor.fetchone()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": task[0], "title": task[1], "done": bool(task[2])}

#POST new task
@app.post("/tasks", status_code=201, summary="Create a new task", description="Creates a new task with the provided title")
def create_task(task: TaskCreate):

    if task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Title cannot be empty")

    database.cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (task.title, 0))
    database.connection.commit()

    new_task = {
        "id" : database.cursor.lastrowid,
        "title": task.title,
        "done": False
    }
    return new_task

#PUT update task
@app.put("/tasks/{task_id}", summary="Update a task", description="Updates the title and done status of an existing task")
def update_task(task_id: int, updated_task: TaskUpdate):

    for task in tasks:
        if task["id"] == task_id:

            if updated_task.title.strip() == "":
                raise HTTPException(status_code=400, detail="Title cannot be empty")
            
            task["title"] = updated_task.title
            task["done"] = updated_task.done

            return task
        
    raise HTTPException(status_code=404, detail="Task not found")

#DELETE task
@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task", description="Deletes an existing task")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return
        
    raise HTTPException(status_code=404, detail="Task not found")