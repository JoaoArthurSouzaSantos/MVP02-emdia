"""CRUD Inicial"""
from fastapi import APIRouter
from .model import MedicoModel

router = APIRouter()


#Create

@router.post("/create_medico/{id}", response_model= MedicoModel)
def create_medico():
    #Cria um novo medico com id
    return "Create medico"

#Read

@router.get("/read_medico/{id}", response_model= MedicoModel)
def get_medico():
    #Retorna o medico escolhido pelo id
    return "Read medico"

#Update

@router.put("/update_medico/{id}", response_model= MedicoModel)
def update_medico():
    #Atualiza os dados de um medico pelo id
    return "Update medico"

#Delete

@router.delete("/delete_medico/{id}", response_model= MedicoModel)
def delete_medico():
    #Deleta um medico pelo id
    return "Delete medico"