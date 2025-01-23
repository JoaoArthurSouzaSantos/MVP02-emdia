from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import relationship
from db.base import Base

class PacienteModel(Base):
    __tablename__ = "pacientes"

    numeroSUS = Column(VARCHAR(45), primary_key=True, index=True)  # Número SUS como chave primária
    email = Column(VARCHAR(45))
    telefone = Column(VARCHAR(45))
    sexo = Column(VARCHAR(45), index=True)
    info = Column(VARCHAR(45), index=True)
    dataNascimento = Column(VARCHAR(45))
    microRegiao = Column(VARCHAR(45))

    consulta = relationship("consulta", back_populates="consulta")
    biometria = relationship("biometria")

