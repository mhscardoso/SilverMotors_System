"""empty message

Revision ID: f9bbaccda991
Revises: a921a5a0ee12
Create Date: 2022-01-19 13:35:47.317368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9bbaccda991'
down_revision = 'a921a5a0ee12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('quantidade_itens', sa.Integer(), nullable=True))
    op.add_column('cart', sa.Column('carrinho_vazio', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cart', 'carrinho_vazio')
    op.drop_column('cart', 'quantidade_itens')
    # ### end Alembic commands ###
