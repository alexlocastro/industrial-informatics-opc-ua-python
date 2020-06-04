# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_sub.ui'
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
        self.label.setGeometry(QtCore.QRect(50, 30, 121, 17))
        self.label.setObjectName("label")
        self.subscriptionId = QtWidgets.QLineEdit(Dialog)
        self.subscriptionId.setGeometry(QtCore.QRect(50, 80, 113, 25))
        self.subscriptionId.setObjectName("subscriptionId")
        self.deleteSubButton = QtWidgets.QPushButton(Dialog)
        self.deleteSubButton.setGeometry(QtCore.QRect(60, 180, 89, 25))
        self.deleteSubButton.setObjectName("deleteSubButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Subscription Id"))
        self.deleteSubButton.setText(_translate("Dialog", "Delete"))
