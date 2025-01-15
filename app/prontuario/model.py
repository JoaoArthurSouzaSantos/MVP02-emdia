from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from db.base import Base

class ProntuarioModel(Base):
    __tablename__ = "prontuarios"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    medico_crm = Column(String(20), ForeignKey("medicos.crm"), nullable=False)
    descricao = Column(String(500), nullable=False)
    exame_id = Column(Integer, ForeignKey("exames.id"), nullable=True)

    paciente = relationship("PacienteModel", back_populates="prontuarios")
    exame = relationship("ExameModel")
