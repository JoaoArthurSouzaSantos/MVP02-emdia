from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship
from shared.database import Base

class PatologiaModel(Base):
    __tablename__ = "patologia"

    id = Column(Integer, primary_key= True, index= True)
    nome = Column(String(255))
    
    paciente = relationship("PacienteModel", back_populates="patologia")