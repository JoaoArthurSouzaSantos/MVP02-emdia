from pydantic import BaseModel
from typing import Optional

class RetornosSchema(BaseModel):
    id: Optional[int]  # Opcional para criação (campo gerado automaticamente pelo banco)
    FkPaciente: str
    FkEspecialidade: int

    class Config:
        orm_mode = True
