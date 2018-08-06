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
        self.lineEdit = QtWidgets.QLineEdit(Cadastrar_casa)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 32))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Cadastrar_casa)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 113, 32))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(Cadastrar_casa)
        self.checkBox.setGeometry(QtCore.QRect(10, 130, 111, 22))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(Cadastrar_casa)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Cadastrar_casa)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 111, 18))
        self.label_2.setObjectName("label_2")
        self.checkBox_2 = QtWidgets.QCheckBox(Cadastrar_casa)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 160, 101, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(Cadastrar_casa)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Cadastrar_casa)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 230, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Cadastrar_casa)
        QtCore.QMetaObject.connectSlotsByName(Cadastrar_casa)

    def retranslateUi(self, Cadastrar_casa):
        _translate = QtCore.QCoreApplication.translate
        Cadastrar_casa.setWindowTitle(_translate("Cadastrar_casa", "Cadastrar casa"))
        self.checkBox.setText(_translate("Cadastrar_casa", "Agua inclusa"))
        self.label.setText(_translate("Cadastrar_casa", "Nome da casa"))
        self.label_2.setText(_translate("Cadastrar_casa", "Valor do aluguel"))
        self.checkBox_2.setText(_translate("Cadastrar_casa", "Luz inclusa"))
        self.pushButton.setText(_translate("Cadastrar_casa", "Concluir"))
        self.pushButton_2.setText(_translate("Cadastrar_casa", "Cancelar"))

