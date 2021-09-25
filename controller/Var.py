import sys

from PyQt5.QtWidgets import QApplication

from view.Var import Var as VarView
from model.Var import Var as VarModel
from model.types.VarType import VarType

from model.Domain import Domain


class Var:
    def __init__(self, model, domains=None, parent=None):
        self.__model = model
        self.__view = VarView(model, domains, parent)

        self.__view.change_signal.connect(self.change_var)

        self.__view.show()

    def change_var(self):
        try:
            pass
        except ValueError as v_e:
            self.__view.show_error(v_e)

    @property
    def model(self):
        return self.__model


if __name__ == '__main__':
    app = QApplication(sys.argv)

    _model = VarModel('Test_var')

    controller = Var(_model)
    sys.exit(app.exec_())
