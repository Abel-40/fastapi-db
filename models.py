from pydantic import BaseModel
from datetime import datetime
class ProductIn(BaseModel):
  name:str
  description:str
  price:float
  quantity:int
class ProductOut(BaseModel):
    id: int
    name: str
    description: str  
    price: float       
    quantity: int

    class Config:
        from_attributes = True  

class UserCreate(BaseModel):
  username:str
  email:str

class UserOut(UserCreate):
  id:int
  created_at:datetime
  
  class Config:
    from_attributes = True