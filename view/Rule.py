import sys
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import pyqtSignal

from functools import partial

from view.windows.RuleWindow import UIRuleWindow

from model.Rule import Rule as RuleModel
from model.Fact import Fact as FactModel
from controller.Fact import Fact as FactnController

from utils.Mixins import *


class Rule(IShowError):
    change_signal = pyqtSignal()

    def __init__(self, rule, parent=None):
        super(Rule, self).__init__(parent)

        self.ui_name = rule.name
        self.ui_description = rule.description
        self.ui_rule = rule

        self.ui = UIRuleWindow()
        self.ui.setup_ui(self)

        self.refresh_requisite()
        self.refresh_conclusion()

        self.setup_buttons()
        self.setup_events()

    def setup_buttons(self):
        pass

    def setup_events(self):
        pass

    def refresh_requisite(self):
        pass

    def refresh_conclusion(self):
        pass

    def accept_changes(self):
        pass

    def add_requisite(self):
        pass

    def add_conclusion(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    _model = RuleModel()
    view = Rule(_model)
    view.exec()
    sys.exit(app.exec_())

