from extentions import db
from sqlalchemy import *


class Product(db.Model):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False, index=True)
    price = Column(Integer, nullable=False, index=True)
    active = Column(Integer, nullable=False, index=True)
    
    