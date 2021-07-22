"""empty message

Revision ID: 7da8798ffa59
Revises:
Create Date: 2021-07-22 00:43:56.567991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7da8798ffa59"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "actor",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column("gender",
                  sa.Enum("Male", "Female", name="gender"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "movie",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("release_date", sa.DateTime(), nullable=False),
        sa.Column("genre", sa.String(length=80), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "movie_actor",
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("actor_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["actor_id"],
            ["actor.id"],
        ),
        sa.ForeignKeyConstraint(
            ["movie_id"],
            ["movie.id"],
        ),
        sa.PrimaryKeyConstraint("movie_id", "actor_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("movie_actor")
    op.drop_table("movie")
    op.drop_table("actor")
    # ### end Alembic commands ###