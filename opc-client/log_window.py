# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 455)
        MainWindow.setStyleSheet("\n"
"background-color: white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 447, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.logTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.logTextEdit.setGeometry(QtCore.QRect(10, 70, 621, 371))
        self.logTextEdit.setStyleSheet("border: 2px solid black;\n"
"")
        self.logTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.logTextEdit.setObjectName("logTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Logs"))
        self.label_5.setText(_translate("MainWindow", "Log"))
