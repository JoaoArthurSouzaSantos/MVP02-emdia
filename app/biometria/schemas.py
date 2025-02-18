from pydantic import BaseModel
from datetime import date

class BiometriaSchema(BaseModel):
    imc: float
    peso: float
    altura: float
    data: date
    cintura: float
    fk_paciente: int
    fk_consulta: int

    class Config:
        orm_mode = True