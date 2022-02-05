"""empty message

Revision ID: 32986e804c51
Revises: 
Create Date: 2022-02-05 21:37:34.932393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32986e804c51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'name')
    # ### end Alembic commands ###
