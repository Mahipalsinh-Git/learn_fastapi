"""phone column unique

Revision ID: 68c448e167a0
Revises: 1748984c9704
Create Date: 2025-08-13 21:20:02.227498

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "68c448e167a0"
down_revision: Union[str, Sequence[str], None] = "1748984c9704"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.create_unique_constraint("uq_users_phone", "users", ["phone"])
    with op.batch_alter_table("users") as batch_op:  # when update constraints in DB
        batch_op.create_unique_constraint("uq_users_phone", ["phone"])


def downgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_constraint("uq_users_phone", type_="unique")
