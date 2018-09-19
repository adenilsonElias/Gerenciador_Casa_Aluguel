"""isuue #7

Revision ID: c0dc38f4ef62
Revises: 5fe688a037c9
Create Date: 2018-09-19 15:03:57.931484

"""
import sys
import sqlalchemy as sa
import sqlite3
from alembic import op
# import config

# from api.models import Contrato

# revision identifiers, used by Alembic.
revision = 'c0dc38f4ef62'
down_revision = '5fe688a037c9'
branch_labels = None
depends_on = None


def upgrade():
    # with op.batch_alter_table('contrato', schema=None) as contrato:
        # contrato.alter_column('venc_contrato')
    with sqlite3.connect('sqlite:///teste.bd') as db:
        db.execute("""
            pragma foreign_keys = off;
            alter table contrato rename to _contrato_old;
            CREATE TABLE contrato ( 
                id_contrato INTEGER NOT NULL, 
                valor DECIMAL NOT NULL, 
                ativo BOOLEAN NOT NULL, 
                dt_venc_contrato DATE NOT NULL, 
                id_casa INTEGER NOT NULL, 
                id_inq INTEGER NOT NULL, 
                PRIMARY KEY (id_contrato), 
                CHECK (ativo IN (0, 1)), 
                FOREIGN KEY(id_casa) 
                REFERENCES casa (id_casa), 
                FOREIGN KEY(id_inq) 
                REFERENCES inquilino (id_inq) );
                
                
            insert into contrato (id_contrato , 
                valor , 
                ativo , 
                dt_venc_contrato , 
                id_casa , 
                id_inq ) select id_contrato , 
                valor , 
                ativo , 
                venc_contrato , 
                id_casa , 
                id_inq from _contrato_old;
            commit;
            drop table _contrato_old;
            PRAGMA foreign_keys=on;
        """)
    op.add_column('contrato', sa.Column('dia_venc_aluguel', sa.Integer))
    # pass


def downgrade():
    op.drop_column('contrato', 'dia_venc_aluguel')
    op.alter_column('contrato', 'dt_fim_contrato', name='venc_contrato')
    #  = Column()
    # pass
