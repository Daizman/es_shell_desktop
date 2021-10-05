from PyQt5.QtWidgets import QDialog

from view.Var import Var as VarView
from model.exceptions.UsedVar import UsedVar


class Var:
    def __init__(self, model, domains, parent=None):
        self.__model = model
        self.__view = VarView(model, domains, parent)
        self.__domains = domains

        self.__view.change_signal.connect(self.change_var)

    def change_var(self):
        try:
            self.__model.name = self.__view.ui_name
            self.__model.domain = self.__view.ui_domain
            self.__model.can_be_goal = self.__view.ui_can_be_goal
            self.__model.var_type = self.__view.ui_type
            self.__model.question = self.__view.ui_question
            self.__domains.clear()
            for domain in self.__view.ui_domains:
                self.__domains.append(domain)
            self.__view.setResult(QDialog.Accepted)
            self.__view.accept()
        except ValueError as v_e:
            self.__view.show_error(v_e)
        except UsedVar as u_v:
            self.__view.show_error(u_v)

    @property
    def model(self):
        return self.__model

    def get_var(self):
        return self.__view.exec()
