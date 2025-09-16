from fastapi import APIRouter, Depends, HTTPException, status
from app.db.database import get_db
from app.domain.user.repository import UserRepository
from app.domain.user.services import UserService
from app.domain.user.schemas import CreateUser, ResponseUser
from sqlalchemy.orm import Session

user_router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    return UserService(repository)

# Inserir novo usuário:
@user_router.post('/user', response_model=ResponseUser)
def create_user(user: CreateUser, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

# Buscar todos os usuários:
@user_router.get('/users', response_model=list[ResponseUser])
def find_all(service: UserService = Depends(get_user_service)):
    return service.find_all()

# Buscar usuário por ID:
@user_router.get('/user/{user_id}', response_model=ResponseUser)
def find_by_id(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    return user

# Alterar dados de usuário:
@user_router.put('/user/{user_id}', response_model=ResponseUser)
def update(user: CreateUser, user_id: int, service: UserService = Depends(get_user_service)):
    user = service.update(user_id, user)
    if not user:
        raise HTTPException(status_code=404, detail="Nenhum usuário foi encontrado!")
    return user

# Deletar usuários por ID:
@user_router.delete('/user/{user_id}', response_model=ResponseUser)
def delete(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.delete(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    return user