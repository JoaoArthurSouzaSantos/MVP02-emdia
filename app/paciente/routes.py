from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
<<<<<<< HEAD
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
    return db_paciente

@paciente_router.get("/pacientes/", response_model=List[schemas.Paciente])
def read_pacientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_session)):
    pacientes = db.query(models.PacienteModel).offset(skip).limit(limit).all()
    return pacientes

@paciente_router.get("/pacientes/{numeroSUS}", response_model=schemas.Paciente)
def read_paciente(numeroSUS: str, db: Session = Depends(get_db_session)):
    paciente = db.query(models.PacienteModel).filter(models.PacienteModel.numeroSUS == numeroSUS).first()
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    return paciente

@paciente_router.put("/pacientes/{numeroSUS}", response_model=schemas.Paciente)
def update_paciente(numeroSUS: str, paciente: schemas.PacienteUpdate, db: Session = Depends(get_db_session)):
    db_paciente = db.query(models.PacienteModel).filter(models.PacienteModel.numeroSUS == numeroSUS).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    for key, value in paciente.dict().items():
        setattr(db_paciente, key, value)
=======
from depends import get_db_session, token_verifier
from paciente.models import PacienteModel
from paciente.schemas import PacienteSchema
from consulta.models import *
from sqlalchemy.exc import IntegrityError

# Define o router com proteção global
paciente_router = APIRouter(
    dependencies=[Depends(token_verifier)]  # Aplica verificação de token a todas as rotas
)

@paciente_router.post("/create/", response_model=PacienteSchema)
def create_paciente(paciente_create: PacienteSchema, db: Session = Depends(get_db_session)):
    paciente_existente = db.query(PacienteModel).filter(PacienteModel.numeroSUS == paciente_create.numeroSUS).first()
    if paciente_existente:
        raise HTTPException(status_code=400, detail="Paciente com o número SUS já existe")
    
    try:
        db_paciente = PacienteModel(**paciente_create.dict())
        db.add(db_paciente)
        db.commit()
        db.refresh(db_paciente)
        return db_paciente
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Erro de integridade ao criar o paciente")


@paciente_router.get("/read/{numeroSUS}", response_model=PacienteSchema)
def read_paciente(numeroSUS: str, db: Session = Depends(get_db_session)):
    paciente = db.query(PacienteModel).filter(PacienteModel.numeroSUS == numeroSUS).first()
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente


@paciente_router.put("/update/{numeroSUS}", response_model=PacienteSchema)
def update_paciente(numeroSUS: str, paciente_update: PacienteSchema, db: Session = Depends(get_db_session)):
    db_paciente = db.query(PacienteModel).filter(PacienteModel.numeroSUS == numeroSUS).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    for field, value in paciente_update.dict(exclude_unset=True).items():
        setattr(db_paciente, field, value)
>>>>>>> 0ee348ad6d8728d190f7f884d222995af019cc64
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

<<<<<<< HEAD
@paciente_router.delete("/pacientes/{numeroSUS}")
def delete_paciente(numeroSUS: str, db: Session = Depends(get_db_session)):
    db_paciente = db.query(models.PacienteModel).filter(models.PacienteModel.numeroSUS == numeroSUS).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    db.delete(db_paciente)
    db.commit()
    return {"detail": "Paciente deleted"}
=======

@paciente_router.delete("/delete/{numeroSUS}", response_model=PacienteSchema)
def delete_paciente(numeroSUS: str, db: Session = Depends(get_db_session)):
    db_paciente = db.query(PacienteModel).filter(PacienteModel.numeroSUS == numeroSUS).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    db.delete(db_paciente)
    db.commit()
    return db_paciente
>>>>>>> 0ee348ad6d8728d190f7f884d222995af019cc64
