<<<<<<< HEAD
from sqlalchemy import Column, VARCHAR
=======
from sqlalchemy import Column, String, Date
>>>>>>> 349e6a9cfb735b1b5413f13466359a147e8aa015
from sqlalchemy.orm import relationship
from db.base import Base

class PacienteModel(Base):
    __tablename__ = "pacientes"

<<<<<<< HEAD
    numeroSUS = Column(VARCHAR(45), primary_key=True, index=True)  # Número SUS como chave primária
    email = Column(VARCHAR(45))
    telefone = Column(VARCHAR(45))
    sexo = Column(VARCHAR(45), index=True)
    info = Column(VARCHAR(45), index=True)
    dataNascimento = Column(VARCHAR(45))
    microRegiao = Column(VARCHAR(45))

    consulta = relationship("consulta", back_populates="consulta")
    biometria = relationship("biometria")
=======
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
>>>>>>> 349e6a9cfb735b1b5413f13466359a147e8aa015

