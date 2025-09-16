from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean

class Customer(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    razao_social = Column(String(200), nullable=False)
    nome_fantasia = Column(String(200), nullable=False)
    cpfecnpj = Column(String(255))
    cpf = Column(String(30))
    numero_dominio = Column(String(10))
    inscricao_estadual = Column(String(50))
    inscricao_municipal = Column(String(50))
    telefone = Column(String(50))
    celular = Column(String(50))
    email = Column(String(100))
    regime_tributario = Column(String(100))
    tipo_conta = Column(String(10))
    endereco = Column(String(100))
    bairro = Column(String(100))
    cidade = Column(String(100))
    estado = Column(String(5))
    numero = Column(String(10))
    cep = Column(String(10))
    login_gov = Column(String(250))
    senha_gov = Column(String(250))
    certificado = Column(Boolean, default=False)
    zap_contabil = Column(Boolean, default=False)
    representante = Column(String(50))
    email1_iss = Column(String(300))
    email2_iss = Column(String(300))
    email3_iss = Column(String(300))