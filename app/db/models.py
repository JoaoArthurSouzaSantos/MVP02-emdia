from sqlalchemy import Column, Integer, ForeignKey, String, Float, Date
from sqlalchemy.orm import relationship
from db.base import Base

class RetornosModel(Base):
    __tablename__ = "retornos"
    id = Column(Integer, primary_key=True, index=True)
    FkPaciente = Column(Integer, ForeignKey("pacientes.numeroSUS"), nullable=False, index=True)
    FkEspecialidade = Column(Integer, ForeignKey("especialidades.id"), nullable=False, index=True)
    paciente = relationship("PacienteModel", back_populates="retornos")
    especialidade = relationship("EspecialidadeModel", back_populates="retornos")

class ProntuarioExame(Base):
    __tablename__ = "prontuarios"
    id = Column(Integer, primary_key=True, index=True)
    fkfuncionarioespecialidade = Column(Integer, ForeignKey("funcionariosEspecialidades.id"), nullable=False, index=True)
    fkpaciente = Column(Integer, ForeignKey("pacientes.numeroSUS"), nullable=False)
    fkexame = Column(Integer, ForeignKey("exames.id"), nullable=False)
    paciente = relationship("PacienteModel", back_populates="prontuarios")
    funcionarioespecialidade = relationship("FuncionarioEspecialidadeModel", back_populates="prontuarios")
    exame = relationship("ExameModel", back_populates="prontuarios")
    estratificacoes = relationship("EstratificacaoModel", back_populates="prontuario")

class PacientePatologia(Base):
    __tablename__ = "paciente_patologias"
    id = Column(Integer, primary_key=True, index=True)
    FkPatologia = Column(Integer, ForeignKey("patologia.id"), nullable=False)
    Fkpaciente = Column(Integer, ForeignKey("pacientes.numeroSUS"), nullable=False)
    patologia = relationship("PatologiaModel", back_populates="paciente_patologias")
    paciente = relationship("PacienteModel", back_populates="patologias")

class FuncionarioEspecialidadeModel(Base):
    __tablename__ = "funcionariosEspecialidades"
    id = Column(Integer, primary_key=True, index=True)
    FkFuncionario = Column(Integer, ForeignKey("funcionarios.id"), nullable=False, index=True)
    FkEspecialidade = Column(Integer, ForeignKey("especialidades.id"), nullable=False, index=True)
    funcionario = relationship("FuncionarioModel", back_populates="funcionarios")
    especialidade = relationship("EspecialidadeModel", back_populates="funcionarios")
    prontuarios = relationship("ProntuarioExame", back_populates="funcionarioespecialidade")

class FuncionarioModel(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    nome = Column(String(255), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    idPerfil = Column(Integer, ForeignKey("perfis.id"), nullable=False, index=True)
    perfil = relationship("PerfilModel", back_populates="funcionarios")
    funcionarios = relationship("FuncionarioEspecialidadeModel", back_populates="funcionario")

class ExameModel(Base):
    __tablename__ = "exames"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    resultado = Column(String(500), nullable=True)
    data_realizacao = Column(String(50), nullable=False)
    prescricao = relationship("PrescricaoModel", back_populates="exame")
    prontuarios = relationship("ProntuarioExame", back_populates="exame")

class BiometriaModel(Base):
    __tablename__ = "biometrias"
    id = Column(Integer, primary_key=True, index=True)
    imc = Column(Float, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    data = Column(Date, nullable=False)
    cintura = Column(Float, nullable=False)
    paciente_i = Column(Integer, ForeignKey("pacientes.numeroSUS"), nullable=False)
    paciente = relationship("PacienteModel", back_populates="biometrias")

class PrescricaoModel(Base):
    __tablename__ = "prescricoes"
    id = Column(Integer, primary_key=True, index=True)
    inicio = Column(Date, nullable=False)
    fim = Column(Date, nullable=True)
    status = Column(String(255), nullable=False)
    frequencia = Column(String(255), nullable=False)
    dosagem = Column(String(255), nullable=False)
    fk_medicamento = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    Fkpaciente = Column(Integer, ForeignKey("pacientes.numeroSUS"), nullable=False)
    fk_exame = Column(Integer, ForeignKey("exames.id"), nullable=True)  # Added foreign key
    paciente = relationship("PacienteModel", back_populates="prescricoes")
    medicamento = relationship("MedicamentoModel", back_populates="prescricoes")
    exame = relationship("ExameModel", back_populates="prescricao")

class PatologiaModel(Base):
    __tablename__ = "patologia"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    paciente_patologias = relationship("PacientePatologia", back_populates="patologia")

class PacienteModel(Base):
    __tablename__ = "pacientes"
    numeroSUS = Column(Integer, primary_key=True, index=True)
    dataNascimento = Column(Date)
    sexo = Column(String(255), index=True)
    info = Column(String(255), index=True)
    telefone = Column(String(255), index=True)
    email = Column(String(255), index=True)
    nome = Column(String(255), index=True)
    microRegiao = Column(String(255), index=True)
    consultas = relationship("ConsultaModel", back_populates="paciente", cascade="all, delete-orphan")
    biometrias = relationship("BiometriaModel", back_populates="paciente", cascade="all, delete-orphan")
    prescricoes = relationship("PrescricaoModel", back_populates="paciente", cascade="all, delete-orphan")
    patologias = relationship("PacientePatologia", back_populates="paciente", cascade="all, delete-orphan")
    retornos = relationship("RetornosModel", back_populates="paciente", cascade="all, delete-orphan")
    prontuarios = relationship("ProntuarioExame", back_populates="paciente", cascade="all, delete-orphan")
    findrisk = relationship("FindriskModel", back_populates="paciente", cascade="all, delete-orphan")
    estratificacoes = relationship("EstratificacaoModel", back_populates="paciente", cascade="all, delete-orphan")

class MedicamentoModel(Base):
    __tablename__ = "medicamentos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    info = Column(String(255))
    prescricoes = relationship("PrescricaoModel", back_populates="medicamento")

class FindriskModel(Base):
    __tablename__ = "findrisk"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    pont_historico_familiar_de_diabetes = Column(String(255))
    pont_historico_de_glicemia_elevada = Column(String(255))
    classificacao = Column(String(255))
    pont_idade = Column(String(255))
    pont_imc = Column(String(255))
    pont_circuferencia_cintura = Column(String(255))
    pont_atv_fisica = Column(String(255))
    pont_ingestao_frutas_e_verduras = Column(String(255))
    pont_hipertensao = Column(String(255))
    FkPaciente = Column(Integer, ForeignKey("pacientes.numeroSUS"), nullable=False)
    paciente = relationship("PacienteModel", back_populates="findrisk")

class EspecialidadeModel(Base):
    __tablename__ = "especialidades"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), unique=True, nullable=False)
    funcionarios = relationship("FuncionarioEspecialidadeModel", back_populates="especialidade")
    retornos = relationship("RetornosModel", back_populates="especialidade", cascade="all, delete-orphan")
    consultas = relationship("ConsultaModel", back_populates="especialidade")

class ConsultaModel(Base):
    __tablename__ = "consultas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    FkPaciente = Column(Integer, ForeignKey("pacientes.numeroSUS"), nullable=False, index=True)
    FkEspecialidade = Column(Integer, ForeignKey("especialidades.id"), nullable=False, index=True)
    paciente = relationship("PacienteModel", back_populates="consultas")
    especialidade = relationship("EspecialidadeModel", back_populates="consultas")

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
    perfilpermissao = relationship("PerfilPermissaoModel", back_populates="permissao", cascade="all, delete-orphan")
    
class PerfilPermissaoModel(Base):
    __tablename__ = "perfilpermissoes"
    id = Column(Integer, primary_key=True, index=True)
    idPerfil = Column(Integer, ForeignKey("perfis.id"), nullable=False, index=True)
    idPermissao = Column(Integer, ForeignKey("permissoes.id"), nullable=False, index=True)
    perfil = relationship("PerfilModel", back_populates="permissoes")
    permissao = relationship("PermissaoModel", back_populates="perfilpermissao")


class EstratificacaoModel(Base):
    __tablename__ = "estratificacoes"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    categoria = Column(String(255), nullable=False)
    FkProntuario = Column(Integer, ForeignKey("prontuarios.id"), nullable=False)
    FkPaciente = Column(Integer, ForeignKey("pacientes.numeroSUS"), nullable=False)
    paciente = relationship("PacienteModel", back_populates="estratificacoes")
    prontuario = relationship("ProntuarioExame", back_populates="estratificacoes")
