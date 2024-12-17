from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from db.base import Base

class ConsultaModel(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    medico_crm = Column(String(20), ForeignKey("medicos.crm"), nullable=False)
    data = Column(String(50), nullable=False)

    # Relacionamentos
    medico = relationship("MedicoModel", back_populates="consultas")
    paciente = relationship("PacienteModel", back_populates="consultas")
