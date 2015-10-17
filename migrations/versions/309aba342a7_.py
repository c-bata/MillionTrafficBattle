"""empty message

Revision ID: 309aba342a7
Revises: 3a219b1ab85
Create Date: 2015-10-17 11:22:56.603009

"""

# revision identifiers, used by Alembic.
revision = '309aba342a7'
down_revision = '3a219b1ab85'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###