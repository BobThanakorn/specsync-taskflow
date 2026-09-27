from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.db import init_db
from app.routers import tasks, users

init_db()

app = FastAPI(title="TaskFlow API", version="0.1.0")

app.include_router(tasks.router)
app.include_router(users.router)


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=422, content={"detail": str(exc)})


@app.get("/health")
def health():
    return {"status": "ok"}
