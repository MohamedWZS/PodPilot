from fastapi import FastAPI
from app.routes import jobs

app = FastAPI()

app.include_router(jobs.router)

@app.get("/")
def root():
    return {"message": "PodPilot is running 🚀"}