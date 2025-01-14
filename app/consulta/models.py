from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idPaciente = Column(String(255), ForeignKey('pacientes.numeroSUS'), index=True)  # Alterado para String(255)
    idFuncionario = Column(String(255), ForeignKey('funcionarios.id'), index=True)
    data = Column(Date)
    dataRetorno = Column(Date)
    hbg = Column(Float)
    tomaMedHipertensao = Column(String(255))
    praticaAtivFisica = Column(String(255))
    imc = Column(Float)
    peso = Column(Float)
    historicoAcucarElevado = Column(String(255))
    altura = Column(Float)
    cintura = Column(Float)
    resultadoFindRisc = Column(String(255))
    frequenciaIngestaoVegetaisFrutas = Column(String(255))
    historicoFamiliar  = Column(String(255))
    medico  = Column(String(255))

    paciente = relationship("Paciente", back_populates="consultas")
    funcionario = relationship("FuncionarioModel", back_populates="consultas")
