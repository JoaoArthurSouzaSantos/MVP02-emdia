from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .model import EstratificacaoModel
from .schemas import EstratificacaoSchema
from depends import get_db_session

estratificacao_router = APIRouter()

@estratificacao_router.post('/estratificacao', response_model=EstratificacaoSchema)
def create_estratificacao(estratificacao: EstratificacaoSchema, db_session: Session = Depends(get_db_session)):
    estratificacao_model = EstratificacaoModel(**estratificacao.dict())
    db_session.add(estratificacao_model)
    db_session.commit()
    db_session.refresh(estratificacao_model)
    return estratificacao_model

@estratificacao_router.get('/estratificacao/{id}', response_model=EstratificacaoSchema)
def get_estratificacao(id: int, db_session: Session = Depends(get_db_session)):
    estratificacao_model = db_session.query(EstratificacaoModel).filter(EstratificacaoModel.id == id).first()
    if not estratificacao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estratificação not found")
    return estratificacao_model

@estratificacao_router.put('/estratificacao/{id}', response_model=EstratificacaoSchema)
def update_estratificacao(id: int, estratificacao: EstratificacaoSchema, db_session: Session = Depends(get_db_session)):
    estratificacao_model = db_session.query(EstratificacaoModel).filter(EstratificacaoModel.id == id).first()
    if not estratificacao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estratificação not found")
    
    for key, value in estratificacao.dict().items():
        setattr(estratificacao_model, key, value)
    
    db_session.commit()
    db_session.refresh(estratificacao_model)
    return estratificacao_model

@estratificacao_router.delete('/estratificacao/{id}')
def delete_estratificacao(id: int, db_session: Session = Depends(get_db_session)):
    estratificacao_model = db_session.query(EstratificacaoModel).filter(EstratificacaoModel.id == id).first()
    if not estratificacao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estratificação not found")
    
    db_session.delete(estratificacao_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Estratificação deleted successfully'}, status_code=status.HTTP_200_OK)
