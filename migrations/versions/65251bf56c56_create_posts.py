"""create-posts

Revision ID: 65251bf56c56
Revises: 
Create Date: 2021-05-18 12:11:40.418933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65251bf56c56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('body', sa.String)
    )


def downgrade():
    op.drop_table('posts')
