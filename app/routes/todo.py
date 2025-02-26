from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.database import get_db
from app.models import ToDo

router = APIRouter(prefix="/todos", tags=["todos"])

# Create a new To-Do item
@router.post("/")
async def create_todo(todo: ToDo, db: AsyncSession = Depends(get_db)):
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo

# Get all To-Do items
@router.get("/")
async def get_todos(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ToDo))
    return result.scalars().all()

# Get a single To-Do item by ID
@router.get("/{todo_id}")
async def get_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    todo = await db.get(ToDo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="To-Do not found")
    return todo

# Update a To-Do item
@router.put("/{todo_id}")
async def update_todo(todo_id: int, updated_todo: ToDo, db: AsyncSession = Depends(get_db)):
    todo = await db.get(ToDo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="To-Do not found")
    todo.title = updated_todo.title
    todo.description = updated_todo.description
    todo.completed = updated_todo.completed
    await db.commit()
    await db.refresh(todo)
    return todo

# Delete a To-Do item
@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    todo = await db.get(ToDo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="To-Do not found")
    await db.delete(todo)
    await db.commit()
    return {"message": "To-Do deleted successfully"}