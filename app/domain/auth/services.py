from app.domain.auth.schemas import LoginRequest
from app.domain.user.repository import UserRepository

class AuthService:
    
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def authenticate(self, credentials: LoginRequest):
        return self.repository.verify_user(credentials)


