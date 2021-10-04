import view.Shell as ShellView


class Shell:
    def __init__(self, model):
        self.__model = model
        self.__view = ShellView.Shell(model)

        self.__view.change_signal.connect(self.handle_change)

    def handle_change(self):
        pass
