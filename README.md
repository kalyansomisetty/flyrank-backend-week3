# 🚀 FlyRank Backend Track - Week 2

## Task API (CRUD) using FastAPI

This project is a simple backend application built using FastAPI that demonstrates full CRUD (Create, Read, Update, Delete) operations on a Task resource.

It covers core backend concepts such as:
- REST API design
- HTTP methods (GET, POST, PUT, DELETE)
- Request validation using Pydantic
- Proper status codes
- API documentation using Swagger UI

---

## 📦 Installation & Run

### Run the project (one command)

```bash
uvicorn main:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

| Method | Endpoint | Description | Status Codes |
|--------|----------|------------|--------------|
| GET | `/` | API information | 200 |
| GET | `/health` | Health check | 200 |
| GET | `/tasks` | Get all tasks | 200 |
| GET | `/tasks/{task_id}` | Get task by ID | 200, 404 |
| POST | `/tasks` | Create new task | 201, 400, 422 |
| PUT | `/tasks/{task_id}` | Update task | 200, 400, 404, 422 |
| DELETE | `/tasks/{task_id}` | Delete task | 204, 404 |

---

## 🔧 Example curl Request

### Create Task

```bash
curl -i -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title": "Learn FastAPI"}'
```

### Example Response

```
HTTP/1.1 201 Created
content-type: application/json

{
  "id": 4,
  "title": "Learn FastAPI",
  "done": false
}
```

---

## 📖 Swagger Documentation

FastAPI provides interactive API documentation automatically.

Open:

```
http://127.0.0.1:8000/docs
```

### Screenshot

![Swagger Docs](image.png)

---

## 🧠 Key Learnings

- CRUD operations using REST APIs
- Request body validation using Pydantic models
- Difference between 400, 404, 422 status codes
- Proper API design principles
- Testing APIs using curl and Swagger
- Structuring backend projects
- Version control using Git & GitHub

---

## ⚙️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- Git & GitHub

---

## 👤 Author

Venkata Naga Sri Kalyan Somisetty  
FlyRank Backend Engineer Track - Week 2