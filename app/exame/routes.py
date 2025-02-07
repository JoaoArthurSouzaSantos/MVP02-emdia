from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import ExameSchema
from db.models import ExameModel
from depends import get_db_session

exame_router = APIRouter()

@exame_router.post('/exame', response_model=ExameSchema)
def create_exame(prontuario: ExameSchema, db_session: Session = Depends(get_db_session)):
    exame_model = ExameModel(**prontuario.dict())
    db_session.add(exame_model)
    db_session.commit()
    db_session.refresh(exame_model)
    return exame_model

@exame_router.get('/exame/{id}', response_model=ExameSchema)
def get_exame(id: int, db_session: Session = Depends(get_db_session)):
    exame_model = db_session.query(ExameModel).filter(ExameModel.id == id).first()
    if not exame_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="exame não encontrado")
    return exame_model

@exame_router.put('/exame/{id}', response_model=ExameSchema)
def update_exame(id: int, prontuario: ExameSchema, db_session: Session = Depends(get_db_session)):
    exame_model = db_session.query(ExameModel).filter(ExameModel.id == id).first()
    if not exame_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="exame não encontrado")
    
    for key, value in prontuario.dict().items():
        setattr(exame_model, key, value)
    
    db_session.commit()
    db_session.refresh(exame_model)
    return exame_model

@exame_router.delete('/exame/{id}')
def delete_exame(id: int, db_session: Session = Depends(get_db_session)):
    exame_model = db_session.query(ExameModel).filter(ExameModel.id == id).first()
    if not exame_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="exame não encontrado")
    
    db_session.delete(exame_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Prontuario deleted successfully'}, status_code=status.HTTP_200_OK)