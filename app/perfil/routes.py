from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import PerfilSchema
from db.models import PerfilModel
from depends import get_db_session

perfil_router = APIRouter()

@perfil_router.post('/perfil', response_model=PerfilSchema)
def create_perfil(perfil: PerfilSchema, db_session: Session = Depends(get_db_session)):
    perfil_model = PerfilModel(**perfil.dict())
    db_session.add(perfil_model)
    db_session.commit()
    db_session.refresh(perfil_model)
    return perfil_model

@perfil_router.get('/perfil/{id}', response_model=PerfilSchema)
def get_perfil(id: int, db_session: Session = Depends(get_db_session)):
    perfil_model = db_session.query(PerfilModel).filter(PerfilModel.id == id).first()
    if not perfil_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Perfil not found")
    return perfil_model

@perfil_router.put('/perfil/{id}', response_model=PerfilSchema)
def update_perfil(id: int, perfil: PerfilSchema, db_session: Session = Depends(get_db_session)):
    perfil_model = db_session.query(PerfilModel).filter(PerfilModel.id == id).first()
    if not perfil_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Perfil not found")
    
    for key, value in perfil.dict().items():
        setattr(perfil_model, key, value)
    
    db_session.commit()
    db_session.refresh(perfil_model)
    return perfil_model

@perfil_router.delete('/perfil/{id}')
def delete_perfil(id: int, db_session: Session = Depends(get_db_session)):
    perfil_model = db_session.query(PerfilModel).filter(PerfilModel.id == id).first()
    if not perfil_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Perfil not found")
    
    db_session.delete(perfil_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Perfil deleted successfully'}, status_code=status.HTTP_200_OK)