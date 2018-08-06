import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDialog
from Editar import interagir_Inquilino,interagir_casa,interagir_menu

class cadastrar_Casa(QDialog):
    def __init__(self):
        super().__init__()
        print("aloo")
        self.interface = interagir_casa()
        self.interface.setupUi(self)
        self.interface.on_click()
        # self.show()
class cadastrar_inquilino(QDialog):
    def __init__(self):
        super().__init__()
        self.interface = interagir_Inquilino()
        self.interface.setupUi(self)
        self.interface.on_click()
        # self.show()

class menu(QDialog):
    def __init__(self):
        super().__init__()
        self.interface = interagir_menu()
        self.interface.setupUi(self)
        self.interface.on_click()
        self.second = cadastrar_Casa()
        self.third = cadastrar_inquilino()
        self.show()

class programa(QDialog):
    def carregar_cadInq(self):
        app = QApplication(sys.argv)
        w = cadastrar_inquilino()
        w.show()

    def carregar_cadCasa(self):
        app = QApplication(sys.argv)
        w = cadastrar_Casa()
        w.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = menu()
    w.show()
    sys.exit(app.exec_())