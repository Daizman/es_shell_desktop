from PyQt5.QtCore import pyqtSignal

from functools import partial

from view.windows.VarWindow import UIVarWindow

from model.types.VarType import VarType

from model.Domain import Domain as DomainModel
from controller.Domain import Domain as DomainController

from utils.Mixins import *


class Var(IShowError):
    change_signal = pyqtSignal()

    def __init__(self, var, domains, parent=None):
        super(Var, self).__init__(parent)

        self.ui_name = var.name
        self.ui_domain = var.domain
        self.ui_type = var.var_type
        self.ui_question = var.question

        self.ui_domains = domains if domains else []

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

        self.refresh_domains()

        self.setup_buttons()
        self.setup_events()

    def setup_buttons(self):
        self.ui.domain_add_button.clicked.connect(self.add_domain)
        self.ui.domain_add_button.setShortcut('+')

        self.ui.ok_button.clicked.connect(self.accept_changes)

        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.cancel_button.setShortcut('Ctrl+Q')

    def setup_events(self):
        self.ui.var_name_text.textChanged.connect(partial(setattr, self, 'ui_name'))

        self.ui.domain_combo.currentTextChanged[str].connect(self.change_domain)

        self.ui.var_type_radio_inferred.clicked.connect(self.change_var_type)
        self.ui.var_type_radio_requested.clicked.connect(self.change_var_type)
        self.ui.var_type_radio_out_requested.clicked.connect(self.change_var_type)

        self.ui.question_text.textChanged.connect(partial(setattr, self, 'ui_question'))

    def refresh_domains(self):
        self.ui.domain_combo.clear()
        self.ui.domain_combo.addItems(map(str, self.ui_domains))

    def change_domain(self, new_dom):
        self.ui_domain = self.ui_domains[self.ui_domains.index(lambda a: str(a) == new_dom)]

    def change_var_type(self):
        sender = self.sender()
        if sender == self.ui.var_type_radio_inferred:
            self.ui_type = VarType.INFERRED
        elif sender == self.ui.var_type_radio_requested:
            self.ui_type = VarType.REQUESTED
        else:
            self.ui_type = VarType.OUTPUT_REQUESTED

    def accept_changes(self):
        if not self.ui_name.strip():
            self.show_error('Не введено имя переменной')
            return
        self.change_signal.emit()

    def add_domain(self):
        new_domain = DomainModel()
        new_domain_controller = DomainController(new_domain)
