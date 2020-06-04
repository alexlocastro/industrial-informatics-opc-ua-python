# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitored_item.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 433)
        Dialog.setStyleSheet("QDialog {\n"
"    background-color: white;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.subscriptionId = QtWidgets.QLineEdit(Dialog)
        self.subscriptionId.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.subscriptionId.setObjectName("subscriptionId")
        self.verticalLayout.addWidget(self.subscriptionId)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.queueSize = QtWidgets.QLineEdit(Dialog)
        self.queueSize.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.queueSize.setObjectName("queueSize")
        self.verticalLayout.addWidget(self.queueSize)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.samplingInterval = QtWidgets.QLineEdit(Dialog)
        self.samplingInterval.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.samplingInterval.setObjectName("samplingInterval")
        self.verticalLayout.addWidget(self.samplingInterval)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.deadbandValue = QtWidgets.QLineEdit(Dialog)
        self.deadbandValue.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.deadbandValue.setObjectName("deadbandValue")
        self.verticalLayout.addWidget(self.deadbandValue)
        self.percentageDeadbandButton = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.percentageDeadbandButton.setFont(font)
        self.percentageDeadbandButton.setStyleSheet("margin-left:70")
        self.percentageDeadbandButton.setObjectName("percentageDeadbandButton")
        self.verticalLayout.addWidget(self.percentageDeadbandButton)
        self.absDeadbandButton = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.absDeadbandButton.setFont(font)
        self.absDeadbandButton.setStyleSheet("margin-left:70")
        self.absDeadbandButton.setObjectName("absDeadbandButton")
        self.verticalLayout.addWidget(self.absDeadbandButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.discardOldestBox = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.discardOldestBox.setFont(font)
        self.discardOldestBox.setStyleSheet("margin-left:70")
        self.discardOldestBox.setObjectName("discardOldestBox")
        self.verticalLayout.addWidget(self.discardOldestBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.subscribeButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subscribeButton.setFont(font)
        self.subscribeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.subscribeButton.setObjectName("subscribeButton")
        self.verticalLayout.addWidget(self.subscribeButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Subscription Id"))
        self.label_3.setText(_translate("Dialog", "Queue Size"))
        self.label.setText(_translate("Dialog", "Sampling Interval"))
        self.label_2.setText(_translate("Dialog", "DeadBand Value"))
        self.percentageDeadbandButton.setText(_translate("Dialog", "Relative Deadband"))
        self.absDeadbandButton.setText(_translate("Dialog", "Absolute Deadband"))
        self.discardOldestBox.setText(_translate("Dialog", "Discard Oldest"))
        self.subscribeButton.setText(_translate("Dialog", "Subscribe"))
