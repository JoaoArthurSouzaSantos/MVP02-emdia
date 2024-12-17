from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

# Modelo Funcionario
class FuncionarioModel(Base):
    __tablename__ = "funcionarios"

    cpf = Column(String(255), primary_key=True, index=True)
    password = Column(String(255), nullable=False)
    nome = Column(String(255), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    idPerfil = Column(int, ForeignKey("perfis.id"), nullable=False, index=True)

    perfil = relationship("PerfilModel", back_populates="funcionarios")