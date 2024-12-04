from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import onboarding, analytics
from app.database import create_tables

app = FastAPI(title="Onboarding Funnel")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(onboarding.router)
app.include_router(analytics.router)


@app.on_event("startup")
async def startup_event():
    create_tables()


@app.get("/")
def read_root():
    return {"message": "Welcome to the onboarding funnel API!"}