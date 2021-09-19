from PyQt5.QtWidgets import QErrorMessage,\
    QShortcut, \
    QDialog, \
    QTableWidgetItem

from PyQt5.QtGui import QKeySequence

from utils.Observer import Observer
from utils.ObserverMeta import ObserverMeta

from view.DomainWindow import UIDomainWindow


class Domain(QDialog, Observer, metaclass=ObserverMeta):
    def __init__(self, controller, model, parent=None):
        super(QDialog, self).__init__(parent)

        self.__controller = controller
        self.__model = model

        self.__old = model

        self.ui = UIDomainWindow()
        self.ui.setup_ui(self)

        self.__model.add_observer(self)
        self.connect_buttons()
        self.connect_hotkeys()

    def show_error(self, e):
        error_dialog = QErrorMessage(self)
        error_dialog.setWindowTitle('Ошибка!')
        error_dialog.showMessage(e)

    def connect_buttons(self):
        self.ui.domain_add_button.clicked.connect(self.add_value)
        self.ui.remove_domain_val_button.clicked.connect(self.remove_value)
        self.ui.ok_button.clicked.connect(lambda: self.close())

        self.cancel_button.clicked.connect(self.restore_domain)

    def connect_hotkeys(self):
        self.ui.shortcut_del = QShortcut(QKeySequence('Delete'), self)
        self.ui.shortcut_del.activated.connect(self.remove_value)

    def add_value(self):
        new_val = self.ui.domain_val_text.text()
        try:
            self.__controller.add_value(new_val)
            self.notify_model_is_changed()
        except ValueError as v_e:
            self.show_error(v_e)

    def remove_value(self):
        rows = self.ui.domain_val_view.selectedItems()
        try:
            for row in reversed(rows):
                self.__controller.remove_value(row.text())
        except ValueError as v_e:
            self.show_error(v_e)

    def restore_domain(self):
        self.__model.remove_observer(self)
        self.__model.values = self.__old.values
        self.__model.name = self.__old.name
        self.close()

    def notify_model_is_changed(self):
        self.ui.domain_val_view.clear()
        values = self.__model.values
        self.ui.domain_val_view.setColumnCount(1)
        self.ui.domain_val_view.setHorizontalHeaderLabels(['Значения'])
        self.ui.domain_val_view.setRowCount(len(values))
        for i, value in enumerate(values):
            self.ui.domain_val_view.setItem(i, 0, QTableWidgetItem(value))
