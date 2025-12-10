from fastapi import FastAPI
from database import session,engine
import database_models
from models import Product
app = FastAPI()


products = [
    Product(
        id=1,
        name="Laptop Stand",
        description="A lightweight adjustable laptop stand made of aluminum.",
        price = 200.00,
        quantity=50
    ),
    Product(
        id=2,
        name="Wireless Mouse",
        description="Ergonomic 2.4GHz wireless mouse with USB receiver.",
        price = 300.00,
        quantity=120
    ),
    Product(
        id=3,
        name="Mechanical Keyboard",
        description="RGB backlit mechanical keyboard with blue switches.",
        price=400,
        quantity=30
    ),
    Product(
        id=4,
        name="USB-C Cable",
        description="1-meter fast-charging USB-C cable.",
        price = 500.00,
        quantity=200
    )
]


database_models.Base.metadata.create_all(bind=engine)


def add_dumy_data():
  db = session()
  count = db.query(database_models.Product).count()
  if count == 0:
    for product in products:
      db.add(database_models.Product(**product.model_dump()))
    db.commit()
async def db_injection():
  db = session()
  yield db
  db.close()
add_dumy_data() 

@app.get("/")
async def check():
  return {"msg":"check"}