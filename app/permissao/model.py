from sqlalchemy import Column, String , ForeignKey , Integer
from sqlalchemy.orm import relationship
from db.base import Base

# Modelo Permissao
class PermissaoModel(Base):
    __tablename__ = "permissoes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False, index=True)

    perfis = relationship("PerfilPermissaoModel", back_populates="permissao", cascade="all, delete-orphan")
    perfis_rel = relationship("PerfilModel", secondary="perfilpermissoes", back_populates="permissoes_rel")


