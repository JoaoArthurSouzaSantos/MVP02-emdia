from pydantic import BaseModel
from datetime import date

class ExameSchema(BaseModel):
    id: int
    data_realizacao: date
    resultado: str
    fk_paciente: int
    fk_tipo_exame: int
    fk_consulta: int

    class Config:
        orm_mode = True