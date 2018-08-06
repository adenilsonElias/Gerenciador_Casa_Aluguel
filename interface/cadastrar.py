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
        self.lineEdit = QtWidgets.QLineEdit(Cadastrar)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 181, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Cadastrar)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 181, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Cadastrar)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 150, 181, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(Cadastrar)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Cadastrar)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 58, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Cadastrar)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 58, 18))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Cadastrar)
        self.pushButton.setGeometry(QtCore.QRect(10, 250, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Cadastrar)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 250, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Cadastrar)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 58, 18))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Cadastrar)
        self.comboBox.setGeometry(QtCore.QRect(10, 210, 181, 32))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Cadastrar)
        QtCore.QMetaObject.connectSlotsByName(Cadastrar)
        Cadastrar.setTabOrder(self.lineEdit, self.lineEdit_2)
        Cadastrar.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Cadastrar.setTabOrder(self.lineEdit_3, self.comboBox)
        Cadastrar.setTabOrder(self.comboBox, self.pushButton)
        Cadastrar.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Cadastrar):
        _translate = QtCore.QCoreApplication.translate
        Cadastrar.setWindowTitle(_translate("Cadastrar", "cadastrar"))
        self.label.setText(_translate("Cadastrar", "Nome"))
        self.label_2.setText(_translate("Cadastrar", "CPF"))
        self.label_3.setText(_translate("Cadastrar", "RG"))
        self.pushButton.setText(_translate("Cadastrar", "concluir"))
        self.pushButton_2.setText(_translate("Cadastrar", "cancelar"))
        self.label_4.setText(_translate("Cadastrar", "Casa"))

