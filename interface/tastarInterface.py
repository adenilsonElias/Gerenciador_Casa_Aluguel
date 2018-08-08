import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QWidget,QDialog
from Editar import interagir_menu,interagir_Inquilino,interagir_casa

class menu(QWidget):
    def __init__(self):
        super().__init__()
        # uic.loadUi("Menu.ui",self)
        self.ui = self
        self.menu = interagir_menu()
        loadUi("Menu.ui",self.ui)
        self.menu.on_click(self.ui)
        self.ui.close()
        self.ui = None
        # self.ui.on_click()
        # self = self.ui.load()
        # self.interface.setupUi(self)
        # self.interface.on_click()
        self.show()
        self = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = menu()
    w.show()
    app.exec_()