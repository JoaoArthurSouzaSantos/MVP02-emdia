from pydantic import BaseModel

class PacientePatologiaSchema(BaseModel):
    id: int
    fk_patologia: int
    fk_paciente: int

    class Config:
        orm_mode = True
