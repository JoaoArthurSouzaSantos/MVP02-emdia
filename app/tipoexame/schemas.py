from pydantic import BaseModel

class TipoExameSchema(BaseModel):
    nome: str  
    status: bool 
    class Config:
        orm_mode = True
        from_attributes = True  # Necessário para usar from_orm


class TipoExameStatusSchema(BaseModel):
    id: int  # ID do Tipo de Exame
    nome: str  # Nome do Tipo de Exame

    class Config:
        orm_mode = True
        from_attributes = True 