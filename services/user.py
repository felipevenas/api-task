from models.user import User
from repositories.user import UserRepository
from schemas.user import CreateUser

# Constutor do UserService
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: CreateUser):
        return self.repository.create_user(user)
    
    def find_all(self):
        return self.repository.find_all()
    
    def find_by_id(self, user_id: int):
        return self.repository.find_by_id(user_id)
        
    def update(self, user_id: int, user: CreateUser):
        return self.repository.update(user_id, user)
    
    def delete(self, user_id: int):
        return self.repository.delete(user_id)
