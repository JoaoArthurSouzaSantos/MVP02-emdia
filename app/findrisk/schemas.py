from pydantic import BaseModel
from datetime import date

class FindriskSchema(BaseModel):
    data: date
    pont_historico_familiar_de_diabetes: str
    pont_historico_de_glicemia_elevada: str
    classificacao: str
    pont_idade: str
    pont_imc: str
    pont_circuferencia_cintura: str
    pont_atv_fisica: str
    pont_ingestao_frutas_e_verduras: str
    pont_hipertensao: str
    FkPaciente: int

    class Config:
        orm_mode = True