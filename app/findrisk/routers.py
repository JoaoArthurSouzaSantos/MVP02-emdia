"""CRUD Inicial"""
from fastapi import APIRouter
from .model import FindriskModel

router = APIRouter()


#Create

@router.post("/create_findrisk/{id}", response_model= FindriskModel)
def create_findrisk():
    #Cria um novo findrisk com id
    return "Create findrisk"

#Read

@router.get("/read_findrisk/{id}", response_model= FindriskModel)
def get_findrisk():
    #Retorna o findrisk escolhido pelo id
    return "Read findrisk"

#Update

@router.put("/update_findrisk/{id}", response_model= FindriskModel)
def update_findrisk():
    #Atualiza os dados de um findrisk pelo id
    return "Update findrisk"

#Delete

@router.delete("/delete_findrisk/{id}", response_model= FindriskModel)
def delete_findrisk():
    #Deleta um findrisk pelo id
    return "Delete findrisk"