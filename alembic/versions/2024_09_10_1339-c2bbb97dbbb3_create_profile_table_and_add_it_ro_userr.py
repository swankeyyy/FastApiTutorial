"""Create profile table and add it ro Userr

Revision ID: c2bbb97dbbb3
Revises: b4e41b9354a5
Create Date: 2024-09-10 13:39:19.353285

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c2bbb97dbbb3"
down_revision: Union[str, None] = "b4e41b9354a5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profile",
        sa.Column("firstname", sa.String(length=40), nullable=True),
        sa.Column("lastname", sa.String(length=40), nullable=True),
        sa.Column("bio", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("profile")
    # ### end Alembic commands ###
