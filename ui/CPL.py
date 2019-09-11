# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contentPackLauncher.ui',
# licensing of 'contentPackLauncher.ui' applies.
#
# Created: Thu Sep  5 20:16:11 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(578, 449)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 100, 81, 16))
        self.label_5.setObjectName("label_5")
        self.load = QtWidgets.QPushButton(Form)
        self.load.setGeometry(QtCore.QRect(0, 20, 171, 23))
        self.load.setObjectName("load")
        self.contentPacks = QtWidgets.QComboBox(Form)
        self.contentPacks.setGeometry(QtCore.QRect(0, 70, 571, 22))
        self.contentPacks.setObjectName("contentPacks")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(80, 100, 171, 20))
        self.name.setObjectName("name")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 140, 81, 16))
        self.label_6.setObjectName("label_6")
        self.author = QtWidgets.QLineEdit(Form)
        self.author.setGeometry(QtCore.QRect(80, 140, 171, 20))
        self.author.setObjectName("author")
        self.contentPackPic = QtWidgets.QLabel(Form)
        self.contentPackPic.setGeometry(QtCore.QRect(80, 170, 171, 111))
        self.contentPackPic.setText("")
        self.contentPackPic.setObjectName("contentPackPic")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Name", None, -1))
        self.load.setText(QtWidgets.QApplication.translate("Form", "Load folder", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Author", None, -1))

