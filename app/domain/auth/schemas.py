from pydantic import BaseModel

class LoginRequest(BaseModel):
    login: str
    senha: str

    class Config:
        from_attributes = True

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

    class Config:
        from_attributes = True

class ResponseUserLogin(BaseModel):
    id: int
    login: str
    senha: str

    class Config:
        from_attributes = True
