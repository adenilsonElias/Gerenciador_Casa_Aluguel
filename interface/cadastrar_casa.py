from .. import api

from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class interagir_casa(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        loadUi("cadastrar_casa.ui", self)
        self.mostrar_RGI()
        self.mostrar_instalacao()
        self.ui.botao_concluir.clicked.connect(self.pegarItens)
        self.ui.botao_cancelar.clicked.connect(self.sair)
        self.ui.checkBox_aguaInclusa.stateChanged.connect(self.mostrar_RGI)
        self.ui.checkBox_luzinclusa.stateChanged.connect(
            self.mostrar_instalacao)
        self.show()

    def sair(self):
        self.setParent(None)
        self.hide()
        self.close()

    def move_incremento(self):
        self.botao_concluir.move(10, self.botao_concluir.y() + 36)
        self.botao_cancelar.move(10, self.botao_cancelar.y() + 33)
        self.resize(128, self.height() + 32)

    def move_decrementa(self):
        self.botao_concluir.move(10, self.botao_concluir.y() - 36)
        self.botao_cancelar.move(10, self.botao_cancelar.y() - 33)
        self.resize(128, self.height() - 32)

    def mostrar_RGI(self):

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

    def pegarItens(self):
        info = {
            "nome casa": self.campo_nomeDaCasa.text(),
            "aluguel": self.campo_valorDoAluguel.text(),
            "agua inclusa": self.checkBox_aguaInclusa.checkState(),
            "luz inclusa": self.checkBox_luzinclusa.checkState(),
            "RGI": self.RGI.text(),
            "instalacao": self.campo_numero_instalacao.text()
        }
        print(info)
        self.sair()
