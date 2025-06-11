from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from paciente import schemas
from db import models
from depends import get_db_session

paciente_router = APIRouter()

@paciente_router.post("/pacientes/", response_model=schemas.Paciente)
def create_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db_session)):
    db_paciente = models.PacienteModel(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    HTTPException(200)
    return db_paciente

@paciente_router.get("/pacientes/", response_model=List[schemas.Paciente])
def read_pacientes(db: Session = Depends(get_db_session)):
    pacientes = db.query(models.PacienteModel).all()
    HTTPException(200)
    return pacientes

@paciente_router.get("/pacientes/microregiao")
def get_pacientes_with_microregiao(db: Session = Depends(get_db_session)):
    pacientes = db.query(models.PacienteModel).all()
    result = []
    for p in pacientes:
        microregiao_name = p.micro_regiao.nome if p.micro_regiao else None
        result.append({
            "numeroSUS": p.numeroSUS,
            "data_nascimento": p.data_nascimento,
            "cpf": p.cpf,
            "sexo": p.sexo,
            "info": p.info,
            "telefone": p.telefone,
            "email": p.email,
            "nome": p.nome,
            "micro_regiao_id": p.micro_regiao_id,
            "micro_regiao_nome": microregiao_name
        })
    return result

@paciente_router.get("/pacientes/{numeroSUS}", response_model=schemas.Paciente)
def read_paciente(numeroSUS: str, db: Session = Depends(get_db_session)):
    int(numeroSUS)
    paciente = db.query(models.PacienteModel).filter(models.PacienteModel.numeroSUS == numeroSUS).first()
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    HTTPException(200)
    return paciente

@paciente_router.put("/pacientes/{numeroSUS}", response_model=schemas.Paciente)
def update_paciente(numeroSUS: str, paciente: schemas.PacienteUpdate, db: Session = Depends(get_db_session)):
    db_paciente = db.query(models.PacienteModel).filter(models.PacienteModel.numeroSUS == numeroSUS).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    for key, value in paciente.dict().items():
        setattr(db_paciente, key, value)
    db.commit()
    db.refresh(db_paciente)
    HTTPException(200)
    return db_paciente

@paciente_router.delete("/pacientes/{numeroSUS}")
def delete_paciente(numeroSUS: str, db: Session = Depends(get_db_session)):
    db_paciente = db.query(models.PacienteModel).filter(models.PacienteModel.numeroSUS == numeroSUS).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    db.delete(db_paciente)
    db.commit()
    HTTPException(200)
    return {"detail": "Paciente deleted"}

@paciente_router.get("/pacientes/full-data/{numeroSUS}")
def get_full_data(numeroSUS: str, db: Session = Depends(get_db_session)):
    paciente = db.query(models.PacienteModel).filter(models.PacienteModel.numeroSUS == numeroSUS).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente not found")
    hemoglobina_glicada = next(
        (e.resultado for e in paciente.exames if e.tipo_exame.nome == "Hemoglobina Glicada"), None
    )
    glicemia_jejum = next(
        (e.resultado for e in paciente.exames if e.tipo_exame.nome == "Glicemia em Jejum"), None
    )
    last_findrisk = paciente.findrisk[-1] if paciente.findrisk else None

    return {
        "paciente": {
            "numeroSUS": paciente.numeroSUS,
            "nome": paciente.nome,
            "email": paciente.email,
            "telefone": paciente.telefone,
            "data_nascimento": paciente.data_nascimento,
            "sexo": paciente.sexo,
            "cpf": paciente.cpf,
            "micro_regiao": {
                "id": paciente.micro_regiao_id,
                "nome": paciente.micro_regiao.nome if paciente.micro_regiao else None
            },
        },
        "biometrias": [
            {
                "id": b.id,
                "data": b.data,
                "peso": b.peso,
                "altura": b.altura,
                "imc": b.imc,
                "cintura": b.cintura
            }
            for b in paciente.biometrias
        ],
        "consultas": [
            {
                "id": c.id,
                "data": c.data,
                "status": c.status,
                "observacoes": c.observacoes
            } for c in paciente.consultas
        ],
        "medicamentos": [
            {
                "id": m.id,
                "status": m.status,
                "frequencia": m.frequencia,
                "dosagem": m.dosagem,
                "nome_medicamento": m.tipo_medicamento.nome if m.tipo_medicamento else None
            } for m in paciente.medicamentos
        ],
        "exames": [
            {
                "id": e.id,
                "data_realizacao": e.data_realizacao,
                "resultado": e.resultado,
                "nome_exame": e.tipo_exame.nome
            } for e in paciente.exames
        ],
        "findrisk": [
            {
                "id": f.id,
                "data": f.data,
                "classificacao": f.classificacao,
                "pont_historico_familiar_de_diabetes": f.pont_historico_familiar_de_diabetes,
                "pont_historico_de_glicemia_elevada": f.pont_historico_de_glicemia_elevada,
                "pont_idade": f.pont_idade,
                "pont_imc": f.pont_imc,
                "pont_circunferencia_cintura": f.pont_circunferencia_cintura,
                "pont_atv_fisica": f.pont_atv_fisica,
                "pont_ingestao_frutas_e_verduras": f.pont_ingestao_frutas_e_verduras,
                "pont_hipertensao": f.pont_hipertensao
            } for f in paciente.findrisk
        ],
        "patologias": [
            {
                "nome": p.patologia.nome,
                "icon": p.patologia.icon
            } for p in paciente.patologias
        ],
        "nivelDeRisco": last_findrisk.classificacao if last_findrisk else None,
        "hemoglobinaGlicada": hemoglobina_glicada,
        "glicemiaJejum": glicemia_jejum
    }


