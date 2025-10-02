from sqlalchemy.orm import Session

from app.domain.auth.schemas import LoginRequest, RegisterRequest
from app.domain.user.model import User

class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: RegisterRequest) -> User:
        db_user = User(**user.model_dump())
        self.db.add(db_user)
        self.db.commit()
        return db_user

    def verify_user(self, credentials: LoginRequest) -> User:
        user = self.db.query(User).filter(User.login == credentials.login).first()

        if user:
            if user.senha == credentials.senha:
                return user
            else:
                return False