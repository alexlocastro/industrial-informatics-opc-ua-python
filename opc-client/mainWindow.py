# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1005, 734)
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
        self.refView = QtWidgets.QTableView(self.centralwidget)
        self.refView.setGeometry(QtCore.QRect(70, 320, 861, 89))
        self.refView.setStyleSheet("border: 2px solid black;\n"
"")
        self.refView.setObjectName("refView")
        self.subDataChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.subDataChangeButton.setGeometry(QtCore.QRect(470, 230, 121, 31))
        self.subDataChangeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.subDataChangeButton.setObjectName("subDataChangeButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 290, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 420, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.unsubDataChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.unsubDataChangeButton.setGeometry(QtCore.QRect(810, 420, 121, 31))
        self.unsubDataChangeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.unsubDataChangeButton.setObjectName("unsubDataChangeButton")
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setGeometry(QtCore.QRect(800, 30, 161, 41))
        self.disconnectButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.disconnectButton.setObjectName("disconnectButton")
        self.refAttrButton = QtWidgets.QPushButton(self.centralwidget)
        self.refAttrButton.setGeometry(QtCore.QRect(800, 100, 101, 31))
        self.refAttrButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.refAttrButton.setObjectName("refAttrButton")
        self.logTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.logTextEdit.setGeometry(QtCore.QRect(70, 590, 861, 91))
        self.logTextEdit.setStyleSheet("border: 2px solid black;\n"
"")
        self.logTextEdit.setObjectName("logTextEdit")
        self.subView = QtWidgets.QTableView(self.centralwidget)
        self.subView.setGeometry(QtCore.QRect(70, 460, 861, 91))
        self.subView.setStyleSheet("border: 2px solid black;\n"
"")
        self.subView.setObjectName("subView")
        self.addressComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.addressComboBox.setGeometry(QtCore.QRect(80, 30, 341, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressComboBox.sizePolicy().hasHeightForWidth())
        self.addressComboBox.setSizePolicy(sizePolicy)
        self.addressComboBox.setStyleSheet("border: 2px solid black;")
        self.addressComboBox.setEditable(True)
        self.addressComboBox.setObjectName("addressComboBox")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(650, 30, 131, 41))
        self.connectButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.connectButton.setObjectName("connectButton")
        self.connSettingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.connSettingsButton.setGeometry(QtCore.QRect(440, 20, 191, 41))
        self.connSettingsButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.connSettingsButton.setObjectName("connSettingsButton")
        self.endpointsButton = QtWidgets.QPushButton(self.centralwidget)
        self.endpointsButton.setGeometry(QtCore.QRect(440, 70, 191, 31))
        self.endpointsButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.endpointsButton.setObjectName("endpointsButton")
        self.attrView = QtWidgets.QTreeView(self.centralwidget)
        self.attrView.setGeometry(QtCore.QRect(640, 140, 301, 131))
        self.attrView.setStyleSheet("border: 2px solid black;\n"
"")
        self.attrView.setObjectName("attrView")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(70, 140, 391, 131))
        self.treeView.setStyleSheet("border: 2px solid black;\n"
"")
        self.treeView.setObjectName("treeView")
        self.writeButton = QtWidgets.QPushButton(self.centralwidget)
        self.writeButton.setGeometry(QtCore.QRect(470, 190, 121, 31))
        self.writeButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.writeButton.setObjectName("writeButton")
        self.readButton = QtWidgets.QPushButton(self.centralwidget)
        self.readButton.setGeometry(QtCore.QRect(470, 150, 121, 31))
        self.readButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"}")
        self.readButton.setObjectName("readButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 560, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "OPC UA Client"))
        self.subDataChangeButton.setText(_translate("mainWindow", "Subscribe"))
        self.label.setText(_translate("mainWindow", "References"))
        self.label_2.setText(_translate("mainWindow", "Subscriptions"))
        self.unsubDataChangeButton.setText(_translate("mainWindow", "Unsubscribe"))
        self.disconnectButton.setText(_translate("mainWindow", "Disconnect"))
        self.refAttrButton.setText(_translate("mainWindow", "Refresh"))
        self.connectButton.setText(_translate("mainWindow", "Connect"))
        self.connSettingsButton.setText(_translate("mainWindow", "Connection settings"))
        self.endpointsButton.setText(_translate("mainWindow", "Query Endopoints"))
        self.writeButton.setText(_translate("mainWindow", "Write"))
        self.readButton.setText(_translate("mainWindow", "Read"))
        self.label_3.setText(_translate("mainWindow", "Details"))
        self.label_4.setText(_translate("mainWindow", "Browse"))
        self.label_5.setText(_translate("mainWindow", "Log"))
