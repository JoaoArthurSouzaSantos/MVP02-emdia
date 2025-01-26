from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import ConsultaSchema  # Supondo que você tenha um schema de Consulta
from db.models import ConsultaModel  # Supondo que você tenha o model de Consulta
from depends import get_db_session  # Função de dependência para obter a sessão do DB

consulta_router = APIRouter()

@consulta_router.post('/consultas', response_model=ConsultaSchema)
def create_consulta(consulta: ConsultaSchema, db_session: Session = Depends(get_db_session)):
    consulta_model = ConsultaModel(**consulta.dict())
    db_session.add(consulta_model)
    db_session.commit()
    db_session.refresh(consulta_model)
    return consulta_model

@consulta_router.get('/consultas/{id}', response_model=ConsultaSchema)
def get_consulta(id: int, db_session: Session = Depends(get_db_session)):
    consulta_model = db_session.query(ConsultaModel).filter(ConsultaModel.id == id).first()
    if not consulta_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta not found")
    return consulta_model

@consulta_router.put('/consultas/{id}', response_model=ConsultaSchema)
def update_consulta(id: int, consulta: ConsultaSchema, db_session: Session = Depends(get_db_session)):
    consulta_model = db_session.query(ConsultaModel).filter(ConsultaModel.id == id).first()
    if not consulta_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta not found")
    
    # Atualiza os campos com os valores fornecidos
    for key, value in consulta.dict().items():
        setattr(consulta_model, key, value)
    
    db_session.commit()
    db_session.refresh(consulta_model)
    return consulta_model

@consulta_router.delete('/consultas/{id}')
def delete_consulta(id: int, db_session: Session = Depends(get_db_session)):
    consulta_model = db_session.query(ConsultaModel).filter(ConsultaModel.id == id).first()
    if not consulta_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta not found")
    
    db_session.delete(consulta_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Consulta deleted successfully'}, status_code=status.HTTP_200_OK)
