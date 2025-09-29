from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from app.core.config import setup_cors
from app.domain.user.routes import user_router
from app.domain.task.routes import task_router
from app.domain.customer.routes import customer_router

app = FastAPI()
setup_cors(app)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

app.include_router(user_router)
app.include_router(task_router)
app.include_router(customer_router)