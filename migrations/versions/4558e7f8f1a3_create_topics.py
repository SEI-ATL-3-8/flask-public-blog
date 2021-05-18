"""create-topics

Revision ID: 4558e7f8f1a3
Revises: 48f1d2316b2d
Create Date: 2021-05-18 12:41:58.533754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4558e7f8f1a3'
down_revision = '48f1d2316b2d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'topics',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
    )


def downgrade():
    op.drop_table('topics')
