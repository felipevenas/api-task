from pydantic import BaseModel

class LoginRequest(BaseModel):
    login: str
    senha: str

# Aqui você dita os campos necessários para criação desse objeto:
class RegisterRequest(BaseModel):
    nome: str
    email: str
    telefone: str
    login: str
    senha: str
    grupo: str
    cargo: str
    setor: str
    ativo: str