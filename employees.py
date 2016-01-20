from declerative import Base
from sqlalchemy import Column


class Employees(Base):
    EmployeeID = Column
    LastName = Column
    FirstName = Column
    Title = Column
    TitleOfCourtesy = Column
    BirthDate = Column
    HireDate = Column
    Address = Column
    City = Column
    Region = Column
    PostalCode = Column
    Country = Column
    HomePhone = Column
    Extension = Column
    Photo = Column
    Notes = Column
    ReportsTo = Column
    PhotoPath = Column
    Salary = Column