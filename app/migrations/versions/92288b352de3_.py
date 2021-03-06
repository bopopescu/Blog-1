"""empty message

Revision ID: 92288b352de3
Revises: 0f1ec457928d
Create Date: 2017-11-12 14:51:23.750997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92288b352de3'
down_revision = '0f1ec457928d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    # ### end Alembic commands ###
