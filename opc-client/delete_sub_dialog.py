from PyQt5.QtWidgets import QDialog
from delete_sub import Ui_Dialog
from opcua import ua
from opcua.common.ua_utils import string_to_val

class DeleteSubDialog(QDialog):
    def __init__(self, datachange_ui):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.datachange_ui = datachange_ui

        self.ui.deleteSubButton.clicked.connect(lambda: self.delete_subscription())

    def delete_subscription(self):
        try:
            sub_id = int(self.ui.subscriptionId.text())
            if sub_id in self.datachange_ui._datachange_sub.keys():
                self.datachange_ui.delete_subscription(sub_id)
            else:
                self.datachange_ui.window.ui.logTextEdit.append("Subscription does not exists")
        except Exception as ex:
            self.datachange_ui.window.ui.logTextEdit.append(str(ex))
        finally:
            self.accept()