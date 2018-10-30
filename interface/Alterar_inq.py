from api import *
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class Alterar_inq(QWidget):
    def __init__(self,parente,info):
        super().__init__()
        self.parente = parente
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
        if atualizar:
            self.parente.atualizar()
        self.close()
    
    def concluir(self):
        print(self.info)
        nome = self.campo_nome.text()
        cpf = self.campo_CPF.text()
        rg = self.campo_RG.text()
        self.parente.Inquilino.altera_inquilino(id=int(self.info[0].text()),
                                                nome=nome,
                                                rg=rg,
                                                cpf=cpf,
                                                commit=True)
        self.cancelar(atualizar=True)