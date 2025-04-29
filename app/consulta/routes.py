from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import ConsultaSchema  
from db.models import ConsultaModel , PacienteModel, BiometriaModel, FindriskModel, ExameModel
from depends import get_db_session  

consulta_router = APIRouter()

@consulta_router.post('/consultas', response_model=ConsultaSchema)
def create_consulta(consulta: ConsultaSchema, db_session: Session = Depends(get_db_session)):
    consulta_model = ConsultaModel(**consulta.dict())
    db_session.add(consulta_model)
    db_session.commit()
    db_session.refresh(consulta_model)
    return consulta_model

@consulta_router.get('/consultas/{id}', response_model=ConsultaSchema)
def get_consulta(id: int, db_session: Session = Depends(get_db_session)):
    consulta_model = db_session.query(ConsultaModel).filter(ConsultaModel.id == id).first()
    if not consulta_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta not found")
    return consulta_model

@consulta_router.put('/consultas/{id}', response_model=ConsultaSchema)
def update_consulta(id: int, consulta: ConsultaSchema, db_session: Session = Depends(get_db_session)):
    consulta_model = db_session.query(ConsultaModel).filter(ConsultaModel.id == id).first()
    if not consulta_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta not found")
    
    # Atualiza os campos com os valores fornecidos
    for key, value in consulta.dict().items():
        setattr(consulta_model, key, value)
    
    db_session.commit()
    db_session.refresh(consulta_model)
    return consulta_model

@consulta_router.delete('/consultas/{id}')
def delete_consulta(id: int, db_session: Session = Depends(get_db_session)):
    consulta_model = db_session.query(ConsultaModel).filter(ConsultaModel.id == id).first()
    if not consulta_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta not found")
    
    db_session.delete(consulta_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Consulta deleted successfully'}, status_code=status.HTTP_200_OK)

@consulta_router.get('/consultaNumeroSUS/{numeroSusPaciente}')
def consulta_numero_sus(numeroSusPaciente: str, db_session: Session = Depends(get_db_session)):
    paciente = db_session.query(PacienteModel).filter(PacienteModel.numeroSUS == numeroSusPaciente).first()
    if not paciente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente not found")

    # Fetch last biometria
    last_biometria = (
        db_session.query(BiometriaModel)
        .filter(BiometriaModel.fk_paciente == numeroSusPaciente)
        .order_by(BiometriaModel.data.desc())
        .first()
    )

    # Fetch last findrisk
    last_findrisk = (
        db_session.query(FindriskModel)
        .filter(FindriskModel.fk_paciente == numeroSusPaciente)
        .order_by(FindriskModel.data.desc())
        .first()
    )

    # Fetch patologias
    patologias = [p.patologia.nome for p in paciente.patologias]

    # Fetch last exam results
    last_exames = (
        db_session.query(ExameModel)
        .filter(ExameModel.fk_paciente == numeroSusPaciente)
        .order_by(ExameModel.data_realizacao.desc())
        .all()
    )

    hemoglobina_glicada = next((e.resultado for e in last_exames if e.tipo_exame.nome == "Hemoglobina Glicada"), None)
    glicemia_em_jejum = next((e.resultado for e in last_exames if e.tipo_exame.nome == "Glicemia em Jejum"), None)

    response = {
        "nome": paciente.nome,
        "data_nascimento": paciente.data_nascimento,
        "sexo": paciente.sexo,
        "micro_regiao": paciente.micro_regiao.nome if paciente.micro_regiao else None,
        "info": paciente.info,
        "patologia": patologias,
        "data": last_biometria.data if last_biometria else None,
        "peso": last_biometria.peso if last_biometria else None,
        "altura": last_biometria.altura if last_biometria else None,
        "imc": last_biometria.imc if last_biometria else None,
        "cintura": last_biometria.cintura if last_biometria else None,
        "nivelDeRisco": last_findrisk.classificacao if last_findrisk else None,
        "pontuacaoDoUltimoFindrisc": last_findrisk.pont_idade if last_findrisk else None,
        "dataDoUltimoFindrisc": last_findrisk.data if last_findrisk else None,
        "ultimoResultadoExame": {
            "HemoglobinaGlicada": hemoglobina_glicada,
            "GlicemiaEmJejum": glicemia_em_jejum,
        },
    }

    return response
