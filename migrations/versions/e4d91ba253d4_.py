"""empty message

Revision ID: e4d91ba253d4
Revises: 005ce6e94401
Create Date: 2023-11-25 14:21:12.316770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4d91ba253d4'
down_revision = '005ce6e94401'
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
