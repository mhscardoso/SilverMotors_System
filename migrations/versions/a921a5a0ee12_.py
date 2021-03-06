"""empty message

Revision ID: a921a5a0ee12
Revises: 2fff050fced8
Create Date: 2022-01-19 12:58:17.242310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a921a5a0ee12'
down_revision = '2fff050fced8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('carro', 'update_time')
    op.drop_column('carro', 'create_time')
    op.drop_column('cart', 'update_time')
    op.drop_column('cart', 'create_time')
    op.drop_column('cupom', 'update_time')
    op.drop_column('cupom', 'create_time')
    op.drop_column('moto', 'update_time')
    op.drop_column('moto', 'create_time')
    op.drop_column('user', 'update_time')
    op.drop_column('user', 'create_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('create_time', sa.VARCHAR(), nullable=True))
    op.add_column('user', sa.Column('update_time', sa.VARCHAR(), nullable=True))
    op.add_column('moto', sa.Column('create_time', sa.VARCHAR(), nullable=True))
    op.add_column('moto', sa.Column('update_time', sa.VARCHAR(), nullable=True))
    op.add_column('cupom', sa.Column('create_time', sa.VARCHAR(), nullable=True))
    op.add_column('cupom', sa.Column('update_time', sa.VARCHAR(), nullable=True))
    op.add_column('cart', sa.Column('create_time', sa.VARCHAR(), nullable=True))
    op.add_column('cart', sa.Column('update_time', sa.VARCHAR(), nullable=True))
    op.add_column('carro', sa.Column('create_time', sa.VARCHAR(), nullable=True))
    op.add_column('carro', sa.Column('update_time', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
