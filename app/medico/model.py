from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from db.base import Base

# Modelo Medico
class MedicoModel(Base):
    __tablename__ = "medicos"

    crm = Column(String(20), primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    especialidade = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    telefone = Column(String(20), nullable=True)

    # Relacionamentos
    consultas = relationship("ConsultaModel", back_populates="medico")
    prontuarios = relationship("ProntuarioModel", back_populates="medico")
    prescricoes = relationship("PrescricaoModel", back_populates="medico")