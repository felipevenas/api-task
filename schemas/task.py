from pydantic import BaseModel

class CreateTask(BaseModel):
    title: str
    description:str
    checkbox: bool

class ResponseTask(BaseModel):
    id: int
    title: str
    description:str
    checkbox: bool

class Config:
    from_attributes = True