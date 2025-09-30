from fastapi import FastAPI

from app.core.config import setup_cors
from app.domain.user.routes import user_router
from app.domain.task.routes import task_router
from app.domain.customer.routes import customer_router

app = FastAPI()
setup_cors(app)

app.include_router(user_router)
app.include_router(task_router)
app.include_router(customer_router)