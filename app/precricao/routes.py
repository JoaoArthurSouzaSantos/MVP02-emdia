from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.models import PrescricaoModel
from .schemas import PrescricaoSchema
from depends import get_db_session

prescricao_router = APIRouter()

@prescricao_router.post('/prescricao', response_model=PrescricaoSchema)
def create_prescricao(prescricao: PrescricaoSchema, db_session: Session = Depends(get_db_session)):
    prescricao_model = PrescricaoModel(**prescricao.dict())
    db_session.add(prescricao_model)
    db_session.commit()
    db_session.refresh(prescricao_model)
    return prescricao_model

@prescricao_router.get('/prescricao/{id}', response_model=PrescricaoSchema)
def get_prescricao(id: int, db_session: Session = Depends(get_db_session)):
    prescricao_model = db_session.query(PrescricaoModel).filter(PrescricaoModel.id == id).first()
    if not prescricao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prescricao not found")
    return prescricao_model

@prescricao_router.put('/prescricao/{id}', response_model=PrescricaoSchema)
def update_prescricao(id: int, prescricao: PrescricaoSchema, db_session: Session = Depends(get_db_session)):
    prescricao_model = db_session.query(PrescricaoModel).filter(PrescricaoModel.id == id).first()
    if not prescricao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prescricao not found")
    
    for key, value in prescricao.dict().items():
        setattr(prescricao_model, key, value)
    
    db_session.commit()
    db_session.refresh(prescricao_model)
    return prescricao_model

@prescricao_router.delete('/prescricao/{id}')
def delete_prescricao(id: int, db_session: Session = Depends(get_db_session)):
    prescricao_model = db_session.query(PrescricaoModel).filter(PrescricaoModel.id == id).first()
    if not prescricao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prescricao not found")
    
    db_session.delete(prescricao_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Prescricao deleted successfully'}, status_code=status.HTTP_200_OK)
