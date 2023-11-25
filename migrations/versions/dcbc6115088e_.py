"""empty message

Revision ID: dcbc6115088e
Revises: d092852a2506
Create Date: 2023-11-25 15:10:35.619510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcbc6115088e'
down_revision = 'd092852a2506'
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
