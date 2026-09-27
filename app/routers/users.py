import sqlite3

from fastapi import APIRouter, Depends, HTTPException

from app.db import get_db
from app.schemas import UserCreate, UserOut

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserOut, status_code=201)
def create_user(payload: UserCreate, db: sqlite3.Connection = Depends(get_db)):
    try:
        cur = db.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (payload.name, payload.email),
        )
        db.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Email already registered")
    row = db.execute("SELECT * FROM users WHERE id = ?", (cur.lastrowid,)).fetchone()
    return UserOut(id=row["id"], name=row["name"], email=row["email"])


@router.get("", response_model=list[UserOut])
def list_users(db: sqlite3.Connection = Depends(get_db)):
    rows = db.execute("SELECT * FROM users ORDER BY id").fetchall()
    return [UserOut(id=r["id"], name=r["name"], email=r["email"]) for r in rows]
