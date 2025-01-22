from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from db.base import Base

class EstratificacaoModel(Base):
    __tablename__ = "estartificoes"
    data = Column(Date)
    categoria = Column(String(255), nullable=False)

    FkProntuario = Column(Integer, ForeignKey("prontuarios.id"), nullable=False)
    FkPaciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)

    # Relacionamentos
    paciente = relationship("Paciente", back_populates="prescricoes")
    medicamento = relationship("Medicamento", back_populates="prescricoes")
