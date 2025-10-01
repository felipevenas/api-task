from app.domain.task.schemas import CreateTask
from app.domain.task.model import Task

from sqlalchemy.orm import Session

# Constutor do UserRepository:
class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task: CreateTask) -> Task:
        db_task = Task(**task.model_dump())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
    
    def find_all(self):
        return self.db.query(Task).all()
    
    def find_by_id(self, task_id: int):
        return self.db.query(Task).filter(Task.id == task_id).first()

    def update_status(self, task_id: int, status: str) -> Task | None:
        db_task = self.find_by_id(task_id)
        if db_task:
            db_task.status = status
            self.db.commit()
            self.db.refresh(db_task)
            return db_task

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
    
    def find_by_user(self, user_id: int):
        tasks = self.db.query(Task).filter(Task.user_id == user_id).all()
        return tasks
