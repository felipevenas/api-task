from pydantic import BaseModel
from models.task import Task
from typing import List ,Optional

class User(BaseModel):
    name: str
    email: str
    age: int
    tel: int
    tasks: Optional[List[Task]] = []