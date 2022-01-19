"""empty message

Revision ID: 8d49c3a37938
Revises: f9bbaccda991
Create Date: 2022-01-19 19:44:08.519376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d49c3a37938'
down_revision = 'f9bbaccda991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cupom', sa.Column('desconto', sa.Float(), nullable=True))
    op.add_column('cupom', sa.Column('codigo', sa.String(length=10), nullable=True))
    op.drop_column('cupom', 'desconto_moto')
    op.drop_column('cupom', 'desconto_carro')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cupom', sa.Column('desconto_carro', sa.INTEGER(), nullable=True))
    op.add_column('cupom', sa.Column('desconto_moto', sa.INTEGER(), nullable=True))
    op.drop_column('cupom', 'codigo')
    op.drop_column('cupom', 'desconto')
    # ### end Alembic commands ###
