from pydantic import BaseModel

class JobCreate(BaseModel):
    name: str

class JobUpdate(BaseModel):
    name: str | None = None
    status: str | None = None

class JobResponse(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        from_attributes = True