# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CPL.ui',
# licensing of 'CPL.ui' applies.
#
# Created: Sat Sep 14 17:34:02 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CPL(object):
    def setupUi(self, CPL):
        CPL.setObjectName("CPL")
        CPL.resize(178, 164)
        self.load = QtWidgets.QPushButton(CPL)
        self.load.setGeometry(QtCore.QRect(0, 20, 171, 23))
        self.load.setObjectName("load")
        self.contentPackPic = QtWidgets.QLabel(CPL)
        self.contentPackPic.setGeometry(QtCore.QRect(80, 170, 171, 111))
        self.contentPackPic.setText("")
        self.contentPackPic.setObjectName("contentPackPic")
        self.back = QtWidgets.QPushButton(CPL)
        self.back.setGeometry(QtCore.QRect(0, 110, 171, 23))
        self.back.setObjectName("back")
        self.load_cp = QtWidgets.QPushButton(CPL)
        self.load_cp.setGeometry(QtCore.QRect(0, 60, 171, 23))
        self.load_cp.setObjectName("load_cp")

        self.retranslateUi(CPL)
        QtCore.QMetaObject.connectSlotsByName(CPL)

    def retranslateUi(self, CPL):
        CPL.setWindowTitle(QtWidgets.QApplication.translate("CPL", "Content Pack Launcher", None, -1))
        self.load.setText(QtWidgets.QApplication.translate("CPL", "Open folder", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("CPL", "Back", None, -1))
        self.load_cp.setText(QtWidgets.QApplication.translate("CPL", "Load content pack", None, -1))

