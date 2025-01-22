from pydantic import BaseModel

class ProntuarioExameSchema(BaseModel):
    id: int
    FkFuncionario: int
    FkPaciente: str
    FkExame: str

    class Config:
        orm_mode = True