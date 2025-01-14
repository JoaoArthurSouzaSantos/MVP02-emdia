from sqlalchemy import Column, String,ForeignKey,Integer
from sqlalchemy.orm import relationship
from db.base import Base

# Modelo Perfil
class PerfilModel(Base):
    __tablename__ = "perfis"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False, index=True)

    funcionarios = relationship("FuncionarioModel", back_populates="perfil")
    permissoes = relationship("PerfilPermissaoModel", back_populates="perfil", cascade="all, delete-orphan")

