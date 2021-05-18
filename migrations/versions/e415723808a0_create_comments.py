"""create-comments

Revision ID: e415723808a0
Revises: 65251bf56c56
Create Date: 2021-05-18 12:14:57.190991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e415723808a0'
down_revision = '65251bf56c56'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('body', sa.String),
    )


def downgrade():
    op.drop_table('comments')
