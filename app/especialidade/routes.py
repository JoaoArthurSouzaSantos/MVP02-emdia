from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .model import EspecialidadeModel
from .schemas import EspecialidadeSchema
from depends import get_db_session

especialidade_router = APIRouter()

@especialidade_router.post('/especialidades', response_model=EspecialidadeSchema)
def create_especialidade(especialidade: EspecialidadeSchema, db_session: Session = Depends(get_db_session)):
    especialidade_model = EspecialidadeModel(**especialidade.dict())
    db_session.add(especialidade_model)
    db_session.commit()
    db_session.refresh(especialidade_model)
    return especialidade_model

@especialidade_router.get('/especialidades/{id}', response_model=EspecialidadeSchema)
def get_especialidade(id: int, db_session: Session = Depends(get_db_session)):
    especialidade_model = db_session.query(EspecialidadeModel).filter(EspecialidadeModel.id == id).first()
    if not especialidade_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Especialidade not found")
    return especialidade_model

@especialidade_router.put('/especialidades/{id}', response_model=EspecialidadeSchema)
def update_especialidade(id: int, especialidade: EspecialidadeSchema, db_session: Session = Depends(get_db_session)):
    especialidade_model = db_session.query(EspecialidadeModel).filter(EspecialidadeModel.id == id).first()
    if not especialidade_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Especialidade not found")
    
    for key, value in especialidade.dict(exclude_unset=True).items():
        setattr(especialidade_model, key, value)
    
    db_session.commit()
    db_session.refresh(especialidade_model)
    return especialidade_model

@especialidade_router.delete('/especialidades/{id}')
def delete_especialidade(id: int, db_session: Session = Depends(get_db_session)):
    especialidade_model = db_session.query(EspecialidadeModel).filter(EspecialidadeModel.id == id).first()
    if not especialidade_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Especialidade not found")
    
    db_session.delete(especialidade_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Especialidade deleted successfully'}, status_code=status.HTTP_200_OK)
