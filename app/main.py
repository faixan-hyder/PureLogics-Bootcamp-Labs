from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

todos_db = []
current_id = 1

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

def find_task(task_id: int):
    for task in todos_db:
        if task["id"] == task_id:
            return task
    return None

@app.post("/todos", response_model=Task)
def create_task(task: TaskCreate):
    global current_id
    new_task = {
        "id": current_id,
        "title": task.title,
        "completed": False
    }
    todos_db.append(new_task)
    current_id += 1
    return new_task

@app.get("/todos", response_model=List[Task])
def get_all_tasks():
    return todos_db

@app.get("/todos/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
    return task

@app.put("/todos/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
    if task_update.title is not None:
        task["title"] = task_update.title
    if task_update.completed is not None:
        task["completed"] = task_update.completed
    return task

@app.delete("/todos/{task_id}")
def delete_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
    todos_db.remove(task)
    return {"message": f"Task with ID {task_id} deleted successfully"}

@app.get("/")
def root():
    return {
        "message": "Welcome to To-Do List API!",
        "docs": "/docs"
    }

@app.post("/reset")
def reset_data():
    """Reset everything - ID 1 se start"""
    global todos_db, current_id
    todos_db = []
    current_id = 1
    return {"message": "Data reset successfully! Now ID will start from 1"}