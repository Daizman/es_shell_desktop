from PyQt5.QtWidgets import QErrorMessage,\
    QShortcut, \
    QDialog, \
    QTableWidgetItem

from PyQt5.QtGui import QKeySequence

from utils.Observer import Observer
from utils.ObserverMeta import ObserverMeta

from view.windows.VarWindow import UIVarWindow


class Var(QDialog, Observer, metaclass=ObserverMeta):
    def __init__(self, controller, model, parent=None):
        super(QDialog, self).__init__(parent)

        self.__controller = controller
        self.__model = model

        self.__old = model

        self.ui = UIVarWindow()
        self.ui.setup_ui(self)

        self.__model.add_observer(self)
        self.connect_buttons()

    def notify_model_is_changed(self):
        pass
