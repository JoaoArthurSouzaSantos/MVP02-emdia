from pydantic import BaseModel

class TipoExameSchema(BaseModel):
    id: int
    nome: str
    status: bool  # New field

    class Config:
        orm_mode = True