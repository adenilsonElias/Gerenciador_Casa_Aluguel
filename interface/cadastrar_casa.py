from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class interagir_casa(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        loadUi("cadastrar_casa.ui",self)
        self.ui.botao_concluir.clicked.connect(self.pegarItens)
        self.ui.botao_cancelar.clicked.connect(self.sair)
        self.show()
    def sair(self):
        self.setParent(None)
        self.hide()
        self.close()

    def pegarItens(self):
        info = {
            "nome casa": self.campo_nomeDaCasa.text(),
            "aluguel": self.campo_valorDoAluguel.text(),
            "agua inclusa": self.checkBox_aguaInclusa.checkState(),
            "luz inclusa": self.checkBox_luzinclusa.checkState()
        }
        print(info)

