from pydantic import BaseModel

class PerfilPermissaoSchema(BaseModel):
    id: int
    idPerfil: int
    idPermissao: int

    class Config:
        orm_mode = True