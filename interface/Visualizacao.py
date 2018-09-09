from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui,QtCore
from PyQt5.uic import loadUi
from api import *

class visualizacao(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        loadUi("interface/Visualizacao.ui",self.ui)
        # print(mouse.windowPos())
        self.carrega()
        self.tabWidget.currentChanged.connect(self.atualizar)
        self.Gerar_recibo.clicked.connect(self.recibo)
        self.atualizar()
        self.show()
    
    def carregar_inq(self):
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Nome","CPF","RG"])

        inquilinos = self.Inquilino.todos_inquilinos()
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

        casas = self.Casa.todas_casas()
        for i in casas:
            info = [i.nome_casa,str(float(i.valor_aluguel_casa)),i.agua_casa,"NULL",str(i.num_instalacao_eletrica)]
            capsula = []
            for j in info:
                item = QtGui.QStandardItem(j)
                item.setEditable(False)
                item.setEnabled(True)
                capsula.append(item)
            self.model.appendRow(capsula)
    
    def carregar_contrato(self):
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Inquilino","Casa","Valor","Ativo","vencimento"])
        

        casas = self.Casa.todas_casas()
        inquilinos = self.Inquilino.todos_inquilinos()
        contratos = self.Contrato.todos_contratos()

        for i in contratos:
            info_casa = [x.nome_casa for x in casas if x.id_casa == i.id_casa]
            info_inqui = [x.nome_inq for x in inquilinos if x.id_inq == i.id_inq]
            info = [str(info_inqui[0]),str(info_casa[0]),str(float(i.valor)),str(i.ativo),str(i.venc_contrato)]
            capsula = []
            for j in info:
                item = QtGui.QStandardItem(j)
                item.setEditable(False)
                item.setSelectable(False)
                capsula.append(item)
            self.model.appendRow(capsula)

    def mostrar_inq(self):
        self.tabelaInq.setModel(self.model)
    
    def mostrar_casa(self):
        self.tabelaCasa.setModel(self.model)
    
    def mostrar_contrato(self):
        self.tabelaContrato.setModel(self.model)

    def atualizar(self):
        if self.tabWidget.currentIndex() == 0:
            self.mostrar_Botoes()
            self.carregar_contrato()
            self.mostrar_contrato()
            a = self.tabelaContrato.horizontalHeader()
            a.stretchLastSection()
            self.tabelaContrato.resizeColumnsToContents()

            self.tabelaContrato.resize(a.length()+20,self.height())
            self.tabWidget.resize(a.length()+25,self.height())
            self.mostrar_Botoes()

        elif self.tabWidget.currentIndex() == 1:
            self.esconder_Botoes()
            self.carregar_casa()
            self.mostrar_casa()
            a = self.tabelaCasa.horizontalHeader()
            a.stretchLastSection()
            self.tabelaCasa.resizeColumnsToContents()

            self.tabelaCasa.resize(a.length()+20,self.height())
            self.tabWidget.resize(a.length()+25,self.height())
            self.resize(a.length()+25,self.height())

        elif self.tabWidget.currentIndex() == 2:
            self.esconder_Botoes()
            self.carregar_inq()
            self.mostrar_inq()
            a = self.tabelaInq.horizontalHeader()
            a.stretchLastSection()
            self.tabelaInq.resizeColumnsToContents()
            self.tabelaInq.resize(a.length()+20,self.height())
            self.tabWidget.resize(a.length()+20,self.height())
            self.resize(a.length()+20,self.height())
    
    def carrega(self):
        engine = make_engine()
        session = make_connection(engine)
        self.Casa = Casa_DAO(session)
        self.Inquilino = Inquilino_DAO(session)
        self.Contrato = Contrato_DAO(session)

    def mostrar_Botoes(self):
        self.label.show()
        self.label.move(self.tabWidget.width() + 44,self.label.y())
        self.Mes.show()
        self.Mes.move(self.tabWidget.width() + 13,self.Mes.y())
        self.Gerar_recibo.show()
        self.Gerar_recibo.move(self.tabWidget.width() + 23,self.Gerar_recibo.y())
        self.resize(self.Mes.x() + 118,self.height())
    
    def esconder_Botoes(self):
        self.label.hide()
        self.Mes.hide()
        self.Gerar_recibo.hide()

    def recibo(self):
        h = self.tabelaContrato.selectionModel()
        index = h.currentIndex() 
        linha = self.model.takeRow(index.row())
        self.model.insertRow(index.row(),linha)
        if len(linha) > 0:
            dicio = {
                'Nome' : linha[0].text(),
                'Casa' : linha[1].text(),
                'Aluguel' : linha[2].text(),
                'Ativo' : linha[3].text(),
                'data vencimento' : linha[4].text()
            }
            print(dicio)
        else:
            print("Não houve nenhuma seleçao")

