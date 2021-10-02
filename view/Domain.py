from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import pyqtSignal

from functools import partial

from view.windows.DomainWindow import UIDomainWindow

from utils.Mixins import *


class Domain(IValidateMyFields, IShowError):
    change_signal = pyqtSignal()

    def __init__(self, domain, parent=None):
        super(Domain, self).__init__(parent)

        self.ui_name = domain.name
        self.ui_values = domain.values[:]

        self.fields_validators = {
            'ui_name': IValidateMyFields.empty_string_validator,
            'ui_values': IValidateMyFields.empty_array_validator
        }

        self.ui = UIDomainWindow()
        self.ui.setup_ui(self)

        self.ui.domain_name_text.setText(self.ui_name)
        self.refresh_values()

        self.setup_buttons()
        self.setup_events()

    def setup_buttons(self):
        self.ui.domain_add_button.clicked.connect(self.add_value)
        self.ui.domain_add_button.setShortcut('Return')

        self.ui.remove_domain_val_button.clicked.connect(self.remove_value)
        self.ui.remove_domain_val_button.setShortcut('Delete')

        self.ui.button_box.accepted.connect(self.accept_changes)

        self.ui.button_box.rejected.connect(self.reject)

    def setup_events(self):
        self.ui.domain_name_text.textChanged.connect(partial(setattr, self, 'ui_name'))
        self.ui.domain_val_view.set_drop_event_callback(self.change_value_order)

    def change_value_order(self, *args):
        self.ui_values = self.ui.domain_val_view.get_all_rows_content()

    def add_value(self):
        new_val = self.ui.domain_val_text.text().strip().upper()
        if new_val in self.ui_values:
            self.show_error('Значение уже есть!')
        else:
            self.ui_values.append(new_val)
        self.refresh_values()

    def remove_value(self):
        rows = self.ui.domain_val_view.selectedItems()
        for row in reversed(rows):
            self.ui_values.remove(row.text())
        self.refresh_values()

    def refresh_values(self):
        self.ui.domain_val_view.clearContents()
        self.ui.domain_val_view.setRowCount(len(self.ui_values))
        for i, value in enumerate(self.ui_values):
            self.ui.domain_val_view.setItem(i, 0, QTableWidgetItem(value))
