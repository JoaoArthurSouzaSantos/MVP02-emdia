from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base

class ProntuarioExame(Base):
    __tablename__ = "prontuario"

    id = Column(Integer, primary_key=True, index=True)
    FkFuncionario = Column(Integer, ForeignKey("Funcionarios.cpf"), nullable=False, index=True)
    FkPaciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)
    FkExame = Column(String(255), ForeignKey("exames.id"), nullable=False)

    # Relacionamentos
    paciente = relationship("PacienteModel", back_populates="pacientes")
    perfil = relationship("FuncionarioModel", back_populates="funcionarios")
    exame = relationship("ExameModel", back_populates="exames")

