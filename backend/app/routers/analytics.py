from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User


router = APIRouter(prefix="/analytics", tags=["Analytics"])


def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()


@router.get("/completed-users")
def get_completed_users(db: Session = Depends(get_db)):
    completed_count = db.query(User).filter(User.completed == True).count()
    return {"completed_users": completed_count}
