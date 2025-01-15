from sqlalchemy import Column, Date, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class BiometriaModel(Base):
    __tablename__ = "biometrias"

    id = Column(Integer, primary_key=True, index=True)
    imc = Column(Float, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    data = Column(Date, nullable=False)
    cintura = Column(Float, nullable=False)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)

    paciente = relationship("PacienteModel", back_populates="biometrias")