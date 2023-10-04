import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

url = os.getenv("DB_URL")

engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def is_ready():
    db = SessionLocal()
    db_ready_query = text("select TRUE")
    result =  db.execute(db_ready_query)
    db.close()
    return result.scalar()
