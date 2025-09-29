from pydantic import BaseModel
 
# Aqui você dita os campos que irão aparecer no retorno:
class ResponseUser(BaseModel):
    id: int
    nome: str
    email:str
    login: str
    senha: str
    telefone: str
    grupo: str
    cargo: str
    setor: str
    ativo: str

    class Config:
        from_attributes = True
    