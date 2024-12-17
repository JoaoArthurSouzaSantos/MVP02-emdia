from sqlalchemy import Column, String , Date
from sqlalchemy.orm import relationship
from shared.database import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    nome = Column(String(255))
    email = Column(String(255))
    cpf = Column(String(255), index=True)
    telefone = Column(String(255))
    microRegiao = Column(String(255))
    numeroSUS = Column(String(255), primary_key=True, index=True)  # Número SUS como chave primária
    dataNascimento = Column(Date)
    sexo = Column(String(255), index=True)
    info = Column(String(255), index=True)
    
    estratificacao = relationship("Estratificacao", back_populates="paciente")
    retornos = relationship("Retornos", back_populates="paciente")
    
    #pessoa = relationship("Pessoa", back_populates="paciente")
    #consultas = relationship("Consulta", back_populates="paciente")
    #a