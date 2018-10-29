import sys
sys.path.insert(0, 'interface/')
sys.path.insert(0, 'api/')
from api import *

from PyQt5.QtWidgets import QApplication
from Visualizacao import Visualizacao

session = make_connection()
start_db(session)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Visualizacao()
    w.show()
app.exec_()