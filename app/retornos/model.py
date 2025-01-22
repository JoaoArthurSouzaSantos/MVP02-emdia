from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class RetornosModel(Base):
    __tablename__ = "retornos"

    id = Column(Integer, primary_key=True, index=True)

    # Chaves estrangeiras
    FkPaciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False, index=True)
    FkEspecialidade = Column(Integer, ForeignKey("especialidades.id"), nullable=False, index=True)

    # Relacionamentos
    paciente = relationship("PacienteModel", back_populates="retornos")
    especialidade = relationship("EspecialidadeModel", back_populates="retornos")


