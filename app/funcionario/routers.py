"""CRUD Inicial"""
from fastapi import APIRouter
from .model import FuncionarioModel

router = APIRouter()


#Create

@router.post("/create_funcionario/{id}", response_model= FuncionarioModel)
def create_funcionario():
    #Cria um novo funcionario com id
    return "Create funcionario"

#Read

@router.get("/read_funcionario/{id}", response_model= FuncionarioModel)
def get_funcionario():
    #Retorna o funcionario escolhido pelo id
    return "Read funcionario"

#Update

@router.put("/update_funcionario/{id}", response_model= FuncionarioModel)
def update_funcionario():
    #Atualiza os dados de um funcionario pelo id
    return "Update funcionario"

#Delete

@router.delete("/delete_funcionario/{id}", response_model= FuncionarioModel)
def delete_funcionario():
    #Deleta um funcionario pelo id
    return "Delete funcionario"