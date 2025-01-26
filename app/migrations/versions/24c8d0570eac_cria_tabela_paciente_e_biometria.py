"""Cria tabela Paciente e Biometria

Revision ID: 24c8d0570eac
Revises: 
Create Date: 2025-01-14 14:55:41.724388

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer, VARCHAR, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship


# revision identifiers, used by Alembic.
revision: str = '24c8d0570eac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    #Criação da tabela paciente

    op.create_table(
        "paciente",
        Column("numeroSUS", Integer, primary_key=True, nullable=False),
        Column("nome", VARCHAR(45)),
        Column("email", VARCHAR(45)),
        Column("telefone", VARCHAR(45)),
        Column("sexo", VARCHAR(45)),
        Column("info", VARCHAR(45)),
        Column("dataNascimento", VARCHAR(45)),
        Column("microRegiao", VARCHAR(45)),
        relationship("biometria")
    )
    
    #Cria tabela biometria

    op.create_table(
        "biometria",
        Column("id_biometria", Integer, primary_key=True, nullable=False),
        Column("imc", Float),
        Column("peso", Float),
        Column("altura", Float),
        Column("data", DateTime),
        Column("cintura", Float),
        Column("fkPaciente", Integer, ForeignKey("paciente.numeroSUS"))
    )

def downgrade() -> None:
    op.drop_table("paciente")
    op.drop_table("biometria")
