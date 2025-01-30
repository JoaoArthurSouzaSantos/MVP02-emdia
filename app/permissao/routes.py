from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import PermissaoSchema
from db.models import PermissaoModel
from depends import get_db_session

permissao_router = APIRouter()

@permissao_router.post('/permissao', response_model=PermissaoSchema)
def create_permissao(permissao: PermissaoSchema, db_session: Session = Depends(get_db_session)):
    permissao_model = PermissaoModel(**permissao.dict())
    db_session.add(permissao_model)
    db_session.commit()
    db_session.refresh(permissao_model)
    return permissao_model

@permissao_router.get('/permissao/{id}', response_model=PermissaoSchema)
def get_permissao(id: int, db_session: Session = Depends(get_db_session)):
    permissao_model = db_session.query(PermissaoModel).filter(PermissaoModel.id == id).first()
    if not permissao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permissao not found")
    return permissao_model

@permissao_router.put('/permissao/{id}', response_model=PermissaoSchema)
def update_permissao(id: int, permissao: PermissaoSchema, db_session: Session = Depends(get_db_session)):
    permissao_model = db_session.query(PermissaoModel).filter(PermissaoModel.id == id).first()
    if not permissao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permissao not found")
    
    for key, value in permissao.dict().items():
        setattr(permissao_model, key, value)
    
    db_session.commit()
    db_session.refresh(permissao_model)
    return permissao_model

@permissao_router.delete('/permissao/{id}')
def delete_permissao(id: int, db_session: Session = Depends(get_db_session)):
    permissao_model = db_session.query(PermissaoModel).filter(PermissaoModel.id == id).first()
    if not permissao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permissao not found")
    
    db_session.delete(permissao_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Permissao deleted successfully'}, status_code=status.HTTP_200_OK)