# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connection_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        ConnectionDialog.setObjectName("ConnectionDialog")
        ConnectionDialog.resize(461, 300)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        ConnectionDialog.setFont(font)
        ConnectionDialog.setAutoFillBackground(False)
        ConnectionDialog.setStyleSheet("background-color: white;\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(ConnectionDialog)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.certificateLabel = QtWidgets.QLabel(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.certificateLabel.setFont(font)
        self.certificateLabel.setObjectName("certificateLabel")
        self.gridLayout.addWidget(self.certificateLabel, 4, 0, 1, 1)
        self.certificateButton = QtWidgets.QPushButton(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.certificateButton.setFont(font)
        self.certificateButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.certificateButton.setObjectName("certificateButton")
        self.gridLayout.addWidget(self.certificateButton, 4, 1, 1, 2)
        self.policyComboBox = QtWidgets.QComboBox(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.policyComboBox.setFont(font)
        self.policyComboBox.setStyleSheet("border: 2px solid black;")
        self.policyComboBox.setObjectName("policyComboBox")
        self.gridLayout.addWidget(self.policyComboBox, 2, 1, 1, 2)
        self.privateKeyLabel = QtWidgets.QLabel(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.privateKeyLabel.setFont(font)
        self.privateKeyLabel.setObjectName("privateKeyLabel")
        self.gridLayout.addWidget(self.privateKeyLabel, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.queryButton = QtWidgets.QPushButton(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.queryButton.setFont(font)
        self.queryButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.queryButton.setObjectName("queryButton")
        self.gridLayout.addWidget(self.queryButton, 0, 0, 1, 3)
        self.modeComboBox = QtWidgets.QComboBox(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.modeComboBox.setFont(font)
        self.modeComboBox.setStyleSheet("border: 2px solid black;")
        self.modeComboBox.setObjectName("modeComboBox")
        self.gridLayout.addWidget(self.modeComboBox, 3, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.closeButton = QtWidgets.QPushButton(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 6, 2, 1, 1)
        self.privateKeyButton = QtWidgets.QPushButton(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.privateKeyButton.setFont(font)
        self.privateKeyButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.privateKeyButton.setObjectName("privateKeyButton")
        self.gridLayout.addWidget(self.privateKeyButton, 5, 1, 1, 2)

        self.retranslateUi(ConnectionDialog)
        QtCore.QMetaObject.connectSlotsByName(ConnectionDialog)

    def retranslateUi(self, ConnectionDialog):
        _translate = QtCore.QCoreApplication.translate
        ConnectionDialog.setWindowTitle(_translate("ConnectionDialog", "ConnectionDialog"))
        self.certificateLabel.setText(_translate("ConnectionDialog", "None"))
        self.certificateButton.setText(_translate("ConnectionDialog", "Select certificate"))
        self.privateKeyLabel.setText(_translate("ConnectionDialog", "None"))
        self.label.setText(_translate("ConnectionDialog", "Security Policy"))
        self.queryButton.setText(_translate("ConnectionDialog", "Query server capability"))
        self.label_2.setText(_translate("ConnectionDialog", "Message Security Mode"))
        self.closeButton.setText(_translate("ConnectionDialog", "Close"))
        self.privateKeyButton.setText(_translate("ConnectionDialog", "Select private key"))
