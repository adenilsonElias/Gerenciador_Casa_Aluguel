# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastrar_casa.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Cadastrar_casa(object):
    def setupUi(self, Cadastrar_casa):
        Cadastrar_casa.setObjectName("Cadastrar_casa")
        Cadastrar_casa.resize(128, 277)
        self.campo_nomeDaCasa = QtWidgets.QLineEdit(Cadastrar_casa)
        self.campo_nomeDaCasa.setGeometry(QtCore.QRect(10, 30, 113, 32))
        self.campo_nomeDaCasa.setText("")
        self.campo_nomeDaCasa.setObjectName("campo_nomeDaCasa")
        self.campo_valorDoAluguel = QtWidgets.QLineEdit(Cadastrar_casa)
        self.campo_valorDoAluguel.setGeometry(QtCore.QRect(10, 90, 113, 32))
        self.campo_valorDoAluguel.setText("")
        self.campo_valorDoAluguel.setObjectName("campo_valorDoAluguel")
        self.checkBox_aguaInclusa = QtWidgets.QCheckBox(Cadastrar_casa)
        self.checkBox_aguaInclusa.setGeometry(QtCore.QRect(10, 130, 111, 22))
        self.checkBox_aguaInclusa.setObjectName("checkBox_aguaInclusa")
        self.label = QtWidgets.QLabel(Cadastrar_casa)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Cadastrar_casa)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 111, 18))
        self.label_2.setObjectName("label_2")
        self.checkBox_luzinclusa = QtWidgets.QCheckBox(Cadastrar_casa)
        self.checkBox_luzinclusa.setGeometry(QtCore.QRect(10, 160, 101, 22))
        self.checkBox_luzinclusa.setObjectName("checkBox_luzinclusa")
        self.botao_concluir = QtWidgets.QPushButton(Cadastrar_casa)
        self.botao_concluir.setGeometry(QtCore.QRect(10, 190, 88, 34))
        self.botao_concluir.setObjectName("botao_concluir")
        self.botao_cancelar = QtWidgets.QPushButton(Cadastrar_casa)
        self.botao_cancelar.setGeometry(QtCore.QRect(10, 230, 88, 34))
        self.botao_cancelar.setObjectName("botao_cancelar")

        self.retranslateUi(Cadastrar_casa)
        QtCore.QMetaObject.connectSlotsByName(Cadastrar_casa)

    def retranslateUi(self, Cadastrar_casa):
        _translate = QtCore.QCoreApplication.translate
        Cadastrar_casa.setWindowTitle(_translate("Cadastrar_casa", "Cadastrar casa"))
        self.checkBox_aguaInclusa.setText(_translate("Cadastrar_casa", "Agua inclusa"))
        self.label.setText(_translate("Cadastrar_casa", "Nome da casa"))
        self.label_2.setText(_translate("Cadastrar_casa", "Valor do aluguel"))
        self.checkBox_luzinclusa.setText(_translate("Cadastrar_casa", "Luz inclusa"))
        self.botao_concluir.setText(_translate("Cadastrar_casa", "Concluir"))
        self.botao_cancelar.setText(_translate("Cadastrar_casa", "Cancelar"))

