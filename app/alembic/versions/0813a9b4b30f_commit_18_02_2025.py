"""commit 18/02/2025

Revision ID: 0813a9b4b30f
Revises: 7afd59ab66de
Create Date: 2025-02-18 16:59:13.728736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0813a9b4b30f'
down_revision: Union[str, None] = '7afd59ab66de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "micro_regiao",
        sa.Column("id", sa.Integer,  primary_key=True, nullable=False),
        sa.Column("nome",sa.String(255) , nullable=False)
    )

    op.drop_column("pacientes", "microRegiao")
    op.add_columnn(
        "pacientes",
        sa.Column("micro_regiao_id", sa.Integer, nullable=False)
    )
    op.create_foreign_key("fk_micro_regiao_id", "pacientes", "micro_regiao", ["micro_regiao_id"], ["id"])


def downgrade() -> None:
    op.drop_constraint("fk_micro_regiao_id", "pacientes", "foreignkey")
    op.drop_column("pacientes", "micro_regiao_id")
    op.add_column(
        "pacientes",
        sa.Column(
            "microRegiao",
            sa.String(255)
        )
    )
    op.drop_table("micro_regiao")
