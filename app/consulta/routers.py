from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_, func
from depends import get_db_session
from .models import Consulta
from paciente.models import PacienteModel
from funcionario.models import FuncionarioModel
from .schemas import *
from typing import List
from depends import get_db_session, token_verifier
from datetime import date

router = APIRouter(
    dependencies=[Depends(token_verifier)]  # Aplica verificação de token a todas as rotas
)


@router.post("/consulta/", response_model=ConsultaCreate)
def create_consulta(consulta: ConsultaCreate, db: Session = Depends(get_db_session)):
    # Verificar se o paciente existe
    paciente = db.query(PacienteModel).filter(PacienteModel.numeroSUS == consulta.idPaciente).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    
    # Verificar se o funcionário existe
    funcionario = db.query(FuncionarioModel).filter(FuncionarioModel.id == consulta.idFuncionario).first()
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    try:
        # Criar e adicionar a nova consulta
        db_consulta = Consulta(**consulta.dict())
        db.add(db_consulta)
        db.commit()
        db.refresh(db_consulta)
        return db_consulta
    except IntegrityError:
        # Em caso de erro de integridade, como chave estrangeira violada
        db.rollback()
        raise HTTPException(status_code=400, detail="Erro de integridade ao criar a consulta")

@router.get("/consulta/{consulta_id}", response_model=ConsultaOut)
def read_consulta(consulta_id: int, db: Session = Depends(get_db_session)):
    db_consulta = db.query(Consulta).filter(Consulta.id == consulta_id).first()
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta not found")
    return db_consulta

@router.put("/consulta/{consulta_id}", response_model=ConsultaOut)
def update_consulta(consulta_id: int, consulta: ConsultaCreate, db: Session = Depends(get_db_session)):
    db_consulta = db.query(Consulta).filter(Consulta.id == consulta_id).first()
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta not found")
    for key, value in consulta.dict().items():
        setattr(db_consulta, key, value)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta

@router.delete("/consulta/{consulta_id}")
def delete_consulta(consulta_id: int, db: Session = Depends(get_db_session)):
    db_consulta = db.query(Consulta).filter(Consulta.id == consulta_id).first()
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta not found")
    db.delete(db_consulta)
    db.commit()
    return {"message": "Consulta deleted successfully"}

# Histórico de consultas
@router.get("/relatorio/historico", response_model=List[ConsultaOut])
def get_historico_consultas(db: Session = Depends(get_db_session)):
    consultas = db.query(Consulta).all()
    return consultas

# Consultas dentro de uma data escolhida
@router.get("/relatorio/data", response_model=List[ConsultaOut])
def get_consultas_por_data(data_escolhida: date, db: Session = Depends(get_db_session)):
    consultas = db.query(
        Consulta.id,
        Consulta.idPaciente,
        Consulta.idFuncionario,
        Consulta.data,
        Consulta.dataRetorno,
        Consulta.hbg,
        Consulta.tomaMedHipertensao,
        Consulta.praticaAtivFisica,
        Consulta.imc,
        Consulta.peso,
        Consulta.historicoAcucarElevado,
        Consulta.altura,
        Consulta.cintura,
        Consulta.resultadoFindRisc,
        Consulta.frequenciaIngestaoVegetaisFrutas,
        Consulta.historicoFamiliar,
        Consulta.medico
    ).join(PacienteModel, PacienteModel.numeroSUS == Consulta.idPaciente)\
     .filter(Consulta.data == data_escolhida)\
     .all()

    return consultas

@router.get("/relatorio/funcionario/{id_funcionario}", response_model=List[ConsultaFuncionarioId])
def get_consultas_por_funcionario(idFuncionario: str, db: Session = Depends(get_db_session)):
    consultas = db.query(
        Consulta.id,
        Consulta.idPaciente,  # Junta com a tabela Pessoa para pegar o nome
        Consulta.idFuncionario,
        Consulta.data,
        Consulta.dataRetorno,
        Consulta.hbg,
        Consulta.tomaMedHipertensao,
        Consulta.praticaAtivFisica,
        Consulta.imc,
        Consulta.peso,
        Consulta.historicoAcucarElevado,
        Consulta.altura,
        Consulta.cintura,
        Consulta.resultadoFindRisc,
        Consulta.frequenciaIngestaoVegetaisFrutas,
        Consulta.historicoFamiliar,
        Consulta.medico
    ).join(PacienteModel, PacienteModel.numeroSUS == Consulta.idPaciente)\
     .filter(Consulta.idFuncionario == idFuncionario)\
     .all()

    return consultas


@router.get("/relatorio/paciente/{id_paciente}", response_model=List[ConsultaOut])
def get_consultas_por_paciente(idPaciente: str, db: Session = Depends(get_db_session)):
    consultas = db.query(
        Consulta.id,
        Consulta.idPaciente,
        Consulta.idFuncionario,
        Consulta.data,
        Consulta.dataRetorno,
        Consulta.hbg,
        Consulta.tomaMedHipertensao,
        Consulta.praticaAtivFisica,
        Consulta.imc,
        Consulta.peso,
        Consulta.historicoAcucarElevado,
        Consulta.altura,
        Consulta.cintura,
        Consulta.resultadoFindRisc,
        Consulta.frequenciaIngestaoVegetaisFrutas,
        Consulta.historicoFamiliar,
        Consulta.medico
    ).join(PacienteModel, PacienteModel.numeroSUS == Consulta.idPaciente)\
     .filter(Consulta.idPaciente == idPaciente)\
     .all()

    return consultas



@router.get("/relatorio/periodo", response_model=List[ConsultaOut])
def get_consultas_por_periodo(data_inicio: date, data_fim: date, db: Session = Depends(get_db_session)):
    consultas = db.query(
        Consulta.id,
        Consulta.idPaciente,
        Consulta.idFuncionario,
        Consulta.data,
        Consulta.dataRetorno,
        Consulta.hbg,
        Consulta.tomaMedHipertensao,
        Consulta.praticaAtivFisica,
        Consulta.imc,
        Consulta.peso,
        Consulta.historicoAcucarElevado,
        Consulta.altura,
        Consulta.cintura,
        Consulta.resultadoFindRisc,
        Consulta.frequenciaIngestaoVegetaisFrutas,
        Consulta.historicoFamiliar,
        Consulta.medico,
        Pessoa.nome.label("nome")  # Pega o nome diretamente da tabela Pessoa
    ).join(PacienteModel, PacienteModel.numeroSUS == Consulta.idPaciente)\
     .filter(and_(Consulta.data >= data_inicio, Consulta.data <= data_fim))\
     .all()

    return consultas

# Número de consultas por dia
@router.get("/relatorio/consultas_por_dia", response_model=List[dict])
def get_numero_consultas_por_dia(db: Session = Depends(get_db_session)):
    consultas = db.query(Consulta.data, func.count(Consulta.id).label('count')).group_by(Consulta.data).all()
    return [{"data": dia, "count": count} for dia, count in consultas]

# Relatório de consultas futuras
@router.get("/relatorio/futuros", response_model=List[ConsultaOut])
def get_consultas_futuras(db: Session = Depends(get_db_session)):
    today = date.today()
    consultas = db.query(Consulta).filter(Consulta.data >= today).all()
    return consultas



@router.get("/relatorio/paciente/pessoa/consultas_completo_da_pessoa{id_paciente}")
def get_consultas_por_paciente(idPaciente: str, db: Session = Depends(get_db_session)):
    consultas = db.query(Consulta, Paciente, Pessoa).\
        join(PacienteModel, Consulta.idPaciente == PacienteModel.numeroSUS).\
        filter(Consulta.idPaciente == idPaciente).all()

    results = []
    for consulta, paciente, pessoa in consultas:
        results.append({
            "id": consulta.id,
            "idPaciente": consulta.idPaciente,
            "idFuncionario": consulta.idFuncionario,
            "data": consulta.data,
            "dataRetorno": consulta.dataRetorno,
            "hbg": consulta.hbg,
            "tomaMedHipertensao": consulta.tomaMedHipertensao,
            "praticaAtivFisica": consulta.praticaAtivFisica,
            "imc": consulta.imc,
            "peso": consulta.peso,
            "historicoAcucarElevado": consulta.historicoAcucarElevado,
            "altura": consulta.altura,
            "cintura": consulta.cintura,
            "resultadoFindRisc": consulta.resultadoFindRisc,
            "frequenciaIngestaoVegetaisFrutas": consulta.frequenciaIngestaoVegetaisFrutas,
            "historicoFamiliar": consulta.historicoFamiliar,
            "medico": consulta.medico,
            "numeroSUS": paciente.numeroSUS,
            "dataNascimento": paciente.dataNascimento,
            "sexo": paciente.sexo,
            "info": paciente.info,
            "cpf": pessoa.cpf,
            "nome": pessoa.nome,
            "email": pessoa.email
        })

    return results


@router.get("/relatorio/evoluçãoHB{id_paciente}", response_model=List[EvolucaoHB])
def get_consultas_por_paciente(idPaciente: str, db: Session = Depends(get_db_session)):
    consultas = db.query(Consulta, Paciente, Pessoa).\
        join(PacienteModel, Consulta.idPaciente == PacienteModel.numeroSUS).\
        filter(Consulta.idPaciente == idPaciente).all()

    results = []
    for consulta, paciente, pessoa in consultas:
        results.append({
            "data": consulta.data,
            "dataRetorno": consulta.dataRetorno,
            "hbg": consulta.hbg,
            "tomaMedHipertensao": consulta.tomaMedHipertensao,
            "praticaAtivFisica": consulta.praticaAtivFisica,
            "imc": consulta.imc,
            "peso": consulta.peso,
            "historicoAcucarElevado": consulta.historicoAcucarElevado,
            "altura": consulta.altura,
            "cintura": consulta.cintura,
            "resultadoFindRisc": consulta.resultadoFindRisc,
            "frequenciaIngestaoVegetaisFrutas": consulta.frequenciaIngestaoVegetaisFrutas,
            "historicoFamiliar": consulta.historicoFamiliar,
            "medico": consulta.medico,
            "dataNascimento": paciente.dataNascimento,
            "sexo": paciente.sexo,
            "info": paciente.info,
            "nome": pessoa.nome,
        })

    return results