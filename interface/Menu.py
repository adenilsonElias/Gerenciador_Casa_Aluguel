# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(276, 140)
        Menu.setAcceptDrops(False)
        self.Inquilino = QtWidgets.QPushButton(Menu)
        self.Inquilino.setGeometry(QtCore.QRect(20, 10, 88, 34))
        self.Inquilino.setObjectName("Inquilino")
        self.Casa = QtWidgets.QPushButton(Menu)
        self.Casa.setGeometry(QtCore.QRect(20, 50, 88, 34))
        self.Casa.setObjectName("Casa")
        self.label = QtWidgets.QLabel(Menu)
        self.label.setGeometry(QtCore.QRect(120, 20, 121, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Menu)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 111, 18))
        self.label_2.setObjectName("label_2")
        self.Fechar = QtWidgets.QPushButton(Menu)
        self.Fechar.setGeometry(QtCore.QRect(20, 90, 88, 34))
        self.Fechar.setObjectName("Fechar")
        self.label_3 = QtWidgets.QLabel(Menu)
        self.label_3.setGeometry(QtCore.QRect(120, 100, 121, 18))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.Inquilino.setText(_translate("Menu", "Inquilino"))
        self.Casa.setText(_translate("Menu", "Casa"))
        self.label.setText(_translate("Menu", "Cadastrar inquilino"))
        self.label_2.setText(_translate("Menu", "Cadastrar casa"))
        self.Fechar.setText(_translate("Menu", "Fechar"))
        self.label_3.setText(_translate("Menu", "fechar o programa"))

