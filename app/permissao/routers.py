"""CRUD Inicial"""
from fastapi import APIRouter
from .model import PermissaoModel

router = APIRouter()


#Create

@router.post("/create_permissao/{id}", response_model= PermissaoModel)
def create_permissao():
    #Cria uma nova permissão com id
    return "Create permissão"

#Read

@router.get("/read_permissao/{id}", response_model= PermissaoModel)
def get_permissao():
    #Retorna a permissão escolhido pelo id
    return "Read permissão"

#Update

@router.put("/update_permissao/{id}", response_model= PermissaoModel)
def update_permissao():
    #Atualiza os dados de uma permissão pelo id
    return "Update permissão"

#Delete

@router.delete("/delete_permissao/{id}", response_model= PermissaoModel)
def delete_permissao():
    #Deleta uma permissão pelo id
    return "Delete permissão"