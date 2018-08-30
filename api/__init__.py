"""
API do GErenciador de Casas de Aluguel
--------------------------------------

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import Casa, Instalacao_Eletrica, Inquilino, Contrato
import config
# from config import URL


def make_engine():
    """
    TODO
    """
    return create_engine(config.DATABASE_URL)


def make_connection(engine):
    """
    TODO
    """
    if engine is None:
        raise Exception("Necessário prover uma conexão")
    Session = sessionmaker()
    Session.configure(bind=engine)
    return Session()


class DAO():
    """
    TODO
    """

    def __init__(self, session):
        """
        TODO
        """
        self.session = session


class Casa_DAO(DAO):
    """
    TODO
    """

    def adiciona_casa(self, id=None, nome=None, valor_aluguel=None,
                      agua=None, instalacao_eletrica=None):
        """
        TODO
        """
        if None in [nome, valor_aluguel]:
            raise Exception("Campos Obrigatórios Faltantes")
            # TODO: separar raises
        casa = Casa()
        casa.id_casa = id
        casa.nome_casa = nome
        casa.valor_aluguel_casa = valor_aluguel
        casa.agua_casa = agua
        if instalacao_eletrica is not None:
            casa.num_instalacao_eletrica = instalacao_eletrica.num_instalacao

        self.session.add(casa)
        self.session.commit()

        return casa

    def todas_casas(self):
        return [x for x in self.session.query(Casa).all()]


class Instalacao_Eletrica_DAO(DAO):
    """
    TODO
    """

    def adiciona_instalacao_eletrica(self, num_instalacao=None, cpf=None):
        """
        TODO
        """

        if None in [num_instalacao, cpf]:
            raise Exception("Campos Obrigatórios Faltantes")
            # TODO: separar raises
        instalacao = Instalacao_Eletrica()
        instalacao.num_instalacao = num_instalacao
        instalacao.cpf_titular = cpf

        self.session.add(instalacao)
        self.session.commit()

        return instalacao


class Inquilino_DAO(DAO):
    """
    TODO
    """

    def adiciona_inquilino(self, id=None, cpf=None, nome=None, rg=None):
        """
        TODO
        """
        if None in [id, cpf, nome, rg]:
            raise Exception("Campos Obrigatórios Faltantes")
            # TODO: separar raises
        inq = Inquilino()
        inq.id_inq = id
        inq.nome_inq = nome
        inq.cpf_inq = cpf
        inq.rg_inq = rg

        self.session.add(inq)
        self.session.commit()

        return inq


class Contrato_DAO(DAO):
    """
    TODO
    """

    def adiciona_contrato(self, id=None, valor=None, ativo=None,
                          venc=None, casa=None, inq=None):
        """
        TODO
        """
        if None in [id, valor, ativo, venc, casa, inq]:
            raise Exception("Campos Obrigatórios Faltantes")
            # TODO: separar raises
        c = Contrato()
        c.id_contrato = id
        c.valor = valor
        c.ativo = ativo
        c.venc_contrato = venc
        c.id_casa = casa.id_casa
        c.id_inq = inq.id_inq

        self.session.add(c)
        self.session.commit()

        return c
