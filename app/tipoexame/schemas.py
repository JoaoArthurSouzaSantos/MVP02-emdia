from pydantic import BaseModel

class TipoExameSchema(BaseModel):
    id: int
    nome: str
    resultado: str
    data_realizacao: str

    class Config:
        orm_mode = True