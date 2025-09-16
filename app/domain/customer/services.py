from app.domain.customer.repository import CustomerRepository
from app.domain.customer.schemas import CreateCustomer

class CustomerService:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def create(self, customer: CreateCustomer):
        return self.repository.create(customer)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, customer_id: int):
        return self.repository.find_by_id(customer_id)

    def update(self, customer_id: int, customer: CreateCustomer):
        return self.repository.update(customer_id, customer)
    
    def delete(self, customer_id: int):
        return self.repository.delete(customer_id)