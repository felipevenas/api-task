from pydantic import BaseModel

class CreateTask(BaseModel):
    titulo: str
    descricao: str
    user_id: int

class ResponseTask(BaseModel):
    id: int
    titulo: str
    descricao: str
    user_id: int

    class Config:
        orm_mode = True