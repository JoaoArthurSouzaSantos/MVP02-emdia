from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from db.base import Base

class PacienteModel(Base):
    __tablename__ = "pacientes"

    numeroSUS = Column(String(255), primary_key=True, index=True) 
    dataNascimento = Column(Date)
    sexo = Column(String(255), index=True)
    info = Column(String(255), index=True)
    telefone = Column(String(255), index=True)
    email = Column(String(255), index=True)
    nome = Column(String(255), index=True)
    microRegiao = Column(String(255), index=True)

    # Relacionamentos
    consultas = relationship("ConsultaModel", back_populates="paciente", cascade="all, delete-orphan")
    biometria = relationship("BiometriaModel", back_populates="paciente", cascade="all, delete-orphan")
    prescricoes = relationship("PrescricaoModel", back_populates="paciente", cascade="all, delete-orphan")
    patologias = relationship("PacientePatologiaModel", back_populates="paciente", cascade="all, delete-orphan")
    retornos = relationship("RetornosModel", back_populates="paciente", cascade="all, delete-orphan")

