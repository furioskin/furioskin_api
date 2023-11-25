"""empty message

Revision ID: 6e53afdad097
Revises: 099a3fd8f7e7
Create Date: 2023-11-25 14:37:44.888684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e53afdad097'
down_revision = '099a3fd8f7e7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "answers",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("content", sa.Unicode(length=10000)),
        sa.Column("questionId", sa.BigInteger, nullable=False),
        sa.Column("userId", sa.BigInteger, nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    pass
