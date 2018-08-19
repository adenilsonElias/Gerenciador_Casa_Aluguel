from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
class interagir_Inquilino(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        loadUi("cadastrar_inquilino.ui",self.ui)
        self.botao_concluir.clicked.connect(self.pegarItens)
        self.botao_cancelar.clicked.connect(self.cancelar)
        self.addInList()

    def pegarItens(self):
        info = {
            "nome": self.campo_nome.text(),
            "CPF" : self.campo_CPF.text(),
            "RG"  : self.campo_RG.text(),
            "casa": self.comboBox_casa.currentText()
        }
        print(info)
    
    def cancelar(self):
        self.setParent(None)
        self.update()
        self.close()
    
    def addInList(self):
        self.comboBox_casa.addItems(["casa 1","casa 2","casa 3"])

