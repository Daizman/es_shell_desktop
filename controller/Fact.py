import sys

from PyQt5.QtWidgets import QApplication, QDialog

from view.Fact import Fact as FactView
from model.Fact import Fact as FactModel


class Fact:
    def __init__(self, model, variants=None, parent=None):
        self.__model = model
        self.__view = FactView(model, variants, parent)

        self.__view.change_signal.connect(self.change_fact)

    def change_fact(self):
        try:
            self.__model.var = self.__view.ui_var
            self.__model.value = self.__view.ui_value
            self.__view.setResult(QDialog.Accepted)
            self.__view.accept()
        except ValueError as v_e:
            self.__view.show_error(v_e)

    @property
    def model(self):
        return self.__model

    def get_fact(self):
        return self.__view.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    _model = FactModel()

    controller = Fact(_model)
    controller.get_fact()
    sys.exit(app.exec_())

