from pydantic import BaseModel

class MicroRegiaoSchema(BaseModel):
    id: int
    nome: str

