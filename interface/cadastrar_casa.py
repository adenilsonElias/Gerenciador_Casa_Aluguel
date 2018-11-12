from api import *
from PyQt5.QtWidgets import QWidget,QMessageBox
from PyQt5.uic import loadUi


class interagir_casa(QWidget):
    def __init__(self,parente):
        super().__init__()
        self.ui = self
        self.parente = parente
        self.parente.hide()
        loadUi("interface/cadastrar_casa.ui", self.ui)
        self.mostrar_RGI()
        self.mostrar_instalacao()
        self.botao_concluir.clicked.connect(self.pegarItens)
        self.botao_cancelar.clicked.connect(self.sair)
        self.checkBox_aguaInclusa.stateChanged.connect(self.mostrar_RGI)
        self.checkBox_luzinclusa.stateChanged.connect(self.mostrar_instalacao)
        self.setFocus(True)
        self.show()

    def sair(self):
        """
        VIEW
        """
        self.setParent(None)
        self.hide()
        self.parente.show()
        self.parente.atualizar()
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
        instalacao = None
        if self.checkBox_luzinclusa.checkState() == 2:
            instalacao = self.campo_numero_instalacao.text()
            if len(instalacao) != 10:
                self.mensagem("instalacao vazia ou invalida")
                return

            cpf = self.CPF_titular.text()
            if len(cpf) != 11:
                self.mensagem("cpf vazio ou invalido")
                return
            self.parente.Instalacao.adiciona_instalacao_eletrica(num_instalacao=self.campo_numero_instalacao.text(),
                                                                 cpf=self.CPF_titular.text())
        RGI = self.RGI.text()
        if len(RGI) != 10 and len(RGI) != 0:
            self.mensagem("Rgi invalido")
            return 
        nome = self.campo_nomeDaCasa.text()
        if len(nome) == 0:
            self.mensagem("Nome vazio")
            return
        aluguel = self.campo_valorDoAluguel.text()
        try:
            a = float(aluguel)
        except:
            self.mensagem("Erro aluguel")
            return
        self.parente.Casa.adiciona_casa(nome=nome,
                            valor_aluguel=aluguel,
                            agua=RGI,instalacao_eletrica=instalacao,commit=True)         
        self.sair()

    def mensagem(self, mensa):
        mens = QMessageBox()
        mens.setText(mensa)
        mens.exec()

