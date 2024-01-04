"""Renaming grade column to grading

Revision ID: bdcb4bceac2b
Revises: fbe001409d75
Create Date: 2024-01-04 18:12:01.903441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdcb4bceac2b'
down_revision = 'fbe001409d75'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(table_name='scholars', column_name='grade', new_column_name='grading')


def downgrade() -> None:
    op.alter_column(table_name='scholars', column_name='grading', new_column_name='grade')
