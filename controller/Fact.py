from PyQt5.QtWidgets import QDialog

from view.Fact import Fact as FactView


class Fact:
    def __init__(self, model, variants, domains, parent=None):
        self.__model = model
        self.__view = FactView(model, variants, domains, parent)
        self.__variants = variants
        self.__domains = domains

        self.__view.change_signal.connect(self.change_fact)

    def change_fact(self):
        try:
            self.__model.var = self.__view.ui_var
            self.__model.value = self.__view.ui_value
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

    def set_title(self, title):
        self.__view.setWindowTitle(title)

    def get_fact(self):
        return self.__view.exec()
