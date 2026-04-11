from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app import models, schemas
from app.database import get_db

router = APIRouter()


@router.post("/jobs", response_model=schemas.JobResponse)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = models.Job(name=job.name)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/jobs", response_model=list[schemas.JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    result = db.execute(select(models.Job))
    jobs = result.scalars().all()
    return jobs

@router.get("/jobs/{job_id}", response_model=schemas.JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    result = db.execute(select(models.Job).where(models.Job.id == job_id))
    job = result.scalars().first()
    return job

@router.put("/jobs/{job_id}", response_model=schemas.JobResponse)
def update_job(job_id: int, job_update: schemas.JobUpdate, db: Session = Depends(get_db)):
    result = db.execute(select(models.Job).where(models.Job.id == job_id))
    job = result.scalars().first()

    if not job:
        raise HTTPException(status_code=404, detail="job not found")

    if job_update.name is not None:
        job.name = job_update.name

    if job_update.status is not None:
        job.status = job_update.status
    
    db.commit()
    db.refresh(job)
    
    return job

@router.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    result = db.execute(select(models.Job).where(models.Job.id == job_id))
    job = result.scalars().first()

    if not job:
        raise HTTPException(status_code=404, detail="job not found")

    db.delete(job)
    db.commit()

    return {"message": "job deleted successfully"}