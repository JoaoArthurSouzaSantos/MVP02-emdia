from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

from paciente.routes import paciente_router
from funcionario.routes import funcionario_router, test_router
from medicamento.routes import medicamento_router
from funcionarioespecialidade.routes import funcionario_especialidade_router
from pacientepatologia.routes import pacientepatologia_router
from patologia.routes import patologia_router
from consulta.routes import consulta_router
from prontuario.routes import prontuario_router
from especialidade.routes import especialidade_router
from perfilpermissao.routes import perfilpermissao_router
from permissao.routes import permissao_router
from findrisk.routes import findrisk_router
from perfil.routes import perfil_router
from retornos.routes import retornos_router
from biometria.routes import biometria_router
from exame.routes import exame_router
from precricao.routes import prescricao_router
from paciente.routes import paciente_router


app = FastAPI()

DB_URL = config('DB_URL', default='mysql+pymysql://root@localhost/emdia')

# Incluir as rotas relacionadas ao usuário
app.include_router(funcionario_router, prefix="/funcionario", tags=["funcionarios"])
app.include_router(funcionario_especialidade_router, prefix="/funcionarioespecialidade", tags=["funcionarioespecialidades"])
app.include_router(paciente_router,prefix="/paciente", tags=["pacientes"])
app.include_router(consulta_router, prefix="/consulta", tags=["consultas"])
app.include_router(medicamento_router, prefix="/medicamento", tags=["medicamentos"])
app.include_router(pacientepatologia_router, prefix="/pacientepatologia", tags=["pacientepatologias"])
app.include_router(patologia_router, prefix="/patologia", tags=["patologias"])
app.include_router(prontuario_router, prefix="/prontuario", tags=["prontuarios"])
app.include_router(especialidade_router, prefix="/especialidade", tags=["especialidades"])
app.include_router(perfilpermissao_router, prefix="/perfilpermissao", tags=["perfilpermissoes"])
app.include_router(permissao_router, prefix="/permissao", tags=["permissoes"])
app.include_router(findrisk_router, prefix="/findrisk", tags=["findrisk"])
app.include_router(perfil_router, prefix="/perfil", tags=["perfis"])
app.include_router(retornos_router, prefix="/retornos", tags=["retornos"])
app.include_router(biometria_router, prefix="/biometria", tags=["biometrias"])
app.include_router(exame_router, prefix="/exame", tags=["exames"])
app.include_router(prescricao_router, prefix="/prescricao", tags=["prescricoes"])

@app.get("/openapi.json")
async def get_open_api_endpoint():
    return JSONResponse(get_openapi(title="Your Project Name", version="1.0", routes=app.routes))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)