from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

# Define a URL do banco de dados
DB_URL = config('DB_URL', default='mysql+pymysql://root@localhost/emdia')

# Cria o engine do SQLAlchemy
engine = create_engine(DB_URL, pool_pre_ping=True)

# Configura o sessionmaker para gerenciar sessões
Session = sessionmaker(bind=engine)