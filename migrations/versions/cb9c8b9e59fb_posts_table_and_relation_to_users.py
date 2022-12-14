"""posts table and relation to users

Revision ID: cb9c8b9e59fb
Revises: 51e2cd6d8ad9
Create Date: 2022-10-14 11:01:15.342528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb9c8b9e59fb'
down_revision = '51e2cd6d8ad9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_created'), 'post', ['created'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_created'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
