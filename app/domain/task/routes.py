from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.domain.user.model import User
from app.domain.task.repository import TaskRepository
from app.domain.task.schemas import CreateTask, ResponseTask, DoneTask
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

@task_router.get('/tasks/user/{user_id}', response_model=list[ResponseTask])
def find_by_user(user_id: int, service: TaskService = Depends(get_task_service)):
    tasks = service.find_by_user(user_id)
    if not tasks:
        raise HTTPException(status_code=404, detail="Tarefas não encontradas!")
    return tasks

# Buscar usuário por ID:
@task_router.get('/task/{task_id}', response_model=ResponseTask)
def find_by_id(task_id: int, service: TaskService = Depends(get_task_service)):
    task = service.find_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrado!")
    return task

# Alterar dados de usuário:
@task_router.put('/update/{task_id}', response_model=ResponseTask)
def update(task: CreateTask, task_id: int, service: TaskService = Depends(get_task_service)):
    task = service.update(task_id, task)
    if not task:
        raise HTTPException(status_code=404, detail="Nenhuma tarefa foi encontrada!")
    return task

@task_router.put('/done/{task_id}', response_model=ResponseTask)
def update_status(task_id: int, service: TaskService = Depends(get_task_service)):
    task = service.update_status(task_id, 'Finalizada')
    if not task:
        raise HTTPException(status_code=404, detail='Tarefa não encontrada!')
    return task

# Deletar usuários por ID:
@task_router.delete('/delete/{task_id}', response_model=ResponseTask)
def delete(task_id: int, service: TaskService = Depends(get_task_service)):
    task = service.delete(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada!")
    return task