from pydantic import BaseModel
from datetime import date

class EstratificacaoSchema(BaseModel):
    id: int
    data: date
    categoria: str
    fk_prontuario: int
    fk_paciente: str

    class Config:
        orm_mode = True
