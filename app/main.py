from fastapi import FastAPI

from app.db import init_db
from app.routers import tasks, users

init_db()

app = FastAPI(title="TaskFlow API", version="0.1.0")

app.include_router(tasks.router)
app.include_router(users.router)


@app.get("/health")
def health():
    return {"status": "ok"}
