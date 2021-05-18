"""create-taggings

Revision ID: 208591fb00fa
Revises: 4558e7f8f1a3
Create Date: 2021-05-18 12:44:22.314420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '208591fb00fa'
down_revision = '4558e7f8f1a3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'taggings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('post_id', sa.Integer),
        sa.Column('topic_id', sa.Integer),
    )


def downgrade():
    op.drop_table('taggings')
