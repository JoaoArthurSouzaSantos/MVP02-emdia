from pydantic import BaseModel


class FuncionarioBase(BaseModel):
    cpf: str
    nome: str
    email: str
    id_perfil: int


class FuncionarioCreate(FuncionarioBase):
    password: str


class FuncionarioOut(FuncionarioBase):
    id: int
    password: str

    class Config:
        orm_mode = True
