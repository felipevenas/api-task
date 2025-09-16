from app.db.base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..task.model import Task

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(100))
    email = Column(String(70), nullable=False)
    senha = Column(String(100), nullable=False)
    login = Column(String(100), nullable=False)
    grupo = Column(String(30), nullable=False)
    telefone = Column(String(30), nullable=False)
    cargo = Column(String(50))
    setor = Column(String(50))
    ativo = Column(String(20))

    # Um usuário pode ter várias Task:
    tasks = relationship("Task", back_populates="user")