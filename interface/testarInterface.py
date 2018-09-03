import sys
from PyQt5.QtWidgets import QApplication
from Menu import interagir_menu
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = interagir_menu()
    w.show()
    app.exec_()