from declerative import Base
from sqlalchemy import Column


class Customers(Base):
    __tablename__ = "Customers"
    CustomerID = Column()
    CompanyName = Column()
    ContactName = Column()
    ContactTitle = Column()
    Address = Column()
    City = Column()
    Region = Column()
    PostalCode = Column()
    Country = Column()
    Phone = Column()
    Fax = Column()