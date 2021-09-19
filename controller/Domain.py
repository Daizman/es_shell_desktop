import view.Domain as DomainView


class Domain:
    def __init__(self, model):
        self.__model = model
        self.__view = DomainView.Domain(self, self.__model)

        self.__view.show()

    def add_value(self, value):
        self.__model.add_value(value)

    def remove_value(self, value):
        self.__model.remove_value(value)
