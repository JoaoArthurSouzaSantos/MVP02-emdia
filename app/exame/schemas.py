from pydantic import BaseModel

class ExameSchema(BaseModel):
    id: int
    data_realizacao: str
    resultado: str
    fk_paciente: int
    fk_tipo_exame: int
    fk_consulta: int

    class Config:
        orm_mode = True