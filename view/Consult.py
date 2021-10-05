from PyQt5.QtCore import pyqtSignal

from view.windows.ConsultWindow import UIConsultWindow

from utils.Mixins import *


class Consult(IShowErrorDialog):
    change_signal = pyqtSignal()

    def __init__(self, consult, rules, variables, domains, parent=None):
        super(Consult, self).__init__(parent)

        self.ui_rules = rules[:]
        self.ui_variables = variables[:]
        self.ui_domains = domains[:]

        self.first_quest = True

        self.ui = UIConsultWindow()
        self.ui.setup_ui(self)

        self.setup_buttons()
        self.refresh()

    def setup_buttons(self):
        self.ui.exit_b.clicked.connect(self.exit)
        self.ui.answer_b.clicked.connect(self.consult)

    def refresh(self):
        self.ui.answer_cb.clear()
        for i in filter(lambda var: var.can_be_goal, self.ui_variables):
            self.ui.answer_cb.addItem(i.name, i)

    def consult(self):
        pass

