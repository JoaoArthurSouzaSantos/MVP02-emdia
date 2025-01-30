from pydantic import BaseModel

class PacientePatologiaSchema(BaseModel):
    id: int
    FkPatologia: int
    FkPaciente: int

    class Config:
        orm_mode = True
