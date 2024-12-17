from sqlalchemy import Column, Date, Float
from sqlalchemy.orm import relationship
from shared.database import Base

class Paciente(Base):
    __tablename__ = "biometrias"

    imc = Column(Float)
    peso = Column(Float)
    altura = Column(Float)
    data = Column(Date)
    cintura = Column(Float)
    
    paciente = relationship("paciente", back_populates="biometrias")