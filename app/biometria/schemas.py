from pydantic import BaseModel
from datetime import date

class BiometriaSchema(BaseModel):
    imc: float
    peso: float
    altura: float
    data: date
    cintura: float

    class Config:
        orm_mode = True