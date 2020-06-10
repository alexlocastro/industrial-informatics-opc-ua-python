# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subscription_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.subView = QtWidgets.QTableView(self.centralwidget)
        self.subView.setGeometry(QtCore.QRect(20, 80, 461, 281))
        self.subView.setStyleSheet("border: 2px solid black;\n"
"")
        self.subView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.subView.setObjectName("subView")
        self.monItemView = QtWidgets.QTableView(self.centralwidget)
        self.monItemView.setGeometry(QtCore.QRect(510, 80, 471, 281))
        self.monItemView.setStyleSheet("border: 2px solid black;")
        self.monItemView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.monItemView.setObjectName("monItemView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 40, 151, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Subscription"))
        self.label_2.setText(_translate("MainWindow", "Monitored Items"))
