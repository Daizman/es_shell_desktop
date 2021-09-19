import view.Var as VarView
from model.types.VarType import VarType


class Var:
    def __init__(self, model, domains):
        self.__model = model
        self.__view = VarView.Var(self, self.__model)
        self.domains = domains

        self.__view.show()

    def set_name(self):
        try:
            self.__model.name = self.__view.ui.var_name_text.text()
        except ValueError as v_e:
            self.__view.show_error(v_e)

    def set_domain(self):
        try:
            self.__model.domain = list(filter(lambda domain: domain.name == self.__view.ui.domain_combo.currentText(),
                                              self.domains))[0]
        except ValueError as v_e:
            self.__view.show_error(v_e)

    def set_var_type(self):
        if self.__view.ui.var_type_radio1.isChecked():
            self.__model.var_type = VarType.REQUESTED
        elif self.__view.ui.var_type_radio2.isChecked():
            self.__model.var_type = VarType.INFERRED
        else:
            self.__model.var_type = VarType.OUTPUT_REQUESTED

    def set_question(self):
        try:
            self.__model.question = self.__view.ui.question_text.text()
        except ValueError as v_e:
            self.__view.show_error(v_e)
