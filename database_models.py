from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float,DateTime
from datetime import datetime

Base = declarative_base()
class Product(Base):
  __tablename__ = "product"
  id = Column(Integer,primary_key=True,index=True)
  name = Column(String,unique=True,nullable=False)
  description = Column(String)
  price = Column(Float,nullable=False)
  quantity = Column(Integer,nullable=False,default=0)
  
class User(Base):
  __tablename__ = "user"
  id = Column(Integer,primary_key=True,index=True)
  username = Column(String,unique=True,nullable=False)
  email = Column(String,nullable=False)
  created_at = Column(DateTime,default=datetime.now)
  
