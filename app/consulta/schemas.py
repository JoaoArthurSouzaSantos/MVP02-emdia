from pydantic import BaseModel
from typing import Optional

class ConsultaSchema(BaseModel):
    id: Optional[int]
    FkPaciente: str
    FkEspecialidade: int

    class Config:
        orm_mode = True
