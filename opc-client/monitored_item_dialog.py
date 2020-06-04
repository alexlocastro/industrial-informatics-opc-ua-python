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
        self.ui.deadbandValue.setText(str(self.datachange_ui.deadband_value))
        self.ui.discardOldestBox.setChecked(True)
        self.ui.absDeadbandButton.setChecked(True)
        #self.ui.absoluteDeadBand.setText(str(self.datachange_ui.abs_deadband))
        self.ui.subscribeButton.clicked.connect(lambda : self.create_monitored_item())


    def create_monitored_item(self):
        try:
            subscription_id = int(self.ui.subscriptionId.text())
            sampling_interval = float(self.ui.samplingInterval.text())
            queue_size = int(self.ui.queueSize.text())
            deadband_value = float(self.ui.deadbandValue.text())
            if subscription_id in self.datachange_ui._datachange_sub.keys():
                self.datachange_ui.subscription_id = subscription_id
                if sampling_interval > 0 and queue_size >= 0 and deadband_value>=0:       
                    self.datachange_ui.discard_oldest = self.ui.discardOldestBox.isChecked()
                    self.datachange_ui.deadband_type = 1 if self.ui.absDeadbandButton.isChecked() else 2
                    self.datachange_ui.sampling_interval = sampling_interval
                    self.datachange_ui.queue_size = queue_size   
                    self.datachange_ui.deadband_value = deadband_value
                    self.datachange_ui._subscribe()
                else:
                    self.datachange_ui.window.ui.logTextEdit.append("Sampl. Interval must be greater than zero\nQueue size must be equal or greater than zero\nAbs Deadband must be equal or greater than zero")
            else:
                self.datachange_ui.window.ui.logTextEdit.append("Subscription does not exists")             
        except Exception as ex:
            self.datachange_ui.window.ui.logTextEdit.append(str(ex))
        finally:
            self.accept()