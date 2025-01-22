from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import ProntuarioExameSchema
from .model import ProntuarioExame
from depends import get_db_session

prontuario_router = APIRouter()

@prontuario_router.post('/prontuario', response_model=ProntuarioExameSchema)
def create_prontuario(prontuario: ProntuarioExameSchema, db_session: Session = Depends(get_db_session)):
    prontuario_model = ProntuarioExame(**prontuario.dict())
    db_session.add(prontuario_model)
    db_session.commit()
    db_session.refresh(prontuario_model)
    return prontuario_model

@prontuario_router.get('/prontuario/{id}', response_model=ProntuarioExameSchema)
def get_prontuario(id: int, db_session: Session = Depends(get_db_session)):
    prontuario_model = db_session.query(ProntuarioExame).filter(ProntuarioExame.id == id).first()
    if not prontuario_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prontuario not found")
    return prontuario_model

@prontuario_router.put('/prontuario/{id}', response_model=ProntuarioExameSchema)
def update_prontuario(id: int, prontuario: ProntuarioExameSchema, db_session: Session = Depends(get_db_session)):
    prontuario_model = db_session.query(ProntuarioExame).filter(ProntuarioExame.id == id).first()
    if not prontuario_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prontuario not found")
    
    for key, value in prontuario.dict().items():
        setattr(prontuario_model, key, value)
    
    db_session.commit()
    db_session.refresh(prontuario_model)
    return prontuario_model

@prontuario_router.delete('/prontuario/{id}')
def delete_prontuario(id: int, db_session: Session = Depends(get_db_session)):
    prontuario_model = db_session.query(ProntuarioExame).filter(ProntuarioExame.id == id).first()
    if not prontuario_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prontuario not found")
    
    db_session.delete(prontuario_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Prontuario deleted successfully'}, status_code=status.HTTP_200_OK)