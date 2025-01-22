from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Prescricao(Base):
    __tablename__ = "prescricoes"

    id = Column(Integer, primary_key=True, index=True)
    inicio = Column(Date, nullable=False)  
    fim = Column(Date, nullable=True)  
    status = Column(String(255), nullable=False)  
    frequencia = Column(String(255), nullable=False)  
    dosagem = Column(String(255), nullable=False)  

    # Chaves estrangeiras
    fk_medicamento = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    fk_paciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)

    # Relacionamentos
    paciente = relationship("Paciente", back_populates="prescricoes")
    medicamento = relationship("Medicamento", back_populates="prescricoes")
