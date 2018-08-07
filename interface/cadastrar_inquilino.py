# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastrar_inquilino.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Cadastrar(object):
    def setupUi(self, Cadastrar):
        Cadastrar.setObjectName("Cadastrar")
        Cadastrar.setWindowModality(QtCore.Qt.ApplicationModal)
        Cadastrar.resize(208, 294)
        self.campo_nome = QtWidgets.QLineEdit(Cadastrar)
        self.campo_nome.setGeometry(QtCore.QRect(10, 30, 181, 32))
        self.campo_nome.setObjectName("campo_nome")
        self.campo_CPF = QtWidgets.QLineEdit(Cadastrar)
        self.campo_CPF.setGeometry(QtCore.QRect(10, 90, 181, 32))
        self.campo_CPF.setObjectName("campo_CPF")
        self.campo_RG = QtWidgets.QLineEdit(Cadastrar)
        self.campo_RG.setGeometry(QtCore.QRect(10, 150, 181, 32))
        self.campo_RG.setObjectName("campo_RG")
        self.label = QtWidgets.QLabel(Cadastrar)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Cadastrar)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 58, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Cadastrar)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 58, 18))
        self.label_3.setObjectName("label_3")
        self.botao_concluir = QtWidgets.QPushButton(Cadastrar)
        self.botao_concluir.setGeometry(QtCore.QRect(10, 250, 88, 34))
        self.botao_concluir.setObjectName("botao_concluir")
        self.botao_cancelar = QtWidgets.QPushButton(Cadastrar)
        self.botao_cancelar.setGeometry(QtCore.QRect(110, 250, 88, 34))
        self.botao_cancelar.setObjectName("botao_cancelar")
        self.label_4 = QtWidgets.QLabel(Cadastrar)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 58, 18))
        self.label_4.setObjectName("label_4")
        self.comboBox_casa = QtWidgets.QComboBox(Cadastrar)
        self.comboBox_casa.setGeometry(QtCore.QRect(10, 210, 181, 32))
        self.comboBox_casa.setObjectName("comboBox_casa")

        self.retranslateUi(Cadastrar)
        QtCore.QMetaObject.connectSlotsByName(Cadastrar)
        Cadastrar.setTabOrder(self.campo_nome, self.campo_CPF)
        Cadastrar.setTabOrder(self.campo_CPF, self.campo_RG)
        Cadastrar.setTabOrder(self.campo_RG, self.comboBox_casa)
        Cadastrar.setTabOrder(self.comboBox_casa, self.botao_concluir)
        Cadastrar.setTabOrder(self.botao_concluir, self.botao_cancelar)

    def retranslateUi(self, Cadastrar):
        _translate = QtCore.QCoreApplication.translate
        Cadastrar.setWindowTitle(_translate("Cadastrar", "cadastrar"))
        self.label.setText(_translate("Cadastrar", "Nome"))
        self.label_2.setText(_translate("Cadastrar", "CPF"))
        self.label_3.setText(_translate("Cadastrar", "RG"))
        self.botao_concluir.setText(_translate("Cadastrar", "concluir"))
        self.botao_cancelar.setText(_translate("Cadastrar", "cancelar"))
        self.label_4.setText(_translate("Cadastrar", "Casa"))

