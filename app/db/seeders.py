from sqlalchemy.orm import Session
from datetime import date, datetime
from db.base import Base, engine
from models import (
    PacienteModel, FuncionarioModel, PerfilModel, PermissaoModel, 
    PerfilPermissaoModel, TipoExameModel, ConsultaModel, 
    BiometriaModel, MedicamentoModel, TipoMedicamentoModel,
    ExameModel, EstratificacaoModel, EspecialidadeModel, LogModel
)

def seed_database():
    session = Session(bind=engine)
    
    # Criando Perfis e Permissões
    admin_perfil = PerfilModel(name="Admin")
    medico_perfil = PerfilModel(name="Médico")
    session.add_all([admin_perfil, medico_perfil])
    session.commit()
    
    perm_consulta = PermissaoModel(name="Consultar Pacientes")
    perm_editar = PermissaoModel(name="Editar Pacientes")
    session.add_all([perm_consulta, perm_editar])
    session.commit()
    
    session.add(PerfilPermissaoModel(id_perfil=admin_perfil.id, id_permissao=perm_editar.id))
    session.add(PerfilPermissaoModel(id_perfil=medico_perfil.id, id_permissao=perm_consulta.id))
    session.commit()
    
    # Criando Funcionários
    funcionario1 = FuncionarioModel(
        cpf="12345678900", password="senha123", nome="Dr. João", email="joao@example.com", id_perfil=medico_perfil.id
    )
    session.add(funcionario1)
    session.commit()
    
    # Criando Especialidade
    cardiologia = EspecialidadeModel(nome="Cardiologia")
    session.add(cardiologia)
    session.commit()
    
    # Criando Paciente
    paciente1 = PacienteModel(
        numeroSUS=1001, data_nascimento=date(1980, 5, 20), sexo="Masculino", nome="Carlos Silva",
        telefone="11999999999", email="carlos@example.com", micro_regiao="Centro"
    )
    session.add(paciente1)
    session.commit()
    
    # Criando Consulta
    consulta1 = ConsultaModel(
        fk_paciente=paciente1.numeroSUS, fk_especialidade=cardiologia.id, fk_funcionario=funcionario1.id
    )
    session.add(consulta1)
    session.commit()
    
    # Criando Biometria
    biometria1 = BiometriaModel(
        imc=25.0, peso=75.0, altura=1.75, data=date.today(), cintura=90.0,
        fk_paciente=paciente1.numeroSUS, fk_consulta=consulta1.id
    )
    session.add(biometria1)
    session.commit()
    
    # Criando Tipo de Medicamento
    tipo_medicamento1 = TipoMedicamentoModel(nome="Antibiótico", info="Uso contínuo")
    session.add(tipo_medicamento1)
    session.commit()
    
    # Criando Medicamento
    medicamento1 = MedicamentoModel(
        status="Ativo", frequencia="1x ao dia", dosagem="500mg",
        fk_tipo_medicamento=tipo_medicamento1.id, fk_paciente=paciente1.numeroSUS, fk_consulta=consulta1.id
    )
    session.add(medicamento1)
    session.commit()
    
    # Criando Tipo de Exame
    tipo_exame1 = TipoExameModel(nome="Hemograma")
    session.add(tipo_exame1)
    session.commit()
    
    # Criando Exame
    exame1 = ExameModel(
        data_realizacao="2025-02-01", resultado="Normal", 
        fk_paciente=paciente1.numeroSUS, fk_tipo_exame=tipo_exame1.id, fk_consulta=consulta1.id
    )
    session.add(exame1)
    session.commit()
    
    print("Seeders inseridos com sucesso!")

if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Certifique-se de criar as tabelas antes de popular
    seed_database()
