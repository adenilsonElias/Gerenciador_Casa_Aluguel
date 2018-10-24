"""
API do Gerenciador de Casas de Aluguel
======================================

"""
# https://www.pythoncentral.io/introduction-to-sqlite-in-python/

import sqlite3

import config


def make_connection():

    return sqlite3.connect(config.DATABASE_URL)


class DAO():


    def __init__(self, conn):

        self.conn = conn


class Casa_DAO(DAO):


    def adiciona_casa(self, nome=None, valor_aluguel=None, agua=None,
                      instalacao_eletrica=None, commit=False, rollback=False):
        if nome is None:
            raise Exception("Necessário prover nome.")
        if valor_aluguel is None:
            raise Exception("Necessário prover um valor para o aluguel.")

        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO
                casa(nome_casa, valor_aluguel_casa, agua_casa, num_instalacao)
                VALUES
                (?,?,?,?)
            """, (nome, valor_aluguel, agua, instalacao_eletrica))
            if commit:
                self.conn.commit()
            return {
                'id_casa': cursor.lastrowid,
                'nome_casa': nome,
                'valor_aluguel': valor_aluguel,
                'agua_casa': agua,
                'num_instalacao_eletrica': instalacao_eletrica
            }
        except sqlite3.Error as e:
            if rollback: 
                self.conn.rollback()
            return None


    def todas_casas(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM casa;
        """)
        casas = cursor.fetchall()

        return [{
            'id_casa': x[0],
            'nome_casa': x[1],
            'valor_aluguel': x[2],
            'agua_casa': x[3],
            'num_instalacao_eletrica': x[4]
        } for x in casas]


class Instalacao_Eletrica_DAO(DAO):

    def adiciona_instalacao_eletrica(self, num_instalacao=None, cpf=None, commit=False, rollback=False):

        if num_instalacao is None:
            raise Exception("Necessário prover um número de instalação")
        if cpf is None:
            raise Exception("Necessário prover um número de CPF")
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO
                instalacao_eletrica
                VALUES
                (?, ?)
            """, (num_instalacao, cpf))
            if commit:
                self.conn.commit()
            return {
                'num_instalacao': num_instalacao, 
                'cpf_titular': cpf
            }
        except sqlite3.Error as e:
            # e
            if rollback:
                self.conn.rollback()
            return None
    
    def todas_instalacoes(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM instalacao_eletrica;
        """)
        instalcoes = cursor.fetchall()

        return [{
            'num_instalacao': x[0],
            'cpf_titular': x[1]
        } for x in instalacoes]

class Inquilino_DAO(DAO):

    def adiciona_inquilino(self, cpf=None, nome=None,
                           rg=None, commit=False, rollback=False):
        if cpf is None:
            raise Exception("Necessário prover um número de CPF")
        if nome is None:
            raise Exception("Necessário prover um Nome")
        if rg is None:
            raise Exception("Necessário prover um RG")
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO
                inquilino(cpf_inq, nome_inq, rg_inq)
                VALUES
                (?, ?, ?)
            """, (cpf, nome, rg))
            if commit:
                self.conn.commit()
            return {
                'id_inq': cursor.lastrowid,
                'cpf_inq': cpf,
                'nome_inq': nome,
                'rg_inq': rg
            }
        except sqlite3.Error as e:
            if rollback:
                self.conn.rollback()
            return None 

    def todos_inquilinos(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM inquilino;
        """)
        inquilinos = cursor.fetchall()
        return [{
            'id_inq': x[0],
            'cpf_inq': x[1],
            'nome_inq': x[2],
            'rg_inq': x[3]
        } for x in inquilinos]

    def altera_inquilino(self, id=None, commit=False, rollback=False,
                         **kwargs):
        
        if id is None:
            raise Exception("Necessário prover um ID")
        if not len(kwargs):
            raise Exception("Necessário prover novas informações para o Inquilino")

        query = f'''UPDATE inquilino
                SET {', '.join([f'{key}_inq = ?' for key in kwargs.keys()])}
                WHERE id_inq = {id}'''
        print(query)
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, tuple((kwargs[k] for k in kwargs.keys())) + (id))
            if commit:
                self.conn.commit()
        except sqlite3.Error as e:
            if rollback:
                self.conn.rollback()



class Contrato_DAO(DAO):

    def adiciona_contrato(self, valor=None, ativo=True, dia_vencimento=None,
                          fim_contrato=None, casa=None, inq=None,
                          commit=False, rollback=False):
        if valor is None:
            raise Exception("Necessário prover um valor de aluguel para o contrato")
        if dia_vencimento is None:
            raise Exception("Necessário prover uma data de vencimento")
        if casa is None:
            raise Exception("Necessário escolher uma casa")
        if inq is None:
            raise Exception("Necessário escolher um inquilino")
        try:
            cursor = self.conn.cursor()
            print(type(inq))
            cursor.execute("""
                INSERT INTO
                contrato(valor, ativo, dt_fim_contrato, dia_venc_aluguel, id_casa, id_inq)
                VALUES
                (?,?,?,?,?,?)
            """, (valor, ativo,fim_contrato, dia_vencimento, casa, inq))
            if commit:
                self.conn.commit()
            return {
                'id_contrato': cursor.lastrowid,
                'valor': valor,
                'ativo': ativo,
                'dt_fim_contrato': fim_contrato,
                'dia_venc_aluguel': dia_vencimento,
                'id_casa': casa,
                'id_inq': inq
                }
        except sqlite3.Error as e:
            if rollback:
                self.conn.rollback()
            return None

    def todos_contratos(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM contrato;
        """)
        contratos = cursor.fetchall()
        return [{
            'id_contrato': x[0],
            'valor': x[1],
            'ativo': x[2],
            'dt_fim_contrato': x[3],
            'dia_venc_aluguel': x[4],
            'id_casa': x[5],
            'id_inq': x[6]

        } for x in contratos]

    def altera_valor_contrato(self, id=None, valor=None, commit=False, rollback=False):
        
        if id is None:
            raise Exception("Necessário prover um ID")
        if valor is None:
            raise Exception("Necessário prover um valor")

        query = f'''UPDATE contrato
                SET valor = ?
                WHERE id_contrato = ?'''
        print(query)
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (valor, id))
            if commit:
                self.conn.commit()
                
        except sqlite3.Error as e:
            if rollback:
                self.conn.rollback()
            print(e)

class PagamentoDAO(DAO):

    def realiza_pagamento(self, id_contrato=None, dt_pag=None, dt_venc=None, deposito=False, commit=False, rollback=False):

        if id_contrato is None:
            raise Exception("Necessário prover um contrato")
        if dt_venc is None:
            raise Exception("Necessário prover uma data de vencimento")
        if dt_pag is None:
            raise Exception("Necessário prover uma data de pagamento")
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO
                pagamento(dt_venc, dt_pag, deposito, id_contrato)
                VALUES
                (?, ?, ?, ?)
            """, (dt_venc, dt_pag, deposito, id_contrato))
            if commit:
                self.conn.commit()
            return {
                'id_pag': cursor.lastrowid ,
                'dt_venc': dt_venc ,
                'dt_pag': dt_pag ,
                'deposito': deposito ,
                'id_contrato': id_contrato
            }
        except sqlite3.Error as e:
            if rollback:
                self.conn.rollback()
            return None

    def todos_pagamentos(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM pagamento;
        """)
        pagamentos = cursor.fetchall()
        return [{
            'id_pag': x[0] ,
            'dt_venc': x[1] ,
            'dt_pag': x[2] ,
            'deposito': x[3] ,
            'id_contrato': x[4]
        } for x in pagamentos]
    
    def todos_pagamentos_contrato(self, id_contrato):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM pagamento
            WHERE pagamento.id_contrato = ?;
        """, (id_contrato))
        pagamentos = cursor.fetchall()
        return [{
            'id_pag': x[0] ,
            'dt_venc': x[1] ,
            'dt_pag': x[2] ,
            'deposito': x[3] ,
            'id_contrato': x[4]
        } for x in pagamentos]
    
def start_db(conn):
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS instalacao_eletrica (
            num_instalacao VARCHAR(20) NOT NULL PRIMARY KEY,
            cpf_titular VARCHAR(11) NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS casa(
            id_casa INTEGER NOT NULL PRIMARY KEY,
            nome_casa INTEGER NOT NULL,
            valor_aluguel_casa INTEGER NOT NULL,
            agua_casa VARCHAR(10),
            num_instalacao VARCHAR(11) UNIQUE,
            FOREIGN KEY (num_instalacao) REFERENCES instalacao_eletrica(num_instalacao)
        );
        
        CREATE TABLE IF NOT EXISTS inquilino(
            id_inq INTEGER NOT NULL PRIMARY KEY,
            cpf_inq VARCHAR(11) NOT NULL UNIQUE,
            nome_inq VARCHAR(40) NOT NULL,
            rg_inq VARCHAR(10) NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS contrato(
            id_contrato INTEGER NOT NULL PRIMARY KEY,
            valor REAL NOT NULL,
            ativo INTEGER NOT NULL,
            dt_fim_contrato DATE NOT NULL,
            dia_venc_aluguel INTEGER NOT NULL,
            id_casa INTEGER NOT NULL,
            id_inq INTEGER NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS pagamento(
            id_pag INTEGER NOT NULL PRIMARY KEY,
            dt_venc VARCHAR(23) NOT NULL,
            dt_pag VARCHAR(23),
            deposito INTEGER NOT NULL,
            id_contrato INTEGER ,
            FOREIGN KEY (id_contrato) REFERENCES contrato(id_contrato)
        );
        """)
