from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import PatologiaSchema
from .model import PatologiaModel
from depends import get_db_session

patologia_router = APIRouter()

@patologia_router.post('/patologia', response_model=PatologiaSchema)
def create_patologia(patologia: PatologiaSchema, db_session: Session = Depends(get_db_session)):
    patologia_model = PatologiaModel(**patologia.dict())
    db_session.add(patologia_model)
    db_session.commit()
    db_session.refresh(patologia_model)
    return patologia_model

@patologia_router.get('/patologia/{id}', response_model=PatologiaSchema)
def get_patologia(id: int, db_session: Session = Depends(get_db_session)):
    patologia_model = db_session.query(PatologiaModel).filter(PatologiaModel.id == id).first()
    if not patologia_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patologia not found")
    return patologia_model

@patologia_router.put('/patologia/{id}', response_model=PatologiaSchema)
def update_patologia(id: int, patologia: PatologiaSchema, db_session: Session = Depends(get_db_session)):
    patologia_model = db_session.query(PatologiaModel).filter(PatologiaModel.id == id).first()
    if not patologia_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patologia not found")
    
    for key, value in patologia.dict().items():
        setattr(patologia_model, key, value)
    
    db_session.commit()
    db_session.refresh(patologia_model)
    return patologia_model

@patologia_router.delete('/patologia/{id}')
def delete_patologia(id: int, db_session: Session = Depends(get_db_session)):
    patologia_model = db_session.query(PatologiaModel).filter(PatologiaModel.id == id).first()
    if not patologia_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patologia not found")
    
    db_session.delete(patologia_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Patologia deleted successfully'}, status_code=status.HTTP_200_OK)