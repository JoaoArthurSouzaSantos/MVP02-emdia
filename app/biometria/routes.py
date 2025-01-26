from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import BiometriaSchema
from db.models import BiometriaModel
from depends import get_db_session

biometria_router = APIRouter()

@biometria_router.post('/biometria', response_model=BiometriaSchema)
def create_biometria(biometria: BiometriaSchema, db_session: Session = Depends(get_db_session)):
    biometria_model = BiometriaModel(**biometria.dict())
    db_session.add(biometria_model)
    db_session.commit()
    db_session.refresh(biometria_model)
    return biometria_model

@biometria_router.get('/biometria/{id}', response_model=BiometriaSchema)
def get_biometria(id: int, db_session: Session = Depends(get_db_session)):
    biometria_model = db_session.query(BiometriaModel).filter(BiometriaModel.id == id).first()
    if not biometria_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Biometria not found")
    return biometria_model

@biometria_router.put('/biometria/{id}', response_model=BiometriaSchema)
def update_biometria(id: int, biometria: BiometriaSchema, db_session: Session = Depends(get_db_session)):
    biometria_model = db_session.query(BiometriaModel).filter(BiometriaModel.id == id).first()
    if not biometria_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Biometria not found")
    
    for key, value in biometria.dict().items():
        setattr(biometria_model, key, value)
    
    db_session.commit()
    db_session.refresh(biometria_model)
    return biometria_model

@biometria_router.delete('/biometria/{id}')
def delete_biometria(id: int, db_session: Session = Depends(get_db_session)):
    biometria_model = db_session.query(BiometriaModel).filter(BiometriaModel.id == id).first()
    if not biometria_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Biometria not found")
    
    db_session.delete(biometria_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Biometria deleted successfully'}, status_code=status.HTTP_200_OK)