from pydantic import BaseModel
from typing import Optional

class MedicamentoSchema(BaseModel):
    id: Optional[int]  # Opcional para criação (auto-incrementado no banco)
    nome: str
    info: Optional[str]

    class Config:
        orm_mode = True
