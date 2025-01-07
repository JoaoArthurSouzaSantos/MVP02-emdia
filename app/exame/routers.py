"""CRUD Inicial"""
from fastapi import APIRouter
from .model import ExameModel

router = APIRouter()


#Create

@router.post("/create_exame/{id}", response_model= ExameModel)
def create_exame():
    #Cria um novo exame com id
    return "Create exame"

#Read

@router.get("/read_exame/{id}", response_model= ExameModel)
def get_exame():
    #Retorna o exame escolhido pelo id
    return "Read exame"

#Update

@router.put("/update_exame/{id}", response_model= ExameModel)
def update_exame():
    #Atualiza os dados de um exame pelo id
    return "Update exame"

#Delete

@router.delete("/delete_exame/{id}", response_model= ExameModel)
def delete_exame():
    #Deleta um exame pelo id
    return "Delete exame"