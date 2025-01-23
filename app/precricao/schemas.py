from pydantic import BaseModel
from datetime import date
from typing import Optional

class PrescricaoSchema(BaseModel):
    id: int
    inicio: date
    fim: Optional[date]  # Campo opcional
    status: str
    frequencia: str
    dosagem: str
    fk_medicamento: int
    fk_paciente: str

    class Config:
        orm_mode = True
