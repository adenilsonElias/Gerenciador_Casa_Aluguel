import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDialog
from Editar import interagir_Inquilino,interagir_casa,interagir_menu

class menu(QDialog):
    def __init__(self):
        super().__init__()
        self.interface = interagir_menu()
        self.interface.setupUi(self)
        self.interface.on_click()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = menu()
    w.show()
    sys.exit(app.exec_())