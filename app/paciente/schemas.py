from pydantic import BaseModel

class PacienteSchema(BaseModel):
    nome: str
    email: str
    cpf: str
    telefone: str
    microRegiao: str
    numeroSUS: str
    dataNascimento: str
    sexo: str
    info: str