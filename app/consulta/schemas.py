from datetime import date
from pydantic import BaseModel, validator
from typing import Optional

class ConsultaSchema(BaseModel):
    data: date
    status: int
    observacoes: str
    fk_paciente: int
    fk_especialidade: int
    fk_funcionario: int

    class Config:
        orm_mode = True

class ConsultaReturnSchema(ConsultaSchema):
    id: int
    data: date
    status: int
    observacoes: str
    fk_paciente: int
    fk_especialidade: int
    fk_funcionario: int

    class Config:
        orm_mode = True

class PacienteDetailSchema(BaseModel):
    nome: str
    data_nascimento: Optional[str]
    sexo: Optional[str]
    micro_regiao: Optional[str]
    info: Optional[str]
    patologia: list
    data: Optional[str]
    peso: Optional[float]
    altura: Optional[float]
    imc: Optional[float]
    cintura: Optional[float]
    nivelDeRisco: Optional[str]
    pontuacaoDoUltimoFindrisc: Optional[int]
    dataDoUltimoFindrisc: Optional[str]
    ultimoResultadoExame: dict

    class Config:
        orm_mode = True

class AgendaItemSchema(BaseModel):
    data_consulta: Optional[date]
    nome_paciente: Optional[str]
    nivel_de_risco: Optional[str]
    medico: Optional[str]
    especialidade: Optional[str]


    class Config:
        orm_mode = True
