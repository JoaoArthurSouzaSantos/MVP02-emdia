"""CRUD Inicial"""
from fastapi import APIRouter
from .model import EspecialidadeModel

router = APIRouter()


#Create

@router.post("/create_especialidade/{id}", response_model= EspecialidadeModel)
def create_especialidade():
    #Cria um nova especialidade com id
    return "Create Especialidade"

#Read

@router.get("/read_especialidade/{id}", response_model= EspecialidadeModel)
def get_especialidade():
    #Retorna a especialidade pelo id
    return "Read especialidade"

#Update

@router.put("/update_especialidade/{id}", response_model= EspecialidadeModel)
def update_especialidade():
    #Atualiza os dados de um especialidade pelo id
    return "Update especialidade"

#Delete

@router.delete("/delete_especialidade/{id}", response_model= EspecialidadeModel)
def delete_especialidade():
    #Deleta um especialidade pelo id
    return "Delete especialidade"