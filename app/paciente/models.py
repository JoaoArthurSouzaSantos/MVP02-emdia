from sqlalchemy import Column, String , Date , ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    numeroSUS = Column(String(255), primary_key=True, index=True)  # Número SUS como chave primária  # Chave estrangeira referenciando o CPF na tabela pessoas
    dataNascimento = Column(Date)
    sexo = Column(String(255), index=True)
    info = Column(String(255), index=True)
    pessoa = relationship("Pessoa", back_populates="paciente")
    consultas = relationship("Consulta", back_populates="paciente")


