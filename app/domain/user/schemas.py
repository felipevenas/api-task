from pydantic import BaseModel

# Aqui você dita os campos necessários para criação desse objeto:
class CreateUser(BaseModel):
    nome: str
    email:str
    senha: str
    login: str
    grupo: str
    telefone: str
    cargo: str
    setor: str
    ativo: str
  
# Aqui você dita os campos que irão aparecer no retorno:
class ResponseUser(BaseModel):
    id: int
    nome: str
    email:str
    login: str
    telefone: str
    grupo: str
    cargo: str
    setor: str
    ativo: str

    class Config:
        from_attributes = True