from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base

class Medicamento(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    info = Column(String(255))

    # Relacionamentos
    prescricoes = relationship("Prescricao", back_populates="medicamento")
