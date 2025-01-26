from pydantic import BaseModel
from datetime import date

<<<<<<< HEAD
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
=======
class PacienteSchema(BaseModel):
    
    numeroSUS: str
    nome: str
    email: str
    telefone: str
    sexo: str
    info: str
    dataNascimento: str
    microRegiao: str
>>>>>>> 0ee348ad6d8728d190f7f884d222995af019cc64
