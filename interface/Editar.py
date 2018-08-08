from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class interagir_Inquilino():
    _objeto = None
    def __init__(self,obj):
        self._objeto = obj

    def on_click(self):
        self._objeto.botao_concluir.clicked.connect(self.pegarItens)
        self._objeto.botao_cancelar.clicked.connect(self.cancelar)
    
    def pegarItens(self):
        info = {
            "nome": self._objeto.campo_nome.text(),
            "CPF" : self._objeto.campo_CPF.text(),
            "RG"  : self._objeto.campo_RG.text(),
            "casa": self._objeto.comboBox_casa.currentText()
        }
        print(info)
    
    def cancelar(self):
        self._objeto.setParent(None)
        self._objeto.close()
        self._objeto = None
    
    def addInList(self):
        self._objeto.comboBox_casa.addItems(["casa 1","casa 2","casa 3"])

class interagir_casa():
    _objeto = None
    def __init__(self,obj):
        self._objeto = obj

    def on_click(self):
        self._objeto.botao_concluir.clicked.connect(self.pegarItens)
        self._objeto.botao_cancelar.clicked.connect(self.sair)

    def sair(self):
        self._objeto.setParent(None)
        self._objeto.close()
        self._objeto = None

    def pegarItens(self):
        info = {
            "nome casa": self._objeto.campo_nomeDaCasa.text(),
            "aluguel": self._objeto.campo_valorDoAluguel.text(),
            "agua inclusa": self._objeto.checkBox_aguaInclusa.checkState(),
            "luz inclusa": self._objeto.checkBox_luzinclusa.checkState()
        }
        print(info)

class interagir_menu(QWidget):
    # _objeto = None
    # def __init__(self):
    #     self._objeto = obj
    def on_click(self,obj):
        obj.Inquilino.clicked.connect(self.inquilino)
        obj.Casa.clicked.connect(self.casa)
        obj.Fechar.clicked.connect(self.fechar)
    def fechar(self):
        exit(0)

    def inquilino(self):
        self.ui = self
        loadUi("cadastrar_inquilino.ui",self.ui)
        self.window = interagir_Inquilino(self.ui)
        self.window.on_click()
        self.ui.close()
        self.ui = None
        self.show()

    def casa (self):
        loadUi("cadastrar_casa.ui",self)
        self.window = interagir_casa(self)
        self.window.on_click()
        self.show()

    
    
    
