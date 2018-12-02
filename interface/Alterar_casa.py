from api import *
from PyQt5.QtWidgets import QWidget,QMessageBox
from PyQt5.uic import loadUi


class Alterar_casa(QWidget):
    def __init__(self,parente,info):
        super().__init__()
        self.parente = parente
        self.parente.hide()
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
        self.campo_numero_instalacao.setText(self.info[5].text())
        self.CPF_titular.setText(self.info[4].text())
        if self.info[3].text() != "NULL":
            self.checkBox_aguaInclusa.setChecked(True)
        if self.info[4].text() != "NULL":
            self.checkBox_luzinclusa.setChecked(True)
        self.mostrar_RGI()
        self.mostrar_instalacao()
    
    def cancelar(self):
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
            self.label_5.setEnabled(True)
            self.RGI.setEnabled(True)

        else:
            self.label_5.setEnabled(False)
            self.RGI.setEnabled(False)

    def mostrar_instalacao(self):
        """
        VIEW - responsavel por mostrar os itens da parte instalação eletrica
        """
        if self.checkBox_luzinclusa.checkState() == 2:
            self.label_4.setEnabled(True)
            self.campo_numero_instalacao.setEnabled(True)
            self.label_3.setEnabled(True)
            self.CPF_titular.setEnabled(True)

        else:
            self.label_4.setEnabled(False)
            self.campo_numero_instalacao.setEnabled(False)
            self.label_3.setEnabled(False)
            self.CPF_titular.setEnabled(False)

    def pegarItens(self):
        instalacao = None
        RGI = None

        if self.checkBox_aguaInclusa.checkState() == 2:
            RGI = self.RGI.text()
            if len(RGI) != 10:
                self.mensagem("erro RGI")
                return 
        if self.checkBox_luzinclusa.checkState() == 2:
            instalacao = self.campo_numero_instalacao.text()
            Cpf = self.CPF_titular.text()
            if len(instalacao) != 10:
                self.mensagem("Erro instalacao")
                return
            if len(Cpf) != 11:
                self.mensagem("Erro no cpf")
                return
            if self.info[5].text() == self.campo_numero_instalacao.text():
                self.parente.Instalacao.altera_instalacao(num_instalacao=self.campo_numero_instalacao.text(),
                                                        cpf=self.CPF_titular.text())
            else:
                self.parente.Instalacao.adiciona_instalacao_eletrica(num_instalacao=self.campo_numero_instalacao.text(),cpf=self.CPF_titular.text())
        nome = self.campo_nomeDaCasa.text()
        if len(nome) == 0:
            self.mensagem("Nome vazio")
            return
        try:
            aluguel = float(self.campo_valorDoAluguel.text())
        except:
            self.mensagem("Erro aluguel")
            return        
        self.parente.Casa.altera_casa(nome=nome,
                            valor_aluguel=aluguel,
                            agua=RGI,id=int(self.info[0].text()),num_instalacao=instalacao,commit=True)         
        self.cancelar()
        
    def mensagem(self, mensa):
        mens = QMessageBox()
        mens.setText(mensa)
        mens.exec()        

    def closeEvent(self,event):
        event.ignore()
        self.cancelar() 