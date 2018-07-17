"""Made stack_id a string instead of a hybrid method/property

Revision ID: aa61c2068005
Revises: 5776cd8b9a7f
Create Date: 2018-07-18 00:40:52.829401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa61c2068005'
down_revision = '5776cd8b9a7f'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_engine1():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('replays', sa.Column('dire_stack_id', sa.String(), nullable=True))
    op.add_column('replays', sa.Column('radiant_stack_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade_engine1():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('replays', 'radiant_stack_id')
    op.drop_column('replays', 'dire_stack_id')
    # ### end Alembic commands ###


def upgrade_engine2():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team_info', sa.Column('stack_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade_engine2():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('team_info', 'stack_id')
    # ### end Alembic commands ###

