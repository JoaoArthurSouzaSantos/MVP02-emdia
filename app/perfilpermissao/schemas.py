from pydantic import BaseModel

class PerfilPermissaoSchema(BaseModel):
    id: int
    id_perfil: int
    id_permissao: int

    class Config:
        orm_mode = True