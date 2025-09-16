from app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(100))
    description = Column(String(200))
    checkbox = Column(Boolean, default=False)

    # Chave estrangeira que aponta para User.ID:
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relacionamento: Cada Task pertence a UM usuário:
    user = relationship("User", back_populates="tasks")