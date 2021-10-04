from view.Shell import Shell as ShellView


class Shell:
    def __init__(self, model):
        self.__model = model
        self.__view = ShellView(model)

        self.__view.change_signal.connect(self.handle_change)

    def handle_change(self):
        self.__model.name = self.__view.ui_name
        self.__model.domains = self.__view.ui_domains
        self.__model.vars = self.__view.ui_vars
        self.__model.rules = self.__view.ui_rules

    def show(self):
        self.__view.show()
