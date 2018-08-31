import sys
sys.path.insert(0, '..') 
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from api import *
class interagir_Inquilino(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        loadUi("cadastrar_inquilino.ui",self.ui)
        self.botao_concluir.clicked.connect(self.pegarItens)
        self.botao_cancelar.clicked.connect(self.cancelar)
        self.tipo_aluguel.stateChanged.connect(self.novo_aluguel)
        self.novo_aluguel()
        self.addInList()

    def pegarItens(self):
        info = {
            "nome": self.campo_nome.text(),
            "CPF" : self.campo_CPF.text(),
            "RG"  : self.campo_RG.text(),
            "casa": self.comboBox_casa.currentText(),
            "vencimento": self.vencimento.text(),
            "inicio_contrato": self.inicio_do_contrato.text(),
            "novo_aluguel": self.Novo_aluguel.text()
        }
        engine = make_engine()
        session = make_connection(engine)
        inq = Inquilino_DAO(session)
        inq.adiciona_inquilino(cpf=self.campo_CPF.text(),
                                nome=self.campo_nome.text(),
                                rg=self.campo_RG.text(),)
        print(info)
        self.cancelar()
    
    def novo_aluguel(self):
        if self.tipo_aluguel.checkState() == 0:
            self.label_7.show()
            self.Novo_aluguel.show()
            self.botao_concluir.move(self.botao_concluir.x(),self.Novo_aluguel.y() + 40)
            self.botao_cancelar.move(self.botao_cancelar.x(),self.Novo_aluguel.y() + 40)
            self.resize(self.width(),self.botao_concluir.y() + 40)
        else:
            self.label_7.hide()
            self.Novo_aluguel.hide()
            self.botao_concluir.move(self.botao_concluir.x(),self.tipo_aluguel.y() + 32)
            self.botao_cancelar.move(self.botao_cancelar.x(),self.tipo_aluguel.y() + 32)
            self.resize(self.width(),self.botao_concluir.y() + 40)
    
    def cancelar(self):
        self.setParent(None)
        self.update()
        self.close()
    
    def addInList(self):
        engine = make_engine()
        session = make_connection(engine)
        casa = Casa_DAO(session)
        self.comboBox_casa.addItems(casa.todas_casas())

