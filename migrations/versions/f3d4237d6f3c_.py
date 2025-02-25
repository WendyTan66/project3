"""empty message

Revision ID: f3d4237d6f3c
Revises: 
Create Date: 2025-02-25 03:51:42.273866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3d4237d6f3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    op.drop_table('recipe')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('ingredients', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('instructions', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name='recipe_category_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='recipe_pkey')
    )
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('category_name', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='category_pkey'),
    sa.UniqueConstraint('category_name', name='category_category_name_key')
    )
    # ### end Alembic commands ###
