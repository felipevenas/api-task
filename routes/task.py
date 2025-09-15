from fastapi import APIRouter
from bson import ObjectId
from config.database import connection
from models.task import Task
from schemas.task import taskEntity, listTaskEntity

task_router = APIRouter()

# Listar todas as tarefas:
@task_router.get('/task')
async def list_users():
    return listTaskEntity(connection.local.task.find())

# Buscar uma tarefa por ID:
@task_router.get('/task/{id_task}')
async def find_by_id(id_task: str):
    task = connection.local.task.find_one({"_id": ObjectId(id_task)})
    if task:
        print("✅ Tarefa encontrada!")
        return {"Info:": "Tarefa encontrada!"}, taskEntity(task)
    return {"Erro:": "Nenhuma informação encontrada."}

# Inserir nova tarefa:
@task_router.post('/task')
async def create_user(task: Task):
    connection.local.task.insert_one(dict(task))
    print("✅ Tarefa criada!")
    return listTaskEntity(connection.local.task.find())

# Atualizar uma tarefa pelo ID:
@task_router.put('/task/{id_task}')
async def update_user(id_task: str, task: Task):
    connection.local.user.find_one_and_update(
        {"_id": ObjectId(id_task)}, # Busca o objeto pelo ID.
        {"$set": dict(task)} # Seta os novos valores em formato de dicionário.
    )
    print("✅ Tarefa atualizada!")
    return {"Info:": "Tarefa atualizada!"}, taskEntity(
        connection.local.task.find_one({"_id": ObjectId(id_task)})
    )    

# Deletar uma tarefa pelo ID:
@task_router.delete('/task/{id_task}')
async def delete_user(id_task: str):
    task = connection.local.task.find_one_and_delete({"_id": ObjectId(id_task)})
    if task:
        print("✅ Tarefa deletada!")
        return {"Info:": "Tarefa deletada!"}, taskEntity(task)
    return {"Erro:": "Nenhuma tarefa encontrada!"}