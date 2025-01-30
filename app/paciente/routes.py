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
def read_pacientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_session)):
    pacientes = db.query(models.PacienteModel).offset(skip).limit(limit).all()
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
