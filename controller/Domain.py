from view.Domain import Domain as DomainView
import sys
from PyQt5.QtWidgets import QApplication
from model.Domain import Domain as DomainModel


class Domain:
    def __init__(self, model):
        self.__model = model
        self.__view = DomainView()

        self.__view.change_signal.connect(self.change_domain)

        self.__view.show()

    def change_domain(self):
        try:
            self.__model.name = self.__view.name
            self.__model.values = self.__view.values
            self.__view.close()
        except ValueError as v_e:
            self.__view.show_error(v_e)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    _model = DomainModel('Test')
    controller = Domain(_model)

    sys.exit(app.exec_())
