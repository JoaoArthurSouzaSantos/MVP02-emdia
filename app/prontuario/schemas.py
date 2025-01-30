from pydantic import BaseModel

class ProntuarioExameSchema(BaseModel):
    id: int
    FkFuncionarioEspecialidade: int
    FkPaciente: int
    FkExame: int

    class Config:
        orm_mode = True