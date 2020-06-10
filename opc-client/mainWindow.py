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
        mainWindow.resize(927, 550)
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setStyleSheet("border: 2px solid black;\n"
"")
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 6, 0, 5, 1)
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.disconnectButton.setObjectName("disconnectButton")
        self.gridLayout.addWidget(self.disconnectButton, 5, 3, 1, 1)
        self.showLogsButton = QtWidgets.QPushButton(self.centralwidget)
        self.showLogsButton.setObjectName("showLogsButton")
        self.gridLayout.addWidget(self.showLogsButton, 16, 0, 1, 1)
        self.addressComboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressComboBox.sizePolicy().hasHeightForWidth())
        self.addressComboBox.setSizePolicy(sizePolicy)
        self.addressComboBox.setStyleSheet("border: 2px solid black;")
        self.addressComboBox.setEditable(True)
        self.addressComboBox.setObjectName("addressComboBox")
        self.gridLayout.addWidget(self.addressComboBox, 2, 0, 1, 1)
        self.endpointsButton = QtWidgets.QPushButton(self.centralwidget)
        self.endpointsButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.endpointsButton.setObjectName("endpointsButton")
        self.gridLayout.addWidget(self.endpointsButton, 2, 2, 1, 1)
        self.connSettingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.connSettingsButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.connSettingsButton.setObjectName("connSettingsButton")
        self.gridLayout.addWidget(self.connSettingsButton, 2, 1, 1, 1)
        self.showSubscriptionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.showSubscriptionsButton.setObjectName("showSubscriptionsButton")
        self.gridLayout.addWidget(self.showSubscriptionsButton, 12, 0, 1, 1)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.showReferencesButton = QtWidgets.QPushButton(self.centralwidget)
        self.showReferencesButton.setObjectName("showReferencesButton")
        self.gridLayout.addWidget(self.showReferencesButton, 11, 0, 1, 1)
        self.createSubButton = QtWidgets.QPushButton(self.centralwidget)
        self.createSubButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.createSubButton.setObjectName("createSubButton")
        self.gridLayout.addWidget(self.createSubButton, 16, 1, 1, 1)
        self.subDataChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.subDataChangeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.subDataChangeButton.setObjectName("subDataChangeButton")
        self.gridLayout.addWidget(self.subDataChangeButton, 12, 1, 1, 1)
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
        self.gridLayout.addWidget(self.readButton, 11, 1, 1, 1)
        self.deleteSubButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteSubButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.deleteSubButton.setObjectName("deleteSubButton")
        self.gridLayout.addWidget(self.deleteSubButton, 16, 2, 1, 1)
        self.unsubDataChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.unsubDataChangeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.unsubDataChangeButton.setObjectName("unsubDataChangeButton")
        self.gridLayout.addWidget(self.unsubDataChangeButton, 12, 2, 1, 1)
        self.writeButton = QtWidgets.QPushButton(self.centralwidget)
        self.writeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.writeButton.setObjectName("writeButton")
        self.gridLayout.addWidget(self.writeButton, 11, 2, 1, 1)
        self.attrView = QtWidgets.QTreeView(self.centralwidget)
        self.attrView.setEnabled(True)
        self.attrView.setStyleSheet("border: 2px solid black;\n"
"")
        self.attrView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.attrView.setObjectName("attrView")
        self.gridLayout.addWidget(self.attrView, 6, 1, 5, 4)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "OPC UA Client"))
        self.label_4.setText(_translate("mainWindow", "Browse"))
        self.disconnectButton.setText(_translate("mainWindow", "Disconnect"))
        self.showLogsButton.setText(_translate("mainWindow", "Logs"))
        self.endpointsButton.setText(_translate("mainWindow", "Query Endpoints"))
        self.connSettingsButton.setText(_translate("mainWindow", "Connection settings"))
        self.showSubscriptionsButton.setText(_translate("mainWindow", "Subscriptions"))
        self.connectButton.setText(_translate("mainWindow", "Connect"))
        self.label_3.setText(_translate("mainWindow", "Details"))
        self.showReferencesButton.setText(_translate("mainWindow", "References"))
        self.createSubButton.setText(_translate("mainWindow", "Create Subscription"))
        self.subDataChangeButton.setText(_translate("mainWindow", "Add monitored item"))
        self.readButton.setText(_translate("mainWindow", "Read"))
        self.deleteSubButton.setText(_translate("mainWindow", "Delete subscription"))
        self.unsubDataChangeButton.setText(_translate("mainWindow", "Delete monitored item"))
        self.writeButton.setText(_translate("mainWindow", "Write"))
