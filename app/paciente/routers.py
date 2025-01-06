"""CRUD Inicial"""
from fastapi import APIRouter
from .model import PacienteModel

router = APIRouter()


#Create

@router.post("/create_paciente/{id}", response_model= PacienteModel)
def create_paciente():
    #Cria um novo paciente com id
    return "Create Paciente"

#Read

@router.get("/read_paciente/{id}", response_model= PacienteModel)
def get_paciente():
    #Retorna o paciente escolhido pelo id
    return "Read Paciente"

#Update

@router.put("/update_paciente/{id}", response_model= PacienteModel)
def update_paciente():
    #Atualiza os dados de um paciente pelo id
    return "Update Paciente"

#Delete

@router.delete("/delete_paciente/{id}", response_model= PacienteModel)
def delete_paciente():
    #Deleta um paciente pelo id
    return "Delete Paciente"