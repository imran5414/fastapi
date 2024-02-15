"""create posts table

Revision ID: eb0cc34cfa2a
Revises: 
Create Date: 2024-01-10 16:21:34.905706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb0cc34cfa2a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    
    sa.Column('title',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_table('posts')
    pass
