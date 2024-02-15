"""add users table

Revision ID: ee556cdf41c2
Revises: c72d98405432
Create Date: 2024-01-22 16:57:43.767833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee556cdf41c2'
down_revision: Union[str, None] = 'c72d98405432'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )
                    
                    
                    
                    
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
