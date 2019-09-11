# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Thu Sep  5 20:11:51 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 322)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.option = QtWidgets.QComboBox(self.centralwidget)
        self.option.setGeometry(QtCore.QRect(100, 80, 171, 22))
        self.option.setObjectName("option")
        self.option.addItem("")
        self.option.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(100, 50, 171, 20))
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 81, 16))
        self.label_3.setObjectName("label_3")
        self.IP = QtWidgets.QLineEdit(self.centralwidget)
        self.IP.setGeometry(QtCore.QRect(100, 140, 171, 20))
        self.IP.setObjectName("IP")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(100, 240, 171, 23))
        self.playButton.setObjectName("playButton")
        self.contentPacks = QtWidgets.QPushButton(self.centralwidget)
        self.contentPacks.setGeometry(QtCore.QRect(100, 110, 171, 23))
        self.contentPacks.setText("")
        self.contentPacks.setObjectName("contentPacks")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 81, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Toontown Launcher", None, -1))
        self.option.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Local", None, -1))
        self.option.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Server", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Gamemode", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Username", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Server Address", None, -1))
        self.playButton.setText(QtWidgets.QApplication.translate("MainWindow", "Play Game", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Content Packs", None, -1))

