from sqlalchemy import Column, String, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from db.base import Base

# Modelo Funcionario
class FindriskModel(Base):
    __tablename__ = "findrisk"

    idFindrisk = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    data = Column(Date)
    pont_historico_familiar_de_diabetes = Column(String(255))
    pont_hipertensao = Column(String(255))
    pont_ingestao_frutas_e_verduras = Column(String(255))
    pont_atv_fisica = Column(String(255))
    pont_circuferencia_cintura = Column(String(255))
    pont_imc = Column(String(255))
    pont_idade = Column(String(255))
    classificacao = Column(String(255))
    pont_historico_de_glicemia_elevada = Column(String(255))
    fkPaciente = Column(Integer, ForeignKey("paciente.numeroSUS"))
    

    paciente = relationship("paciente", back_populates="findrisk")