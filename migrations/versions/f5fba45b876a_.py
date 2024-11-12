"""empty message

Revision ID: f5fba45b876a
Revises: 551fa9081b70
Create Date: 2024-11-12 09:43:19.225314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5fba45b876a'
down_revision = '551fa9081b70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profile', schema=None) as batch_op:
        batch_op.add_column(sa.Column('github', sa.String(length=39), nullable=True))
        batch_op.create_unique_constraint(None, ['github'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profile', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('github')

    # ### end Alembic commands ###
