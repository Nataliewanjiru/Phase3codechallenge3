"""Add columns 'first_name' and 'last_name' to customers and 'restaurant_name' and 'restaurant_price' to restaurants.

Revision ID: 16e5a5a54c2f
Revises:
Create Date: 2023-09-02 15:18:27.801354
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision: str = '16e5a5a54c2f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Define column names and lengths as constants
CUSTOMER_TABLE = 'customers'
RESTAURANT_TABLE = 'restaurants'
COL_LENGTH = 100

def upgrade() -> None:
    op.add_column(CUSTOMER_TABLE, sa.Column('first_name', sa.String(length=COL_LENGTH), nullable=True))
    op.add_column(CUSTOMER_TABLE, sa.Column('last_name', sa.String(length=COL_LENGTH), nullable=True))
    op.drop_column(CUSTOMER_TABLE, 'name')

    op.add_column(RESTAURANT_TABLE, sa.Column('restaurant_name', sa.String(length=COL_LENGTH), nullable=True))
    op.add_column(RESTAURANT_TABLE, sa.Column('restaurant_price', sa.Integer(), nullable=True))
    op.drop_column(RESTAURANT_TABLE, 'name')

def downgrade() -> None:
    op.add_column(CUSTOMER_TABLE, sa.Column('name', sa.String(length=COL_LENGTH), nullable=True))
    op.drop_column(CUSTOMER_TABLE, 'last_name')
    op.drop_column(CUSTOMER_TABLE, 'first_name')

    op.add_column(RESTAURANT_TABLE, sa.Column('name', sa.String(length=COL_LENGTH), nullable=True))
    op.drop_column(RESTAURANT_TABLE, 'restaurant_price')
    op.drop_column(RESTAURANT_TABLE, 'restaurant_name')
