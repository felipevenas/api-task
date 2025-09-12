from fastapi import APIRouter
from config.database import connection
from models.user import User
from schemas.user import userEntity, listUserEntity

user_router = APIRouter()

@user_router.get('/')
async def start():
    return "API was initialized."

# Listar todos os usuários:
@user_router.get('/user')
async def list_users():
    return connection.local.user.find()

# Inserir novo usuário:
@user_router.post('/user')
async def create_user(user: User):
    connection.local.user.insert_one(dict(user))
    return listUserEntity(connection.local.user.find())