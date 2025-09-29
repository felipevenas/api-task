from pydantic import BaseModel

class CreateTask(BaseModel):
    title: str
    description: str

class ResponseTask(BaseModel):
    id: int
    title: str
    description:str
    owner_id: int

    class Config:
        orm_mode = True