from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .schemas import PacientePatologiaSchema
from db.models import PacientePatologia
from depends import get_db_session

pacientepatologia_router = APIRouter()

@pacientepatologia_router.post('/pacientepatologia', response_model=PacientePatologiaSchema)
def create_pacientepatologia(pacientepatologia: PacientePatologiaSchema, db_session: Session = Depends(get_db_session)):
    pacientepatologia_model = PacientePatologia(**pacientepatologia.dict())
    db_session.add(pacientepatologia_model)
    db_session.commit()
    db_session.refresh(pacientepatologia_model)
    return pacientepatologia_model

@pacientepatologia_router.get('/pacientepatologia/{id}', response_model=PacientePatologiaSchema)
def get_pacientepatologia(id: int, db_session: Session = Depends(get_db_session)):
    pacientepatologia_model = db_session.query(PacientePatologia).filter(PacientePatologia.id == id).first()
    if not pacientepatologia_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="pacientepatologia not found")
    return pacientepatologia_model

@pacientepatologia_router.put('/pacientepatologia/{id}', response_model=PacientePatologiaSchema)
def update_pacientepatologia(id: int, pacientepatologia: PacientePatologiaSchema, db_session: Session = Depends(get_db_session)):
    pacientepatologia_model = db_session.query(PacientePatologia).filter(PacientePatologia.id == id).first()
    if not pacientepatologia_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="pacientepatologia not found")
    
    for key, value in pacientepatologia.dict().items():
        setattr(pacientepatologia_model, key, value)
    
    db_session.commit()
    db_session.refresh(pacientepatologia_model)
    return pacientepatologia_model

@pacientepatologia_router.delete('/pacientepatologia/{id}')
def delete_pacientepatologia(id: int, db_session: Session = Depends(get_db_session)):
    pacientepatologia_model = db_session.query(PacientePatologia).filter(PacientePatologia.id == id).first()
    if not pacientepatologia_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="pacientepatologia not found")
    
    db_session.delete(pacientepatologia_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'pacientepatologia deleted successfully'}, status_code=status.HTTP_200_OK)
