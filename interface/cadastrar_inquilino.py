from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi
from api import *
from datetime import datetime


class interagir_Inquilino(QWidget):
    def __init__(self, parente):
        super().__init__()
        self.ui = self
        self.parente = parente
        self.parente.hide()
        loadUi("interface/cadastrar_inquilino.ui", self.ui)
        self.botao_concluir.clicked.connect(self.pegarItens)
        self.botao_cancelar.clicked.connect(self.cancelar)
        self.tipo_aluguel.stateChanged.connect(self.novo_aluguel)
        self.novo_aluguel()
        self.addInList()

    def mensagem(self, mensa):
        mens = QMessageBox()
        mens.setText(mensa)
        mens.exec()

    def pegarItens(self):
        '''
        VIEW
        Pega os intens dos textField e insere no banco

        atençao: salvando as informaçoes sem alterar o aluguel padrao
        '''
        ########
        session = make_connection()
        inq = Inquilino_DAO(session)
        nome = self.campo_nome.text()
        if len(nome) == 0:
            self.mensagem("Nome vazio")
            return
        rg = self.campo_RG.text()
        if len(rg) == 0:
            self.mensagem("RG vaio")
            return
        cpf = self.campo_CPF.text()
        if len(cpf) != 11:
            self.mensagem("CPF vazio ou invalido")
            return

        self.parente.Inquilino.adiciona_inquilino(
            cpf=self.campo_CPF.text(),
            nome=self.campo_nome.text(),
            rg=self.campo_RG.text())
        casas = self.parente.Casa.todas_casas()
        if len(self.comboBox_casa.currentText()) == 0:
            self.mensagem("Nenhuma casa selecionada")
            return
        id_casa = [
            x["id_casa"] for x in casas
            if x["nome_casa"] == self.comboBox_casa.currentText()
        ]
        valor = [
            x["valor_aluguel"] for x in casas
            if x["nome_casa"] == self.comboBox_casa.currentText()
        ]
        if self.tipo_aluguel == 0:
            try:
                valor[0] = float(self.Novo_aluguel.text())
            except:
                self.mensagem("Erro novo Valor")
                return
        delta = self.contrato(id_casa[0], self.campo_CPF.text(),
                      self.parente.Inquilino.todos_inquilinos(), valor[0])
        if delta:
            return
        ##########
        self.cancelar()

    def novo_aluguel(self):
        '''
        VIEW
        Controla os novos elementos na interface
        '''
        if self.tipo_aluguel.checkState() == 0:
            self.label_7.setEnabled(True)
            self.Novo_aluguel.setEnabled(True)
        else:
            self.label_7.setEnabled(False)
            self.Novo_aluguel.setEnabled(False)

    def cancelar(self):
        """
        VIEW
        """
        self.setParent(None)
        self.hide()
        self.parente.show()
        self.parente.atualizar()
        self.close()

    def addInList(self):
        '''
        CONTROL
        Adiciona as casas no no combobox
        '''
        session = make_connection()
        casa = Casa_DAO(session)
        mostrar_casa = casa.todas_casas(vazias=True)
        for x in mostrar_casa:
            self.comboBox_casa.addItem(x["nome_casa"])

    def contrato(self, id_casa, cpf, objInq, valor):
        """
        CONTROL
        Passa as informaçoes para gerar o contrato para a api
        """

        inqui = [x["id_inq"] for x in objInq if x["cpf_inq"] == cpf]
        try:
            date = datetime.strptime(self.inicio_do_contrato.text(),
                                     "%d/%m/%Y")
            date = date.replace(year=date.year + 1)
        except:
            self.mensagem("Erro data")
            return True

        dia_vencimento = int(self.vencimento.text())
        if dia_vencimento > 31 and dia_vencimento <= 0:
            self.mensagem("Data invalida")
            return True
        print(type(date), date)
        self.parente.Contrato.adiciona_contrato(
            ativo=True,
            dia_vencimento=dia_vencimento,
            casa=id_casa,
            inq=inqui[0],
            valor=valor,
            fim_contrato=date,
            commit=True)
    
    def closeEvent(self,event):
        event.ignore()
        self.cancelar() 
