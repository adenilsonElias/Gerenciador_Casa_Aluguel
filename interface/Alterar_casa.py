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
        self.botao_concluir.clicked.connect(self.concluir)
        self.setInfo()
        self.show()
    
    def setInfo(self):
        nome_casa = self.parente[1]
        valor_aluguel = self.parente[2]
        
