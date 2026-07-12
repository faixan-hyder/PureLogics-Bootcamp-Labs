# To-Do List API

A simple REST API for managing daily tasks. Built with **FastAPI** and **Python**.

---

## Features

- Add new tasks
- View all tasks
- View specific task by ID
- Update task (title and status)
- Delete task
- Automatic API documentation (Swagger UI)

---

## Tech Stack

- **FastAPI** - Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Python** - Programming language

---

## Task Structure

Each task has the following fields:

```json
{
  "id": 1,
  "title": "I am Faizan Haider.",
  "completed": false
}