"""CRUD Inicial"""
from fastapi import APIRouter
from .model import PrescricaoModel

router = APIRouter()


#Create

@router.post("/create_prescricao/{id}", response_model= PrescricaoModel)
def create_prescricao():
    #Cria uma nova prescricão com id
    return "Create prescricão"

#Read

@router.get("/read_prescricao/{id}", response_model= PrescricaoModel)
def get_prescricao():
    #Retorna a prescricão escolhido pelo id
    return "Read prescricão"

#Update

@router.put("/update_prescricao/{id}", response_model= PrescricaoModel)
def update_prescricao():
    #Atualiza os dados de uma prescricão pelo id
    return "Update prescricão"

#Delete

@router.delete("/delete_prescricao/{id}", response_model= PrescricaoModel)
def delete_prescricao():
    #Deleta uma prescricão pelo id
    return "Delete prescricão"