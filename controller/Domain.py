import view.Domain as DomainView


class Domain:
    def __init__(self, model):
        self.__model = model
        self.__view = DomainView.Domain(self, self.__model)

        self.__view.show()

    def set_name(self):
        try:
            self.__model.name = self.__view.ui.domain_name_text.text()
        except ValueError as v_e:
            self.__view.show_error(v_e)

    def set_values(self, values):
        self.__model.values = values

    def add_value(self, value):
        self.__model.add_value(value)

    def remove_value(self, value):
        self.__model.remove_value(value)
