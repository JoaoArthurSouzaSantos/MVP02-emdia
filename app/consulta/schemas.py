from datetime import date
from pydantic import BaseModel
from typing import Optional

class ConsultaSchema(BaseModel):
    id: Optional[int]
    data: date
    status: int
    observacoes: str
    fk_paciente: int
    fk_especialista: int
    fk_funcionario: int

    class Config:
        orm_mode = True
