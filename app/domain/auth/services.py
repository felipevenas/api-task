from app.domain.auth.schemas import LoginRequest, RegisterRequest
from app.domain.auth.repository import AuthRepository

class AuthService:
    
    def __init__(self, repository: AuthRepository):
        self.repository = repository

    def authenticate(self, credentials: LoginRequest):
        return self.repository.verify_user(credentials)
    
    def register(self, credentials: RegisterRequest):
        return self.repository.create(credentials)


