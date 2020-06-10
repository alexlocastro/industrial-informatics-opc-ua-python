# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connection_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        ConnectionDialog.setObjectName("ConnectionDialog")
        ConnectionDialog.resize(1089, 524)
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
        self.gridLayout.addWidget(self.certificateLabel, 6, 0, 1, 1)
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
        self.selectableEndpointsTable = QtWidgets.QTableWidget(ConnectionDialog)
        self.selectableEndpointsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.selectableEndpointsTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.selectableEndpointsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.selectableEndpointsTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.selectableEndpointsTable.setObjectName("selectableEndpointsTable")
        self.selectableEndpointsTable.setColumnCount(0)
        self.selectableEndpointsTable.setRowCount(0)
        self.gridLayout.addWidget(self.selectableEndpointsTable, 1, 0, 1, 3)
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
        self.gridLayout.addWidget(self.closeButton, 8, 2, 1, 1)
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
        self.gridLayout.addWidget(self.certificateButton, 6, 1, 1, 2)
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
        self.gridLayout.addWidget(self.privateKeyButton, 7, 1, 1, 2)
        self.privateKeyLabel = QtWidgets.QLabel(ConnectionDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.privateKeyLabel.setFont(font)
        self.privateKeyLabel.setObjectName("privateKeyLabel")
        self.gridLayout.addWidget(self.privateKeyLabel, 7, 0, 1, 1)
        self.unselectableEndpointsTable = QtWidgets.QTableWidget(ConnectionDialog)
        self.unselectableEndpointsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.unselectableEndpointsTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.unselectableEndpointsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.unselectableEndpointsTable.setObjectName("unselectableEndpointsTable")
        self.unselectableEndpointsTable.setColumnCount(0)
        self.unselectableEndpointsTable.setRowCount(0)
        self.gridLayout.addWidget(self.unselectableEndpointsTable, 2, 0, 1, 3)

        self.retranslateUi(ConnectionDialog)
        QtCore.QMetaObject.connectSlotsByName(ConnectionDialog)

    def retranslateUi(self, ConnectionDialog):
        _translate = QtCore.QCoreApplication.translate
        ConnectionDialog.setWindowTitle(_translate("ConnectionDialog", "ConnectionDialog"))
        self.certificateLabel.setText(_translate("ConnectionDialog", "None"))
        self.queryButton.setText(_translate("ConnectionDialog", "Query server capability"))
        self.closeButton.setText(_translate("ConnectionDialog", "Close"))
        self.certificateButton.setText(_translate("ConnectionDialog", "Select certificate"))
        self.privateKeyButton.setText(_translate("ConnectionDialog", "Select private key"))
        self.privateKeyLabel.setText(_translate("ConnectionDialog", "None"))
