from fastapi import FastAPI
from sqlmodel import SQLModel
from app.database import engine
from app.routes import todo
from app.config import settings
print("DATABASE_URL:", settings.SQLALCHEMY_DATABASE_URL)

app = FastAPI()

# Create database tables on startup
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# Include To-Do routes
app.include_router(todo.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the To-Do API!"}