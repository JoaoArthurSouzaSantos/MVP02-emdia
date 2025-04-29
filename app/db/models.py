from sqlalchemy import Column, Integer, ForeignKey, String, Float, Date, DateTime, Boolean
from sqlalchemy.orm import relationship
from db.base import Base
from datetime import datetime


class ExameModel(Base):
    __tablename__ = "exames"
    id = Column(Integer, primary_key=True, index=True)
    data_realizacao = Column(String(50), nullable=False)
    resultado = Column(String(500), nullable=True)
    fk_paciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)
    fk_tipo_exame = Column(Integer, ForeignKey("tipos_exames.id"), nullable=False)
    fk_consulta = Column(Integer, ForeignKey("consultas.id"), nullable=False)

    paciente = relationship("PacienteModel", back_populates="exames")
    tipo_exame = relationship("TipoExameModel", back_populates="exames")
    consulta = relationship("ConsultaModel", back_populates="exames")


class PacientePatologia(Base):
    __tablename__ = "paciente_patologias"
    id = Column(Integer, primary_key=True, index=True)
    fk_patologia = Column(Integer, ForeignKey("patologia.id"), nullable=False)
    fk_paciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)

    patologia = relationship("PatologiaModel", back_populates="paciente_patologias")
    paciente = relationship("PacienteModel", back_populates="patologias")


class FuncionarioModel(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    nome = Column(String(255), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    id_perfil = Column(Integer, ForeignKey("perfis.id"), nullable=False, index=True)

    perfil = relationship("PerfilModel", back_populates="funcionarios")
    logs = relationship("LogModel", back_populates="user")
    consultas = relationship("ConsultaModel", back_populates="funcionario")
    especialidades = relationship("FuncionarioEspecialidadeModel", back_populates="funcionario", cascade="all, delete-orphan")


class TipoExameModel(Base):
    __tablename__ = "tipos_exames"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    status = Column(Boolean, default=True, nullable=False)  

    exames = relationship("ExameModel", back_populates="tipo_exame")


class BiometriaModel(Base):
    __tablename__ = "biometrias"
    id = Column(Integer, primary_key=True, index=True)
    imc = Column(Float, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    data = Column(Date, nullable=False)
    cintura = Column(Float, nullable=False)
    fk_paciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)
    fk_consulta = Column(Integer, ForeignKey("consultas.id"), nullable=False)

    paciente = relationship("PacienteModel", back_populates="biometrias")
    consulta = relationship("ConsultaModel", back_populates="biometrias")


class MedicamentoModel(Base):
    __tablename__ = "medicamentos"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(255), nullable=False)
    frequencia = Column(String(255), nullable=False)
    dosagem = Column(String(255), nullable=False)
    fk_tipo_medicamento = Column(Integer, ForeignKey("tipos_medicamentos.id"), nullable=False)
    fk_paciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)
    fk_consulta = Column(Integer, ForeignKey("consultas.id"), nullable=True)

    paciente = relationship("PacienteModel", back_populates="medicamentos")
    tipo_medicamento = relationship("TipoMedicamentoModel", back_populates="medicamentos")
    consulta = relationship("ConsultaModel", back_populates="medicamentos")


class PatologiaModel(Base):
    __tablename__ = "patologia"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))

    paciente_patologias = relationship("PacientePatologia", back_populates="patologia")


class MicroRegiaoModel(Base):
    __tablename__ = "microregiao"
    id = Column(Integer, nullable=False, primary_key=True)
    nome = Column(String(255), nullable=False)
    
    paciente = relationship("PacienteModel", back_populates="micro_regiao")


class PacienteModel(Base):
    __tablename__ = "pacientes"
    numeroSUS = Column(String(255), primary_key=True, index=True)
    data_nascimento = Column(Date)
    cpf = Column(String(255), index=True)
    sexo = Column(String(255), index=True)
    info = Column(String(255), index=True)
    telefone = Column(String(255), index=True)
    email = Column(String(255), index=True)
    nome = Column(String(255), index=True)
    micro_regiao_id = Column(Integer, ForeignKey("microregiao.id"))
    
    # Removido delete-orphan do cascade
    micro_regiao = relationship("MicroRegiaoModel", back_populates="paciente")
    consultas = relationship("ConsultaModel", back_populates="paciente", cascade="all, delete-orphan")
    biometrias = relationship("BiometriaModel", back_populates="paciente", cascade="all, delete-orphan")
    medicamentos = relationship("MedicamentoModel", back_populates="paciente", cascade="all, delete-orphan")
    patologias = relationship("PacientePatologia", back_populates="paciente", cascade="all, delete-orphan")
    exames = relationship("ExameModel", back_populates="paciente", cascade="all, delete-orphan")
    findrisk = relationship("FindriskModel", back_populates="paciente", cascade="all, delete-orphan")
    estratificacoes = relationship("EstratificacaoModel", back_populates="paciente", cascade="all, delete-orphan")


class TipoMedicamentoModel(Base):
    __tablename__ = "tipos_medicamentos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    info = Column(String(255))

    medicamentos = relationship("MedicamentoModel", back_populates="tipo_medicamento")


class FindriskModel(Base):
    __tablename__ = "findrisk"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    pont_historico_familiar_de_diabetes = Column(String(255))
    pont_historico_de_glicemia_elevada = Column(String(255))
    classificacao = Column(String(255))
    pont_idade = Column(String(255))
    pont_imc = Column(String(255))
    pont_circunferencia_cintura = Column(String(255))
    pont_atv_fisica = Column(String(255))
    pont_ingestao_frutas_e_verduras = Column(String(255))
    pont_hipertensao = Column(String(255))
    fk_paciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)
    fk_consulta = Column(Integer, ForeignKey("consultas.id"), nullable=True)

    paciente = relationship("PacienteModel", back_populates="findrisk")
    consulta = relationship("ConsultaModel", back_populates="findrisk")


class EspecialidadeModel(Base):
    __tablename__ = "especialidades"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), unique=True, nullable=False)

    consultas = relationship("ConsultaModel", back_populates="especialidade")
    funcionarios = relationship("FuncionarioEspecialidadeModel", back_populates="especialidade", cascade="all, delete-orphan")


class ConsultaModel(Base):
    __tablename__ = "consultas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fk_paciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False, index=True)
    fk_especialidade = Column(Integer, ForeignKey("especialidades.id"), nullable=False, index=True)
    fk_funcionario = Column(Integer, ForeignKey("funcionarios.id"), nullable=False, index=True)
    data = Column(Date, nullable=True)
    status = Column(Integer, default=1, nullable=False)
    observacoes = Column(String(255), nullable=True)

    paciente = relationship("PacienteModel", back_populates="consultas")
    especialidade = relationship("EspecialidadeModel", back_populates="consultas")
    funcionario = relationship("FuncionarioModel", back_populates="consultas")
    biometrias = relationship("BiometriaModel", back_populates="consulta")
    medicamentos = relationship("MedicamentoModel", back_populates="consulta")
    exames = relationship("ExameModel", back_populates="consulta")
    estratificacoes = relationship("EstratificacaoModel", back_populates="consulta")
    findrisk = relationship("FindriskModel", back_populates="consulta", cascade="all, delete-orphan")


class PerfilModel(Base):
    __tablename__ = "perfis"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False, index=True)

    funcionarios = relationship("FuncionarioModel", back_populates="perfil")
    permissoes = relationship("PerfilPermissaoModel", back_populates="perfil", cascade="all, delete-orphan")


class PermissaoModel(Base):
    __tablename__ = "permissoes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False, index=True)

    perfil_permissoes = relationship("PerfilPermissaoModel", back_populates="permissao", cascade="all, delete-orphan")


class PerfilPermissaoModel(Base):
    __tablename__ = "perfilpermissoes"
    id = Column(Integer, primary_key=True, index=True)
    id_perfil = Column(Integer, ForeignKey("perfis.id"), nullable=False, index=True)
    id_permissao = Column(Integer, ForeignKey("permissoes.id"), nullable=False, index=True)

    perfil = relationship("PerfilModel", back_populates="permissoes")
    permissao = relationship("PermissaoModel", back_populates="perfil_permissoes")


class EstratificacaoModel(Base):
    __tablename__ = "estratificacoes"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    categoria = Column(String(255), nullable=False)
    fk_paciente = Column(String(255), ForeignKey("pacientes.numeroSUS"), nullable=False)
    fk_consulta = Column(Integer, ForeignKey("consultas.id"), nullable=False)

    paciente = relationship("PacienteModel", back_populates="estratificacoes")
    consulta = relationship("ConsultaModel", back_populates="estratificacoes")


class LogModel(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    usuario_id = Column(Integer, ForeignKey("funcionarios.id"), nullable=False)
    ip_origem = Column(String(255), nullable=False)
    acao = Column(String(255), nullable=False)
    tabela_afetada = Column(String(255), nullable=True)
    registro_id = Column(Integer, nullable=True)
    descricao = Column(String(255), nullable=True)
    status = Column(String(255), nullable=False)
    detalhes_erro = Column(String(255), nullable=True)
    origem = Column(String(255), nullable=False)
    metodo_http = Column(String(10), nullable=True)

    user = relationship("FuncionarioModel", back_populates="logs")


class FuncionarioEspecialidadeModel(Base):
    __tablename__ = "funcionario_especialidades"
    id = Column(Integer, primary_key=True, index=True)
    fk_funcionario = Column(Integer, ForeignKey("funcionarios.id"), nullable=False, index=True)
    fk_especialidade = Column(Integer, ForeignKey("especialidades.id"), nullable=False, index=True)

    funcionario = relationship("FuncionarioModel", back_populates="especialidades")
    especialidade = relationship("EspecialidadeModel", back_populates="funcionarios")
