"""empty message

Revision ID: 986022f81e08
Revises: 2f428e7d4df5
Create Date: 2024-11-10 17:28:08.015087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '986022f81e08'
down_revision = '2f428e7d4df5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_developer', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_developer')

    # ### end Alembic commands ###
