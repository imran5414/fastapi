"""add content column to posts table

Revision ID: c72d98405432
Revises: eb0cc34cfa2a
Create Date: 2024-01-22 16:50:04.182320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c72d98405432'
down_revision: Union[str, None] = 'eb0cc34cfa2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
