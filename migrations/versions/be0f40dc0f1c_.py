"""empty message

Revision ID: be0f40dc0f1c
Revises: 9f5d3e3d3512
Create Date: 2023-11-25 16:47:13.645945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be0f40dc0f1c'
down_revision = '9f5d3e3d3512'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "doctors",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("hospital", sa.Unicode(length=10000)),
        sa.Column("userId", sa.BigInteger, nullable=False),
    )


def downgrade():
    pass
