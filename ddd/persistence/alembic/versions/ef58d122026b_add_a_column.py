"""Add a column

Revision ID: ef58d122026b
Revises: 4e8f7b23daa5
Create Date: 2022-08-16 20:53:26.407161

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ef58d122026b'
down_revision = '4e8f7b23daa5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'students',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.Unicode(200)),
        sa.Column('DOB', sa.String(200), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('students')
