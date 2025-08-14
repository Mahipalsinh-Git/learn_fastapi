"""create tables

Revision ID: d52c3f4f135a
Revises:
Create Date: 2025-08-13 20:51:24.103624

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d52c3f4f135a"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("email", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
