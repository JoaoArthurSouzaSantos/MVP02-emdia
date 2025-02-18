from pydantic import BaseModel

class TipoExameSchema(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True