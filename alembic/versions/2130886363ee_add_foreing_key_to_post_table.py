"""add foreing key to post table

Revision ID: 2130886363ee
Revises: 1900cd5c1828
Create Date: 2022-02-20 16:04:46.772062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2130886363ee'
down_revision = '1900cd5c1828'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
