from PyQt5.QtWidgets import QDialog
from monitored_item import Ui_Dialog
from opcua import ua
from opcua.common.ua_utils import string_to_val

class MonitoredItemDialog(QDialog):
    def __init__(self, datachange_ui):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.datachange_ui = datachange_ui
        self.ui.queueSize.setText(str(self.datachange_ui.queue_size))
        self.ui.samplingInterval.setText(str(self.datachange_ui.sampling_interval))
        self.ui.monitoringMode.addItems(["Reporting", "Disabled", "Sampling"])
        self.ui.deadbandValue.setText(str(self.datachange_ui.deadband_value))
        self.ui.discardOldestBox.setChecked(True)
        self.ui.deadbandValue.setDisabled(True) 
        self.ui.subscribeButton.clicked.connect(lambda : self.create_monitored_item())
        self.ui.absDeadbandBox.clicked.connect(lambda: self.percentage_box_status())
        self.ui.percentageDeadbandBox.clicked.connect(lambda: self.abs_box_status())

    def percentage_box_status(self):
        if self.ui.percentageDeadbandBox.isChecked():
            self.ui.percentageDeadbandBox.setChecked(False)
        if self.ui.absDeadbandBox.isChecked():
            self.ui.deadbandValue.setDisabled(False)
        else:
            self.ui.deadbandValue.setDisabled(True)


    def abs_box_status(self):
        if self.ui.absDeadbandBox.isChecked():
            self.ui.absDeadbandBox.setChecked(False)
        if self.ui.percentageDeadbandBox.isChecked():
            self.ui.deadbandValue.setDisabled(False)
        else:
            self.ui.deadbandValue.setDisabled(True)


    def create_monitored_item(self):
        try:
            subscription_id = int(self.ui.subscriptionId.text())
            sampling_interval = float(self.ui.samplingInterval.text())
            queue_size = int(self.ui.queueSize.text())
            deadband_value = float(self.ui.deadbandValue.text())
            if self.ui.monitoringMode.currentText() == "Disabled":
                monitoring_mode = ua.uaprotocol_auto.MonitoringMode.Disabled
            elif self.ui.monitoringMode.currentText() == "Reporting":
                monitoring_mode = ua.uaprotocol_auto.MonitoringMode.Reporting
            elif self.ui.monitoringMode.currentText() == "Sampling":
                monitoring_mode = ua.uaprotocol_auto.MonitoringMode.Sampling
                
            if subscription_id in self.datachange_ui._datachange_sub.keys():
                self.datachange_ui.subscription_id = subscription_id
                if sampling_interval > 0 and queue_size >= 0 and deadband_value>=0:       
                    self.datachange_ui.discard_oldest = self.ui.discardOldestBox.isChecked()
                    if self.ui.absDeadbandBox.isChecked():
                        self.datachange_ui.deadband_type = 1
                    elif self.ui.percentageDeadbandBox.isChecked():
                        self.datachange_ui.deadband_type = 2
                    else:
                        self.datachange_ui.deadband_type = None
                    self.datachange_ui.sampling_interval = sampling_interval
                    self.datachange_ui.queue_size = queue_size   
                    self.datachange_ui.deadband_value = deadband_value
                    self.datachange_ui.monitoring_mode = monitoring_mode
                    self.datachange_ui._subscribe()
                else:
                    self.datachange_ui.window.ui.logTextEdit.append("Sampl. Interval must be greater than zero\nQueue size must be equal or greater than zero\nAbs Deadband must be equal or greater than zero")
            else:
                self.datachange_ui.window.ui.logTextEdit.append("Subscription does not exists")             
        except Exception as ex:
            self.datachange_ui.window.ui.logTextEdit.append(str(ex))
        finally:
            self.accept()