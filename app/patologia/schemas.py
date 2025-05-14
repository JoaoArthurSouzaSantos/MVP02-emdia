from pydantic import BaseModel

class PatologiaSchema(BaseModel):
    nome: str
    icon: int

    class Config:
        orm_mode = True