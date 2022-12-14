"""Init

Revision ID: 098620465df2
Revises: 
Create Date: 2022-12-07 16:32:51.368586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '098620465df2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FurnitureModel',
    sa.Column('furn_model', sa.String(), nullable=False),
    sa.Column('furn_model_name', sa.String(), nullable=True),
    sa.Column('characteristics', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('furn_model'),
    sa.UniqueConstraint('furn_model_name')
    )
    op.create_index(op.f('ix_FurnitureModel_furn_model'), 'FurnitureModel', ['furn_model'], unique=False)
    op.create_table('KA',
    sa.Column('id_ka', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('adress', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id_ka')
    )
    op.create_index(op.f('ix_KA_id_ka'), 'KA', ['id_ka'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('DocPayment',
    sa.Column('doc_num', sa.String(), nullable=False),
    sa.Column('id_KA', sa.Integer(), nullable=False),
    sa.Column('date_create', sa.DateTime(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_KA'], ['KA.id_ka'], ),
    sa.PrimaryKeyConstraint('doc_num')
    )
    op.create_index(op.f('ix_DocPayment_doc_num'), 'DocPayment', ['doc_num'], unique=False)
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_items_description'), 'items', ['description'], unique=False)
    op.create_index(op.f('ix_items_id'), 'items', ['id'], unique=False)
    op.create_index(op.f('ix_items_title'), 'items', ['title'], unique=False)
    op.create_table('Payment',
    sa.Column('id_payment', sa.Integer(), nullable=False),
    sa.Column('doc_num', sa.String(), nullable=False),
    sa.Column('furn_model', sa.String(), nullable=False),
    sa.Column('furn_name', sa.String(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['doc_num'], ['DocPayment.doc_num'], ),
    sa.ForeignKeyConstraint(['furn_model'], ['FurnitureModel.furn_model'], ),
    sa.PrimaryKeyConstraint('id_payment')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Payment')
    op.drop_index(op.f('ix_items_title'), table_name='items')
    op.drop_index(op.f('ix_items_id'), table_name='items')
    op.drop_index(op.f('ix_items_description'), table_name='items')
    op.drop_table('items')
    op.drop_index(op.f('ix_DocPayment_doc_num'), table_name='DocPayment')
    op.drop_table('DocPayment')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_KA_id_ka'), table_name='KA')
    op.drop_table('KA')
    op.drop_index(op.f('ix_FurnitureModel_furn_model'), table_name='FurnitureModel')
    op.drop_table('FurnitureModel')
    # ### end Alembic commands ###
