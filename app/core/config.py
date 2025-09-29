from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app: FastAPI):

    origins = [
    "http://127.0.0.1:5000",
    "http://127.0.0.1:5000/register",
<<<<<<< HEAD
    "http://127.0.0.1:5000/auth",
=======
    "http://127.0.0.1:5000/login",
>>>>>>> a16d0600c0996d352d28f4b098ccd9b055ee64f3
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"], # Habilita todos os métodos HTTP
        allow_headers={"*"}  # Permite todos os cabeçalhos
        )
    
    print("CORS Middleware configurado com sucesso!")