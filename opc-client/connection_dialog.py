from PyQt5.QtWidgets import QDialog, QFileDialog,QTableWidgetItem
from PyQt5.QtCore import Qt

from connection_ui import Ui_ConnectionDialog
from uawidgets.utils import trycatchslot


class ConnectionDialog(QDialog):
    def __init__(self, parent, uri):
        QDialog.__init__(self)
        self.ui = Ui_ConnectionDialog()
        self.ui.setupUi(self)
        self.ui.endpointsTable.setRowCount(0)
        self.ui.endpointsTable.setColumnCount(4)
        self.ui.endpointsTable.setHorizontalHeaderLabels(["EndpointUrl","SecurityMode","SecurityPolicy","TransportProfileUri"])
        self.ui.endpointsTable.horizontalHeader().setSectionResizeMode(0)
        self.ui.endpointsTable.horizontalHeader().setStretchLastSection(True)
        self.uaclient = parent
        self.uri = uri
        self.supported_endpoint = "uatcp-uasc-uabinary"
        
        '''self.ui.modeComboBox.addItem("None")
        self.ui.modeComboBox.addItem("Sign")
        self.ui.modeComboBox.addItem("SignAndEncrypt")

        self.ui.policyComboBox.addItem("None")
        self.ui.policyComboBox.addItem("Basic128Rsa15")
        self.ui.policyComboBox.addItem("Basic256")
        self.ui.policyComboBox.addItem("Basic256Sha256")'''


        self.ui.closeButton.clicked.connect(lambda : self.close())
        self.ui.certificateButton.clicked.connect(self.get_certificate)
        self.ui.privateKeyButton.clicked.connect(self.get_private_key)
        self.ui.queryButton.clicked.connect(self.query)

    '''@trycatchslot
    def query(self):
        self.ui.modeComboBox.clear()
        self.ui.policyComboBox.clear()
        endpoints = self.uaclient.get_endpoints()
        modes = []
        policies = []
        for edp in endpoints:
            mode = edp.SecurityMode.name
            if mode not in modes:
                self.ui.modeComboBox.addItem(mode)
                modes.append(mode)
            policy = edp.SecurityPolicyUri.split("#")[1]
            if policy not in policies:
                self.ui.policyComboBox.addItem(policy)
                policies.append(policy)'''
    def query(self):
        try:
            endpoints = self.uaclient.get_endpoints()
            for edp in endpoints:
                self.endpoint_url = edp.EndpointUrl
                self.mode = edp.SecurityMode.name
                self.policy = edp.SecurityPolicyUri.split("#")[1]
                self.transport_profile_uri = edp.TransportProfileUri
                rowPosition = self.ui.endpointsTable.rowCount()
                self.ui.endpointsTable.insertRow(rowPosition)
                
                self.ui.endpointsTable.setItem(rowPosition , 0, QTableWidgetItem(self.endpoint_url))
                self.ui.endpointsTable.setItem(rowPosition , 1, QTableWidgetItem(self.mode))
                self.ui.endpointsTable.setItem(rowPosition , 2, QTableWidgetItem(self.policy))
                self.ui.endpointsTable.setItem(rowPosition , 3, QTableWidgetItem(self.transport_profile_uri))
                
                if self.supported_endpoint not in self.transport_profile_uri:
                    #row not selectable
                    
        except Exception as ex:
            self.uaclient.log_window.ui.logTextEdit.append(str(ex))
    
    def close(self):
        row = self.ui.endpointsTable.currentRow()
        if row > -1:
            security_mode = self.ui.endpointsTable.item(row,1).text()
            if security_mode ==  "None":
                self.uaclient.security_mode = None
            else:
                self.uaclient.security_mode = security_mode
            security_policy = self.ui.endpointsTable.item(row,2).text()
            if security_policy == "None":
                self.uaclient.security_policy = None
            else:
                self.uaclient.security_policy = security_policy
        
        self.accept()


    '''@property
    def security_mode(self):
        text = self.ui.modeComboBox.currentText()
        if text == "None":
            return None
        return text

    @security_mode.setter
    def security_mode(self, value):
        self.ui.modeComboBox.setCurrentText(value)

    @property
    def security_policy(self):
        text = self.ui.policyComboBox.currentText()
        if text == "None":
            return None
        return text

    @security_policy.setter
    def security_policy(self, value):
        self.ui.policyComboBox.setCurrentText(value)
    '''
    @property
    def certificate_path(self):
        return self.ui.certificateLabel.text()

    @certificate_path.setter
    def certificate_path(self, value):
        self.ui.certificateLabel.setText(value)

    @property
    def private_key_path(self):
        return self.ui.privateKeyLabel.text()

    @private_key_path.setter
    def private_key_path(self, value):
        self.ui.privateKeyLabel.setText(value)

    def get_certificate(self):
        path, ok = QFileDialog.getOpenFileName(self, "Select certificate", self.certificate_path, "Certificate (*.der)")
        if ok:
            self.ui.certificateLabel.setText(path)

    def get_private_key(self):
        path, ok = QFileDialog.getOpenFileName(self, "Select private key", self.private_key_path, "Private key (*.pem)")
        if ok:
            self.ui.privateKeyLabel.setText(path)


