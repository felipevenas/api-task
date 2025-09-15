from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .task import Task

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100))
    email = Column(String(70), unique=True)
    age = Column(Integer())
    tel = Column(Integer(), unique=True)

    # Um usuário pode ter várias Task:
    tasks = relationship("Task", back_populates="user")