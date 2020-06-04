# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_sub.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 231)
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
        self.subscriptionId = QtWidgets.QLineEdit(Dialog)
        self.subscriptionId.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.subscriptionId.setObjectName("subscriptionId")
        self.verticalLayout.addWidget(self.subscriptionId)
        spacerItem = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.deleteSubButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deleteSubButton.setFont(font)
        self.deleteSubButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.deleteSubButton.setObjectName("deleteSubButton")
        self.verticalLayout.addWidget(self.deleteSubButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Subscription Id"))
        self.deleteSubButton.setText(_translate("Dialog", "Delete"))
