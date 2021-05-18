"""add-post_id-to-comments

Revision ID: 48f1d2316b2d
Revises: e415723808a0
Create Date: 2021-05-18 12:16:57.059195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48f1d2316b2d'
down_revision = 'e415723808a0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'comments',
        sa.Column('post_id', sa.Integer)
    )


def downgrade():
    op.remove_column('comments', 'post_id')
