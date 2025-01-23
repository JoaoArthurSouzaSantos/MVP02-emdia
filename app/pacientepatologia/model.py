from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class PacientePatologia(Base):
    __tablename__ = "paciente_patologias"

    id = Column(Integer, primary_key=True, index=True)  # ID da associação
    FkPatologia = Column(Integer, ForeignKey("patologia.id"), nullable=False)  # FK para Patologia
    FkPaciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)  # FK para Paciente

    patologia = relationship("PatologiaModel", back_populates="paciente")
    paciente = relationship("PacienteModel", back_populates="patologia")
