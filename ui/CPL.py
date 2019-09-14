# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CPL.ui',
# licensing of 'CPL.ui' applies.
#
# Created: Sat Sep 14 17:09:39 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CPL(object):
    def setupUi(self, CPL):
        CPL.setObjectName("CPL")
        CPL.resize(578, 449)
        self.label_5 = QtWidgets.QLabel(CPL)
        self.label_5.setGeometry(QtCore.QRect(0, 100, 81, 16))
        self.label_5.setObjectName("label_5")
        self.load = QtWidgets.QPushButton(CPL)
        self.load.setGeometry(QtCore.QRect(0, 20, 171, 23))
        self.load.setObjectName("load")
        self.name = QtWidgets.QLineEdit(CPL)
        self.name.setGeometry(QtCore.QRect(80, 100, 171, 20))
        self.name.setObjectName("name")
        self.label_6 = QtWidgets.QLabel(CPL)
        self.label_6.setGeometry(QtCore.QRect(0, 140, 81, 16))
        self.label_6.setObjectName("label_6")
        self.author = QtWidgets.QLineEdit(CPL)
        self.author.setGeometry(QtCore.QRect(80, 140, 171, 20))
        self.author.setObjectName("author")
        self.contentPackPic = QtWidgets.QLabel(CPL)
        self.contentPackPic.setGeometry(QtCore.QRect(80, 170, 171, 111))
        self.contentPackPic.setText("")
        self.contentPackPic.setObjectName("contentPackPic")
        self.back = QtWidgets.QPushButton(CPL)
        self.back.setGeometry(QtCore.QRect(0, 410, 171, 23))
        self.back.setObjectName("back")
        self.load_cp = QtWidgets.QPushButton(CPL)
        self.load_cp.setGeometry(QtCore.QRect(0, 60, 251, 23))
        self.load_cp.setObjectName("load_cp")

        self.retranslateUi(CPL)
        QtCore.QMetaObject.connectSlotsByName(CPL)

    def retranslateUi(self, CPL):
        CPL.setWindowTitle(QtWidgets.QApplication.translate("CPL", "Content Pack Launcher", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("CPL", "Name", None, -1))
        self.load.setText(QtWidgets.QApplication.translate("CPL", "Open folder", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("CPL", "Author", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("CPL", "Back", None, -1))
        self.load_cp.setText(QtWidgets.QApplication.translate("CPL", "Load content pack", None, -1))

