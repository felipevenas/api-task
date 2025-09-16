from app.domain.customer.schemas import CreateCustomer
from app.domain.customer.model import Customer
from sqlalchemy.orm import Session

class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, customer: CreateCustomer) -> Customer:
        db_customer = Customer(**customer.dict())
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer
    
    def find_all(self):
        return self.db.query(Customer).all()
    
    def find_by_id(self, Customer_id: int):
        return self.db.query(Customer).filter(Customer.id == Customer_id).first()
    
    def update(self, Customer_id: int, Customer: CreateCustomer) -> Customer:
        db_customer = self.find_by_id(Customer_id)
        if not db_customer:
            return None
        for key, value in Customer.dict().items():
            setattr(db_customer, key, value)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def delete(self, customer_id: int):
        db_customer = self.find_by_id(customer_id)
        if not db_customer:
            return None
        self.db.delete(db_customer)
        self.db.commit()
        return db_customer
    
