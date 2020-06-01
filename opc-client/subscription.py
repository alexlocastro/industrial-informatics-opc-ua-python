# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subscription.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("QDialog {\n"
"    background-color: white;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.pubInterval = QtWidgets.QLineEdit(Dialog)
        self.pubInterval.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.pubInterval.setObjectName("pubInterval")
        self.verticalLayout.addWidget(self.pubInterval)
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
        self.queueSize = QtWidgets.QLineEdit(Dialog)
        self.queueSize.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.queueSize.setObjectName("queueSize")
        self.verticalLayout.addWidget(self.queueSize)
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
        self.absoluteDeadBand = QtWidgets.QLineEdit(Dialog)
        self.absoluteDeadBand.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.absoluteDeadBand.setObjectName("absoluteDeadBand")
        self.verticalLayout.addWidget(self.absoluteDeadBand)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.subButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subButton.setFont(font)
        self.subButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.subButton.setObjectName("subButton")
        self.verticalLayout.addWidget(self.subButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Subscribe"))
        self.label.setText(_translate("Dialog", "Publishing Interval (ms)"))
        self.label_2.setText(_translate("Dialog", "Queue Size"))
        self.label_3.setText(_translate("Dialog", "Absolute  deadband"))
        self.subButton.setText(_translate("Dialog", "Subscribe"))
