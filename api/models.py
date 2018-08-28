from sqlalchemy import (Column, Integer, String, Date, Boolean,
                        DECIMAL, create_engine, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Instalacao_Eletrica(Base):
    __tablename__ = 'instalacao_eletrica'
    num_instalacao = Column(String(20), primary_key=True, nullable=False)
    cpf_titular = Column(String(11), nullable=False, unique=True)
    # casas = relationship("Casa", backref='instalacao_eletrica')
    casas = relationship("Casa")


class Casa(Base):
    __tablename__ = 'casa'
    id_casa = Column(Integer, primary_key=True, nullable=False)
    nome_casa = Column(String(40), nullable=False)
    valor_aluguel_casa = Column(DECIMAL, nullable=False)
    agua_casa = Column(String(10))
    num_instalacao_eletrica = Column(
        Integer, ForeignKey('instalacao_eletrica.num_instalacao'))
    # instalacoes_eletricas = relationship('Instalacao_Eletrica',
    # backref='casa')
    # instalacoes_eletricas = relationship('Instalacao_Eletrica',
    # backref='casa')


class Inquilino(Base):
    __tablename__ = 'inquilino'
    id_inq = Column(Integer, primary_key=True, nullable=False)
    cpf_inq = Column(String(11), nullable=False, unique=True)
    nome_inq = Column(String(40), nullable=False)
    rg_inq = Column(String(10), nullable=False)


class Pagamento(Base):
    __tablename__ = 'pagamento'
    id_pag = Column(Integer, primary_key=True, nullable=False)
    dt_venc = Column(Date, nullable=False)
    dt_pag = Column(Date)
    deposito = Column(Boolean, nullable=False)
    id_inq = Column(Integer, ForeignKey('inquilino.id_inq'))
    id_contrato = Column(Integer, ForeignKey(
        'contrato.id_contrato'), nullable=False)


class Contrato(Base):
    __tablename__ = 'contrato'
    id_contrato = Column(Integer, primary_key=True, nullable=False)
    valor = Column(DECIMAL, nullable=False)
    ativo = Column(Boolean, nullable=False)
    venc_contrato = Column(Date, nullable=False)
    id_casa = Column(Integer, ForeignKey('casa.id_casa'), nullable=False)
    id_inq = Column(Integer, ForeignKey('inquilino.id_inq'), nullable=False)
    # id_pag = Column(Integer, ForeignKey('pagamento.id_pag'), )


engine = create_engine('sqlite:///teste.bd')
Base.metadata.create_all(engine)
