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


class BaseService:
    def __init__(self, db: Session):
        self.db = db


class OnboardingService(BaseService):
    def create_user(self, user_name: str) -> User:
        user = User(name=user_name)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def log_step(self, user_id: int, step: str) -> Analytics:
        analytics = Analytics(user_id=user_id, step=step)
        self.db.add(analytics)
        self.db.commit()
        return analytics

    def mark_user_as_completed(self, user: User):
        user.completed = True
        self.db.commit()


@router.post("/start")
def start_onboarding(request: StartOnboardingRequest, db: Session = Depends(get_db)):
    service = OnboardingService(db)
    user = service.create_user(request.user_name)
    return {"message": f"User {user.name} started onboarding!", "user_id": user.id}


@router.post("/complete-step")
def complete_step(request: CompleteStepRequest, db: Session = Depends(get_db)):
    service = OnboardingService(db)

    user = service.get_user_by_id(request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    service.log_step(request.user_id, request.step)

    if request.step == "step-3":
        service.mark_user_as_completed(user)

    return {"message": f"Step {request.step} completed for user {request.user_id}!"}
