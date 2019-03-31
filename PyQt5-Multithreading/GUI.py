# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 363)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btns = QtWidgets.QPushButton(self.centralWidget)
        self.btns.setGeometry(QtCore.QRect(90, 55, 150, 50))
        self.btns.setMinimumSize(QtCore.QSize(100, 50))
        self.btns.setObjectName("btns")
        self.stops = QtWidgets.QPushButton(self.centralWidget)
        self.stops.setGeometry(QtCore.QRect(290, 55, 150, 50))
        self.stops.setMinimumSize(QtCore.QSize(100, 50))
        self.stops.setObjectName("stops")
        self.stopr = QtWidgets.QPushButton(self.centralWidget)
        self.stopr.setGeometry(QtCore.QRect(290, 128, 150, 50))
        self.stopr.setMinimumSize(QtCore.QSize(100, 50))
        self.stopr.setObjectName("stopr")
        self.btnr = QtWidgets.QPushButton(self.centralWidget)
        self.btnr.setGeometry(QtCore.QRect(90, 128, 150, 50))
        self.btnr.setMinimumSize(QtCore.QSize(100, 50))
        self.btnr.setObjectName("btnr")
        self.alls = QtWidgets.QPushButton(self.centralWidget)
        self.alls.setGeometry(QtCore.QRect(90, 200, 150, 50))
        self.alls.setMinimumSize(QtCore.QSize(100, 50))
        self.alls.setObjectName("alls")
        self.alle = QtWidgets.QPushButton(self.centralWidget)
        self.alle.setGeometry(QtCore.QRect(290, 200, 150, 50))
        self.alle.setMinimumSize(QtCore.QSize(100, 50))
        self.alle.setObjectName("alle")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 553, 20))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btns.setText(_translate("MainWindow", "开始发送线程"))
        self.stops.setText(_translate("MainWindow", "退出发送线程"))
        self.stopr.setText(_translate("MainWindow", "退出接收线程"))
        self.btnr.setText(_translate("MainWindow", "开始接收线程"))
        self.alls.setText(_translate("MainWindow", "开始接收和发送线程"))
        self.alle.setText(_translate("MainWindow", "退出接收和发送线程"))

