from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str
    email:str
    age: int
    tel: int

class ResponseUser(BaseModel):
    id: int
    name: str
    email:str
    age: int
    tel: int

    class Config:
        from_attributes = True