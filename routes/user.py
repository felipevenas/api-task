from fastapi import APIRouter
from bson import ObjectId
from config.database import connection
from models.user import User
from schemas.user import userEntity, listUserEntity

user_router = APIRouter()

@user_router.get('/')
async def start():
    return "API foi inicializada!"

# Listar todos os usuários:
@user_router.get('/user')
async def list_users():
    return listUserEntity(connection.local.user.find())

# Buscar um usuário por ID:
@user_router.get('/user/{id_user}')
async def find_by_id(id_user: str):
    user = connection.local.user.find_one({"_id": ObjectId(id_user)}) # "'_id' é a informação que está salva no banco."
    if user:
        print("✅ Usuário encontrado!")
        return {"Info:": "Usuário encontrado!"}, userEntity(user)
    return {"Erro:": "Nenhuma informação encontrada."}

# Inserir novo usuário:
@user_router.post('/user')
async def create_user(user: User):
    connection.local.user.insert_one(dict(user))
    print("✅ Usuário criado!")
    return listUserEntity(connection.local.user.find())

# Atualizar um usuário pelo ID:
@user_router.put('/user/{id_user}')
async def update_user(id_user: str, user: User):
    connection.local.user.find_one_and_update(
        {"_id": ObjectId(id_user)}, # Busca o objeto pelo ID.
        {"$set": dict(user)} # Seta os novos valores em formato de dicionário.
    )
    print("✅ Usuário atualizado!")
    return {"Info:": "Usuário atualizado!"}, userEntity(
        connection.local.user.find_one({"_id": ObjectId(id_user)})
    )    

# Deletar um usuário:
@user_router.delete('/user/{id_user}')
async def delete_user(id_user: str):
    user = connection.local.user.find_one_and_delete({"_id": ObjectId(id_user)})
    if user:
        print("✅ Usuário deletado!")
        return {"Info:": "Usuário deletado!"}, userEntity(user)
    return {"Erro:": "Nenhum usuário encontrado!"}

# Adicionar uma tarefa ao usuário:
@user_router.post("/user/{id_user}/task")
async def add_task(id_user: str, task: dict):
    connection.local.user.update_one(
        {"_id": ObjectId(id_user)},
        {"$push": {"tasks": task}}  # Adiciona nova task na lista do usuário.
    )
    return {"Info:": "Task adicionada com sucesso!"}