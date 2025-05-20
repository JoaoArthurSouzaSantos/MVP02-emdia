from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models import FuncionarioEspecialidadeModel
from .schemas import FuncionarioEspecialidadeBase, FuncionarioEspecialidadeOut
from depends import get_db_session


funcionario_especialidade_router = APIRouter()

# Create
@funcionario_especialidade_router.post('/funcionario_especialidades', response_model=FuncionarioEspecialidadeOut)
def create_funcionario_especialidade(data: FuncionarioEspecialidadeBase, db: Session = Depends(get_db_session)):
    funcionario_especialidade = FuncionarioEspecialidadeModel(**data.dict())
    db.add(funcionario_especialidade)
    db.commit()
    db.refresh(funcionario_especialidade)
    return funcionario_especialidade

# Read (Get by ID)
@funcionario_especialidade_router.get('/funcionario_especialidades/{id}', response_model=FuncionarioEspecialidadeOut)
def get_funcionario_especialidade(id: int, db: Session = Depends(get_db_session)):
    funcionario_especialidade = db.query(FuncionarioEspecialidadeModel).filter(FuncionarioEspecialidadeModel.id == id).first()
    if not funcionario_especialidade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="FuncionarioEspecialidade not found")
    return funcionario_especialidade

# Update
@funcionario_especialidade_router.put('/funcionario_especialidades/{id}', response_model=FuncionarioEspecialidadeOut)
def update_funcionario_especialidade(id: int, data: FuncionarioEspecialidadeBase, db: Session = Depends(get_db_session)):
    funcionario_especialidade = db.query(FuncionarioEspecialidadeModel).filter(FuncionarioEspecialidadeModel.id == id).first()
    if not funcionario_especialidade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="FuncionarioEspecialidade not found")
    
    for key, value in data.dict(exclude_unset=True).items():
        setattr(funcionario_especialidade, key, value)
    
    db.commit()
    db.refresh(funcionario_especialidade)
    return funcionario_especialidade

# Delete
@funcionario_especialidade_router.delete('/funcionario_especialidades/{id}')
def delete_funcionario_especialidade(id: int, db: Session = Depends(get_db_session)):
    funcionario_especialidade = db.query(FuncionarioEspecialidadeModel).filter(FuncionarioEspecialidadeModel.id == id).first()
    if not funcionario_especialidade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="FuncionarioEspecialidade not found")
    
    db.delete(funcionario_especialidade)
    db.commit()
    return {"msg": "FuncionarioEspecialidade deleted successfully"}