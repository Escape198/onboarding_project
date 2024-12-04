from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User, Analytics


router = APIRouter(prefix="/onboarding", tags=["Onboarding"])


class StartOnboardingRequest(BaseModel):
    user_name: str


class CompleteStepRequest(BaseModel):
    user_id: int
    step: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/start")
def start_onboarding(request: StartOnboardingRequest, db: Session = Depends(get_db)):
    user = User(name=request.user_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": f"User {user.name} started onboarding!", "user_id": user.id}


@router.post("/complete-step")
def complete_step(request: CompleteStepRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == request.user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    analytics = Analytics(user_id=request.user_id, step=request.step)
    db.add(analytics)
    db.commit()

    if request.step == "step-3":
        user.completed = True
        db.commit()
    return {"message": f"Step {request.step} completed for user {request.user_id}!"}
