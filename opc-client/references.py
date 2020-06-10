from PyQt5.QtWidgets import QMainWindow
from references_window import Ui_MainWindow
from uawidgets.refs_widget import RefsWidget
from PyQt5.QtCore import QItemSelection


class ReferencesWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, client):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.client = client

        self.refs_ui = RefsWidget(self.ui.refView)
        node = self.client.get_current_node()
        if node:
            self.refs_ui.show_refs(node)

        self.client.ui.treeView.selectionModel().selectionChanged.connect(lambda sel: self.show_refs(sel))

    def show_refs(self, selection):
        if isinstance(selection, QItemSelection):
            if not selection.indexes(): # no selection
                return
        node = self.client.get_current_node()
        if node:
            self.refs_ui.show_refs(node)

        