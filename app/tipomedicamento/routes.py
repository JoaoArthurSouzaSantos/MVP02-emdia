from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.models import MedicamentoModel
from .schemas import MedicamentoSchema
from depends import get_db_session

tipo_medicamento_router = APIRouter()

@tipo_medicamento_router.post('/medicamento', response_model=MedicamentoSchema)
def create_medicamento(medicamento: MedicamentoSchema, db_session: Session = Depends(get_db_session)):
    medicamento_model = MedicamentoModel(**medicamento.dict())
    db_session.add(medicamento_model)
    db_session.commit()
    db_session.refresh(medicamento_model)
    return medicamento_model

@tipo_medicamento_router.get('/medicamento/{id}', response_model=MedicamentoSchema)
def get_medicamento(id: int, db_session: Session = Depends(get_db_session)):
    medicamento_model = db_session.query(MedicamentoModel).filter(MedicamentoModel.id == id).first()
    if not medicamento_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medicamento not found")
    return medicamento_model

@tipo_medicamento_router.put('/medicamento/{id}', response_model=MedicamentoSchema)
def update_medicamento(id: int, medicamento: MedicamentoSchema, db_session: Session = Depends(get_db_session)):
    medicamento_model = db_session.query(MedicamentoModel).filter(MedicamentoModel.id == id).first()
    if not medicamento_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medicamento not found")
    
    for key, value in medicamento.dict(exclude_unset=True).items():
        setattr(medicamento_model, key, value)
    
    db_session.commit()
    db_session.refresh(medicamento_model)
    return medicamento_model

@tipo_medicamento_router.delete('/medicamento/{id}')
def delete_medicamento(id: int, db_session: Session = Depends(get_db_session)):
    medicamento_model = db_session.query(MedicamentoModel).filter(MedicamentoModel.id == id).first()
    if not medicamento_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medicamento not found")
    
    db_session.delete(medicamento_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Medicamento deleted successfully'}, status_code=status.HTTP_200_OK)
