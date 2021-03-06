"""timestamp for address table

Revision ID: 61ab9f1f9600
Revises: f431f181d6fe
Create Date: 2019-01-30 14:56:53.288762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61ab9f1f9600'
down_revision = 'f431f181d6fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_address_timestamp'), 'address', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_address_timestamp'), table_name='address')
    op.drop_column('address', 'timestamp')
    # ### end Alembic commands ###
