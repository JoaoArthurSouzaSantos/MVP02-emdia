from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from db.base import Base

class FuncionarioEspecialidadeModel(Base):
    __tablename__ = "funcionariosEspecialidades"

    id = Column(Integer, primary_key=True, index=True)  # Chave primária

    Fkfuncionario = Column(String(255), ForeignKey("funcionarios.cpf"), nullable=False, index=True)
    Fkespecialidade = Column(Integer, ForeignKey("especialidades.id"), nullable=False, index=True)

    
    funcionario = relationship("FuncionarioModel", back_populates="especialidades")
    especialidade = relationship("EspecialidadeModel", back_populates="funcionarios")
