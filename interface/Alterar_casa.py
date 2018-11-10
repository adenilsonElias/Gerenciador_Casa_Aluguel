from api import *
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class Alterar_casa(QWidget):
    def __init__(self,parente,info):
        super().__init__()
        self.parente = parente
        self.info = info
        self.ui = self
        loadUi("interface/Alterar_casa.ui", self.ui)
        self.botao_cancelar.clicked.connect(self.cancelar)
        self.botao_concluir.clicked.connect(self.pegarItens)
        self.checkBox_aguaInclusa.stateChanged.connect(self.mostrar_RGI)
        self.checkBox_luzinclusa.stateChanged.connect(self.mostrar_instalacao)
        self.setInfo()
        self.show()
    
    def setInfo(self):
        self.campo_nomeDaCasa.setText(self.info[1].text())
        self.campo_valorDoAluguel.setText(self.info[2].text())
        self.RGI.setText(self.info[3].text())
        self.campo_numero_instalacao.setText(self.info[4].text())
        self.CPF_titular.setText(self.info[5].text())
        if self.info[3].text() != "NULL":
            self.checkBox_aguaInclusa.setChecked(True)
        if self.info[4].text() != "NULL":
            self.checkBox_luzinclusa.setChecked(True)
        self.mostrar_RGI()
        self.mostrar_instalacao()
    
    def cancelar(self):
        self.setParent(None)
        self.hide()
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
        instalacao = None
        # if self.checkBox_luzinclusa.checkState() == 2:
        #     print("adas")
        #     instalacao = ins.adiciona_instalacao_eletrica(num_instalacao=self.campo_numero_instalacao.text(),
        #                                     cpf=self.CPF_titular.text())
        self.parente.Casa.altera_casa(nome=self.campo_nomeDaCasa.text(),
                            valor_aluguel=self.campo_valorDoAluguel.text(),
                            agua=self.RGI.text(),id=int(self.info[0].text()),instalacao_eletrica=instalacao,commit=True)         
        self.cancelar()
        
        
