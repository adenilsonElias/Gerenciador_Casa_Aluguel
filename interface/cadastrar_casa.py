from api import *
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class interagir_casa(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        loadUi("interface/cadastrar_casa.ui", self.ui)
        self.mostrar_RGI()
        self.mostrar_instalacao()
        self.botao_concluir.clicked.connect(self.pegarItens)
        self.botao_cancelar.clicked.connect(self.sair)
        self.checkBox_aguaInclusa.stateChanged.connect(self.mostrar_RGI)
        self.checkBox_luzinclusa.stateChanged.connect(self.mostrar_instalacao)
        self.show()

    def sair(self):
        """
        VIEW
        """
        self.setParent(None)
        self.hide()
        self.close()

    def mostrar_RGI(self):
        """
        VIEW
        """

        if self.checkBox_aguaInclusa.checkState() == 2:
            self.label_5.show()
            self.RGI.show()
            self.checkBox_luzinclusa.move(
                self.checkBox_luzinclusa.x(), self.RGI.y() + 40)
            self.mostrar_instalacao()
        else:
            self.label_5.hide()
            self.RGI.hide()
            self.checkBox_luzinclusa.move(
                self.checkBox_luzinclusa.x(), self.checkBox_aguaInclusa.y() + 30)
            self.mostrar_instalacao()

    def mostrar_instalacao(self):
        """
        VIEW - responsavel por mostrar os itens da parte instalação eletrica
        """
        if self.checkBox_luzinclusa.checkState() == 2:
            self.label_4.show()
            self.label_4.move(self.label_4.x(),
                              self.checkBox_luzinclusa.y() + 30)
            self.campo_numero_instalacao.show()
            self.campo_numero_instalacao.move(self.campo_numero_instalacao.x(),
                                              self.label_4.y() + 30)
            self.label_3.show()
            self.label_3.move(self.label_3.x(),
                              self.campo_numero_instalacao.y() + 30)
            self.CPF_titular.show()
            self.CPF_titular.move(self.CPF_titular.x(), self.label_3.y() + 30)
            self.botao_concluir.move(
                self.botao_concluir.x(), self.CPF_titular.y() + 40)
            self.botao_cancelar.move(
                self.botao_cancelar.x(), self.CPF_titular.y() + 40)
            self.resize(self.width(), self.botao_concluir.y() + 40)
            self.setFixedSize(self.width(), self.botao_concluir.y() + 40)

        else:
            self.label_4.hide()
            self.campo_numero_instalacao.hide()
            self.label_3.hide()
            self.CPF_titular.hide()
            self.botao_concluir.move(
                self.botao_concluir.x(), self.checkBox_luzinclusa.y() + 30)
            self.botao_cancelar.move(
                self.botao_cancelar.x(), self.checkBox_luzinclusa.y() + 30)
            self.resize(self.width(), self.botao_concluir.y() + 40)
            self.setFixedSize(self.width(), self.botao_concluir.y() + 40)


    def pegarItens(self):
        """
        CONTROL pega os itens do views e manda para as apis DAO
        """
        conn = make_connection()
        casas = Casa_DAO(conn)
        instalacao = None
        if self.checkBox_luzinclusa.checkState() == 2:
            ins = Instalacao_Eletrica_DAO(conn)
            instalacao = ins.adiciona_instalacao_eletrica(num_instalacao=self.campo_numero_instalacao.text(),
                                            cpf=self.CPF_titular.text())
        casas.adiciona_casa(nome=self.campo_nomeDaCasa.text(),
                            valor_aluguel=self.campo_valorDoAluguel.text(),
                            agua=self.RGI.text(),instalacao_eletrica=instalacao,commit=True)         
        self.sair()


