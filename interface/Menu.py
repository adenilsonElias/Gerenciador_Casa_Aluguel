from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from cadastrar_casa import interagir_casa
from cadastrar_inquilino import interagir_Inquilino

class interagir_menu(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        loadUi("Menu.ui",self.ui)
        self.on_click()
        self.show()

    def on_click(self):
        self.Inquilino.clicked.connect(self.inquilino)
        self.Casa.clicked.connect(self.casa)
        self.Fechar.clicked.connect(self.fechar)
    def fechar(self):
        exit(0)

    def inquilino(self):
        inq = interagir_Inquilino()
        inq.show()

    def casa (self):
        casa = interagir_casa()
        casa.show()
