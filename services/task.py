from models.task import Task
from repositories.task import TaskRepository
from schemas.task import CreateTask

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
        
    def update(self, task_id: int, task: CreateTask):
        return self.repository.update(task_id, task)
    
    def delete(self, task_id: int):
        return self.repository.delete(task_id)
