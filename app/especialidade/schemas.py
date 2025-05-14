from pydantic import BaseModel
from typing import Optional

class EspecialidadeSchema(BaseModel):
    nome: str

    class Config:
        orm_mode = True
