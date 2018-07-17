"""Initial with hybrid Replay.stack_id

Revision ID: 5776cd8b9a7f
Revises: 
Create Date: 2018-07-18 00:05:20.524102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5776cd8b9a7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_engine1():
    pass


def downgrade_engine1():
    pass


def upgrade_engine2():
    pass


def downgrade_engine2():
    pass

