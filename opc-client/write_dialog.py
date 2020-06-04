# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'write_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(346, 109)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("QDialog {\n"
"    background-color:white;\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.writeValue = QtWidgets.QLineEdit(Dialog)
        self.writeValue.setGeometry(QtCore.QRect(80, 20, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.writeValue.setFont(font)
        self.writeValue.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"}")
        self.writeValue.setText("")
        self.writeValue.setObjectName("writeValue")
        self.writeButton = QtWidgets.QPushButton(Dialog)
        self.writeButton.setGeometry(QtCore.QRect(120, 70, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.writeButton.setFont(font)
        self.writeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.writeButton.setObjectName("writeButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Write value"))
        self.label.setText(_translate("Dialog", "Value"))
        self.writeButton.setText(_translate("Dialog", "Write"))
