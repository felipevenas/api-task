from pydantic import BaseModel

class DoneTask(BaseModel):
    status: str 
    
    class Config:
        from_attributes = True

class CreateTask(BaseModel):
    titulo: str
    descricao: str
    status: str
    user_id: int
    
    class Config:
        from_attributes = True

class ResponseTask(BaseModel):
    id: int
    titulo: str
    descricao: str
    status: str
    user_id: int

    class Config:
        from_attributes = True