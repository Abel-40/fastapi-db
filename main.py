from fastapi import FastAPI,Depends,HTTPException
from database import sessionLocal,engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import database_models
from database_models import Base
from models import ProductIn,ProductOut
app = FastAPI()

# Base.metadata.create_all(bind=engine)
def get_db():
  db = sessionLocal()
  try:
   yield db
  finally:
    db.close()
  
  
product_orm_object = database_models.Product
@app.post("/create/product/",response_model =ProductOut)
async def create_product(data:ProductIn,db:Session = Depends(get_db)):
  orm_product = database_models.Product(**data.model_dump())
  # print(orm_product)
  db.add(orm_product)
  try:
   db.commit()
   db.refresh(orm_product)
  except IntegrityError:
    db.rollback()
    raise HTTPException(400,"Product already exist!!!")
  return ProductOut.model_validate(orm_product)

@app.get("/product/{id}/",response_model=ProductOut)
async def check(id:int,db:Session = Depends(get_db)):
  product = db.query(product_orm_object).filter(product_orm_object.id == id).first()
  if not product:
    raise HTTPException(404,"Product doesn't exist")
  
  return ProductOut.model_validate(product)

@app.get("/products/",response_model = list[ProductOut])
async def get_all_product(db:Session = Depends(get_db)):
  products = db.query(product_orm_object).all()
  return [ProductOut.model_validate(product) for product in products]

@app.delete("/delete/{id}")
async def delete_product(id:int,db:Session = Depends(get_db)):
  product_to_delete = db.query(product_orm_object).filter(product_orm_object.id == id).first()
  if not product_to_delete:
    raise HTTPException(404,"product doesn't exist")
  db.delete(product_to_delete)
  db.commit()
  return {"detail":"User deleted"}