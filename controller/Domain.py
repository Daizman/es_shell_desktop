from PyQt5.QtWidgets import QDialog

from view.Domain import Domain as DomainView


class Domain:
    def __init__(self, model, parent=None):
        self.__model = model
        self.__view = DomainView(model, parent)

        self.__view.change_signal.connect(self.change_domain)

    def change_domain(self):
        try:
            self.__model.name = self.__view.ui_name
            self.__model.values = self.__view.ui_values
            self.__view.setResult(QDialog.Accepted)
            self.__view.accept()
        except ValueError as v_e:
            self.__view.show_error(v_e)

    @property
    def model(self):
        return self.__model

    def get_domain(self):
        return self.__view.exec()
