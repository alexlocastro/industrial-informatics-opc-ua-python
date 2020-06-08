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
        Dialog.resize(389, 434)
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
        self.lifetimeCount = QtWidgets.QLineEdit(Dialog)
        self.lifetimeCount.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.lifetimeCount.setObjectName("lifetimeCount")
        self.verticalLayout.addWidget(self.lifetimeCount)
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
        self.maxKeepAliveCount = QtWidgets.QLineEdit(Dialog)
        self.maxKeepAliveCount.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.maxKeepAliveCount.setObjectName("maxKeepAliveCount")
        self.verticalLayout.addWidget(self.maxKeepAliveCount)
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
        self.maxNotificationsPerPublish = QtWidgets.QLineEdit(Dialog)
        self.maxNotificationsPerPublish.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.maxNotificationsPerPublish.setObjectName("maxNotificationsPerPublish")
        self.verticalLayout.addWidget(self.maxNotificationsPerPublish)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.priority = QtWidgets.QLineEdit(Dialog)
        self.priority.setStyleSheet("QLineEdit {\n"
"    border: 2px solid black;\n"
"    margin-left: 80px;\n"
"    margin-right: 80px;\n"
"}")
        self.priority.setObjectName("priority")
        self.verticalLayout.addWidget(self.priority)
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
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
        self.label_2.setText(_translate("Dialog", "Lifetime Count (ms)"))
        self.label_3.setText(_translate("Dialog", "Max Keep Alive Count (ms)"))
        self.label_4.setText(_translate("Dialog", "Max Notifications Per Publish"))
        self.label_5.setText(_translate("Dialog", "Priority"))
        self.subButton.setText(_translate("Dialog", "Subscribe"))
