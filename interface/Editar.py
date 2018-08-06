from cadastrar import Ui_Cadastrar
from cadastrar_casa import Ui_Cadastrar_casa
from Menu import Ui_Menu

class interagir_Inquilino(Ui_Cadastrar):
    def on_click(self):
        self.pushButton.clicked.connect(self.pegarItens)
        self.pushButton_2.clicked.connect(self.cancelar)
    
    def pegarItens(self):
        info = {
            "nome": self.lineEdit.text(),
            "CPF" : self.lineEdit_2.text(),
            "RG"  : self.lineEdit_3.text(),
            "casa": self.comboBox.currentText()
        }
        print(info)
    
    def cancelar(self):
        exit(0)
    
    def addInList(self):
        self.comboBox.addItems(["casa 1","casa 2","casa 3"])

class interagir_casa(Ui_Cadastrar_casa):
    def on_click(self):
        self.pushButton.clicked.connect(self.pegarItens)
        self.pushButton_2.clicked.connect(self.sair)

    def sair(self):
        exit(0)

    def pegarItens(self):
        info = {
            "nome casa": self.lineEdit.text(),
            "aluguel": self.lineEdit_2.text(),
            "agua inclusa": self.checkBox.checkState(),
            "luz inclusa": self.checkBox_2.checkState()
        }
        print(info)

class interagir_menu(Ui_Menu):
    def on_click(self):
        self.Inquilino.clicked.connect(self.inquilino)
        self.Casa.clicked.connect(self.casa)
        self.Fechar.clicked.connect(self.fechar)
    
    def fechar(self):
        exit(0)

    def inquilino(self):
        from tastarInterface import cadastrar_inquilino
        a = cadastrar_inquilino()
        a.show
    def casa (self):
        from tastarInterface import cadastrar_Casa
        a = cadastrar_Casa()
        a.show()
    
    
