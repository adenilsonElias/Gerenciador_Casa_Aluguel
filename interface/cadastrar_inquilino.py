from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from api import *
from datetime import datetime

class interagir_Inquilino(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self
        loadUi("interface/cadastrar_inquilino.ui",self.ui)
        self.botao_concluir.clicked.connect(self.pegarItens)
        self.botao_cancelar.clicked.connect(self.cancelar)
        self.tipo_aluguel.stateChanged.connect(self.novo_aluguel)
        self.novo_aluguel()
        self.addInList()

    def pegarItens(self):
        '''
        VIEW
        Pega os intens dos textField e insere no banco

        atençao: salvando as informaçoes sem alterar o aluguel padrao
        '''
        ########
        session = make_connection()
        inq = Inquilino_DAO(session)

        inq.adiciona_inquilino(cpf=self.campo_CPF.text(),
                               nome=self.campo_nome.text(),
                               rg=self.campo_RG.text())
        casa = Casa_DAO(session)
        casas = casa.todas_casas()
        id_casa = [x["id_casa"] for x in casas if x["nome_casa"] == self.comboBox_casa.currentText()]
        valor = [x["valor_aluguel"] for x in casas if x["nome_casa"] == self.comboBox_casa.currentText()]
        self.contrato(id_casa[0],
                      self.campo_CPF.text(),
                      session,inq.todos_inquilinos(),
                      valor[0])
        ##########
        self.cancelar()
    
    def novo_aluguel(self):
        '''
        VIEW
        Controla os novos elementos na interface
        '''
        if self.tipo_aluguel.checkState() == 0:
            self.label_7.show()
            self.Novo_aluguel.show()
            self.botao_concluir.move(self.botao_concluir.x(),self.Novo_aluguel.y() + 40)
            self.botao_cancelar.move(self.botao_cancelar.x(),self.Novo_aluguel.y() + 40)
            self.resize(self.width(),self.botao_concluir.y() + 40)
            self.setFixedSize(self.width(),self.botao_concluir.y() + 40)
        else:
            self.label_7.hide()
            self.Novo_aluguel.hide()
            self.botao_concluir.move(self.botao_concluir.x(),self.tipo_aluguel.y() + 32)
            self.botao_cancelar.move(self.botao_cancelar.x(),self.tipo_aluguel.y() + 32)
            self.resize(self.width(),self.botao_concluir.y() + 40)
            self.setFixedSize(self.width(),self.botao_concluir.y() + 40)
            
    
    def cancelar(self):
        """
        VIEW
        """
        self.setParent(None)
        self.update()
        self.close()
    
    def addInList(self):
        '''
        CONTROL
        Adiciona as casas no no combobox
        '''
        session = make_connection()
        casa = Casa_DAO(session)
        mostrar_casa = casa.todas_casas()
        for x in mostrar_casa:
            self.comboBox_casa.addItem(x["nome_casa"])
    
    def contrato(self,id_casa,cpf,session,objInq,valor):
        """
        CONTROL
        Passa as informaçoes para gerar o contrato para a api
        """
        # objInq = inquilino.DAO(session)
        inqui = [x["id_inq"]  for x in objInq if x["cpf_inq"] == cpf]
        contrato = Contrato_DAO(session)
        date = datetime.strptime(self.inicio_do_contrato.text(),"%d/%m/%Y")
        date = date.replace(year=date.year + 1)
        print(type(date),date)
        contrato.adiciona_contrato(ativo=True,
                                    dia_vencimento=int(self.vencimento.text()),
                                    casa=id_casa,
                                    inq=inqui[0],
                                    valor=valor,
                                    fim_contrato=date,
                                    commit=True)
    

        
