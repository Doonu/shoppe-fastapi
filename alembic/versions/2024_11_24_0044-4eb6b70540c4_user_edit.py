"""user edit

Revision ID: 4eb6b70540c4
Revises: fe4e94978c4d
Create Date: 2024-11-24 00:44:02.513176

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "4eb6b70540c4"
down_revision: Union[str, None] = "fe4e94978c4d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "user",
        "password",
        existing_type=postgresql.BYTEA(),
        type_=sa.String(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "user",
        "password",
        existing_type=sa.String(),
        type_=postgresql.BYTEA(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###