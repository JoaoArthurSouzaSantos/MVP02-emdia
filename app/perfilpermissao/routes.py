from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import PerfilPermissaoSchema
from .model import PerfilPermissaoModel
from depends import get_db_session

perfilpermissao_router = APIRouter()

@perfilpermissao_router.post('/perfilpermissao', response_model=PerfilPermissaoSchema)
def create_perfilpermissao(perfilpermissao: PerfilPermissaoSchema, db_session: Session = Depends(get_db_session)):
    perfilpermissao_model = PerfilPermissaoModel(**perfilpermissao.dict())
    db_session.add(perfilpermissao_model)
    db_session.commit()
    db_session.refresh(perfilpermissao_model)
    return perfilpermissao_model

@perfilpermissao_router.get('/perfilpermissao/{id}', response_model=PerfilPermissaoSchema)
def get_perfilpermissao(id: int, db_session: Session = Depends(get_db_session)):
    perfilpermissao_model = db_session.query(PerfilPermissaoModel).filter(PerfilPermissaoModel.id == id).first()
    if not perfilpermissao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PerfilPermissao not found")
    return perfilpermissao_model

@perfilpermissao_router.put('/perfilpermissao/{id}', response_model=PerfilPermissaoSchema)
def update_perfilpermissao(id: int, perfilpermissao: PerfilPermissaoSchema, db_session: Session = Depends(get_db_session)):
    perfilpermissao_model = db_session.query(PerfilPermissaoModel).filter(PerfilPermissaoModel.id == id).first()
    if not perfilpermissao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PerfilPermissao not found")
    
    for key, value in perfilpermissao.dict().items():
        setattr(perfilpermissao_model, key, value)
    
    db_session.commit()
    db_session.refresh(perfilpermissao_model)
    return perfilpermissao_model

@perfilpermissao_router.delete('/perfilpermissao/{id}')
def delete_perfilpermissao(id: int, db_session: Session = Depends(get_db_session)):
    perfilpermissao_model = db_session.query(PerfilPermissaoModel).filter(PerfilPermissaoModel.id == id).first()
    if not perfilpermissao_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PerfilPermissao not found")
    
    db_session.delete(perfilpermissao_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'PerfilPermissao deleted successfully'}, status_code=status.HTTP_200_OK)