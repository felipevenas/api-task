from pydantic import BaseModel

class CreateCustomer(BaseModel):
    razao_social: str
    nome_fantasia: str
    cpfecnpj: str
    cpf: str
    numero_dominio: str
    inscricao_estadual: str
    inscricao_municipal: str
    telefone: str
    celular: str
    email: str
    regime_tributario: str
    tipo_conta: str
    endereco: str
    bairro: str
    cidade: str
    estado: str
    numero: str
    cep: str
    login_gov: str
    senha_gov: str
    certificado: bool
    zap_contabil: bool
    representante: str
    email1_iss: str
    email2_iss: str
    email3_iss: str

class ResponseCustomer(BaseModel):
    razao_social: str
    nome_fantasia: str
    email: str
    cidade: str
    estado: str

    class Config:
        from_attributes = True