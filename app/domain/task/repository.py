from app.domain.task.schemas import CreateTask
from app.domain.task.model import Task
from sqlalchemy.orm import Session

# Constutor do UserRepository:
class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, user: CreateTask) -> Task:
        db_task = Task(**user.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
    
    def find_all(self):
        return self.db.query(Task).all()
    
    def find_by_id(self, task_id: int):
        return self.db.query(Task).filter(Task.id == task_id).first()
    
    def update(self, task_id: int, task: CreateTask) -> Task:
        db_task = self.find_by_id(task_id)
        if not db_task:
            return None
        for key, value in task.dict().items():
            setattr(db_task, key, value)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def delete(self, task_id: int):
        db_task = self.find_by_id(task_id)
        if not db_task:
            return None
        self.db.delete(db_task)
        self.db.commit()
        return db_task
    
    
