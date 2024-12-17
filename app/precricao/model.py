from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from db.base import Base

class PrescricaoModel(Base):
    __tablename__ = "prescricoes"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    medico_crm = Column(String(20), ForeignKey("medicos.crm"), nullable=False)
    medicamento = Column(String(255), nullable=False)
    dosagem = Column(String(255), nullable=False)

    # Relacionamentos
    medico = relationship("MedicoModel", back_populates="prescricoes")
    paciente = relationship("PacienteModel", back_populates="prescricoes")
