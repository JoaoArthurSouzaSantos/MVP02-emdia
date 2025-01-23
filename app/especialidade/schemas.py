from pydantic import BaseModel
from typing import Optional

class EspecialidadeSchema(BaseModel):
    id: Optional[int]  # Opcional para criação (auto-incrementado no banco)
    nome: str

    class Config:
        orm_mode = True
