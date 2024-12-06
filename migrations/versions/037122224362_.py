"""empty message

Revision ID: 037122224362
Revises: cfcd0d284d0d
Create Date: 2024-12-05 20:09:55.662614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '037122224362'
down_revision = 'cfcd0d284d0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=100), nullable=False))
        batch_op.create_unique_constraint(None, ['name'])
        batch_op.create_unique_constraint(None, ['last_name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('last_name')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
