"""CRUD Inicial"""
from fastapi import APIRouter
from .model import PerfilPermissaoModel

router = APIRouter()


#Create

@router.post("/create_perfil_permissao/{id}", response_model= PerfilPermissaoModel)
def create_perfil_permissao():
    #Cria um novo perfil com permissão e id
    return "Create perfil_permissao"

#Read

@router.get("/read_perfil_permissao/{id}", response_model= PerfilPermissaoModel)
def get_perfil_permissao():
    #Retorna o perfil e permissões pelo id
    return "Read perfil_permissao"

#Update

@router.put("/update_perfil_permissao/{id}", response_model= PerfilPermissaoModel)
def update_perfil_permissao():
    #Atualiza as permissões pelo id
    return "Update perfil_permissao"

#Delete

@router.delete("/delete_perfil_permissao/{id}", response_model= PerfilPermissaoModel)
def delete_perfil_permissao():
    #Deleta um perfil_permissao pelo id
    return "Delete perfil_permissao"