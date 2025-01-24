from pydantic import BaseModel

class PacienteSchema(BaseModel):
    
    numeroSUS: str
    nome: str
    email: str
    telefone: str
    sexo: str
    info: str
    dataNascimento: str
    microRegiao: str