from pydantic import BaseModel
from datetime import date

class EstratificacaoSchema(BaseModel):
    id: int
    data: date
    categoria: str
    fk_paciente: int
    fk_consulta: int

    class Config:
        orm_mode = True
