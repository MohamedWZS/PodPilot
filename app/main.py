from fastapi import FastAPI
from app.routes import jobs
from app.database import engine, Base
import app.models

app = FastAPI()

# creates table in PostgreSQL
Base.metadata.create_all(bind=engine)

app.include_router(jobs.router)

@app.get("/")
def root():
    return {"message": "PodPilot is running 🚀"}