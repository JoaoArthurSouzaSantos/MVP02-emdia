from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .model import FuncionarioEspecialidadeModel
from .schemas import FuncionarioEspecialidadeSchema
from depends import get_db_session

funcionario_especialidade_router = APIRouter()

@funcionario_especialidade_router.post('/funcionario_especialidade', response_model=FuncionarioEspecialidadeSchema)
def create_funcionario_especialidade(funcionario_especialidade: FuncionarioEspecialidadeSchema, db_session: Session = Depends(get_db_session)):
    funcionario_especialidade_model = FuncionarioEspecialidadeModel(**funcionario_especialidade.dict())
    db_session.add(funcionario_especialidade_model)
    db_session.commit()
    db_session.refresh(funcionario_especialidade_model)
    return funcionario_especialidade_model

@funcionario_especialidade_router.get('/funcionario_especialidade/{id}', response_model=FuncionarioEspecialidadeSchema)
def get_funcionario_especialidade(id: int, db_session: Session = Depends(get_db_session)):
    funcionario_especialidade_model = db_session.query(FuncionarioEspecialidadeModel).filter(FuncionarioEspecialidadeModel.id == id).first()
    if not funcionario_especialidade_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Funcionario Especialidade not found")
    return funcionario_especialidade_model

@funcionario_especialidade_router.put('/funcionario_especialidade/{id}', response_model=FuncionarioEspecialidadeSchema)
def update_funcionario_especialidade(id: int, funcionario_especialidade: FuncionarioEspecialidadeSchema, db_session: Session = Depends(get_db_session)):
    funcionario_especialidade_model = db_session.query(FuncionarioEspecialidadeModel).filter(FuncionarioEspecialidadeModel.id == id).first()
    if not funcionario_especialidade_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Funcionario Especialidade not found")
    
    for key, value in funcionario_especialidade.dict(exclude_unset=True).items():
        setattr(funcionario_especialidade_model, key, value)
    
    db_session.commit()
    db_session.refresh(funcionario_especialidade_model)
    return funcionario_especialidade_model

@funcionario_especialidade_router.delete('/funcionario_especialidade/{id}')
def delete_funcionario_especialidade(id: int, db_session: Session = Depends(get_db_session)):
    funcionario_especialidade_model = db_session.query(FuncionarioEspecialidadeModel).filter(FuncionarioEspecialidadeModel.id == id).first()
    if not funcionario_especialidade_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Funcionario Especialidade not found")
    
    db_session.delete(funcionario_especialidade_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Funcionario Especialidade deleted successfully'}, status_code=status.HTTP_200_OK)
