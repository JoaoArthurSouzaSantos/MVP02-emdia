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
