from pydantic import BaseModel

class CreateTask(BaseModel):
    title: str
<<<<<<< HEAD
    description: str
    checkbox: bool
    user_id: int
=======
    description:str
    checkbox: bool
>>>>>>> cb0e5b90397ae64b2c927d15119aa22885b9f4c8

class ResponseTask(BaseModel):
    id: int
    title: str
    description:str
    checkbox: bool

class Config:
    from_attributes = True