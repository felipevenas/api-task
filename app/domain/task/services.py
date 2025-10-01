from app.domain.task.repository import TaskRepository
from app.domain.task.schemas import CreateTask, DoneTask

# Constutor do UserService
class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, task: CreateTask):
        return self.repository.create_task(task)
    
    def find_all(self):
        return self.repository.find_all()
    
    def find_by_id(self, task_id: int):
        return self.repository.find_by_id(task_id)

    def update_status(self, task_id: int, status: str):
        return self.repository.update_status(task_id, status)

    def update(self, task_id: int, task: CreateTask):
        return self.repository.update(task_id, task)
    
    def delete(self, task_id: int):
        return self.repository.delete(task_id)
    
    def find_by_user(self, user_id: int):
        return self.repository.find_by_user(user_id)
