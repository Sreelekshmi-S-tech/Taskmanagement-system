from fastapi import FastAPI
from database import engine, Base
import models

from routers import users, tasks

app = FastAPI()

# Create tables in database
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/")
def home():
    return {"message": "Task Manager API (DB version) running"}