from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.domain.user.routes import user_router
from app.domain.task.routes import task_router
from app.domain.customer.routes import customer_router

app = FastAPI()

origins = {
    "http://127.0.0.1:5000",
    "http://127.0.0.1:5000/register",
    "http://127.0.0.1:5000/login",
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Habilita todos os métodos HTTP
    allow_headers={"*"}  # Permite todos os cabeçalhos
)

app.include_router(user_router)
app.include_router(task_router)
app.include_router(customer_router)