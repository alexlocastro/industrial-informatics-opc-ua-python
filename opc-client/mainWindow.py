# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(927, 734)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setStyleSheet("\n"
"background-color: white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.unsubDataChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.unsubDataChangeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.unsubDataChangeButton.setObjectName("unsubDataChangeButton")
        self.gridLayout.addWidget(self.unsubDataChangeButton, 10, 5, 1, 1)
        self.endpointsButton = QtWidgets.QPushButton(self.centralwidget)
        self.endpointsButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.endpointsButton.setObjectName("endpointsButton")
        self.gridLayout.addWidget(self.endpointsButton, 0, 2, 1, 1)
        self.addressComboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressComboBox.sizePolicy().hasHeightForWidth())
        self.addressComboBox.setSizePolicy(sizePolicy)
        self.addressComboBox.setStyleSheet("border: 2px solid black;")
        self.addressComboBox.setEditable(True)
        self.addressComboBox.setObjectName("addressComboBox")
        self.gridLayout.addWidget(self.addressComboBox, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.logTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.logTextEdit.setStyleSheet("border: 2px solid black;\n"
"")
        self.logTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.logTextEdit.setObjectName("logTextEdit")
        self.gridLayout.addWidget(self.logTextEdit, 14, 0, 1, 6)
        self.refView = QtWidgets.QTableView(self.centralwidget)
        self.refView.setEnabled(True)
        self.refView.setStyleSheet("border: 2px solid black;\n"
"")
        self.refView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.refView.setObjectName("refView")
        self.gridLayout.addWidget(self.refView, 9, 0, 1, 6)
        self.connSettingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.connSettingsButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.connSettingsButton.setObjectName("connSettingsButton")
        self.gridLayout.addWidget(self.connSettingsButton, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 12, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)
        self.writeButton = QtWidgets.QPushButton(self.centralwidget)
        self.writeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.writeButton.setObjectName("writeButton")
        self.gridLayout.addWidget(self.writeButton, 7, 2, 1, 1)
        self.subDataChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.subDataChangeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.subDataChangeButton.setObjectName("subDataChangeButton")
        self.gridLayout.addWidget(self.subDataChangeButton, 10, 4, 1, 1)
        self.readButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readButton.sizePolicy().hasHeightForWidth())
        self.readButton.setSizePolicy(sizePolicy)
        self.readButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.readButton.setObjectName("readButton")
        self.gridLayout.addWidget(self.readButton, 7, 1, 1, 1)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setStyleSheet("border: 2px solid black;\n"
"")
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 3, 0, 5, 1)
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.disconnectButton.setObjectName("disconnectButton")
        self.gridLayout.addWidget(self.disconnectButton, 0, 5, 1, 1)
        self.attrView = QtWidgets.QTreeView(self.centralwidget)
        self.attrView.setEnabled(True)
        self.attrView.setStyleSheet("border: 2px solid black;\n"
"")
        self.attrView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.attrView.setObjectName("attrView")
        self.gridLayout.addWidget(self.attrView, 3, 1, 4, 5)
        self.subView = QtWidgets.QTableView(self.centralwidget)
        self.subView.setStyleSheet("border: 2px solid black;\n"
"")
        self.subView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.subView.setObjectName("subView")
        self.gridLayout.addWidget(self.subView, 11, 0, 1, 1)
        self.createSubButton = QtWidgets.QPushButton(self.centralwidget)
        self.createSubButton.setObjectName("createSubButton")
        self.gridLayout.addWidget(self.createSubButton, 10, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 0, 4, 1, 1)
        self.monItemView = QtWidgets.QTableView(self.centralwidget)
        self.monItemView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.monItemView.setObjectName("monItemView")
        self.gridLayout.addWidget(self.monItemView, 11, 1, 1, 5)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "OPC UA Client"))
        self.label_3.setText(_translate("mainWindow", "Details"))
        self.unsubDataChangeButton.setText(_translate("mainWindow", "Unsubscribe"))
        self.endpointsButton.setText(_translate("mainWindow", "Query Endopoints"))
        self.label_4.setText(_translate("mainWindow", "Browse"))
        self.connSettingsButton.setText(_translate("mainWindow", "Connection settings"))
        self.label_5.setText(_translate("mainWindow", "Log"))
        self.label_2.setText(_translate("mainWindow", "Subscriptions"))
        self.writeButton.setText(_translate("mainWindow", "Write"))
        self.subDataChangeButton.setText(_translate("mainWindow", "Subscribe"))
        self.readButton.setText(_translate("mainWindow", "Read"))
        self.disconnectButton.setText(_translate("mainWindow", "Disconnect"))
        self.createSubButton.setText(_translate("mainWindow", "Create Subscription"))
        self.label.setText(_translate("mainWindow", "References"))
        self.connectButton.setText(_translate("mainWindow", "Connect"))
