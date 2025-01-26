from pydantic import BaseModel

class PerfilSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True