from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from db.base import Base

# Modelo Medico
class MedicoModel(Base):
    __tablename__ = "medicos"

    crm = Column(String(20), primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    telefone = Column(String(20), nullable=True)
    idPerfil = Column(Integer, ForeignKey("perfis.id"), nullable=False, index=True)

    # Chave estrangeira para Especialidade
    especialidade_id = Column(Integer, ForeignKey("especialidades.id"), nullable=False)

    # Relacionamentos
    perfil = relationship("PerfilModel", back_populates="medico")
    consultas = relationship("ConsultaModel", back_populates="medico")
    prontuarios = relationship("ProntuarioModel", back_populates="medico")
    prescricoes = relationship("PrescricaoModel", back_populates="medico")
    especialidade = relationship("EspecialidadeModel", back_populates="medicos")
