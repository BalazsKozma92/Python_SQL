from declerative import Base
from sqlalchemy import Column


class OrderDetails(Base):
    OrderID = Column
    ProductID = Column
    UnitPrice = Column
    Quantity = Column
    Discount = Column