"""Renaming students to scholars

Revision ID: fbe001409d75
Revises: 791279dd0760
Create Date: 2024-01-04 17:47:13.532534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbe001409d75'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')