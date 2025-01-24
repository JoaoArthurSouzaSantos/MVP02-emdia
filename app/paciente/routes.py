from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
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
    db.commit()
    db.refresh(db_paciente)
    return db_paciente


@paciente_router.delete("/delete/{numeroSUS}", response_model=PacienteSchema)
def delete_paciente(numeroSUS: str, db: Session = Depends(get_db_session)):
    db_paciente = db.query(PacienteModel).filter(PacienteModel.numeroSUS == numeroSUS).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    db.delete(db_paciente)
    db.commit()
    return db_paciente
