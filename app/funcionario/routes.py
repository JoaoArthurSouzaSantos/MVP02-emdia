from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError
from db.base import SessionLocal
from db.models import FuncionarioModel
from funcionario.schemas import FuncionarioCreate, FuncionarioOut
from depends import get_db_session
from funcionario.auth import AuthService

# Configurações
SECRET_KEY = "secret-key-for-jwt"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

# Esquema OAuth2 para autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/funcionario/token")

funcionario_router = APIRouter()

auth_service = AuthService(SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)

# Função para buscar funcionário por CPF
def get_funcionario_by_cpf(db: Session, cpf: str):
    return db.query(FuncionarioModel).filter(FuncionarioModel.cpf == cpf).first()


# Rota para registrar um funcionário
@funcionario_router.post("/register/", response_model=FuncionarioOut)
def register_funcionario(funcionario: FuncionarioCreate, db: Session = Depends(get_db_session)):
    hashed_password = auth_service.get_password_hash(funcionario.password)
    db_funcionario = FuncionarioModel(
        cpf=funcionario.cpf,
        password=hashed_password,
        nome=funcionario.nome,
        email=funcionario.email,
        id_perfil=funcionario.id_perfil,  # Ajuste de nomenclatura
    )
    db.add(db_funcionario)
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario


# Rota para autenticação e geração do token
@funcionario_router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_session)):
    funcionario = auth_service.authenticate_funcionario(db, form_data.username, form_data.password)
    if not funcionario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="CPF ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = auth_service.create_access_token(
        data={"sub": funcionario.cpf},
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Endpoint protegido para obter informações do funcionário logado
@funcionario_router.get("/funcionarios/me", response_model=FuncionarioOut)
def read_funcionario_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = auth_service.decode_token(token)
        cpf: str = payload.get("sub")
        if cpf is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    funcionario = get_funcionario_by_cpf(db, cpf)
    if not funcionario:
        raise credentials_exception
    return funcionario


# Rota de teste
test_router = APIRouter()

@test_router.get("/test")
def test_endpoint():
    return {"message": "Test endpoint"}