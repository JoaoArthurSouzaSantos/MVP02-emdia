from sqlalchemy.ext.declarative import declarative_base
from db.connection import engine, Session as SessionLocal

Base = declarative_base()
