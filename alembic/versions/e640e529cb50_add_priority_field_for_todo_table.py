"""add priority field for todo table

Revision ID: e640e529cb50
Revises: 74bc6e3bc0a5
Create Date: 2024-12-19 15:21:03.135969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e640e529cb50'
down_revision: Union[str, None] = '74bc6e3bc0a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('priority', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'priority')
    # ### end Alembic commands ###
