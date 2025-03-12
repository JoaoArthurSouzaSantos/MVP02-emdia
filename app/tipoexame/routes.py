from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from .schemas import TipoExameSchema
from db.models import TipoExameModel
from depends import get_db_session

tipo_exame_router = APIRouter()

@tipo_exame_router.post('/tipo_exame', response_model=TipoExameSchema)
def create_exame(exame: TipoExameSchema, db_session: Session = Depends(get_db_session)):
    tipo_exame_model = TipoExameModel(**exame.dict())
    db_session.add(tipo_exame_model)
    db_session.commit()
    db_session.refresh(tipo_exame_model)
    return tipo_exame_model

@tipo_exame_router.get('/tipo_exame/{id}', response_model=TipoExameSchema)
def get_tipo_exame(id: int, db_session: Session = Depends(get_db_session)):
    tipo_exame_model = db_session.query(TipoExameModel).filter(TipoExameModel.id == id).first()
    if not tipo_exame_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de Exame não encontrado")
    return tipo_exame_model

@tipo_exame_router.put('/tipo_exame/{id}', response_model=TipoExameSchema)
def update_tipo_exame(id: int, exame: TipoExameSchema, db_session: Session = Depends(get_db_session)):
    tipo_exame_model = db_session.query(TipoExameModel).filter(TipoExameModel.id == id).first()
    if not tipo_exame_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de Exame não encontrado")
    
    for key, value in exame.dict().items():
        setattr(tipo_exame_model, key, value)
    
    db_session.commit()
    db_session.refresh(tipo_exame_model)
    return tipo_exame_model

@tipo_exame_router.delete('/tipo_exame/{id}')
def delete_tipo_exame(id: int, db_session: Session = Depends(get_db_session)):
    tipo_exame_model = db_session.query(TipoExameModel).filter(TipoExameModel.id == id).first()
    if not tipo_exame_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de Exame não encontrado")
    
    db_session.delete(tipo_exame_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Tipo de exame deletado com successo'}, status_code=status.HTTP_200_OK)

@tipo_exame_router.get('/tipo_exame/active', response_model=List[TipoExameSchema])
def get_active_tipo_exames(db_session: Session = Depends(get_db_session)):
    active_tipo_exames = db_session.query(TipoExameModel).filter(TipoExameModel.status == True).all()
    return active_tipo_exames