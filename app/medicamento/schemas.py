from pydantic import BaseModel
from datetime import date
from typing import Optional

class MedicamentoSchema(BaseModel):
    status: str
    frequencia: str
    dosagem: str
    fk_tipo_medicamento: int
    fk_paciente: int
    fk_consulta: Optional[int]

    class Config:
        orm_mode = True
