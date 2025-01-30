from db.connection import Session as SessionLocal
from decouple import config

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()