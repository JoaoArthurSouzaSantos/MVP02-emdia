from sqlalchemy import Column, String , ForeignKey , Integer
from sqlalchemy.orm import relationship
from db.base import Base


# Modelo PerfilPermissao
class PerfilPermissaoModel(Base):
    __tablename__ = "perfilpermissoes"

    id = Column(Integer, primary_key=True, index=True)
    idPerfil = Column(Integer, ForeignKey("perfis.id"), nullable=False, index=True)
    idPermissao = Column(Integer, ForeignKey("permissoes.id"), nullable=False, index=True)

    perfil = relationship("PerfilModel", back_populates="permissoes")
    permissao = relationship("PermissaoModel", back_populates="perfis")
