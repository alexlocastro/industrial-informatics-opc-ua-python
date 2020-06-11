# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subscription_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 467)
        MainWindow.setStyleSheet("\n"
"background-color: white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.subView = QtWidgets.QTableView(self.centralwidget)
        self.subView.setStyleSheet("border: 2px solid black;\n"
"")
        self.subView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.subView.setObjectName("subView")
        self.gridLayout.addWidget(self.subView, 1, 0, 1, 1)
        self.monItemView = QtWidgets.QTableView(self.centralwidget)
        self.monItemView.setStyleSheet("border: 2px solid black;")
        self.monItemView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.monItemView.setObjectName("monItemView")
        self.gridLayout.addWidget(self.monItemView, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Subscription"))
        self.label_2.setText(_translate("MainWindow", "Monitored Items"))
