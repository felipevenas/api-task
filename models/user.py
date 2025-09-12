from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    idade: int
    tel: int