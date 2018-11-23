from api import *
from PyQt5.QtWidgets import QWidget,QMessageBox
from PyQt5.uic import loadUi


class Alterar_inq(QWidget):
    def __init__(self,parente,info):
        super().__init__()
        self.parente = parente
        self.parente.hide()
        self.info = info
        self.ui = self
        loadUi("interface/Alterar_inq.ui", self.ui)
        self.botao_cancelar.clicked.connect(self.cancelar)
        self.botao_concluir.clicked.connect(self.concluir)
        self.setInfo()
        self.show()
    
    def setInfo(self):
        self.campo_nome.setText(self.info[1].text())
        self.campo_CPF.setText(self.info[2].text())
        self.campo_RG.setText(self.info[3].text())
    
    def cancelar(self,atualizar=False):
        self.setParent(None)
        self.hide()
        self.parente.show()
        if atualizar:
            self.parente.atualizar()
        self.close()
    
    def mensagem(self,mensa):
        mens = QMessageBox()
        mens.setText(mensa)
        mens.exec()

    def concluir(self):
        print(self.info)
        nome = self.campo_nome.text()
        if len(nome) == 0:
            self.mensagem("Nome esta vazio")
            return
        cpf = self.campo_CPF.text()
        if len(cpf) != 11:
            self.mensagem("CPF vazio ou invalido")
            return
        rg = self.campo_RG.text()
        if len(rg) == 0:
            self.mensagem("Rg vazio")
            return
        self.parente.Inquilino.altera_inquilino(id=int(self.info[0].text()),
                                                nome=nome,
                                                rg=rg,
                                                cpf=cpf,
                                                commit=True)
        self.cancelar(atualizar=True)

    def closeEvent(self,event):
        event.ignore()
        self.cancelar() 