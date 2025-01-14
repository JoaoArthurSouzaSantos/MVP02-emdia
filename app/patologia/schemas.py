from pydantic import BaseModel

class PatologiaSchema(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True