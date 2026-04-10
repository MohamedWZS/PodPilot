from fastapi import APIRouter

router = APIRouter()

jobs = []

@router.post("/jobs")
def create_job(name: str):
    job = {
        "id": len(jobs) + 1,
        "name": name,
        "status": "pending"
    }
    jobs.append(job)

@router.get("/jobs")
def get_jobs():
    return jobs