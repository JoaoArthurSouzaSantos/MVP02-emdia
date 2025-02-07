from pydantic import BaseModel

class ExameSchema(BaseModel):
    id: int
    FkFuncionarioEspecialidade: int
    FkPaciente: int
    FkExame: int

    class Config:
        orm_mode = True