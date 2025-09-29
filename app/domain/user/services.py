from app.domain.user.repository import UserRepository
from app.domain.auth.schemas import RegisterRequest

# Constutor do UserService + Injeção de dependência (Repository)
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: RegisterRequest):
        return self.repository.create(user)
    
    def find_all(self):
        return self.repository.find_all()
    
    def find_by_id(self, user_id: int):
        return self.repository.find_by_id(user_id)
        
    def update(self, user_id: int, user: RegisterRequest):
        return self.repository.update(user_id, user)
    
    def delete(self, user_id: int):
        return self.repository.delete(user_id)