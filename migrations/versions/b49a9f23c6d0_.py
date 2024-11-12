"""empty message

Revision ID: b49a9f23c6d0
Revises: f5fba45b876a
Create Date: 2024-11-12 10:52:28.833539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b49a9f23c6d0'
down_revision = 'f5fba45b876a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('google_id', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('is_developer', sa.Boolean(), nullable=False))
        batch_op.create_unique_constraint(None, ['google_id'])

    with op.batch_alter_table('user_profile', schema=None) as batch_op:
        batch_op.add_column(sa.Column('github', sa.String(length=39), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profile', schema=None) as batch_op:
        batch_op.drop_column('github')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('is_developer')
        batch_op.drop_column('google_id')

    # ### end Alembic commands ###
