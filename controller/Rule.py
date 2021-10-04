import sys

from PyQt5.QtWidgets import QDialog, QApplication

from model.Rule import Rule as RuleModel
from view.Rule import Rule as RuleView


class Rule:
    def __init__(self, model, variants, domains, parent=None):
        self.__model = model
        self.__view = RuleView(model, variants, domains, parent)
        self.__variants = variants
        self.__domains = domains

        self.__view.change_signal.connect(self.change_rule)

    def change_rule(self):
        try:
            self.__model.name = self.__view.ui_name
            self.__model.description = self.__view.ui_description
            self.__model.reasons = self.__view.ui_reasons
            self.__model.conclusions = self.__view.ui_conclusions
            self._update_glob(self.__variants, self.__view.ui_variants)
            self._update_glob(self.__domains, self.__view.ui_domains)
            self.__view.setResult(QDialog.Accepted)
            self.__view.accept()
        except ValueError as v_e:
            self.__view.show_error(v_e)

    def _update_glob(self, glob_arr, local_arr):
        glob_arr.clear()
        for el in local_arr:
            glob_arr.append(el)

    @property
    def model(self):
        return self.__model

    def get_rule(self):
        return self.__view.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    glob_variants_list = []
    glob_domains_list = []
    _model = RuleModel()

    controller = Rule(_model, glob_variants_list, glob_domains_list)
    controller.get_rule()
    sys.exit(app.exec_())
