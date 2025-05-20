from pydantic import BaseModel

class FuncionarioEspecialidadeBase(BaseModel):
    fk_funcionario: int
    fk_especialidade: int


class FuncionarioEspecialidadeOut(FuncionarioEspecialidadeBase):
    id: int

    class Config:
        orm_mode = True