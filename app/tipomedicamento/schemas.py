from pydantic import BaseModel
from typing import Optional

class MedicamentoSchema(BaseModel):
    id: Optional[int]
    nome: str
    info: Optional[str]

    class Config:
        orm_mode = True
