from PyQt5.QtWidgets import QErrorMessage, \
    QShortcut, \
    QDialog, \
    QTableWidgetItem, \
    QWidget, \
    QMainWindow

from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import *

from view.windows.DomainWindow import UIDomainWindow

from functools import partial


class Domain(QMainWindow):
    change_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(Domain, self).__init__(parent)

        self.name = ''
        self.values = []

        self.ui = UIDomainWindow()
        self.ui.setup_ui(self)

        self.connect_buttons()
        self.connect_events()
        self.connect_hotkeys()

    def show_error(self, e):
        error_dialog = QErrorMessage(self)
        error_dialog.setWindowTitle('Ошибка!')
        error_dialog.showMessage(e)

    def clear(self):
        self.ui.domain_val_view.clear()
        self.ui.domain_name_text.clear()

    def connect_buttons(self):
        self.ui.domain_add_button.clicked.connect(self.add_value)
        self.ui.remove_domain_val_button.clicked.connect(self.remove_value)

        self.ui.ok_button.clicked.connect(self.change_signal)
        self.ui.cancel_button.clicked.connect(lambda: self.close())

    def connect_events(self):
        self.ui.domain_name_text.textChanged.connect(partial(setattr, self, "name"))
        self.ui.domain_val_view.set_drop_event_callback(self.change_value_order)

    def change_value_order(self, *args):
        self.values = self.ui.domain_val_view.items(QMimeData())

    def connect_hotkeys(self):
        self.ui.shortcut_del = QShortcut(QKeySequence('Delete'), self)
        self.ui.shortcut_add = QShortcut(QKeySequence('Return'), self)
        self.ui.shortcut_del.activated.connect(self.remove_value)
        self.ui.shortcut_add.activated.connect(self.add_value)

    def add_value(self):
        new_val = self.ui.domain_val_text.text().strip().upper()
        if new_val in self.values:
            self.show_error('Значение уже есть!')
        else:
            self.values.append(new_val)
        self.refresh_values()

    def remove_value(self):
        rows = self.ui.domain_val_view.selectedItems()
        for row in reversed(rows):
            self.values.remove(row.text())
        self.refresh_values()

    def refresh_values(self):
        self.ui.domain_val_view.clear()
        self.ui.domain_val_view.setColumnCount(1)
        self.ui.domain_val_view.setHorizontalHeaderLabels(['Значения'])
        self.ui.domain_val_view.setRowCount(len(self.values))
        for i, value in enumerate(self.values):
            self.ui.domain_val_view.setItem(i, 0, QTableWidgetItem(value))
