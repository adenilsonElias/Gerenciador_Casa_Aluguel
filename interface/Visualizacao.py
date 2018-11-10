from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui,QtCore
from PyQt5.uic import loadUi
from api import *
from api.recibos import gera_recibo
from cadastrar_casa import interagir_casa
from cadastrar_inquilino import interagir_Inquilino
from Alterar_inq import Alterar_inq
from Alterar_casa import Alterar_casa

class Visualizacao(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        loadUi("interface/Visualizacao.ui",self.ui)
        self.linha = []
        self.carrega()
        self.tabWidget.currentChanged.connect(self.atualizar)
        self.Gerar_recibo.clicked.connect(self.recibo)
        self.Valor.clicked.connect(self.alterar_valor)
        self.Add_inquilino.clicked.connect(self.inquilino)
        self.Add_casa.clicked.connect(self.casa)
        self.Add_casa.clicked.connect(self.atualizar)
        self.Alterar_inq.clicked.connect(self.alterar_inq_func)
        self.Ativo_Desativo.clicked.connect(self.inqInativos)
        self.Alter_casa.clicked.connect(self.alterar_casa)
        self.Ativo_Desativo_casa.clicked.connect(self.casaInativa)
        self.inqInativos()
        self.casaInativa()
        self.show()
    
    def carregar_inq(self,ativo=False):
        """
        CONTROL
        função responsavel por criar os model do QT para inquilino
        """

        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["id","Nome","CPF","RG"])

        if ativo:
            inquilinos = self.Inquilino.todos_inquilinos(True)
        else:
            inquilinos = self.Inquilino.todos_inquilinos()
        for i in inquilinos:
            info = [str(i["id_inq"]),i["nome_inq"],i["cpf_inq"],i["rg_inq"]]
            capsula = []
            for j in info:
                item = QtGui.QStandardItem(j)
                item.setEditable(False)
                item.setSelectable(False)
                capsula.append(item)
            self.model.appendRow(capsula)
        
    def carregar_casa(self,ativo=False):
        """
        CONTROL
        função responsavel por criar os model do QT para casa
        """
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["id","Nome","Valor Aluguel","RGI","CPF","numero estalacao"])
        if ativo:
            casas = self.Casa.todas_casas(True)
        else:
            casas = self.Casa.todas_casas()
        for i in casas:
            info = [str(i["id_casa"]),i["nome_casa"],str(float(i["valor_aluguel"])),i["agua_casa"],i["cpf"],i["num_instalacao_eletrica"]]
            capsula = []
            for j in info:
                if j == "":
                    j = "NULL"
                item = QtGui.QStandardItem(j)
                item.setEditable(False)
                item.setSelectable(False)
                capsula.append(item)
            capsula[0].setEnabled(False)
            self.model.appendRow(capsula)
    
    def carregar_contrato(self):
        """
        CONTROL
        função responsavel por criar os model do QT para contrato
        """
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Id","Inquilino","Casa","Valor","Ativo","vencimento"])

        casas = self.Casa.todas_casas()
        inquilinos = self.Inquilino.todos_inquilinos()
        contratos = self.Contrato.todos_contratos()

        for i in contratos:
            info_casa = [x["nome_casa"] for x in casas if x['id_casa'] == i['id_casa']]
            info_inqui = [x["nome_inq"] for x in inquilinos if x["id_inq"] == i["id_inq"]]
            info = [str(i['id_contrato']),str(info_inqui[0]),str(info_casa[0]),str(float(i["valor"])),str(i["ativo"]),str(i["dia_venc_aluguel"])]
            capsula = []
            for j in info:
                item = QtGui.QStandardItem(j)
                item.setEditable(False)
                item.setSelectable(False)
                capsula.append(item)
            if len(capsula) > 0:
                capsula[0].setEnabled(False)
            self.model.appendRow(capsula)

    def mostrar_inq(self):
        """
        VIEW
        """
        self.tabelaInq.setModel(self.model)
    
    def mostrar_casa(self):
        """
        VIEW
        """
        self.tabelaCasa.setModel(self.model)
    
    def mostrar_contrato(self):
        """
        VIEW
        """
        self.tabelaContrato.setModel(self.model)

    def atualizar(self,vai = True,ativo=False):
        """
        VIEW responsavel pelas mudanças de abas
        ARRUMAR 
        """
        if self.tabWidget.currentIndex() == 0:
            self.carregar_contrato()
            self.mostrar_contrato()
            self.tabelaContrato.selectionModel().currentRowChanged.connect(self.ativa_desativa)
            a = self.tabelaContrato.horizontalHeader()
            a.setStretchLastSection(True)
            self.tabelaContrato.resizeColumnsToContents()
            ta = self.tabelaContrato.size()
            a.resize(ta.width(),a.height())
            if vai:
                self.ativa_desativa()

        elif self.tabWidget.currentIndex() == 1:
            self.carregar_casa(ativo)
            self.mostrar_casa()
            a = self.tabelaCasa.horizontalHeader()
            a.setStretchLastSection(True)
            self.tabelaCasa.resizeColumnsToContents()
            ta = self.tabelaCasa.size()
            a.resize(ta.width(),a.height())

        elif self.tabWidget.currentIndex() == 2:
            self.carregar_inq(ativo=ativo)
            self.mostrar_inq()
            a = self.tabelaInq.horizontalHeader()
            a.setStretchLastSection(True)
            self.tabelaInq.resizeColumnsToContents()
            ta = self.tabelaInq.size()
            a.resize(ta.width(),a.height())

    def carrega(self):
        """
        CONTROL
        """
        session = make_connection()
        self.Instalacao = Instalacao_Eletrica_DAO(session)
        self.Casa = Casa_DAO(session)
        self.Inquilino = Inquilino_DAO(session)
        self.Contrato = Contrato_DAO(session)

    def recibo(self):
        """
        CONTROL pega o item selecionado e manda as informaçoes para gerar o recibo.pdf
        """
        linha = self.linha
        if len(linha) > 0:
            gera_recibo(linha[1].text(),linha[5].text(),int(self.Mes.text().split("/")[0]),
                        self.Mes.text().split("/")[1],float(linha[3].text()))
        else:
            print("errou")
    def coletaLinha(self,tabela):
        h = tabela.selectionModel()
        index = h.currentIndex()
        linha = self.model.takeRow(index.row())
        self.model.insertRow(index.row(),linha)
        return linha

    def ativa_desativa(self):
        self.tabelaContrato.selectionModel().currentRowChanged.disconnect(self.ativa_desativa)
        self.linha = self.coletaLinha(self.tabelaContrato)
        self.tabelaContrato.selectionModel().reset()
        if (len(self.linha) > 0):
            self.Idsao.setText(self.linha[0].text())
            if self.linha[4].text() == "1":
                self.Gerar_recibo.setEnabled(True)
                self.At_De.setText("Desativar")
                self._conectar(self.Desativar_contrato)
                self._desconectar(self.ativar_contrato)
                self.New_value.setEnabled(True)
                self.Valor.setEnabled(True)
                self.New_value.setText(self.linha[3].text())
            else:
                self.Gerar_recibo.setEnabled(False)
                self.At_De.setText("Ativar")
                self._conectar(self.ativar_contrato)
                self._desconectar(self.Desativar_contrato)
                self.New_value.setEnabled(False)
                self.Valor.setEnabled(False)
                self.New_value.setText("")
            self.At_De.setEnabled(True)
        else:
            self._disativaBotoes()
        self.tabelaContrato.selectionModel().currentRowChanged.connect(self.ativa_desativa)

    def _disativaBotoes(self):
        self.New_value.setEnabled(False)
        self.Valor.setEnabled(False)
        self.New_value.setText("")
        self.Idsao.setText("")
        self.Gerar_recibo.setEnabled(False)
        self._desconectar(self.Desativar_contrato)
        self._desconectar(self.ativar_contrato)
        self.At_De.setEnabled(False)
        self.At_De.setText("Ativa/Desativa")

    def _conectar(self,func):
        try: # Não questione só aceite
            self.At_De.clicked.connect(func)
        except:
            pass

    def _desconectar(self,func):
        try: # Não questione só aceite
            self.At_De.clicked.disconnect(func)
        except:
            pass

    def Desativar_contrato(self):
        linha = self.linha
        try: # Não questione só aceite
            self.Contrato.inativa_contrato(id=int(linha[0].text()),commit=True)
        except:
            pass
        self.atualizar(vai=False)
        self._disativaBotoes()
    
    def ativar_contrato(self):
        linha = self.linha
        try: # Não questione só aceite
            self.Contrato.ativa_contrato(id=int(linha[0].text()),commit=True)
        except:
            pass
        self.atualizar(vai=False)
        self._disativaBotoes()
    
    def alterar_valor(self):
        linha = self.linha
        try: # Não questione só aceite
            self.Contrato.altera_valor_contrato(int(linha[0].text()),float(self.New_value.text()),commit=True)
        except:
            pass
        self.atualizar(vai=False)
        self._disativaBotoes()
    
    def inquilino(self):
        inq = interagir_Inquilino(self)
        inq.show()

    def casa (self):
        casa = interagir_casa(self)
        casa.show()

    def alterar_inq_func(self):
        info = self.coletaLinha(self.tabelaInq)
        alter = Alterar_inq(self,info)
        alter.show()

    def inqAtivos(self):
        self.atualizar(ativo=True)
        self.Ativo_Desativo.setText("Ativo: True")
        self.Ativo_Desativo.clicked.disconnect(self.inqAtivos)
        self.Ativo_Desativo.clicked.connect(self.inqInativos)
    
    def inqInativos(self):
        self.atualizar()
        self.Ativo_Desativo.setText("Ativo: False")
        self.Ativo_Desativo.clicked.disconnect(self.inqInativos)
        self.Ativo_Desativo.clicked.connect(self.inqAtivos)
    
    def alterar_casa(self):
        info = self.coletaLinha(self.tabelaCasa)
        alter = Alterar_casa(self,info)
        alter.show()

    def casaAtiva(self):
        self.atualizar(ativo=True)
        self.Ativo_Desativo_casa.setText("Ativo: True")
        self.Ativo_Desativo_casa.clicked.disconnect(self.casaAtiva)
        self.Ativo_Desativo_casa.clicked.connect(self.casaInativa)
    
    def casaInativa(self):
        self.atualizar()
        self.Ativo_Desativo_casa.setText("Ativo: False")
        self.Ativo_Desativo_casa.clicked.disconnect(self.casaInativa)
        self.Ativo_Desativo_casa.clicked.connect(self.casaAtiva)
