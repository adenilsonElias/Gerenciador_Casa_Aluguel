from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from api import *

class visualizacao(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        loadUi("interface/Visualizacao.ui",self.ui)
        self.tabWidget.currentChanged.connect(self.atualizar)
        self.carregar_inq()
        self.mostrar_inq()
        a = self.tabelaInq.horizontalHeader()
        a.stretchLastSection()
        self.carregar_casa()
        self.mostrar_casa()
        a = self.tabelaCasa.horizontalHeader()
        a.stretchLastSection()
        self.tabelaInq.resizeColumnsToContents()
        self.atualizar()
        self.show()
    
    def carregar_inq(self):
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Nome","CPF","RG"])

        engine = make_engine()
        session = make_connection(engine)
        inq = Inquilino_DAO(session)
        inquilinos = inq.todos_inquilinos()
        for i in inquilinos:
            info = [i.nome_inq,i.cpf_inq,i.rg_inq]
            capsula = []
            for j in info:
                item = QtGui.QStandardItem(j)
                item.setEditable(False)
                capsula.append(item)
            self.model.appendRow(capsula)
        
    def carregar_casa(self):
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Nome","Valor Aluguel","RGI","CPF","numero estalacao"])

        engine = make_engine()
        session = make_connection(engine)
        casa = Casa_DAO(session)
        casas = casa.todas_casas()
        for i in casas:
            info = [i.nome_casa,str(float(i.valor_aluguel_casa)),i.agua_casa,"NULL",str(i.num_instalacao_eletrica)]
            capsula = []
            for j in info:
                item = QtGui.QStandardItem(j)
                item.setEditable(False)
                capsula.append(item)
            self.model.appendRow(capsula)
    
    def mostrar_inq(self):
        self.tabelaInq.setModel(self.model)
    
    def mostrar_casa(self):
        self.tabelaCasa.setModel(self.model)
    
    def atualizar(self):
        if self.tabWidget.currentIndex() == 0:
            a = self.tabelaCasa.horizontalHeader()
            self.tabelaCasa.resize(a.length()+20,self.height())
            self.tabWidget.resize(a.length()+25,self.height())
            self.resize(a.length()+25,self.height())
        elif self.tabWidget.currentIndex() == 1:
            a = self.tabelaInq.horizontalHeader()
            self.tabelaInq.resize(a.length()+20,self.height())
            self.tabWidget.resize(a.length()+20,self.height())
            self.resize(a.length()+20,self.height())