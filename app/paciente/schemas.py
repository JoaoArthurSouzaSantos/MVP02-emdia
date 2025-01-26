from pydantic import BaseModel
from datetime import date

class PacienteBase(BaseModel):
    numeroSUS: str
    dataNascimento: date
    sexo: str
    info: str
    telefone: str
    email: str
    nome: str
    microRegiao: str

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(PacienteBase):
    pass

class Paciente(PacienteBase):
    class Config:
        orm_mode: True