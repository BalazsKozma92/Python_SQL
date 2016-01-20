from declerative import Base
from sqlalchemy import Column


class Orders(Base):
    OrderID = Column
    CustomerID = Column
    EmployeeID = Column
    OrderDate = Column
    RequiredDate = Column
    ShippedDate = Column
    ShipVia = Column
    Freight = Column
    ShipName = Column
    ShipAddress = Column
    ShipCity = Column
    ShipRegion = Column
    ShipPostalCode = Column
    ShipCountry = Column