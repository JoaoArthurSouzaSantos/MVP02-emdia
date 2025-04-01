from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from db.models import TipoMedicamentoModel
from .schemas import TipoMedicamentoSchema
from depends import get_db_session

tipo_medicamento_router = APIRouter()

@tipo_medicamento_router.post('/tipomedicamentos', response_model=TipoMedicamentoSchema, status_code=status.HTTP_201_CREATED)
def create_tipo_medicamento(tipo_medicamento: TipoMedicamentoSchema, db_session: Session = Depends(get_db_session)):
    new_tipo_medicamento = TipoMedicamentoModel(**tipo_medicamento.dict(exclude_unset=True))
    db_session.add(new_tipo_medicamento)
    db_session.commit()
    db_session.refresh(new_tipo_medicamento)
    return new_tipo_medicamento

@tipo_medicamento_router.get('/tipomedicamentos', response_model=List[TipoMedicamentoSchema])
def get_all_tipos_medicamento(db_session: Session = Depends(get_db_session)):
    return db_session.query(TipoMedicamentoModel).all()

@tipo_medicamento_router.get('/tipomedicamentos/{id}', response_model=TipoMedicamentoSchema)
def get_tipo_medicamento(id: int, db_session: Session = Depends(get_db_session)):
    tipo_medicamento = db_session.query(TipoMedicamentoModel).filter(TipoMedicamentoModel.id == id).first()
    if not tipo_medicamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipoMedicamento not found")
    return tipo_medicamento

@tipo_medicamento_router.put('/tipomedicamentos/{id}', response_model=TipoMedicamentoSchema)
def update_tipo_medicamento(id: int, tipo_medicamento: TipoMedicamentoSchema, db_session: Session = Depends(get_db_session)):
    existing_tipo_medicamento = db_session.query(TipoMedicamentoModel).filter(TipoMedicamentoModel.id == id).first()
    if not existing_tipo_medicamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipoMedicamento not found")
    for key, value in tipo_medicamento.dict(exclude_unset=True).items():
        setattr(existing_tipo_medicamento, key, value)
    db_session.commit()
    db_session.refresh(existing_tipo_medicamento)
    return existing_tipo_medicamento

@tipo_medicamento_router.delete('/tipomedicamentos/{id}')
def delete_tipo_medicamento(id: int, db_session: Session = Depends(get_db_session)):
    existing_tipo_medicamento = db_session.query(TipoMedicamentoModel).filter(TipoMedicamentoModel.id == id).first()
    if not existing_tipo_medicamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipoMedicamento not found")
    db_session.delete(existing_tipo_medicamento)
    db_session.commit()
    return JSONResponse(content={'msg': 'TipoMedicamento deleted successfully'}, status_code=status.HTTP_200_OK)
