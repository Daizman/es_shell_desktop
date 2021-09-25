import sys

from PyQt5.QtWidgets import QApplication, QDialog

from view.Domain import Domain as DomainView
from model.Domain import Domain as DomainModel


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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # _model = DomainModel('Test')
    _model = DomainModel('Test_with_values')
    _model.values = ['Stop', 'me', 'now']
    controller = Domain(_model)
    controller.get_domain()

    sys.exit(app.exec_())
