from sqlalchemy import Column, Integer, String
from database.db_coonect import Base


class Item(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    quantity = Column(Integer)




