from datetime import date
from pydantic import BaseModel
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
