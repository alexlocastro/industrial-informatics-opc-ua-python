# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subscription.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pubInterval = QtWidgets.QLineEdit(Dialog)
        self.pubInterval.setGeometry(QtCore.QRect(30, 40, 113, 25))
        self.pubInterval.setObjectName("pubInterval")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 181, 17))
        self.label.setObjectName("label")
        self.subButton = QtWidgets.QPushButton(Dialog)
        self.subButton.setGeometry(QtCore.QRect(270, 240, 89, 25))
        self.subButton.setObjectName("subButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 161, 17))
        self.label_2.setObjectName("label_2")
        self.queueSize = QtWidgets.QLineEdit(Dialog)
        self.queueSize.setGeometry(QtCore.QRect(30, 120, 113, 25))
        self.queueSize.setObjectName("queueSize")
        self.absoluteDeadBand = QtWidgets.QLineEdit(Dialog)
        self.absoluteDeadBand.setGeometry(QtCore.QRect(30, 210, 113, 25))
        self.absoluteDeadBand.setObjectName("absoluteDeadBand")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 141, 17))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Publishing Interval (ms)"))
        self.subButton.setText(_translate("Dialog", "Subscribe"))
        self.label_2.setText(_translate("Dialog", "Queue Size"))
        self.label_3.setText(_translate("Dialog", "Absolute  deadband"))
