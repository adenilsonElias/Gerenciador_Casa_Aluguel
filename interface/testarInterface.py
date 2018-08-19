import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QWidget,QDialog
from Menu import interagir_menu

class menu(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        self.menu = interagir_menu()
        loadUi("Menu.ui",self.ui)
        self.menu.on_click(self.ui)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = menu()
    w.show()
    app.exec_()