from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.domain.auth.repository import AuthRepository
from app.domain.auth.services import AuthService
from app.domain.auth.schemas import LoginRequest, ResponseUserLogin, RegisterRequest
from app.domain.user.schemas import ResponseUser

auth_router = APIRouter()

def get_auth_service(db: Session = Depends(get_db)):
    repository = AuthRepository(db)
    return AuthService(repository)

@auth_router.post('/auth', response_model=ResponseUserLogin)
def auth(credentials: LoginRequest, service: AuthService = Depends(get_auth_service)):
    user = service.authenticate(credentials)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    return user

@auth_router.post('/register', response_model=ResponseUser)
def create_user(user: RegisterRequest, service: AuthService = Depends(get_auth_service)):
    return service.register(user)