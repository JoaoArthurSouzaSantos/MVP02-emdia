"""CRUD Inicial"""
from fastapi import APIRouter
from .model import PerfilModel

router = APIRouter()


#Create

@router.post("/create_perfil/{id}", response_model= PerfilModel)
def create_perfil():
    #Cria um novo perfil com id
    return "Create perfil"

#Read

@router.get("/read_perfil/{id}", response_model= PerfilModel)
def get_perfil():
    #Retorna o perfil escolhido pelo id
    return "Read perfil"

#Update

@router.put("/update_perfil/{id}", response_model= PerfilModel)
def update_perfil():
    #Atualiza os dados de um perfil pelo id
    return "Update perfil"

#Delete

@router.delete("/delete_perfil/{id}", response_model= PerfilModel)
def delete_perfil():
    #Deleta um perfil pelo id
    return "Delete perfil"