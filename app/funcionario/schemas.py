from pydantic import BaseModel


class FuncionarioBase(BaseModel):
    cpf: str
    nome: str
    email: str
    idPerfil: int


class FuncionarioCreate(FuncionarioBase):
    password: str


class FuncionarioOut(FuncionarioBase):
    id: int
    password: str
