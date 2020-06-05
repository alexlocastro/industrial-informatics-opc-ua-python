from connection_dialog import ConnectionDialog
from subscription_dialog import SubscriptionDialog
from monitored_item_dialog import MonitoredItemDialog
from delete_sub_dialog import DeleteSubDialog
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
from datetime import datetime
import time

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
        #self._datachange_sub = None
        self._datachange_sub = {} #key: subscriptionId, value: subscription class
        self._subs_dc = {} #key: nodeId, value: (handler,subscriptionId)
        self.model = QStandardItemModel()
        self.monitored_item_model = QStandardItemModel()
        self.window.ui.subView.setModel(self.model)
        self.window.ui.subView.horizontalHeader().setSectionResizeMode(1)
        self.window.ui.monItemView.setModel(self.monitored_item_model)
        self.window.ui.monItemView.horizontalHeader().setSectionResizeMode(1)
        
        self.pub_interval = 500
        self.subscription_id = None
        self.sampling_interval = 500
        self.queue_size = 1
        self.deadband_value = 0
        self.discard_oldest = True
        self.deadband_type = None
        
        self.window.ui.createSubButton.clicked.connect(lambda: self.show_sub_dialog())
        self.window.ui.subDataChangeButton.clicked.connect(lambda: self.show_monitored_item_dialog())
        self.window.ui.unsubDataChangeButton.clicked.connect(lambda: self._unsubscribe())
        self.window.ui.deleteSubButton.clicked.connect(lambda: self.show_delete_sub_dialog())

        # handle subscriptions
        self._subhandler.data_change_fired.connect(self._update_subscription_model, type=Qt.QueuedConnection)
        
        self.numeric_types = [  ua.uatypes.VariantType.Int16,
                                ua.uatypes.VariantType.UInt16,
                                ua.uatypes.VariantType.Int32,
                                ua.uatypes.VariantType.UInt32,
                                ua.uatypes.VariantType.Int64,
                                ua.uatypes.VariantType.UInt64,
                                ua.uatypes.VariantType.Float,
                                ua.uatypes.VariantType.Double
                            ]
    
    def show_sub_dialog(self):
        dia = SubscriptionDialog(self)
        dia.exec_()
    
    def show_monitored_item_dialog(self):
        dia = MonitoredItemDialog(self)
        dia.exec_()
    
    def show_delete_sub_dialog(self):
        dia = DeleteSubDialog(self)
        dia.exec_()

    def clear(self):
        self._subscribed_nodes = []
        self.model.clear()
        self.monitored_item_model.clear()

    def create_subscription(self):
        try:
            #if not self._datachange_sub:
            sub = self.window.client.create_subscription(self.pub_interval, self._subhandler)
            self._datachange_sub[sub.subscription_id] = sub
            self.model.setHorizontalHeaderLabels(["Subscription Id", "Publishing Interval"])
            row = [QStandardItem(str(sub.subscription_id)), QStandardItem(str(sub.parameters.RequestedPublishingInterval))]
            row[0].setData(sub)
            self.model.appendRow(row)         
        except Exception as ex:
            self.window.ui.logTextEdit.append(str(ex))
            raise
            #modelidx = self.model.indexFromItem(row[0])
            #self.model.takeRow(idx.row())
    
    def _subscribe(self, node = None):
        if not isinstance(node, Node):
            node = self.window.get_current_node()
            if node is None:
                    return
        if node.get_node_class() != ua.NodeClass.Variable:
            self.window.ui.logTextEdit.append("Select a variable node")
            return
        if node in self._subscribed_nodes:
            self.window.ui.logTextEdit.append("already subscribed to node: %s " % node)
            return
        self.monitored_item_model.setHorizontalHeaderLabels(["DisplayName", "Value", "Timestamp","Subscription Id"])
        text = str(node.get_display_name().Text)
        row = [QStandardItem(text), QStandardItem("No Data yet"), QStandardItem(""), QStandardItem(str(self.subscription_id))]
        row[0].setData(node)
        self.monitored_item_model.appendRow(row)
        self._subscribed_nodes.append(node)
        try:
            mir = self._datachange_sub[self.subscription_id]._make_monitored_item_request(node,ua.AttributeIds.Value, None, self.queue_size) #mfilter, queue size
            mir.RequestedParameters.DiscardOldest = self.discard_oldest
            mir.RequestedParameters.SamplingInterval= self.sampling_interval
            mod_filter = ua.DataChangeFilter()
            mod_filter.Trigger = ua.DataChangeTrigger(1)  # send notification when status or value change
            if self.deadband_type != None:
                if self.deadband_type == 1:
                    if node.get_data_type_as_variant_type() in self.numeric_types:           
                        mod_filter.DeadbandType = self.deadband_type #1 assoluta , 2 percentage
                        mod_filter.DeadbandValue =  self.deadband_value
                    else:
                        self.window.ui.logTextEdit.append("filter must be used for numeric data type")
                elif self.deadband_type == 2 and node.get_type_definition().Identifier == ua.object_ids.ObjectIds.AnalogItemType:
                    if node.get_data_type_as_variant_type() in self.numeric_types:           
                        mod_filter.DeadbandType = self.deadband_type #1 assoluta , 2 percentage
                        mod_filter.DeadbandValue =  self.deadband_value
                    else:
                        self.window.ui.logTextEdit.append("filter must be used for numeric data type")
                else:
                    self.window.ui.logTextEdit.append("percentage deadband must be applied to AnalagoItemType with EUrange")

            mir.RequestedParameters.Filter = mod_filter
            handle = self._datachange_sub[self.subscription_id].create_monitored_items([mir]) 
            self._subs_dc[node.nodeid] = (handle[0], self.subscription_id)
        except Exception as ex:
            print("exception")
            self.window.ui.logTextEdit.append(str(ex))
            idx = self.monitored_item_model.indexFromItem(row[0])
            self.monitored_item_model.takeRow(idx.row())

    def _unsubscribe(self, node=None):
        try:
            if node is None:
                node = self.window.get_current_node()
            if node is None:
                return
            sub_id = self._subs_dc[node.nodeid][1]
            handle = self._subs_dc[node.nodeid][0]
            self._datachange_sub[sub_id].unsubscribe(handle)
            self._subscribed_nodes.remove(node)
            i = 0
            while self.monitored_item_model.item(i):
                item = self.monitored_item_model.item(i)
                if item.data() == node:
                    self.monitored_item_model.removeRow(i)
                i += 1
        except Exception as ex:
            self.window.ui.logTextEdit.append(str(ex))

    def _update_subscription_model(self, node, value, timestamp):
        i = 0
        while self.monitored_item_model.item(i):
            item = self.monitored_item_model.item(i)
            if item.data() == node:
                it = self.monitored_item_model.item(i, 1)
                it.setText(value)
                it_ts = self.monitored_item_model.item(i, 2)
                it_ts.setText(timestamp)
            i += 1

    def delete_subscription(self, subscription_id):
        for k,v in self._subs_dc.items():
            if v[1] == subscription_id:
                node = self.get_node(k)
                if node is not None:
                    self._unsubscribe(node = node)

        sub = self._datachange_sub[subscription_id].delete()
        self._datachange_sub.pop(subscription_id)
        i = 0
        while self.model.item(i):
            item = self.model.item(i)
            if item.data().subscription_id == subscription_id:
                self.model.removeRow(i)
            i += 1
    
    def get_node(self,node_id):
        for node in self._subscribed_nodes:
            if node != None:
                if node.nodeid == node_id:
                    return node
        return None
    
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
        self.ui.closeEvent = self.closeEvent

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
        self.ui.treeView.selectionModel().selectionChanged.connect(lambda sel: self.show_attrs(sel))
        self.ui.treeView.selectionModel().selectionChanged.connect(lambda sel: self.show_refs(sel))
        self.ui.readButton.clicked.connect(lambda : self.read_value())
        self.ui.writeButton.clicked.connect(lambda : self.show_write_dialog())
    
    def closeEvent(self, event):
        self.disconnect()

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
        print(self.security_mode)
        print(self.security_policy)
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
            self.client.application_uri = "urn:opcua:python:client"
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
        try:
            self.client.uaclient._uasocket._thread.isAlive()
            self.tree_ui.set_root_node(self.client.get_root_node())
            self.ui.treeView.setFocus()
        except Exception as ex:
            print("Connection error")


    def _reset(self):
        self.client = None
        self._connected = False
        self.datachange_ui._datachange_sub = {}
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
            self.attrs_ui.show_attrs(node)
            if node.get_node_class() == ua.NodeClass.Variable:
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

    