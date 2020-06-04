# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitored_item.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.discardOldestBox = QtWidgets.QCheckBox(Dialog)
        self.discardOldestBox.setGeometry(QtCore.QRect(30, 230, 141, 23))
        self.discardOldestBox.setObjectName("discardOldestBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 110, 131, 17))
        self.label.setObjectName("label")
        self.samplingInterval = QtWidgets.QLineEdit(Dialog)
        self.samplingInterval.setGeometry(QtCore.QRect(250, 140, 113, 25))
        self.samplingInterval.setObjectName("samplingInterval")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 131, 17))
        self.label_2.setObjectName("label_2")
        self.deadbandValue = QtWidgets.QLineEdit(Dialog)
        self.deadbandValue.setGeometry(QtCore.QRect(30, 180, 113, 25))
        self.deadbandValue.setObjectName("deadbandValue")
        self.absDeadbandButton = QtWidgets.QRadioButton(Dialog)
        self.absDeadbandButton.setGeometry(QtCore.QRect(30, 90, 171, 23))
        self.absDeadbandButton.setObjectName("absDeadbandButton")
        self.percentageDeadbandButton = QtWidgets.QRadioButton(Dialog)
        self.percentageDeadbandButton.setGeometry(QtCore.QRect(30, 120, 161, 23))
        self.percentageDeadbandButton.setObjectName("percentageDeadbandButton")
        self.subscribeButton = QtWidgets.QPushButton(Dialog)
        self.subscribeButton.setGeometry(QtCore.QRect(240, 230, 89, 25))
        self.subscribeButton.setObjectName("subscribeButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 20, 131, 17))
        self.label_3.setObjectName("label_3")
        self.queueSize = QtWidgets.QLineEdit(Dialog)
        self.queueSize.setGeometry(QtCore.QRect(250, 50, 113, 25))
        self.queueSize.setObjectName("queueSize")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 111, 17))
        self.label_4.setObjectName("label_4")
        self.subscriptionId = QtWidgets.QLineEdit(Dialog)
        self.subscriptionId.setGeometry(QtCore.QRect(50, 50, 113, 25))
        self.subscriptionId.setObjectName("subscriptionId")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.discardOldestBox.setText(_translate("Dialog", "Discard Oldest"))
        self.label.setText(_translate("Dialog", "Sampling Interval"))
        self.label_2.setText(_translate("Dialog", "DeadBand Value"))
        self.absDeadbandButton.setText(_translate("Dialog", "Absolute Deadband"))
        self.percentageDeadbandButton.setText(_translate("Dialog", "Relative Deadband"))
        self.subscribeButton.setText(_translate("Dialog", "Subscribe"))
        self.label_3.setText(_translate("Dialog", "Queue Size"))
        self.label_4.setText(_translate("Dialog", "Subscription Id"))
