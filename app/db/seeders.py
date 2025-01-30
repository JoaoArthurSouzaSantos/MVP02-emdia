from sqlalchemy.orm import Session
from app.db.models import (
    PacienteModel, FuncionarioModel, EspecialidadeModel, 
    FuncionarioEspecialidadeModel, ExameModel, BiometriaModel, 
    PrescricaoModel, PatologiaModel, PacientePatologia, 
    FindriskModel, EstratificacaoModel, PerfilModel, 
    PermissaoModel, PerfilPermissaoModel, ConsultaModel, 
    RetornosModel, MedicamentoModel
)
from datetime import date
from app.funcionario.auth import crypt_context

def seed_data(db: Session):
    # Create profiles
    admin_profile = PerfilModel(name="Admin")
    user_profile = PerfilModel(name="Usuário")
    db.add_all([admin_profile, user_profile])
    db.commit()

    # Create permissions
    perm1 = PermissaoModel(name="leitura")
    perm2 = PermissaoModel(name="escrita")
    db.add_all([perm1, perm2])
    db.commit()

    # Assign permissions to profiles
    admin_perms = [
        PerfilPermissaoModel(idPerfil=admin_profile.id, idPermissao=perm1.id),
        PerfilPermissaoModel(idPerfil=admin_profile.id, idPermissao=perm2.id)
    ]
    user_perms = [PerfilPermissaoModel(idPerfil=user_profile.id, idPermissao=perm1.id)]
    db.add_all(admin_perms + user_perms)
    db.commit()

    # Create patients
    patient1 = PacienteModel(
        numeroSUS=123456789, dataNascimento=date(1990, 1, 1), sexo="M", 
        info="Info1", telefone="123456789", email="paciente1@exemplo.com", 
        nome="João Arthur Souza Santos", microRegiao="Região1"
    )
    patient2 = PacienteModel(
        numeroSUS=987654321, dataNascimento=date(1985, 5, 5), sexo="F", 
        info="Info2", telefone="987654321", email="paciente2@exemplo.com", 
        nome="Alyson Steve Lacerda", microRegiao="Região2"
    )
    db.add_all([patient1, patient2])
    db.commit()

    # Create employees with hashed passwords
    employee1 = FuncionarioModel(
        cpf="11111111111", password=crypt_context.hash("senha1"), nome="Funcionário Um", 
        email="funcionario1@exemplo.com", idPerfil=admin_profile.id
    )
    employee2 = FuncionarioModel(
        cpf="22222222222", password=crypt_context.hash("senha2"), nome="Funcionário Dois", 
        email="funcionario2@exemplo.com", idPerfil=user_profile.id
    )
    db.add_all([employee1, employee2])
    db.commit()

    # Create specialties
    specialty1 = EspecialidadeModel(nome="Cardiologia")
    specialty2 = EspecialidadeModel(nome="Neurologia")
    db.add_all([specialty1, specialty2])
    db.commit()

    # Assign specialties to employees
    emp_spec1 = FuncionarioEspecialidadeModel(FkFuncionario=employee1.id, FkEspecialidade=specialty1.id)
    emp_spec2 = FuncionarioEspecialidadeModel(FkFuncionario=employee2.id, FkEspecialidade=specialty2.id)
    db.add_all([emp_spec1, emp_spec2])
    db.commit()

    # Create exams
    exam1 = ExameModel(nome="Exame de Sangue", resultado="Normal", data_realizacao="2023-01-01")
    exam2 = ExameModel(nome="Ressonância Magnética", resultado="Normal", data_realizacao="2023-02-01")
    db.add_all([exam1, exam2])
    db.commit()

    # Create biometrics
    biometrics1 = BiometriaModel(imc=22.5, peso=70, altura=1.75, data=date(2023, 1, 1), cintura=80, paciente_i=patient1.numeroSUS)
    biometrics2 = BiometriaModel(imc=25.0, peso=80, altura=1.80, data=date(2023, 2, 1), cintura=85, paciente_i=patient2.numeroSUS)
    db.add_all([biometrics1, biometrics2])
    db.commit()

    # Create prescriptions
    prescription1 = PrescricaoModel(inicio=date(2023, 1, 1), fim=date(2023, 6, 1), status="Ativa", frequencia="Diária", dosagem="1 comprimido", fk_medicamento=1, Fkpaciente=patient1.numeroSUS)
    prescription2 = PrescricaoModel(inicio=date(2023, 2, 1), fim=date(2023, 7, 1), status="Ativa", frequencia="Semanal", dosagem="2 comprimidos", fk_medicamento=2, Fkpaciente=patient2.numeroSUS)
    db.add_all([prescription1, prescription2])
    db.commit()

    # Create pathologies
    pathology1 = PatologiaModel(nome="Diabetes")
    pathology2 = PatologiaModel(nome="Hipertensão")
    db.add_all([pathology1, pathology2])
    db.commit()

    # Assign pathologies to patients
    patient_pathology1 = PacientePatologia(FkPatologia=pathology1.id, Fkpaciente=patient1.numeroSUS)
    patient_pathology2 = PacientePatologia(FkPatologia=pathology2.id, Fkpaciente=patient2.numeroSUS)
    db.add_all([patient_pathology1, patient_pathology2])
    db.commit()

    # Create findrisk records
    findrisk1 = FindriskModel(data=date(2023, 1, 1), pont_historico_familiar_de_diabetes="Baixo", pont_historico_de_glicemia_elevada="Baixo", classificacao="Baixo", pont_idade="Baixo", pont_imc="Baixo", pont_circuferencia_cintura="Baixo", pont_atv_fisica="Alto", pont_ingestao_frutas_e_verduras="Alto", pont_hipertensao="Baixo", FkPaciente=patient1.numeroSUS)
    findrisk2 = FindriskModel(data=date(2023, 2, 1), pont_historico_familiar_de_diabetes="Alto", pont_historico_de_glicemia_elevada="Alto", classificacao="Alto", pont_idade="Alto", pont_imc="Alto", pont_circuferencia_cintura="Alto", pont_atv_fisica="Baixo", pont_ingestao_frutas_e_verduras="Baixo", pont_hipertensao="Alto", FkPaciente=patient2.numeroSUS)
    db.add_all([findrisk1, findrisk2])
    db.commit()

    # Create stratifications
    stratification1 = EstratificacaoModel(data=date(2023, 1, 1), categoria="Baixo Risco", FkProntuario=1, FkPaciente=patient1.numeroSUS)
    stratification2 = EstratificacaoModel(data=date(2023, 2, 1), categoria="Alto Risco", FkProntuario=2, FkPaciente=patient2.numeroSUS)
    db.add_all([stratification1, stratification2])
    db.commit()

    # Create consultations
    consultation1 = ConsultaModel(FkPaciente=patient1.numeroSUS, FkEspecialidade=specialty1.id)
    consultation2 = ConsultaModel(FkPaciente=patient2.numeroSUS, FkEspecialidade=specialty2.id)
    db.add_all([consultation1, consultation2])
    db.commit()

    # Create returns
    return1 = RetornosModel(FkPaciente=patient1.numeroSUS, FkEspecialidade=specialty1.id)
    return2 = RetornosModel(FkPaciente=patient2.numeroSUS, FkEspecialidade=specialty2.id)
    db.add_all([return1, return2])
    db.commit()

    # Create medications
    medication1 = MedicamentoModel(nome="Aspirina", info="Analgésico")
    medication2 = MedicamentoModel(nome="Metformina", info="Medicamento para diabetes")
    db.add_all([medication1, medication2])
    db.commit()
