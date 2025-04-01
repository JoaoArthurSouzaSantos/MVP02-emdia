from pydantic import BaseModel
from datetime import date

class PacienteBase(BaseModel):
    numeroSUS: str
    data_nascimento: date
    cpf: str
    sexo: str
    info: str
    telefone: str
    email: str
    nome: str
    micro_regiao_id: int

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(PacienteBase):
    pass

class Paciente(PacienteBase):
    class Config:
        orm_mode = True