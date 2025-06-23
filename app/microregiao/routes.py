from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from .schemas import MicroRegiaoSchema
from depends import get_db_session
from db.models import MicroRegiaoModel
from sqlalchemy.orm import Session
from typing import List

microregiao_router = APIRouter()

@microregiao_router.get("/microregiao/read_microregiao/{id}", response_model=MicroRegiaoSchema)
def get_microregiao(id: int, db_session: Session = Depends(get_db_session)):
    microregiao_in_db = db_session.query(MicroRegiaoModel).filter(MicroRegiaoModel.id == id).first()

    if not microregiao_in_db:
        raise HTTPException(status_code=404, detail="Micro-região não encontrada!")
    return microregiao_in_db
    
@microregiao_router.post("/microregiao/create_microregiao/")
def create_microregiao(schema: MicroRegiaoSchema, db_session: Session = Depends(get_db_session)):
    microregiao_body = MicroRegiaoModel(**schema.dict())
    
    if db_session.query(MicroRegiaoModel).filter(MicroRegiaoModel == microregiao_body).first():
       raise HTTPException(status_code=403, detail="Essa micro-região já existe!")

    db_session.add(microregiao_body)
    db_session.commit()
    db_session.refresh(microregiao_body)
    return microregiao_body
    

@microregiao_router.put("/microregiao/update_microregiao/{id}")
def update_microregiao(id: int, schema: MicroRegiaoSchema, db_session: Session = Depends(get_db_session)):
    microregiao_body = MicroRegiaoModel(**schema.dict())
    microregiao_model = db_session.query(MicroRegiaoModel).filter(MicroRegiaoModel.id == id).first()
    if not microregiao_model:
        raise HTTPException(status_code=404, detail="Micro Região não encontrada")
    
    for key, value in microregiao_body.dict().items():
        setattr(microregiao_model, key, value)
    
    db_session.commit()
    db_session.refresh(microregiao_model)
    return microregiao_model

@microregiao_router.delete("/microregiao/delete_microregiao/{id}")
def delete_microregiao(id: int, db_session: Session = Depends(get_db_session)):  # Removed schema parameter
    microregiao_model = db_session.query(MicroRegiaoModel).filter(MicroRegiaoModel.id == id).first()
    if not microregiao_model:
        raise HTTPException(status_code=404, detail="Micro Região não encontrada")
    db_session.delete(microregiao_model)
    db_session.commit()
    return JSONResponse(content={'msg': 'Micro Região deleted successfully'}, status_code=200)

@microregiao_router.get("/microregiao/read_microregioes", response_model=List[MicroRegiaoSchema])
def get_all_microregioes(db_session: Session = Depends(get_db_session)):
    return db_session.query(MicroRegiaoModel).all()
