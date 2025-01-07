"""CRUD Inicial"""
from fastapi import APIRouter
from .model import PatologiaModel

router = APIRouter()


#Create

@router.post("/create_patologia/{id}", response_model= PatologiaModel)
def create_patologia():
    #Cria um nova patologia com id
    return "Create patologia"

#Read

@router.get("/read_patologia/{id}", response_model= PatologiaModel)
def get_patologia():
    #Retorna a patologia escolhido pelo id
    return "Read patologia"

#Update

@router.put("/update_patologia/{id}", response_model= PatologiaModel)
def update_patologia():
    #Atualiza os dados de uma patologia pelo id
    return "Update patologia"

#Delete

@router.delete("/delete_patologia/{id}", response_model= PatologiaModel)
def delete_patologia():
    #Deleta uma patologia pelo id
    return "Delete patologia"