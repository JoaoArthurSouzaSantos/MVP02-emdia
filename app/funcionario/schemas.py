from pydantic import BaseModel
from typing import Optional


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


class FuncionarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    id_perfil: Optional[int] = None
    password: Optional[str] = None
