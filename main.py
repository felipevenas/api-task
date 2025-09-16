<<<<<<< HEAD
from fastapi import FastAPI
from routes.user import user_router
from routes.task import task_router
from config.database import Base, engine

app = FastAPI()

app.include_router(user_router)
app.include_router(task_router)
=======
from fastapi import FastAPI
from routes.user import user_router
from config.database import Base, engine

app = FastAPI()

app.include_router(user_router)
>>>>>>> cb0e5b90397ae64b2c927d15119aa22885b9f4c8
