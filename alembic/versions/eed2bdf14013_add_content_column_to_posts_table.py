"""add content column to posts table

Revision ID: eed2bdf14013
Revises: f783935d6cd6
Create Date: 2022-02-20 15:45:28.776931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eed2bdf14013'
down_revision = 'f783935d6cd6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
