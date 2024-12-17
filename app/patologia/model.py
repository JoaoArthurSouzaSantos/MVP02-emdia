from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship
from shared.database import Base

class Paciente(Base):
    __tablename__ = "patologia"

    id = Column(Integer, )
    nome = Column(String(255))
    
    paciente = relationship("paciente", back_populates="patologia")