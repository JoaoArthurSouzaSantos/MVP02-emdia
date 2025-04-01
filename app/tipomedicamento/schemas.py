from pydantic import BaseModel
from typing import Optional

class TipoMedicamentoSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    info: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True
