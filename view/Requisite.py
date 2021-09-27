from PyQt5.QtWidgets import QErrorMessage,\
    QShortcut, \
    QDialog, \
    QTableWidgetItem

from PyQt5.QtGui import QKeySequence

from view.windows.RequisiteWindow import UIRequisiteWindow

from copy import deepcopy


class Requisite(QDialog, Observer, metaclass=ObserverMeta):
    def __init__(self, controller, model, parent=None):
        super(QDialog, self).__init__(parent)

        self.__controller = controller
        self.__model = model

        if model.name:
            self.__old = deepcopy(model)
            self.notify_model_is_changed()

        self.ui = UIRequisiteWindow()
        self.ui.setup_ui(self)

        self.__model.add_observer(self)
        self.connect_buttons()
        self.connect_events()

    def show_error(self, e):
        error_dialog = QErrorMessage(self)
        error_dialog.setWindowTitle('Ошибка!')
        error_dialog.showMessage(e)

    def restore_fact(self):
        if self.__old:
            pass
        self.close()

    def connect_buttons(self):
        self.ui.add_button.clicked.connect(self.add_var)
        self.ui.ok_button.clicked.connect(lambda: self.close())
        self.ui.cancel_button.clicked.connect(self.restore_fact)

    def connect_events(self):
        self.ui.combo.currentTextChanged.connect(self.__controller.set_var)
        self.ui.value_combo.currentTextChanged.connect(self.__controller.set_value)

    def notify_model_is_changed(self):
        pass
