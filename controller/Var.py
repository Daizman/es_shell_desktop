from PyQt5.QtWidgets import QDialog

from view.Var import Var as VarView


class Var:
    def __init__(self, model, domains=None, parent=None):
        self.__model = model
        self.__view = VarView(model, domains, parent)

        self.__view.change_signal.connect(self.change_var)

    def change_var(self):
        try:
            self.__model.name = self.__view.ui_name
            self.__model.domain = self.__view.ui_domain
            self.__model.can_be_goal = self.__view.ui_can_be_goal
            self.__model.var_type = self.__view.ui_type
            self.__model.question = self.__view.ui_question
            self.__view.setResult(QDialog.Accepted)
            self.__view.accept()
        except ValueError as v_e:
            self.__view.show_error(v_e)

    @property
    def model(self):
        return self.__model

    def get_var(self):
        return self.__view.exec()
