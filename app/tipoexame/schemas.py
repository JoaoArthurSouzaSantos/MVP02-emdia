from pydantic import BaseModel

class TipoExameSchema(BaseModel):
    id: int | None = None  # Campo opcional para criação
    nome: str  # Nome do Tipo de Exame
    status: bool  # Status ativo/inativo

    class Config:
        orm_mode = True
        from_attributes = True  # Necessário para usar from_orm


class TipoExameStatusSchema(BaseModel):
    nome: str  # Nome do Tipo de Exame

    class Config:
        orm_mode = True
        from_attributes = True  # Necessário para usar from_orm