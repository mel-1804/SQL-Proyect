"""empty message

Revision ID: 928d6b3564e5
Revises: 
Create Date: 2024-09-30 18:56:44.954925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '928d6b3564e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('animal_type_id', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('age_months', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('animal_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('animal', sa.String(length=50), nullable=False),
    sa.Column('pet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pets_id', sa.Integer(), nullable=True),
    sa.Column('loc_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pets_id'], ['pets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('loc_id')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('region', sa.String(length=50), nullable=False),
    sa.Column('comuna', sa.String(length=50), nullable=False),
    sa.Column('pet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sterilization_state',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('pet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sterilization_state')
    op.drop_table('location')
    op.drop_table('favorites')
    op.drop_table('animal_type')
    op.drop_table('user')
    op.drop_table('pets')
    # ### end Alembic commands ###
