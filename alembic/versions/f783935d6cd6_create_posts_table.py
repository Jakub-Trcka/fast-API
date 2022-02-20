"""create posts table

Revision ID: f783935d6cd6
Revises: 
Create Date: 2022-02-20 15:36:14.608287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f783935d6cd6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer, primary_key=True, nullable=False), sa.Column('title', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
