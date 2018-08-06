def importe_de_vagabundo():
    from PyQt5.QtWidgets import QApplication,QWidget,QDialog
    import sys
    from Editar import interagir_Inquilino,interagir_casa,interagir_menu

class cadastrar_Casa(QDialog):
    def __init__(self):
        super().__init__()
        self.interface = interagir_casa()
        self.interface.setupUi(self)
        self.interface.on_click()
        self.show()
class cadastrar_inquilino(QDialog):
    def __init__(self):
        super().__init__()
        self.interface = interagir_Inquilino()
        self.interface.setupUi(self)
        self.interface.on_click()
        self.show()

class menu(QDialog):
    def __init__(self):
        super().__init__()
        a = programa()
        self.interface = interagir_menu(a)
        self.interface.setupUi(self)
        self.interface.on_click()
        self.show()

# class programa(QDialog):
    

    
