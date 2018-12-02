from api import *
from PyQt5.QtWidgets import QWidget,QMessageBox
from PyQt5.uic import loadUi
from datetime import datetime

class Contrato(QWidget):
    def __init__(self,parente):
        super().__init__()
        self.ui = self
        self.parente = parente
        self.parente.hide()
        loadUi("interface/Contrato.ui",self.ui)
        self.Cancelar.clicked.connect(self.sair)
        self.Concluir.clicked.connect(self.concluir)
        self.carregar()

    def carregar(self):
        self.casas = self.parente.Casa.todas_casas(vazias=True)            
        inqs = self.parente.Inquilino.todos_inquilinos(inativos=True) # alterar aqui
        for x in self.casas:
            self.Casa.addItem(str(x["id_casa"]) + "-" + x["nome_casa"])
        for x in inqs:
            self.Inquilino.addItem(str(x["id_inq"]) + "-" + x["nome_inq"])
    
    def sair(self):
        self.setParent(None)
        self.hide()
        self.parente.show()
        self.parente.atualizar()
        self.close()
    
    def concluir(self):
        casa = self.Casa.currentText()
        if len(casa) == 0:
            self.mensagem("Nenhuma casa selecionada")
            return
        inq = self.Inquilino.currentText()
        if len(inq) == 0:
            self.mensagem("Nenhum inquilino selecionado")
            return
        id_casa,casa = casa.split("-")
        id_casa = int(id_casa)
        inq = int(inq.split("-")[0])
        valor = [x["valor_aluguel"] for x in self.casas if x["id_casa"] == id_casa]
        valor = float(valor[0])
        try:
            venc = int(self.Dia_venc.text())
        except:
            self.mensagem("Dia invalido")
            return
        if venc > 31 or venc <= 0:
            self.mensagem("Dia invalido vencimento")
            return
        try:
            date = datetime.strptime(self.Inicio_con.text(),
                                     "%d/%m/%Y")
            date = date.replace(year=date.year + 1)
        except:
            self.mensagem("data de inicio invalido")
            return
        self.parente.Contrato.adiciona_contrato(ativo=True,
            dia_vencimento=venc,
            casa=id_casa,
            inq=inq,
            valor=valor,
            fim_contrato=date,
            commit=True)
        self.sair()

    def mensagem(self, mensa):
        mens = QMessageBox()
        mens.setText(mensa)
        mens.exec()
    
    def closeEvent(self,event):
        event.ignore()
        self.sair() 