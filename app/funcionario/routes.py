from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional

from db.base import SessionLocal
from db.models import FuncionarioModel
from funcionario.schemas import FuncionarioCreate, FuncionarioOut
from depends import get_db_session

# Configurações
SECRET_KEY = "secret-key-for-jwt"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

# Esquema OAuth2 para autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/funcionario/token")

funcionario_router = APIRouter()

# Configuração para hashing de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Função para criptografar senha
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# Função para verificar senha
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Função para buscar funcionário por CPF
def get_funcionario_by_cpf(db: Session, cpf: str):
    return db.query(FuncionarioModel).filter(FuncionarioModel.cpf == cpf).first()


# Função para autenticar o funcionário
def authenticate_funcionario(db: Session, cpf: str, password: str):
    funcionario = get_funcionario_by_cpf(db, cpf)
    if not funcionario or not verify_password(password, funcionario.password):
        return None
    return funcionario


# Função para criar um token JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Rota para registrar um funcionário
@funcionario_router.post("/register/", response_model=FuncionarioOut)
def register_funcionario(funcionario: FuncionarioCreate, db: Session = Depends(get_db_session)):
    hashed_password = get_password_hash(funcionario.password)
    db_funcionario = FuncionarioModel(
        cpf=funcionario.cpf,
        password=hashed_password,
        nome=funcionario.nome,
        email=funcionario.email,
        idPerfil=funcionario.idPerfil,  # Ajuste de nomenclatura
    )
    db.add(db_funcionario)
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario


# Rota para autenticação e geração do token
@funcionario_router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_session)):
    funcionario = authenticate_funcionario(db, form_data.username, form_data.password)
    if not funcionario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="CPF ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": funcionario.cpf},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
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
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
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
