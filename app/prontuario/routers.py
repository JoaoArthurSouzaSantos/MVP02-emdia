"""CRUD Inicial"""
from fastapi import APIRouter
from .model import ProntuarioModel

router = APIRouter()


#Create

@router.post("/create_prontuario/{id}", response_model= ProntuarioModel)
def create_prontuario():
    #Cria um novo prontuário com id
    return "Create prontuário"

#Read

@router.get("/read_prontuario/{id}", response_model= ProntuarioModel)
def get_prontuario():
    #Retorna o prontuário escolhido pelo id
    return "Read prontuário"

#Update

@router.put("/update_prontuario/{id}", response_model= ProntuarioModel)
def update_prontuario():
    #Atualiza os dados de um prontuário pelo id
    return "Update prontuário"

#Delete

@router.delete("/delete_prontuario/{id}", response_model= ProntuarioModel)
def delete_prontuario():
    #Deleta um prontuário pelo id
    return "Delete prontuário"