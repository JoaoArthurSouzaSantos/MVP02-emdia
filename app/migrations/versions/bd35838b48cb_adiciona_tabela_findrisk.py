"""adiciona tabela findrisk

Revision ID: bd35838b48cb
Revises: 24c8d0570eac
Create Date: 2025-01-24 14:21:47.299913

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import String, Integer, Date, Column, Float, ForeignKey
from sqlalchemy.orm import relationship

# revision identifiers, used by Alembic.
revision: str = 'bd35838b48cb'
down_revision: Union[str, None] = '24c8d0570eac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "paciente",
        Column("numeroSUS", String(255), primary_key=True, nullable=False),
        Column("nome", String(255)),
        Column("email", String(255)),
        Column("telefone", String(255)),
        Column("sexo", String(255)),
        Column("info", String(255)),
        Column("dataNascimento", String(255)),
        Column("microRegiao", String(255)),
        relationship("biometria")
    )
    
    #Cria tabela biometria

    op.create_table(
        "biometria",
        Column("id_biometria", Integer, primary_key=True, nullable=False),
        Column("imc", Float),
        Column("peso", Float),
        Column("altura", Float),
        Column("data", Date),
        Column("cintura", Float),
        Column("fkPaciente", String(255), ForeignKey("paciente.numeroSUS"))
    )

    op.create_table(
        "findrisk",
        Column("idFindrisk", Integer, primary_key=True, nullable=False, autoincrement=True),
        Column("data", Date),
        Column("pont_historico_familiar_de_diabetes", String(255)),
        Column("pont_hipertensao", String(255)),
        Column("pont_ingestao_frutas_e_verduras", String(255)),
        Column("pont_atv_fisica", String(255)),
        Column("pont_circunferencia_cintura", String(255)),
        Column("pont_imc", String(255)),
        Column("pont_idade", String(255)),
        Column("pont_historico_de_glicemia_elevada", String(255)),
        Column("classificacao", String(255)),
        Column("fkPaciente", String(255), ForeignKey("paciente.numeroSUS")),
        relationship("paciente", back_populates="findrisk")
        )


def downgrade() -> None:
    op.drop_table("findrisk")
