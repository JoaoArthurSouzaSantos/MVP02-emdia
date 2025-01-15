from pydantic import BaseModel
from datetime import date
from typing import Optional

class ConsultaCreate(BaseModel):
    idPaciente: int  
    idFuncionario: str  
    data: date  
    dataRetorno: date  # Certifique-se de que este nome corresponde ao nome do campo no SQLAlchemy
    hbg: Optional[float] = None  
    tomaMedHipertensao: Optional[str] = None  
    praticaAtivFisica: Optional[str] = None  
    imc: Optional[float] = None  
    peso: Optional[float] = None  
    historicoAcucarElevado: Optional[str] = None  
    altura: Optional[float] = None  
    cintura: Optional[float] = None  
    resultadoFindRisc: Optional[str] = None  
    historicoFamiliar: Optional[str] = None
    frequenciaIngestaoVegetaisFrutas: Optional[str] = None  
    medico: Optional[str] = None  
    class Config:
        orm_mode = True

class ConsultaOut(BaseModel):
    id: int
    idPaciente: str
    idFuncionario: str
    data: date
    dataRetorno: date
    hbg: float
    tomaMedHipertensao: str
    praticaAtivFisica: str
    imc: float
    peso: float
    historicoAcucarElevado: str
    altura: float
    cintura: float
    resultadoFindRisc: str
    frequenciaIngestaoVegetaisFrutas: str
    historicoFamiliar: str
    medico: str

    class Config:
        orm_mode = True

class ConsultaFuncionarioId(BaseModel):
    id: int
    idPaciente: str
    idFuncionario: str
    data: date
    dataRetorno: date
    hbg: float
    tomaMedHipertensao: str
    praticaAtivFisica: str
    imc: float
    peso: float
    historicoAcucarElevado: str
    altura: float
    cintura: float
    resultadoFindRisc: str
    frequenciaIngestaoVegetaisFrutas: str
    historicoFamiliar: str
    medico: str
    nome: str

    class Config:
        orm_mode = True



class ConsultaPacientePessoaOut(BaseModel):
    id: int
    idPaciente: str
    idFuncionario: str
    data: date
    dataRetorno: date
    hbg: Optional[float] = None
    tomaMedHipertensao: Optional[str] = None
    praticaAtivFisica: Optional[str] = None
    imc: Optional[float] = None
    peso: Optional[float] = None
    historicoAcucarElevado: Optional[str] = None
    altura: Optional[float] = None
    cintura: Optional[float] = None
    resultadoFindRisc: Optional[str] = None
    frequenciaIngestaoVegetaisFrutas: Optional[str] = None
    historicoFamiliar: Optional[str] = None
    medico: Optional[str] = None
    
    numeroSUS: str
    data_nascimento: date
    sexo: str
    info: str
    cpf: str
    nome: str
    email: str

    class Config:
        orm_mode = True

class EvolucaoHB(BaseModel):
    data: date
    hbg: Optional[float] = None
    tomaMedHipertensao: Optional[str] = None
    praticaAtivFisica: Optional[str] = None
    imc: Optional[float] = None
    peso: Optional[float] = None
    historicoAcucarElevado: Optional[str] = None
    altura: Optional[float] = None
    cintura: Optional[float] = None
    resultadoFindRisc: Optional[str] = None
    frequenciaIngestaoVegetaisFrutas: Optional[str] = None
    historicoFamiliar: Optional[str] = None
    medico: Optional[str] = None
    dataNascimento: date
    sexo: str
    info: str
    nome: str

    class Config:
        orm_mode = True
