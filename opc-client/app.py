from connection_dialog import ConnectionDialog
from subscription_dialog import SubscriptionDialog
from write import WriteDialog

from mainWindow import Ui_mainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QItemSelection, Qt, QObject, pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QStandardItem


from uawidgets.tree_widget import TreeWidget
from uawidgets.attrs_widget import AttrsWidget
from uawidgets.refs_widget import RefsWidget

from opcua import Client, crypto, ua, Node
from opcua.tools import endpoint_to_strings

import sys
import logging
from datetime import datetime


class DataChangeHandler(QObject):
    data_change_fired = pyqtSignal(object, str, str)

    def datachange_notification(self, node, val, data):
        if data.monitored_item.Value.SourceTimestamp:
            dato = data.monitored_item.Value.SourceTimestamp.isoformat()
        elif data.monitored_item.Value.ServerTimestamp:
            dato = data.monitored_item.Value.ServerTimestamp.isoformat()
        else:
            dato = datetime.now().isoformat()
        self.data_change_fired.emit(node, str(val), dato)


class DataChangeUI(object):

    def __init__(self, window):
        self.window = window
        self._subhandler = DataChangeHandler()
        self._subscribed_nodes = []
        self._datachange_sub = None
        self._subs_dc = {}
        self.model = QStandardItemModel()
        self.window.ui.subView.setModel(self.model)
        self.window.ui.subView.horizontalHeader().setSectionResizeMode(1)
        self.pub_interval = 500
        self.queue_size = 1
        self.abs_deadband = 0
        
        self.window.ui.subDataChangeButton.clicked.connect(lambda: self.show_sub_dialog())
        self.window.ui.unsubDataChangeButton.clicked.connect(lambda: self._unsubscribe())

        # handle subscriptions
        self._subhandler.data_change_fired.connect(self._update_subscription_model, type=Qt.QueuedConnection)
        
    
    def show_sub_dialog(self):
        dia = SubscriptionDialog(self)
        dia.exec_()

    def clear(self):
        self._subscribed_nodes = []
        self.model.clear()

    def _subscribe(self, node=None):
        if not isinstance(node, Node):
            node = self.window.get_current_node()
            if node is None:
                return
        if node in self._subscribed_nodes:
            self.window.ui.logTextEdit.append("already subscribed to node: %s " % node)
            return
        self.model.setHorizontalHeaderLabels(["DisplayName", "Value", "Timestamp"])
        text = str(node.get_display_name().Text)
        row = [QStandardItem(text), QStandardItem("No Data yet"), QStandardItem("")]
        row[0].setData(node)
        self.model.appendRow(row)
        self._subscribed_nodes.append(node)
        
        try:
            if not self._datachange_sub:
                self._datachange_sub = self.window.client.create_subscription(self.pub_interval, self._subhandler)
            #handle = self._datachange_sub.subscribe_data_change(node,queuesize=self.queue_size)
            handle = self._datachange_sub.deadband_monitor(node,self.abs_deadband,queuesize=self.queue_size ) 
            self._subs_dc[node.nodeid] = handle
            
        except Exception as ex:
            self.window.ui.logTextEdit.append(str(ex))
            idx = self.model.indexFromItem(row[0])
            self.model.takeRow(idx.row())

    def _unsubscribe(self):
        node = self.window.get_current_node()
        if node is None:
            return
        self._datachange_sub.unsubscribe(self._subs_dc[node.nodeid])
        self._subscribed_nodes.remove(node)
        i = 0
        while self.model.item(i):
            item = self.model.item(i)
            if item.data() == node:
                self.model.removeRow(i)
            i += 1

    def _update_subscription_model(self, node, value, timestamp):
        i = 0
        while self.model.item(i):
            item = self.model.item(i)
            if item.data() == node:
                it = self.model.item(i, 1)
                it.setText(value)
                it_ts = self.model.item(i, 2)
                it_ts.setText(timestamp)
            i += 1





class ClientController:

    def __init__(self, view):
        self.ui = view
        self.client = None
        self._connected = False
        self.address_list = ["opc.tcp://localhost:4840"]
        self.security_mode = None
        self.security_policy = None
        self.certificate_path = None
        self.private_key_path = None

        #self.ui.showMaximized()
        for addr in self.address_list:
            self.ui.addressComboBox.addItem(addr) 
        

        self.tree_ui = TreeWidget(self.ui.treeView)
        self.attrs_ui = AttrsWidget(self.ui.attrView)
        self.refs_ui = RefsWidget(self.ui.refView)
        self.datachange_ui = DataChangeUI(self)

        self.ui.endpointsButton.clicked.connect(lambda : self.get_endpoints())
        self.ui.connSettingsButton.clicked.connect(lambda : self.show_connection_dialog())
        self.ui.connectButton.clicked.connect(lambda : self.connect())
        self.ui.disconnectButton.clicked.connect(lambda: self.disconnect())
        self.ui.refAttrButton.clicked.connect(lambda sel: self.show_attrs(sel))
        self.ui.treeView.selectionModel().selectionChanged.connect(lambda sel: self.show_attrs(sel))
        self.ui.treeView.selectionModel().selectionChanged.connect(lambda sel: self.show_refs(sel))
        self.ui.readButton.clicked.connect(lambda : self.read_value())
        self.ui.writeButton.clicked.connect(lambda : self.show_write_dialog())

    def get_endpoints(self):
        uri = self.ui.addressComboBox.currentText() 
        client = Client(uri, timeout=2)
        edps = client.connect_and_get_server_endpoints()
        for i, ep in enumerate(edps, start=1):
            self.ui.logTextEdit.append('Endpoint %s:' % i)
            for (n, v) in endpoint_to_strings(ep):
                self.ui.logTextEdit.append('  %s: %s' % (n, v))
            self.ui.logTextEdit.append('')
        return edps

    def show_connection_dialog(self):
        dia = ConnectionDialog(self, self.ui.addressComboBox.currentText())
        dia.security_mode = self.security_mode
        dia.security_policy = self.security_policy
        dia.certificate_path = self.certificate_path
        dia.private_key_path = self.private_key_path
        ret = dia.exec_()
        if ret:
            self.security_mode = dia.security_mode
            self.security_policy = dia.security_policy
            self.certificate_path = dia.certificate_path
            self.private_key_path = dia.private_key_path
    
    def show_write_dialog(self):
        node = self.get_current_node()
        if node.get_node_class() == ua.NodeClass.Variable:
            dia = WriteDialog(node,self.ui.logTextEdit)
            ret = dia.exec_()
        else:
            self.ui.logTextEdit.append("Only Variable can be written")


    def connect(self):
        self.disconnect()
        uri = self.ui.addressComboBox.currentText()
        self.ui.logTextEdit.append("Connecting to %s with parameters %s, %s, %s, %s" % (uri, self.security_mode, self.security_policy, self.certificate_path, self.private_key_path))
        try:
            self.client = Client(uri)
            if self.security_mode is not None and self.security_policy is not None:
                self.client.set_security(
                    getattr(crypto.security_policies, 'SecurityPolicy' + self.security_policy),
                    self.certificate_path,
                    self.private_key_path,
                    mode=getattr(ua.MessageSecurityMode, self.security_mode)
                )
            self.client.connect()
            self._connected = True
        except Exception as ex:
            self.ui.logTextEdit.append(str(ex))

        self.tree_ui.set_root_node(self.client.get_root_node())
        self.ui.treeView.setFocus()


    
    def _reset(self):
        self.client = None
        self._connected = False
        self.datachange_ui._datachange_sub = None
        self.datachange_ui._subs_dc = {}
    
    def disconnect(self):
        try:
            if self._connected:
                self.ui.logTextEdit.append("Disconnecting from server")
                self._connected = False
            if self.client:
                self.client.disconnect()
                self._reset()
        except Exception as ex:
            self.ui.logTextEdit.append(str(ex))
        finally:
            self.tree_ui.clear()
            self.refs_ui.clear()
            self.attrs_ui.clear()
            self.datachange_ui.clear()

    def show_attrs(self, selection):
        if isinstance(selection, QItemSelection):
            if not selection.indexes(): # no selection
                return

        node = self.get_current_node()
        if node:
            self.attrs_ui.show_attrs(node)
    
    def show_refs(self, selection):
        if isinstance(selection, QItemSelection):
            if not selection.indexes(): # no selection
                return

        node = self.get_current_node()
        if node:
            self.refs_ui.show_refs(node)
    
    def get_current_node(self, idx=None):
        return self.tree_ui.get_current_node(idx)

    def read_value(self):
        node = self.get_current_node()
        try:
            value = node.get_value()
            data = "Node: %s, Value: %s" % (node.get_browse_name(),value)
            self.ui.logTextEdit.append(data)
        except Exception as ex:
            self.ui.logTextEdit.append(str(ex))



class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainWindow()
    c = ClientController(view=view)
    view.show()
    sys.exit(app.exec_())

    