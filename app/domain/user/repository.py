from app.domain.user.schemas import CreateUser
from app.domain.user.model import User
from sqlalchemy.orm import Session

# Constutor do UserRepository:
class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: CreateUser) -> User:
        db_user = User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def find_all(self):
        return self.db.query(User).all()
    
    def find_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()
    
    def update(self, user_id: int, user: CreateUser) -> User:
        db_user = self.find_by_id(user_id)
        if not db_user:
            return None
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int):
        db_user = self.find_by_id(user_id)
        if not db_user:
            return None
        self.db.delete(db_user)
        self.db.commit()
        return db_user
    
