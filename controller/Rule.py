import sys

from PyQt5.QtWidgets import QDialog, QApplication

from model.Rule import Rule as RuleModel
from view.Rule import Rule as RuleView


class Rule:
    def __init__(self, model, variants, parent=None):
        self.__model = model
        self.__view = RuleView(model, variants, parent)

        self.__view.change_signal.connect(self.change_rule)

    def change_rule(self):
        try:
            self.__model.name = self.__view.ui_name
            self.__model.description = self.__view.ui_description
            self.__model.reasons = self.__view.ui_rule.reasons
            self.__model.conclusions = self.__view.ui_rule.conclusions
            self.__view.setResult(QDialog.Accepted)
            self.__view.accept()
        except ValueError as v_e:
            self.__view.show_error(v_e)

    @property
    def model(self):
        return self.__model

    def get_rule(self):
        return self.__view.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    _model = RuleModel()

    controller = Rule(_model, [])
    controller.get_rule()
    sys.exit(app.exec_())
