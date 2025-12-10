from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import settings


db_url = settings.db_url
engine = create_engine(db_url)
session = sessionmaker(autoflush=False,autocommit=False,bind=engine)