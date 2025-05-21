# Alembic revision identifiers
revision = '7277826737fb'
down_revision = '9174e901c008'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, String, Boolean, Date, Float, Text, DateTime

from sqlalchemy.sql import table, column
from datetime import date

def upgrade() -> None:
    microregiao = table('microregiao',
        column('id', Integer),
        column('nome', String),
    )

    pacientes = table('pacientes',
        column('numeroSUS', Integer),
        column('data_nascimento', Date),
        column('sexo', String),
        column('info', String),
        column('telefone', String),
        column('email', String),
        column('nome', String),
        column('micro_regiao_id', Integer),
        column('cpf', String),
    )

    perfis = table('perfis',
        column('id', Integer),
        column('name', String),
    )

    funcionarios = table('funcionarios',
        column('id', Integer),
        column('cpf', String),
        column('password', String),
        column('nome', String),
        column('email', String),
        column('id_perfil', Integer),
    )

    tipos_exames = table('tipos_exames',
        column('id', Integer),
        column('nome', String),
        column('status', Boolean),
    )

    tipos_medicamentos = table('tipos_medicamentos',
        column('id', Integer),
        column('nome', String),
        column('info', String),
    )

    medicamentos = table('medicamentos',
        column('id', Integer),
        column('status', String),
        column('frequencia', String),
        column('dosagem', String),
        column('fk_tipo_medicamento', Integer),
        column('fk_paciente', Integer),
    )

    especialidades = table('especialidades',
        column('id', Integer),
        column('nome', String),
    )

    consultas = table('consultas',
        column('id', Integer),
        column('fk_paciente', Integer),
        column('fk_especialidade', Integer),
        column('fk_funcionario', Integer),
        column('data', Date),
        column('status', Integer),
        column('observacoes', Text),
    )

    estratificacoes = table('estratificacoes',
        column('id', Integer),
        column('data', Date),
        column('categoria', String),
        column('fk_paciente', Integer),
        column('fk_consulta', Integer),
    )

    findrisk = table('findrisk',
        column('id', Integer),
        column('data', Date),
        column('pont_historico_familiar_de_diabetes', String),
        column('pont_historico_de_glicemia_elevada', String),
        column('classificacao', String),
        column('pont_idade', String),
        column('pont_imc', String),
        column('pont_circunferencia_cintura', String),
        column('pont_atv_fisica', String),
        column('pont_ingestao_frutas_e_verduras', String),
        column('pont_hipertensao', String),
        column('fk_paciente', Integer),
        column('fk_consulta', Integer),
    )

    logs = table('logs',
        column('id', Integer),
        column('timestamp', DateTime),
        column('usuario_id', Integer),
        column('ip_origem', String),
        column('acao', String),
        column('tabela_afetada', String),
        column('registro_id', Integer),
        column('descricao', String),
        column('status', String),
        column('origem', String),
        column('metodo_http', String),
    )

    patologia = table('patologia',
        column('id', Integer),
        column('nome', String),
        column('icon', Integer),
    )

    paciente_patologias = table('paciente_patologias',
        column('id', Integer),
        column('fk_patologia', Integer),
        column('fk_paciente', Integer),
    )

    biometrias = table('biometrias',
        column('id', Integer),
        column('imc', Float),
        column('peso', Float),
        column('altura', Float),
        column('data', Date),
        column('cintura', Float),
        column('fk_paciente', Integer),
        column('fk_consulta', Integer),
    )

    exames = table('exames',
        column('id', Integer),
        column('data_realizacao', Date),
        column('resultado', String),
        column('fk_paciente', Integer),
        column('fk_tipo_exame', Integer),
        column('fk_consulta', Integer),
    )

    permissoes = table('permissoes',
        column('id', Integer),
        column('name', String),
    )

    perfilpermissoes = table('perfilpermissoes',
        column('id', Integer),
        column('id_perfil', Integer),
        column('id_permissao', Integer),
    )

    funcionario_especialidades = table('funcionario_especialidades',
        column('id', Integer),
        column('fk_funcionario', Integer),
        column('fk_especialidade', Integer),
    )

    # Inserções
    op.bulk_insert(microregiao, [
        {'id': 1, 'nome': 'Micro Região Teste'},
        {'id': 2, 'nome': 'Micro Região Extra'},
    ])

    op.bulk_insert(pacientes, [
        {
            'numeroSUS': 123456789,
            'data_nascimento': date(1990, 1, 1),
            'sexo': 'Masculino',
            'info': 'Paciente teste',
            'telefone': '123456789',
            'email': 'paciente@teste.com',
            'nome': 'Paciente Teste',
            'micro_regiao_id': 1,
            'cpf': '111111',
        },
        {
            'numeroSUS': 987654321,
            'data_nascimento': date(1985, 5, 15),
            'sexo': 'Feminino',
            'info': 'Paciente extra',
            'telefone': '987654321',
            'email': 'extra@teste.com',
            'nome': 'Paciente Extra',
            'micro_regiao_id': 2,
            'cpf': '222222',
        }
    ])

    op.bulk_insert(perfis, [
        {'id': 1, 'name': 'Administrador'},
    ])

    op.bulk_insert(funcionarios, [
        {
            'id': 1,
            'cpf': '12345678900',
            'password': '$2b$12$dzj7I3Jv7op/hwAqWLm4YOOnP2sViExA3WZsD.4ZPK7bkNoLZQYBy',
            'nome': 'Funcionario Teste',
            'email': 'funcionario@teste.com',
            'id_perfil': 1
        },
        {
            'id': 2,
            'cpf': '99999999900',
            'password': 'xyz123',
            'nome': 'Funcionario Extra',
            'email': 'extra@teste.com',
            'id_perfil': 1
        }
    ])

    op.bulk_insert(tipos_exames, [
        {'id': 1, 'nome': 'Exame de Sangue', 'status': True}
    ])

    op.bulk_insert(tipos_medicamentos, [
        {'id': 1, 'nome': 'Medicamento Teste', 'info': 'Informação do medicamento'}
    ])

    op.bulk_insert(medicamentos, [
        {'id': 1, 'status': 'Ativo', 'frequencia': 'Diária', 'dosagem': '500mg', 'fk_tipo_medicamento': 1, 'fk_paciente': 123456789},
        {'id': 2, 'status': 'Ativo', 'frequencia': 'Semanal', 'dosagem': '250mg', 'fk_tipo_medicamento': 1, 'fk_paciente': 987654321},
    ])

    op.bulk_insert(especialidades, [
        {'id': 1, 'nome': 'Cardiologia'}
    ])

    op.bulk_insert(consultas, [
        {'id': 1, 'fk_paciente': 123456789, 'fk_especialidade': 1, 'fk_funcionario': 1, 'data': date(2023, 10, 5), 'status': 1, 'observacoes': 'Consulta de teste'},
        {'id': 2, 'fk_paciente': 987654321, 'fk_especialidade': 1, 'fk_funcionario': 2, 'data': date(2023, 11, 10), 'status': 1, 'observacoes': 'Consulta extra'},
    ])

    op.bulk_insert(estratificacoes, [
        {'id': 1, 'data': date.today(), 'categoria': 'Alto Risco', 'fk_paciente': 123456789, 'fk_consulta': 1},
    ])

    op.bulk_insert(findrisk, [
        {
            'id': 1,
            'data': date.today(),
            'pont_historico_familiar_de_diabetes': '2',
            'pont_historico_de_glicemia_elevada': '1',
            'classificacao': 'Moderado',
            'pont_idade': '3',
            'pont_imc': '2',
            'pont_circunferencia_cintura': '1',
            'pont_atv_fisica': '1',
            'pont_ingestao_frutas_e_verduras': '1',
            'pont_hipertensao': '1',
            'fk_paciente': 123456789,
            'fk_consulta': 1,
        }
    ])

    op.bulk_insert(logs, [
        {
            'id': 1,
            'timestamp': sa.func.current_timestamp(),
            'usuario_id': 1,
            'ip_origem': '127.0.0.1',
            'acao': 'Teste de Log',
            'tabela_afetada': 'pacientes',
            'registro_id': 123456789,
            'descricao': 'Log de teste',
            'status': 'Sucesso',
            'origem': 'Sistema',
            'metodo_http': 'POST',
        },
        {
            'id': 2,
            'timestamp': sa.func.current_timestamp(),
            'usuario_id': 2,
            'ip_origem': '127.0.0.1',
            'acao': 'Inserção Extra',
            'tabela_afetada': 'pacientes',
            'registro_id': 987654321,
            'descricao': 'Log extra de teste',
            'status': 'Sucesso',
            'origem': 'Sistema',
            'metodo_http': 'POST',
        }
    ])

    op.bulk_insert(patologia, [
        {'id': 1, 'nome': 'Diabetes Tipo 2', 'icon': 1}
    ])

    op.bulk_insert(paciente_patologias, [
        {'id': 1, 'fk_patologia': 1, 'fk_paciente': 123456789},
    ])

    op.bulk_insert(biometrias, [
        {
            'id': 1,
            'imc': 25.0,
            'peso': 70.0,
            'altura': 1.75,
            'data': date.today(),
            'cintura': 85.0,
            'fk_paciente': 123456789,
            'fk_consulta': 1,
        }
    ])

    op.bulk_insert(exames, [
        {'id': 1, 'data_realizacao': date(2023, 10, 1), 'resultado': 'Normal', 'fk_paciente': 123456789, 'fk_tipo_exame': 1, 'fk_consulta': 1},
        {'id': 2, 'data_realizacao': date(2023, 11, 1), 'resultado': 'Normal', 'fk_paciente': 987654321, 'fk_tipo_exame': 1, 'fk_consulta': 2},
    ])

    op.bulk_insert(permissoes, [
        {'id': 1, 'name': 'Acesso Completo'}
    ])

    op.bulk_insert(perfilpermissoes, [
        {'id': 1, 'id_perfil': 1, 'id_permissao': 1}
    ])

    op.bulk_insert(funcionario_especialidades, [
        {'id': 1, 'fk_funcionario': 1, 'fk_especialidade': 1}
    ])

def downgrade() -> None:
    pass
