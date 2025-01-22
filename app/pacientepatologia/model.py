from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class PacientePatologia(Base):
    __tablename__ = "paciente_patologias"

    id = Column(Integer, primary_key=True, index=True)  # ID da associação
    fk_patologia = Column(Integer, ForeignKey("patologias.id"), nullable=False)  # FK para Patologia
    fk_paciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)  # FK para Paciente

    patologia = relationship("Patologia", back_populates="pacientes")
    paciente = relationship("Paciente", back_populates="patologias")
