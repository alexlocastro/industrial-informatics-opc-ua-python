from PyQt5.QtWidgets import QDialog
from subscription import Ui_Dialog
from opcua import ua
from opcua.common.ua_utils import string_to_val

class SubscriptionDialog(QDialog):
    def __init__(self, datachange_ui):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.datachange_ui = datachange_ui
        self.ui.pubInterval.setText(str(self.datachange_ui.pub_interval))
        self.ui.lifetimeCount.setText(str(self.datachange_ui.lifetime_count))
        self.ui.maxKeepAliveCount.setText(str(self.datachange_ui.max_keep_alive_count))
        self.ui.maxNotificationsPerPublish.setText(str(self.datachange_ui.max_notifications_per_publish))
        self.ui.priority.setText(str(self.datachange_ui.priority))
        self.ui.subButton.clicked.connect(lambda : self.create_subscription())

    def create_subscription(self):
        try:
            pub_interval = int(self.ui.pubInterval.text())
            lifetime_count = int(self.ui.lifetimeCount.text())
            max_keep_alive_count = int(self.ui.maxKeepAliveCount.text())
            max_notifications_per_publish = int(self.ui.maxNotificationsPerPublish.text())
            priority = int(self.ui.priority.text())
            if pub_interval > 0 and lifetime_count > 0 and max_notifications_per_publish > 0 and max_keep_alive_count > 0:
                self.datachange_ui.pub_interval = pub_interval
                self.datachange_ui.lifetime_count = lifetime_count
                self.datachange_ui.max_keep_alive_count = max_keep_alive_count
                self.datachange_ui.max_notifications_per_publish = max_notifications_per_publish
                self.datachange_ui.priority = priority
                self.datachange_ui.create_subscription()
            else:
                self.datachange_ui.window.ui.logTextEdit.append("These parameters must be positive integers")    
        except Exception as ex:
            self.datachange_ui.window.ui.logTextEdit.append(str(ex))
        finally:
            self.accept()

    '''def subscribe(self):
        try:
            pub_interval = float(self.ui.pubInterval.text())
            queue_size = int(self.ui.queueSize.text())
            abs_deadband = float(self.ui.absoluteDeadBand.text())
            if pub_interval > 0 and queue_size >= 0 and abs_deadband>=0:
                self.datachange_ui.pub_interval = pub_interval
                self.datachange_ui.queue_size = queue_size   
                self.datachange_ui.abs_deadband = abs_deadband
                self.datachange_ui._subscribe()
            else:
                self.datachange_ui.window.ui.logTextEdit.append("Pub. Interval must be greater than zero\nQueue size must be equal or greater than zero\nAbs Deadband must be equal or greater than zero")    
        except Exception as ex:
            self.datachange_ui.window.ui.logTextEdit.append(str(ex))
        finally:
            self.accept()'''


        
