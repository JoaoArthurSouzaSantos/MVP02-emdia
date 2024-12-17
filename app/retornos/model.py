from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from db.base import Base

# Modelo Funcionario
class RetornosModel(Base):
    __tablename__ = "retornos"

    data = Column(Date)
    status = Column(String(255))

    paciente = relationship("PacienteModel", back_populates="funcionarios")

