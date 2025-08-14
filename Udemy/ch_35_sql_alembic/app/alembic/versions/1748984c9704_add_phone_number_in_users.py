"""add phone number in users

Revision ID: 1748984c9704
Revises: d52c3f4f135a
Create Date: 2025-08-13 21:10:29.836497

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1748984c9704"
down_revision: Union[str, Sequence[str], None] = "d52c3f4f135a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone", sa.Integer))


def downgrade() -> None:
    op.drop_column("users", "phone")
