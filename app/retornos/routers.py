"""CRUD Inicial"""
from fastapi import APIRouter
from .model import RetornosModel

router = APIRouter()


#Create

@router.post("/create_retorno/{id}", response_model= RetornosModel)
def create_retorno():
    #Cria um novo prontuário com id
    return "Create prontuário"

#Read

@router.get("/read_retorno/{id}", response_model= RetornosModel)
def get_retorno():
    #Retorna o prontuário escolhido pelo id
    return "Read prontuário"

#Update

@router.put("/update_retorno/{id}", response_model= RetornosModel)
def update_retorno():
    #Atualiza os dados de um prontuário pelo id
    return "Update prontuário"

#Delete

@router.delete("/delete_retorno/{id}", response_model= RetornosModel)
def delete_retorno():
    #Deleta um prontuário pelo id
    return "Delete prontuário"