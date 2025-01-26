from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.models import RetornosModel
from .schemas import RetornosSchema
from depends import get_db_session

retornos_router = APIRouter()

@retornos_router.post('/retornos', response_model=RetornosSchema)
def create_retorno(retorno: RetornosSchema, db_session: Session = Depends(get_db_session)):
    retorno_model = RetornosModel(**retorno.dict())
    db_session.add(retorno_model)
    db_session.commit()
    db_session.refresh(retorno_model)
    return retorno_model

@retornos_router.get('/retornos/{id}', response_model=RetornosSchema)
def get_retorno(id: int, db_session: Session = Depends(get_db_session)):
    retorno_model = db_session.query(RetornosModel).filter(RetornosModel.id == id).first()
    if not retorno_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Retorno not found")
    return retorno_model

@retornos_router.put('/retornos/{id}', response_model=RetornosSchema)
def update_retorno(id: int, retorno: RetornosSchema, db_session: Session = Depends(get_db_session)):
    retorno_model = db_session.query(RetornosModel).filter(RetornosModel.id == id).first()
    if not retorno_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Retorno not found")
    
    for key, value in retorno.dict(exclude_unset=True).items():
        setattr(retorno_model, key, value)
    
    db_session.commit()
    db_session.refresh(retorno_model)
    return retorno_model

@retornos_router.delete('/retornos/{id}')
def delete_retorno(id: int, db_session: Session = Depends(get_db_session)):
    retorno_model = db_session.query(RetornosModel).filter(RetornosModel.id == id).first()
    if not retorno_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Retorno not found")
    
    db_session.delete(retorno_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Retorno deleted successfully'}, status_code=status.HTTP_200_OK)
