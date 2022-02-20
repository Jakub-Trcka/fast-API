"""add user table

Revision ID: 1900cd5c1828
Revises: eed2bdf14013
Create Date: 2022-02-20 15:52:41.972311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1900cd5c1828'
down_revision = 'eed2bdf14013'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer, nullable=False), sa.Column('email', sa.String, nullable=False), sa.Column('password', sa.String, nullable=False), sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
