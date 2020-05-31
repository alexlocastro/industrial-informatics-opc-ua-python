# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'write_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 17))
        self.label.setObjectName("label")
        self.writeValue = QtWidgets.QLineEdit(Dialog)
        self.writeValue.setGeometry(QtCore.QRect(30, 80, 151, 25))
        self.writeValue.setObjectName("writeValue")
        self.writeButton = QtWidgets.QPushButton(Dialog)
        self.writeButton.setGeometry(QtCore.QRect(200, 170, 89, 25))
        self.writeButton.setObjectName("writeButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "insert value:"))
        self.writeButton.setText(_translate("Dialog", "write"))
