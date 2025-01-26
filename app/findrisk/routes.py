from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import FindriskSchema
from db.models import FindriskModel
from depends import get_db_session

findrisk_router = APIRouter()

@findrisk_router.post('/findrisk', response_model=FindriskSchema)
def create_findrisk(findrisk: FindriskSchema, db_session: Session = Depends(get_db_session)):
    findrisk_model = FindriskModel(**findrisk.dict())
    db_session.add(findrisk_model)
    db_session.commit()
    db_session.refresh(findrisk_model)
    return findrisk_model

@findrisk_router.get('/findrisk/{id}', response_model=FindriskSchema)
def get_findrisk(id: int, db_session: Session = Depends(get_db_session)):
    findrisk_model = db_session.query(FindriskModel).filter(FindriskModel.id == id).first()
    if not findrisk_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Findrisk not found")
    return findrisk_model

@findrisk_router.put('/findrisk/{id}', response_model=FindriskSchema)
def update_findrisk(id: int, findrisk: FindriskSchema, db_session: Session = Depends(get_db_session)):
    findrisk_model = db_session.query(FindriskModel).filter(FindriskModel.id == id).first()
    if not findrisk_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Findrisk not found")
    
    for key, value in findrisk.dict().items():
        setattr(findrisk_model, key, value)
    
    db_session.commit()
    db_session.refresh(findrisk_model)
    return findrisk_model

@findrisk_router.delete('/findrisk/{id}')
def delete_findrisk(id: int, db_session: Session = Depends(get_db_session)):
    findrisk_model = db_session.query(FindriskModel).filter(FindriskModel.id == id).first()
    if not findrisk_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Findrisk not found")
    
    db_session.delete(findrisk_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Findrisk deleted successfully'}, status_code=status.HTTP_200_OK)