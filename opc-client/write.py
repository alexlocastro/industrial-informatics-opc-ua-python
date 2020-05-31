from PyQt5.QtWidgets import QDialog
from write_dialog import Ui_Dialog
from opcua import ua
from opcua.common.ua_utils import string_to_val

class WriteDialog(QDialog):
    def __init__(self, node, log):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.node = node
        self.log = log

        self.ui.writeButton.clicked.connect(lambda : self.write())

    def write(self):
        try:
            uatype = self.node.get_data_type_as_variant_type()
            data = string_to_val(self.ui.writeValue.text(),uatype)
            dv = ua.DataValue(ua.Variant(data, varianttype=uatype))
            self.node.set_value(dv)       
        except Exception as ex:
            self.log.append(str(ex))
        finally:
            self.accept()

