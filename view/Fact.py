from PyQt5.QtCore import pyqtSignal

from functools import partial

from view.windows.FactWindow import UIFactWindow

from model.Var import Var as VarModel
from controller.Var import Var as VarController

from utils.Mixins import *


class Fact(IValidateMyFields, IShowErrorDialog):
    change_signal = pyqtSignal()

    def __init__(self, fact, variants, domains, parent=None):
        super(Fact, self).__init__(parent)

        self.ui_var = fact.var
        self.ui_value = fact.value
        self.ui_variants = variants[:]
        self.ui_domains = domains[:]
        self.ui_vars_str = [var.name for var in variants]

        self.fields_validators = {
            'ui_var': lambda field: field and IValidateMyFields.empty_string_validator(field.name),
            'ui_value': IValidateMyFields.empty_string_validator
        }

        if not self.ui_var and len(variants) > 0:
            self.ui_var = variants[0]
            self.ui_value = variants[0].domain.values[0]

        self.ui = UIFactWindow()
        self.ui.setup_ui(self)

        self.refresh_fact()

        self.setup_buttons()
        self.setup_events()

    def setup_buttons(self):
        self.ui.add_button.clicked.connect(self.add_var)

        self.ui.button_box.accepted.connect(self.accept_changes)
        self.ui.button_box.rejected.connect(self.reject)

    def setup_events(self):
        self.ui.combo.currentTextChanged[str].connect(self.change_var)
        self.ui.value_combo.currentTextChanged[str].connect(partial(setattr, self, 'ui_value'))

    def refresh_fact(self):
        self.ui.combo.clear()
        backup = self.ui_var
        self.ui.combo.addItems(self.ui_vars_str)
        if not backup:
            return
        self.ui.combo.setCurrentText(backup.name)

        if backup:
            for var in self.ui_variants:
                if var.name == backup.name:
                    self.refresh_values(var)
                    return

    def refresh_values(self, var):
        self.ui.value_combo.clear()
        for val in var.domain.values:
            self.ui.value_combo.addItem(val)
        if self.ui_value:
            self.ui.value_combo.setCurrentText(self.ui_value)
        else:
            self.ui.value_combo.setCurrentIndex(0)

    def add_var(self):
        new_var = VarModel()
        new_var_controller = VarController(new_var, self.ui_domains, parent=self)
        if new_var_controller.get_var():
            if new_var in self.ui_variants:
                self.show_error('Такая переменная уже есть')
                return
            self.ui_var = new_var
            self.ui_variants.append(new_var)
            self.ui_vars_str.append(new_var.name)
            self.refresh_fact()

    def change_var(self, var_name):
        for var in self.ui_variants:
            if var.name == var_name:
                self.ui_var = var
                self.ui_value = var.domain.values[0] if var.domain.values else None
                self.refresh_values(var)
                return
