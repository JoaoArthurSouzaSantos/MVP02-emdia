from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base

class EspecialidadeModel(Base):
    __tablename__ = "especialidades"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), unique=True, nullable=False)

   
