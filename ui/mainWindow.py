# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui',
# licensing of 'mainWindow.ui' applies.
#
# Created: Sun Nov 10 20:24:25 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(280, 80, 171, 20))
        self.name.setObjectName("name")
        self.options_menu = QtWidgets.QPushButton(self.centralwidget)
        self.options_menu.setGeometry(QtCore.QRect(0, 540, 170, 20))
        self.options_menu.setMaximumSize(QtCore.QSize(170, 20))
        self.options_menu.setObjectName("options_menu")
        self.districtName = QtWidgets.QLineEdit(self.centralwidget)
        self.districtName.setGeometry(QtCore.QRect(280, 120, 171, 20))
        self.districtName.setObjectName("districtName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Toontown Launcher", None, -1))
        self.name.setText(QtWidgets.QApplication.translate("MainWindow", "Username...", None, -1))
        self.options_menu.setText(QtWidgets.QApplication.translate("MainWindow", "Options", None, -1))
        self.districtName.setText(QtWidgets.QApplication.translate("MainWindow", "District name...", None, -1))

