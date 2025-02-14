from pydantic import BaseModel

class PermissaoSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True