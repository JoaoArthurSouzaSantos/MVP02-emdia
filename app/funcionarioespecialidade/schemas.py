from pydantic import BaseModel
from typing import Optional

class FuncionarioEspecialidadeSchema(BaseModel):
    id: Optional[int]  # Opcional para criação (auto-incrementado no banco)
    FkFuncionario: int
    FkEspecialidade: int

    class Config:
        orm_mode = True
