from pydantic import BaseModel

class PacientePatologiaSchema(BaseModel):
    id: int
    FkPatologia: int
    FkPaciente: str

    class Config:
        orm_mode = True
