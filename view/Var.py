from PyQt5.QtCore import pyqtSignal

from functools import partial

from view.windows.VarWindow import UIVarWindow

from model.types.VarType import VarType

from model.Domain import Domain as DomainModel
from controller.Domain import Domain as DomainController

from utils.Mixins import *


class Var(IValidateMyFields, IShowErrorDialog):
    change_signal = pyqtSignal()

    def __init__(self, var, domains, parent=None):
        super(Var, self).__init__(parent)

        self.ui_name = var.name
        self.ui_domain = var.domain
        self.ui_type = var.var_type
        self.ui_question = var.question
        self.ui_can_be_goal = var.can_be_goal

        self.fields_validators = {
            'ui_name': IValidateMyFields.empty_string_validator,
            'ui_domain': lambda field: IValidateMyFields.empty_string_validator(field.name)
        }

        self.ui_domains = domains[:]
        if not self.ui_domain and len(domains) > 0:
            self.ui_domain = domains[0]

        self.ui = UIVarWindow()
        self.ui.setup_ui(self)

        self.ui.var_name_text.setText(self.ui_name)
        self.ui.question_text.setText(self.ui_question)

        if self.ui_type == VarType.INFERRED:
            self.ui.var_type_radio_inferred.setChecked(True)
        elif self.ui_type == VarType.REQUESTED:
            self.ui.var_type_radio_requested.setChecked(True)
        else:
            self.ui.var_type_radio_out_requested.setChecked(True)

        self.ui.can_be_goal.setChecked(var.can_be_goal)

        self.refresh_domains()

        self.setup_buttons()
        self.setup_events()

    def setup_buttons(self):
        self.ui.domain_add_button.clicked.connect(self.add_domain)
        self.ui.domain_add_button.setShortcut('+')

        self.ui.button_box.accepted.connect(self.accept_changes)

        self.ui.button_box.rejected.connect(self.reject)

    def setup_events(self):
        self.ui.var_name_text.textChanged.connect(partial(setattr, self, 'ui_name'))

        self.ui.domain_combo.currentTextChanged[str].connect(self.change_domain)

        self.ui.can_be_goal.clicked.connect(self.change_can_be_goal)

        self.ui.var_type_radio_inferred.clicked.connect(self.change_var_type)
        self.ui.var_type_radio_requested.clicked.connect(self.change_var_type)
        self.ui.var_type_radio_out_requested.clicked.connect(self.change_var_type)

        self.ui.question_text.textChanged.connect(self.question_text_change)

    def refresh_domains(self):
        self.ui.domain_combo.clear()
        cur_dom = self.ui_domain
        for dom in self.ui_domains:
            self.ui.domain_combo.addItem(dom.name)
        if cur_dom:
            self.ui.domain_combo.setCurrentText(cur_dom.name)

    def change_domain(self, new_dom):
        for dom in self.ui_domains:
            if new_dom and dom.name == new_dom:
                self.ui_domain = dom
                return

    def change_can_be_goal(self):
        if self.ui_type != VarType.INFERRED:
            self.show_error('Целью не может быть не выводимая переменная')
            self.ui.can_be_goal.setChecked(False)
            return
        self.ui_can_be_goal = self.ui.can_be_goal.isChecked()

    def question_text_change(self):
        self.ui_question = self.ui.question_text.toPlainText()

    def change_var_type(self):
        sender = self.sender()
        if sender == self.ui.var_type_radio_inferred:
            self.ui_type = VarType.INFERRED
        elif sender == self.ui.var_type_radio_requested:
            self.ui_type = VarType.REQUESTED
            self.ui.can_be_goal.setChecked(False)
        else:
            self.ui_type = VarType.OUTPUT_REQUESTED
            self.ui.can_be_goal.setChecked(False)

    def add_domain(self):
        new_domain = DomainModel()
        new_domain_controller = DomainController(new_domain, self)
        if new_domain_controller.exec_view():
            if new_domain in self.ui_domains:
                self.show_error('Такой домен уже есть')
                return
            self.ui_domain = new_domain
            self.ui_domains.append(new_domain)
            self.refresh_domains()
