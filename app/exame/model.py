from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base

class ExameModel(Base):
    __tablename__ = "exames"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    resultado = Column(String(500), nullable=True)
    data_realizacao = Column(String(50), nullable=False)
    
    prescricao = relationship("PrescricaoModel", back_populates="exames")
