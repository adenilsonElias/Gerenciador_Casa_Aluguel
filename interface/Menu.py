from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from cadastrar_casa import interagir_casa
from cadastrar_inquilino import interagir_Inquilino

class interagir_menu(QWidget):
    def on_click(self,obj):
        obj.Inquilino.clicked.connect(self.inquilino)
        obj.Casa.clicked.connect(self.casa)
        obj.Fechar.clicked.connect(self.fechar)
    def fechar(self):
        exit(0)

    def inquilino(self):
        inq = interagir_Inquilino()
        inq.show()

    def casa (self):
        casa = interagir_casa()
        casa.show()
