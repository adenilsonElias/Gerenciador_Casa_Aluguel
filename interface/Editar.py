from cadastrar_inquilino import Ui_Cadastrar
from cadastrar_casa import Ui_Cadastrar_casa
from Menu import Ui_Menu

class interagir_Inquilino(Ui_Cadastrar):
    def on_click(self):
        self.botao_concluir.clicked.connect(self.pegarItens)
        self.botao_cancelar.clicked.connect(self.cancelar)
    
    def pegarItens(self):
        info = {
            "nome": self.campo_nome.text(),
            "CPF" : self.campo_CPF.text(),
            "RG"  : self.campo_RG.text(),
            "casa": self.comboBox_casa.currentText()
        }
        print(info)
    
    def cancelar(self):
        pass
    
    def addInList(self):
        self.comboBox_casa.addItems(["casa 1","casa 2","casa 3"])

class interagir_casa(Ui_Cadastrar_casa):
    def on_click(self):
        self.botao_concluir.clicked.connect(self.pegarItens)
        self.botao_cancelar.clicked.connect(self.sair)

    def sair(self):
        pass

    def pegarItens(self):
        info = {
            "nome casa": self.campo_nomeDaCasa.text(),
            "aluguel": self.campo_valorDoAluguel.text(),
            "agua inclusa": self.checkBox_aguaInclusa.checkState(),
            "luz inclusa": self.checkBox_luzinclusa.checkState()
        }
        print(info)

class interagir_menu(Ui_Menu):
    def on_click(self):
        self.Inquilino.clicked.connect(self.inquilino)
        self.Casa.clicked.connect(self.casa)
        self.Fechar.clicked.connect(self.fechar)
    
    def fechar(self):
        pass

    def inquilino(self):
        from PyQt5 import QtWidgets
        self.window = QtWidgets.QWidget()
        self.ui = interagir_Inquilino()
        self.ui.setupUi(self.window)
        self.ui.on_click()
        self.window.show()
    
    def casa (self):
        from PyQt5 import QtWidgets
        self.window = QtWidgets.QWidget()
        self.ui = interagir_casa()
        self.ui.setupUi(self.window)
        self.ui.on_click()
        self.window.show()
    
    
    
