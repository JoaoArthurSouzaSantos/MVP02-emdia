from pydantic import BaseModel

class MicroRegiaoSchema(BaseModel):
    id: int
    nome: str

class MicroRegiaoGetSchema(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True

