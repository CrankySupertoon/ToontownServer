# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverMenu.ui',
# licensing of 'serverMenu.ui' applies.
#
# Created: Sat Aug 31 16:03:45 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(316, 325)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 220, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 81, 16))
        self.label_5.setObjectName("label_5")
        self.serverName = QtWidgets.QLineEdit(Form)
        self.serverName.setGeometry(QtCore.QRect(130, 30, 171, 20))
        self.serverName.setObjectName("serverName")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 81, 16))
        self.label_6.setObjectName("label_6")
        self.serverIPAddress = QtWidgets.QLineEdit(Form)
        self.serverIPAddress.setGeometry(QtCore.QRect(130, 60, 171, 20))
        self.serverIPAddress.setObjectName("serverIPAddress")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.label_7.setObjectName("label_7")
        self.nameOfServer = QtWidgets.QLineEdit(Form)
        self.nameOfServer.setGeometry(QtCore.QRect(130, 90, 171, 20))
        self.nameOfServer.setObjectName("nameOfServer")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 120, 81, 16))
        self.label_8.setObjectName("label_8")
        self.serverList = QtWidgets.QComboBox(Form)
        self.serverList.setGeometry(QtCore.QRect(130, 120, 171, 22))
        self.serverList.setObjectName("serverList")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 220, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Server Menu", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Save", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "Play", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Username", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "IP Address", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "Name of server", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "Server List", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "Close", None, -1))

