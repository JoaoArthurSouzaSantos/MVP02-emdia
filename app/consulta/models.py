from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    FkPaciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False, index=True)
    FkEspecialidade = Column(Integer, ForeignKey("especialidades.id"), nullable=False, index=True)

    perfil = relationship("PacienteModel", back_populates="pacientes")
    permissao = relationship("EspecialidadeModel", back_populates="especiealidades")

