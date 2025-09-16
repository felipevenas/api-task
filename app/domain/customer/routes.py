from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.domain.customer.repository import CustomerRepository
from app.domain.customer.services import CustomerService
from app.domain.customer.schemas import CreateCustomer, ResponseCustomer

customer_router = APIRouter()

def get_customer_service(db: Session = Depends(get_db)):
    repository = CustomerRepository(db)
    return CustomerService(repository)

# Inserir novo usuário:
@customer_router.post('/customer', response_model=ResponseCustomer)
def create_Customer(customer: CreateCustomer, service: CustomerService = Depends(get_customer_service)):
    return service.create(customer)

# Buscar todos os usuários:
@customer_router.get('/customers', response_model=list[ResponseCustomer])
def find_all(service: CustomerService = Depends(get_customer_service)):
    return service.find_all()

# Buscar usuário por ID:
@customer_router.get('/customer/{customer_id}', response_model=ResponseCustomer)
def find_by_id(customer_id: int, service: CustomerService = Depends(get_customer_service)):
    customer = service.find_by_id(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    return customer

# Alterar dados de usuário:
@customer_router.put('/customer/{customer_id}', response_model=ResponseCustomer)
def update(customer: CreateCustomer, customer_id: int, service: CustomerService = Depends(get_customer_service)):
    customer = service.update(customer_id, customer)
    if not customer:
        raise HTTPException(status_code=404, detail="Nenhum cliente foi encontrado!")
    return customer

# Deletar usuários por ID:
@customer_router.delete('/customer/{customer_id}', response_model=ResponseCustomer)
def delete(customer_id: int, service: CustomerService = Depends(get_customer_service)):
    customer = service.delete(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    return customer