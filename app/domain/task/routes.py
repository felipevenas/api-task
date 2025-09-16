from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.domain.task.repository import TaskRepository
from app.domain.task.schemas import CreateTask, ResponseTask
from app.domain.task.services import TaskService

task_router = APIRouter()

def get_task_service(db: Session = Depends(get_db)):
    repository = TaskRepository(db)
    return TaskService(repository)

# Inserir novo usuário:
@task_router.post('/task', response_model=ResponseTask)
def create_task(task: CreateTask, service: TaskService = Depends(get_task_service)):
    return service.create_task(task)

# Buscar todos os usuários:
@task_router.get('/tasks', response_model=list[ResponseTask])
def find_all(service: TaskService = Depends(get_task_service)):
    return service.find_all()

# Buscar usuário por ID:
@task_router.get('/task/{task_id}', response_model=ResponseTask)
def find_by_id(task_id: int, service: TaskService = Depends(get_task_service)):
    user = service.find_by_id(task_id)
    if not user:
        raise HTTPException(status_code=404, detail="Tarefa não encontrado!")
    return user

# Alterar dados de usuário:
@task_router.put('/task/{task_id}', response_model=ResponseTask)
def update(task: CreateTask, task_id: int, service: TaskService = Depends(get_task_service)):
    user = service.update(task_id, task)
    if not user:
        raise HTTPException(status_code=404, detail="Nenhuma tarefa foi encontrada!")
    return user

# Deletar usuários por ID:
@task_router.delete('/task/{task_id}', response_model=ResponseTask)
def delete(task_id: int, service: TaskService = Depends(get_task_service)):
    user = service.delete(task_id)
    if not user:
        raise HTTPException(status_code=404, detail="Tarefa não encontradas!")
    return user